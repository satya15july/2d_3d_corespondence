# Introduction
This project demonsttrate how to find K and R from 3D to 2D correspondence during 
Forward Projection.

# How To Use

## Annotation
Run `python3 annotate_input.py` and then select 6 corner points and make sure "pts_3d" and "pts_2d"
present in `main.py` are aligned.

[Input Image]

![input](https://user-images.githubusercontent.com/22910010/236404103-f862b879-6b8f-4f0b-a791-bddc67df3543.png)

[Annotated Image]

![image_anotated](https://user-images.githubusercontent.com/22910010/236404275-4b2d04ff-ead8-4c40-81e3-b554864e930f.png)

# Output

Run `python3 main.py`.

Output:

```
K : [[ 1.21535398e+03 -5.90945543e+00  4.22148713e+02]
 [ 0.00000000e+00  1.20543111e+03  2.74236749e+02]
 [ 0.00000000e+00  0.00000000e+00  1.00000000e+00]]
R : [[ 0.72445723 -0.00311026 -0.68931273]
 [ 0.3952897  -0.81735845  0.4191315 ]
 [-0.5647192  -0.57612107 -0.59091179]]
t : [[-0.44951655]
 [ 1.918288  ]
 [12.79677076]]
pt_reproject: [[378.57070643 201.86842548 556.88558511 372.05049304 172.28392615
  575.26591913]
 [454.93577714 335.16317848 328.91681825 216.10337387 111.81427511
  106.0939025 ]

```

[ReProjected Image]

![reprojected_image](https://user-images.githubusercontent.com/22910010/236404490-8aaf5a3b-8468-48b7-bc49-c11110df77a1.jpg)


# Conclusion

3D points are correctly projected on to image plane with reprojection error = 1.87852.
