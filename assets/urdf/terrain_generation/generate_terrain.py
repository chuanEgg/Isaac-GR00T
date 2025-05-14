# source: https://github.com/bulletphysics/bullet3/blob/master/data/terrain.py

import math

TRIANGLE_SIZE = 1
NUM_VERTS_X = int(100 / TRIANGLE_SIZE)
NUM_VERTS_Y = int(100 / TRIANGLE_SIZE)
totalVerts = NUM_VERTS_X * NUM_VERTS_Y
totalTriangles = 2 * (NUM_VERTS_X - 1) * (NUM_VERTS_Y - 1)
offset = -50.0
waveheight = 0.15
gGroundVertices = [None] * totalVerts * 3
gGroundIndices = [None] * totalTriangles * 3

i = 0

for i in range(NUM_VERTS_X):
  for j in range(NUM_VERTS_Y):
    gGroundVertices[(i + j * NUM_VERTS_X) * 3 + 0] = (i - NUM_VERTS_X * 0.5) * TRIANGLE_SIZE
    gGroundVertices[(i + j * NUM_VERTS_X) * 3 + 1] = (j - NUM_VERTS_Y * 0.5) * TRIANGLE_SIZE
    gGroundVertices[(i + j * NUM_VERTS_X) * 3 +
                    2] = waveheight * math.sin(float(i)) * math.cos(float(j) + offset)

index = 0
for i in range(NUM_VERTS_X - 1):
  for j in range(NUM_VERTS_Y - 1):
    gGroundIndices[index] = 1 + j * NUM_VERTS_X + i
    index += 1
    gGroundIndices[index] = 1 + j * NUM_VERTS_X + i + 1
    index += 1
    gGroundIndices[index] = 1 + (j + 1) * NUM_VERTS_X + i + 1
    index += 1
    gGroundIndices[index] = 1 + j * NUM_VERTS_X + i
    index += 1
    gGroundIndices[index] = 1 + (j + 1) * NUM_VERTS_X + i + 1
    index += 1
    gGroundIndices[index] = 1 + (j + 1) * NUM_VERTS_X + i
    index += 1

#print(gGroundVertices)
#print(gGroundIndices)

# print("o Terrain")

# for i in range(totalVerts):
#   print("v", end = ' '),
#   print(gGroundVertices[i * 3 + 0], end = ' '),
#   print(gGroundVertices[i * 3 + 1], end = ' '),
#   print(gGroundVertices[i * 3 + 2])

# for i in range(totalTriangles):
#   print("f", end = ' '),
#   print(gGroundIndices[i * 3 + 0], end=' '),
#   print(gGroundIndices[i * 3 + 1], end=' '),
#   print(gGroundIndices[i * 3 + 2]),

with open("terrain_test.obj", "w") as file:
  file.write("o Terrain\n")
  for i in range(totalVerts):
    file.write(f"v {gGroundVertices[i * 3 + 0]} {gGroundVertices[i * 3 + 1]} {gGroundVertices[i * 3 + 2]}\n")
  file.write("s off\n")
  for i in range(totalTriangles):
    file.write(f"f {gGroundIndices[i * 3 + 0]} {gGroundIndices[i * 3 + 1]} {gGroundIndices[i * 3 + 2]}\n")

print("done")