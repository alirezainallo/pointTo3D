import numpy as np
import trimesh

# ============================
# Configuration
# ============================
STL_FILE = "cube.stl"     # path to STL file

RADIUS = 200.0             # distance of sensors from center (mm)
DELTA_THETA = 1.0          # angular step (degrees)
# Z_POSITIONS = [-20, 0, 20] # sensor Z sweep (mm)
Z_POSITIONS = np.arange(-50, 51, 5)  # از -50 تا 50 mm، گام 5 mm

RAY_LENGTH = 1000.0        # max ray length (mm)

OUTPUT_FILE = "scan_points.csv"

# ============================
# Load STL and center it
# ============================
mesh = trimesh.load(STL_FILE)

# Move mesh center to origin
mesh.vertices -= mesh.centroid

# ============================
# Prepare ray intersector
# ============================
ray_intersector = trimesh.ray.ray_triangle.RayMeshIntersector(mesh)

# ============================
# Prepare scan angles
# ============================
angles_deg = np.arange(0, 360, DELTA_THETA)

hit_points = []

# ============================
# Scan loop
# ============================
for z in Z_POSITIONS:
    for theta_deg in angles_deg:
        theta = np.deg2rad(theta_deg)

        # Sensor position (polar -> Cartesian)
        sensor_pos = np.array([
            RADIUS * np.cos(theta),
            RADIUS * np.sin(theta),
            z
        ])

        # Ray direction (towards origin)
        direction = -sensor_pos
        direction = direction / np.linalg.norm(direction)

        ray_origins = np.array([sensor_pos])
        ray_directions = np.array([direction])

        # Ray intersection
        locations, index_ray, index_tri = ray_intersector.intersects_location(
            ray_origins,
            ray_directions,
            multiple_hits=False
        )

        if len(locations) > 0:
            hit_points.append(locations[0])

# ============================
# Save results
# ============================
hit_points = np.array(hit_points)

print(f"Scan finished. Total points: {len(hit_points)}")

np.savetxt(
    OUTPUT_FILE,
    hit_points,
    delimiter=",",
    header="X,Y,Z",
    comments=""
)

print(f"Saved to: {OUTPUT_FILE}")
