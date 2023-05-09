import open3d as o3d
import numpy as np

# read the point cloud
pcd = o3d.io.read_point_cloud('/home/arun/Downloads/complete/incomplete/00.pcd')

# estimate normals
pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))

# convert to off file
mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(pcd, depth=8)

# print the mesh
# print (mesh[0])

# convert to numpy array
vertices = np.asarray(mesh[0].vertices)
faces = np.asarray(mesh[0].triangles)

print (vertices)
print (faces)

