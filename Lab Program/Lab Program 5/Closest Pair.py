def closest_pair(points):
    import math
    min_dist = float('inf')
    pair = None
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            dist = math.dist(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
                pair = (points[i], points[j])
    return pair, min_dist
points = [(1, 2), (4, 6), (5, 8), (10, 12), (3, 1)]
pair, min_dist = closest_pair(points)
print(f"Closest pair: {pair}")
print(f"Distance: {min_dist}")
