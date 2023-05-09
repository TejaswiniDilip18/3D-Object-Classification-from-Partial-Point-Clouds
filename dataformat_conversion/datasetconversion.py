'''
Run this file to convert the dataset from .pcd to .txt format. The pcd files
are in the folder_path and the converted files are saved in the output_folder.
'''


import os
import open3d as o3d
import numpy as np

folder_path = '/home/arun/RSS/Project/ShapeNetCompletion_custom/ShapeNetCompletion/04530566/test/'
output_folder = '/home/arun/RSS/Project/shapenet_PN2/watercraft/test/'
filelist_folder = '/home/arun/RSS/Project/shapenet_PN2/'

# with open(os.path.join(filelist_folder, 'train.txt'), 'a') as r:
#     with open(os.path.join(filelist_folder, 'filelist.txt'), 'a') as f:
#         files = sorted([a for a in os.listdir(folder_path) if a.endswith('.pcd')])
#         for file_name in files:
                
#                 file_name_without_ext = os.path.splitext(file_name)[0]
#                 f.write('04379243/' + file_name_without_ext + '.txt' + '\n')

#                 r.write(file_name_without_ext + '\n')

#update the counter value to the last value in the train.txt file
counter = 650
for file_name in sorted(os.listdir(folder_path)):
    if file_name.endswith('.pcd'):
                
                counter += 1
                # Create a point cloud object
                pcd = o3d.geometry.PointCloud()
                
                # # Read the triangle mesh file
                # mesh = o3d.io.read_triangle_mesh(os.path.join(folder_path, file_name))
                
                # # Convert to point cloud
                # pcd.points = o3d.utility.Vector3dVector(np.asarray(mesh.vertices))

                # Read the point cloud file
                pcd = o3d.io.read_point_cloud(os.path.join(folder_path, file_name))

                num = len(pcd.points)
                if (num > 10000) :   
                    pcd = pcd.farthest_point_down_sample(10000)

                # # estimate the normals of the point cloud
                # pcd.estimate_normals()
                
                # Translate the point cloud to the origin
                pcd.translate(-pcd.get_center())
                
                # Normalize the point cloud
                pcd.points = o3d.utility.Vector3dVector(np.asarray(pcd.points)/np.max(np.linalg.norm(np.asarray(pcd.points), axis=1)))

                # estimate the normals of the point cloud
                pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))
                
                # Extract the points from the point cloud
                xyz = np.asarray(pcd.points)

                # extract the normals from the point cloud
                normals = np.asarray(pcd.normals)
                
                # Save the points to a txt file
                # output_file_name = '{:03d}_'.format(counter) + os.path.splitext(file_name)[0] + '.txt'

                #save the points and normals to a txt file cabinet_0001.txt
                output_file_name = 'watercraft_' + '{:04d}'.format(counter) + '.txt'
                
    
                # np.savetxt(os.path.join(output_folder, output_file_name), xyz, delimiter=',')
                np.savetxt(os.path.join(output_folder, output_file_name), np.hstack((xyz, normals)), delimiter=',')

print('counter: ', counter)

    
    # read all the file names in the folder and save the names in a .txt file in the following format
    # file_name_1

    # for file_name in os.listdir(folder_path):
    #     if file_name.endswith('.txt'):
    #         with open(os.path.join(output_folder, 'modelnet10_train.txt'), 'a') as f:
    #             f.write(file_name)
    
    # # write the file names in the following format in another .txt file
    # # 02933112/file_name_1.txt

    # for file_name in os.listdir(folder_path):
    #     if file_name.endswith('.txt'):
    #         with open(os.path.join(output_folder, 'filelist.txt'), 'a') as f:
    #             f.write('02933112/' + file_name + '.txt')