# convert txt file to pcd file

import open3d as o3d
import numpy as np


# pcd = o3d.geometry.PointCloud() 
# # # read the txt file
# # xyz = np.loadtxt('/home/arun/Pointnet_Pointnet2_pytorch/data/modelnet40_normal_resampled/airplane/airplane_0001.txt')

# # # convert to point cloud
# # pcd.points = o3d.utility.Vector3dVector(xyz)

# # read the first three points of each line in the txt file
# xyz = np.loadtxt('/home/arun/Pointnet_Pointnet2_pytorch/data/modelnet40_normal_resampled/airplane/airplane_0001.txt', usecols=(0,1,2))
# print(xyz)

# pcd = o3d.io.read_point_cloud("/home/arun/Pointnet_Pointnet2_pytorch/data/modelnet40_normal_resampled/airplane/airplane_0001.txt", format='xyzrgb')
# o3d.visualization.draw_geometries([pcd])

# read the first three points of each line in the txt file

with open('/home/arun/RSS/Project/shapenet_PN2_partial/plane/plane_0795.txt', 'r') as f:
    lines = f.readlines()
    #extract the first three points of each line

output = []
for line in lines:
    points = line.split(",")
    x,y,z = map(float, points[:3])
    output.append([x,y,z])

output = np.asarray(output)

pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(output)



o3d.visualization.draw_geometries([pcd])

# # save the point cloud to a pcd file
# o3d.io.write_point_cloud("/home/arun/Pointnet_Pointnet2_pytorch/bathtub_0001.pcd", pcd)




