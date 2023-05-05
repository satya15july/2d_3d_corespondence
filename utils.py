import numpy as np
import math


def compute_P(pt_2d, pt_3d):
    A = []
    for n in range(pt_2d.shape[0]):
        A.append([[pt_3d[n][0], pt_3d[n][1], pt_3d[n][2], 1, 0, 0, 0, 0, -pt_2d[n][0] * pt_3d[n][0],
                   -pt_2d[n][0] * pt_3d[n][1], -pt_2d[n][0] * pt_3d[n][2], -pt_2d[n][0]],
                  [0, 0, 0, 0, pt_3d[n][0], pt_3d[n][1], pt_3d[n][2], 1, -pt_2d[n][1] * pt_3d[n][0],
                   -pt_2d[n][1] * pt_3d[n][1], -pt_2d[n][1] * pt_3d[n][2], -pt_2d[n][1]]])
    A = np.array(A)
    A = A.reshape(A.shape[0] * A.shape[1], A.shape[2])

    # SVD
    u, s, vh = np.linalg.svd(A)

    # get the smallest singular value of SVD
    P = vh[-1, :].reshape(3, 4)

    return A, P

def compute_KR(P):
    M = P[0:3, 0:3]
    # QR decomposition
    q, r = np.linalg.qr(np.linalg.inv(M))
    R = np.linalg.inv(q)
    K = np.linalg.inv(r)
    # translation vector
    t = np.dot(np.linalg.inv(K), P[:, -1])

    D = np.array([[np.sign(K[0, 0]), 0, 0],
                  [0, np.sign(K[1, 1]), 0],
                  [0, 0, np.sign(K[2, 2])]])

    # K,R,t correction
    K = np.dot(K, D)
    R = np.dot(np.linalg.inv(D), R)
    t = np.dot(np.linalg.inv(D), t)
    t = np.expand_dims(t, axis=1)

    # normalize K
    K = K / K[-1, -1]

    return K, R, t


def reproject(pt_3d, K, R, t):
    pt_3d = np.hstack((pt_3d, np.ones((pt_3d.shape[0], 1))))

    Rt = np.hstack((R, t))
    KRt = np.dot(K, Rt)

    pt_reproject = np.dot(KRt, pt_3d.T)
    pt_reproject = pt_reproject / pt_reproject[-1, :]

    return KRt, pt_reproject  # , extrinsic, projection, intrinsic, P_combined


