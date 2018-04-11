# Point Cloud Labeler
This method voxelizes point clouds in .ply, passes them to a 3D Convolutional Neural Network, and determines building geometries (hopefully)


##### Tech Stack

Code

(1) Import Pointcloud 


(2) Voxelize

    a) compute Pointcloud boundary

    b) divide into cells N x N x N
        - cube radius R = 

    c) occupancy or density

    d) provide unique index label for Tsraining Data
        - use voting for points with multiple classes


(3) 3D Convolutional Neural Network

    a) first convolutional layer

    b) first max-pooling layer

    c) second convolutional layer

    d) second max-pooling layer

    e) dense layer

    f) softmax function
