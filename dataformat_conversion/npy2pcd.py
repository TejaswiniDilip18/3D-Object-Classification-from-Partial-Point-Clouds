import open3d as o3d
import numpy as np


#Create a point cloud object
pcd = o3d.geometry.PointCloud()

# load the numpy array
xyz = np.load('/home/arun/Downloads/fine (1)/fine.npy')

# center the point cloud
xyz = xyz - np.mean(xyz, axis=0)

# normalize the point cloud
xyz/= np.max(np.linalg.norm(xyz, axis=1))


# convert the numpy array to point cloud
pcd.points = o3d.utility.Vector3dVector(xyz)

# #To save the point cloud
# o3d.io.write_point_cloud('/home/arun/RSS/Project/check.ply',pcd)

# 
# # To load the point cloud
# pcd= o3d.io.read_point_cloud('/home/arun/Downloads/complete/incomplete/07.pcd')

# # sample 2050 points uniformly from the point cloud
# pcd = pcd.uniform_down_sample(20)

# # normalize the point cloud
# pcd.normalize_normals()

# # center the point cloud
# pcd.translate(-pcd.get_center())

# norm_pointcloud = pcd - np.mean(pcd, axis=0)
# pcd/= np.max(np.linalg.norm(norm_pointcloud, axis=1))

#To visualize the point cloud
o3d.visualization.draw_geometries([pcd])

#To save the point cloud
# o3d.io.write_point_cloud('/home/arun/RSS/Project/down_shapenet.pcd',pcd)


