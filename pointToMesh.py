import numpy as np

points = np.array([
    [0, 0, 0],
    [10, 0, 0],
    [10, 10, 0],
    [0, 10, 0],
    [0, 0, 10],
    [10, 0, 10],
    [10, 10, 10],
    [0, 10, 10],
])


from scipy.spatial import ConvexHull

hull = ConvexHull(points)
faces = hull.simplices


from stl import mesh

cube_mesh = mesh.Mesh(np.zeros(len(faces), dtype=mesh.Mesh.dtype))

for i, face in enumerate(faces):
    for j in range(3):
        cube_mesh.vectors[i][j] = points[face[j]]

cube_mesh.save("cube.stl")
print("cube.stl created")

# cube.stl
