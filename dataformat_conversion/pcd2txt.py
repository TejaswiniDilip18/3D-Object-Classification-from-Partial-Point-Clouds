#convert point cloud to txt file


import open3d as o3d
import numpy as np

pcd= o3d.io.read_point_cloud('/home/arun/Pointnet_Pointnet2_pytorch/bathtub_0001.pcd')

pcd.translate(-pcd.get_center())
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
np.savetxt('/home/arun/Pointnet_Pointnet2_pytorch/bathtub_0001.txt', np.hstack((xyz, normals)), delimiter=',')



