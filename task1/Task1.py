import sys

def circular_array_path(n, m):
    path = [1]
    pos = 1
    while True:
        pos = (pos + m - 1) % n
        if pos == 0:
            pos = n
        if pos == 1:
            break
        path.append(pos)
    return path

n = int(sys.argv[1])
m = int(sys.argv[2])

print(''.join(map(str, circular_array_path(n, m))))