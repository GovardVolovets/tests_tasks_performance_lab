import sys
import math

with open(sys.argv[1], 'r') as f:
    x_center, y_center = map(float, f.readline().split())
    radius = float(f.readline())

with open(sys.argv[2], 'r') as f:
    points = [list(map(float, line.split())) for line in f]

results = []
for point in points:
    distance = math.sqrt((point[0] - x_center) ** 2 + (point[1] - y_center) ** 2)
    if distance < radius:
        results.append(1)
    elif distance == radius:
        results.append(0)
    else:
        results.append(2)

print(' '.join(map(str, results)))