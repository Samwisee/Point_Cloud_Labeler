### This takes in point cloud data from .ply files and turns them into voxels

from pyntcloud import PyntCloud

cloud = PyntCloud.from_file("/Data/georeferenced_model.ply")

cloud.add_scalar_field("hsv")

voxelgrid_id = cloud.add_structure("voxelgrid", x_y_z=[32, 32, 32])

points = cloud.get_sample("voxelgrid_nearest", voxelgrid=voxelgrid_id)

new_cloud = PyntCloud(points)

new_cloud.to_file("out_file.ply")
