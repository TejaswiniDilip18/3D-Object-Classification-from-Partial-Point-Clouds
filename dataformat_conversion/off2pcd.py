'''
run this file to convert the off file to point cloud
'''


import open3d as o3d
import numpy as np


#Create a point cloud object
pcd = o3d.geometry.PointCloud()

mesh = o3d.io.read_triangle_mesh("/home/arun/Pointnet_Pointnet2_pytorch/ModelNet10/ModelNet10/toilet/train/toilet_0300.off")
pcd = mesh.sample_points_poisson_disk(5000)

# print center of the point cloud
print(pcd.get_center())

# translate the point cloud to the origin
pcd.translate(-pcd.get_center())

#print the center of the point cloud
print(pcd.get_center())


# # center the point cloud
# pcd.points = o3d.utility.Vector3dVector(np.asarray(pcd.points) - np.mean(np.asarray(pcd.points), axis=0))

# normalize the point cloud
pcd.points = o3d.utility.Vector3dVector(np.asarray(pcd.points)/np.max(np.linalg.norm(np.asarray(pcd.points), axis=1)))

# # convert pcd to off
# mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(pcd, depth=9)
# vertices = np.asarray(mesh.vertices)
# faces = np.asarray(mesh.triangles)


# confirm that the point cloud is normalized
print(np.max(np.linalg.norm(np.asarray(pcd.points), axis=1)))

# # confirm that the point cloud is centered, if not print the mean
# print(np.mean(np.asarray(pcd.points), axis=0))

o3d.visualization.draw_geometries([pcd])

o3d.io.write_point_cloud('/home/arun/RSS/Project/sample_pcd/normalized_toilet.pcd',pcd)