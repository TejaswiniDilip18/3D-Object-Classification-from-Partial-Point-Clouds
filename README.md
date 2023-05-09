# Project Description

Point clouds are widely used as geometric data in various deep learning tasks like object detection and segmentation. However, in real-world scenarios, partial point clouds are often encountered due to limitations in sensors, occlusions, and other factors. The classification of objects from partial point clouds is a difficult task because of the sparsity, noise, and lack of complete representation of objects. This project aims to create a 3D object classification system that can classify objects from partial point clouds. To overcome the challenges, the GRNet neural network architecture is used to predict the missing data and complete the partial point clouds, which are then processed by PointNet, a deep learning framework that directly handles raw point clouds for object classification. PointNet++ is used as a baseline for comparison, as it is an extension of PointNet that is specifically designed to handle varying-density point clouds and has demonstrated superior performance in object classification tasks. The proposed method in this project performs equally or better than PointNet++ in object classification tasks using partial point clouds.

## Datasets used


ModelNet10 : The dataset can be downloaded from this link. http://3dvision.princeton.edu/projects/2014/3DShapeNets/ModelNet10.zip

Derived Dataset : In order to conduct our experiments, we also created a custom dataset by combining the ShapeNet dataset and
the ModelNet10 dataset. We selected 8 categories from the ShapeNet dataset, including airplane, bench, cabinet, car, chair, lamp, sofa, and table, as well as 2 categories from
the ModelNet10 dataset, which were bathtub and bed. ShapeNet dataset can be downloaded from this link. https://gateway.infinitescript.com/?fileName=ShapeNetCompletion

test_classification.py provided by https://github.com/yanx27/Pointnet_Pointnet2_pytorch is updated to build a confusion matrix.

train_classification.py provided by https://github.com/yanx27/Pointnet_Pointnet2_pytorch is updated to log losses in a text file.

ModelNetDataloader.py provided by https://github.com/yanx27/Pointnet_Pointnet2_pytorch is updated to handle less number of points in point cloud.


## Acknowledgements

1. Nikita Karaevv : Owner of Github Repository "PyTorch implementation of "PointNet: Deep Learning on Point Sets for 3D Classification and Segmentation". https://github.com/nikitakaraevv/pointnet

2. Benny :Owner of Github Repository  "Pytorch Implementation of PointNet and PointNet++". https://github.com/yanx27/Pointnet_Pointnet2_pytorch

3. Haozhe Xie: Owner of Github Repository "GRNet". https://github.com/hzxie/GRNet



