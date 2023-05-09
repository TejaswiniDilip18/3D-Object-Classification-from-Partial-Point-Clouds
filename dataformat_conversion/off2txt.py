'''
run this file to convert the off file to txt file
'''

import open3d as o3d
import numpy as np


pcd = o3d.geometry.PointCloud() 

#Create a point cloud object
pcd = o3d.geometry.PointCloud()

mesh = o3d.io.read_triangle_mesh("/home/arun/Pointnet_Pointnet2_pytorch/ModelNet10/ModelNet10/bathtub/train/bathtub_0002.off")
#convert to point cloud
pcd = mesh.sample_points_poisson_disk(5000)
# pcd.points = o3d.utility.Vector3dVector(np.asarray(mesh.vertices))

# translate the point cloud to the origin
pcd.translate(-pcd.get_center())

# normalize the point cloud
pcd.points = o3d.utility.Vector3dVector(np.asarray(pcd.points)/np.max(np.linalg.norm(np.asarray(pcd.points), axis=1)))

# estimate the normals of the point cloud
pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))

# visualize the point cloud and the normals
o3d.visualization.draw_geometries([pcd])


# extract the points from the point cloud
xyz = np.asarray(pcd.points)

# extract the normals from the point cloud
normals = np.asarray(pcd.normals)

# save points and normals to a txt file
np.savetxt('/home/arun/RSS/Project/check/bathtub_0002.txt', np.hstack((xyz, normals)), delimiter=',')

# # convert the points to txt file
# np.savetxt('/home/arun/RSS/Project/check/02.txt', xyz, delimiter=',')
