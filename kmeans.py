from random import sample

def kmeans(cluster_num, points, initial_centroids = None):
	centroids = sample(points, k=cluster_num) if initial_centroids is None else initial_centroids.copy()
	distribution = []
	coord_sum = [{'x': 0, 'y': 0, 'count': 0} for i in range(cluster_num)]

	for point in points:
		centroid_index = find_nearest_centroid(point, centroids)
		distribution.append(centroid_index)
		coord_sum[centroid_index]['x'] += point[0]
		coord_sum[centroid_index]['y'] += point[1]
		coord_sum[centroid_index]['count'] += 1

	for index in range(cluster_num):
		x = coord_sum[index]['x']/coord_sum[index]['count']
		y = coord_sum[index]['y']/coord_sum[index]['count']
		centroids[index] = (x, y)

	if centroids == initial_centroids:
		return centroids, distribution
	else:
		return kmeans(cluster_num, points, centroids)

def find_nearest_centroid(point, centroids):
	nearest_centroid_index = 0
	shortest_distance = squared_distance(point, centroids[0])
	for index in range(1, len(centroids)):
		distance = squared_distance(point, centroids[index])
		if distance < shortest_distance:
			shortest_distance = distance
			nearest_centroid_index = index
	return nearest_centroid_index

def squared_distance(pointA, pointB):
	return (pointA[0] - pointB[0])**2 + (pointA[1] - pointB[1])**2