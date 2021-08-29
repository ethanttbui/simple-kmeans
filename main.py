from kmeans import kmeans
from matplotlib.pyplot import *
from random import randint

def visualize(points, centroids, distribution):
	colors = [next(gca()._get_lines.prop_cycler)['color'] for i in range(len(centroids))]

	for index, point in enumerate(points):
		plot(point[0], point[1], marker='o', color=colors[distribution[index]])

	for centroid in centroids:
		plot(centroid[0], centroid[1], marker='x', color='red')

	savefig('kmeans.png')

def main(argv):
	cluster_num = int(argv[0])
	point_num = int(argv[1])
	max_coordinate = int(argv[2])
	points = {(randint(0, max_coordinate), randint(0, max_coordinate)) for i in range(point_num)}
	centroids, distribution = kmeans(cluster_num, points)
	visualize(points, centroids, distribution)

if __name__== '__main__':
	main(sys.argv[1:])