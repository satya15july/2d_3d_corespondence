import cv2
import numpy as np
import math

import utils


final_cord=np.load('final_cord_calibration.npy')
print(final_cord)
print(final_cord.shape)
# Centre Top
center2d_top = final_cord[1,:]
center2d_top_left = final_cord[0,:]
center2d_top_right = final_cord[2,:]
print("center2d_top {}".format(center2d_top))
print("center2d_top_left {}".format(center2d_top_left))
print("center2d_top_right {}".format(center2d_top_right))

center2d = final_cord[4,:]
center2d_left = final_cord[3,:]
center2d_right = final_cord[5,:]
print("Center Bottom {}".format(center2d))
print("Center Bottom Left {}".format(center2d_left))
print("Center Bottom Right {}".format(center2d_right))

pts_3d = np.array([[0, 0, 0], [-3, 0, 0], [0, 0, -3], [0, 3, 0], [-3, 3, 0], [0, 3, -3]])
pts_2d = np.vstack((np.array(center2d), np.array(center2d_left), np.array(center2d_right), np.array(center2d_top), np.array(center2d_top_left), np.array(center2d_top_right)))
# compute projection matrix
A, P = utils.compute_P(pts_2d, pts_3d)

# compute QR decomposition
K, R, t = utils.compute_KR(P)

print("K : {}".format(K))
print("R : {}".format(R))
print("t : {}".format(t))
# reproject
KRt, pt_reproject = utils.reproject(pts_3d, K, R, t)

print("pt_reproject: {}".format(pt_reproject))
print("KRt: {}".format(KRt))
print("KRt.shape: {}".format(KRt.shape))

# compute RMS error
RMS_e = math.sqrt(np.sum((pts_2d - pt_reproject[0:2].T) ** 2) / pts_2d.shape[0])
print("RMS_error: {}".format(RMS_e))

img = cv2.imread('input.png')
# save projected points on image
img_reprojected = img
for j, row in enumerate(pt_reproject[0:2].T):
    cv2.circle(img, tuple(pts_2d[j]), 5, (0, 255, 255), 2)
    cv2.circle(img_reprojected, tuple(row.astype(int)), 4, (0, 0, 255), -1)

cv2.imwrite('reprojected_image.jpg', img_reprojected)
cv2.imshow('reprojected', img_reprojected / 255.0)
cv2.waitKey(0)

