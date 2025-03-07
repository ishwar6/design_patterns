import numpy as np

class Structure:
    def __init__(self, vertices):
        self.vertices = np.array(vertices)
        self.edges = self.calculate_edges()

    def calculate_edges(self):
        edge_list = []
        num_vertices = self.vertices.shape[0]
        for i in range(num_vertices):
            for j in range(i + 1, num_vertices):
                edge_list.append((i, j))
        return edge_list

    def get_centroid(self):
        return np.mean(self.vertices, axis=0)

    def scale(self, factor):
        self.vertices *= factor

    def translate(self, vector):
        self.vertices += np.array(vector)

    def rotate(self, angle, axis):
        axis = np.array(axis) / np.linalg.norm(axis)
        angle_rad = np.radians(angle)
        cos_theta = np.cos(angle_rad)
        sin_theta = np.sin(angle_rad)
        rotation_matrix = np.array([
            [cos_theta + axis[0]**2 * (1 - cos_theta), axis[0] * axis[1] * (1 - cos_theta) - axis[2] * sin_theta, axis[0] * axis[2] * (1 - cos_theta) + axis[1] * sin_theta],
            [axis[1] * axis[0] * (1 - cos_theta) + axis[2] * sin_theta, cos_theta + axis[1]**2 * (1 - cos_theta), axis[1] * axis[2] * (1 - cos_theta) - axis[0] * sin_theta],
            [axis[2] * axis[0] * (1 - cos_theta) - axis[1] * sin_theta, axis[2] * axis[1] * (1 - cos_theta) + axis[0] * sin_theta, cos_theta + axis[2]**2 * (1 - cos_theta)]
        ])
        self.vertices = self.vertices.dot(rotation_matrix.T)

    def __str__(self):
        return f'Structure(vertices={self.vertices.tolist()}, edges={self.edges})'

if __name__ == "__main__":
    cube = Structure(vertices=[[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0], 
                               [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]])
    print(cube)
    cube.scale(2)
    print(cube)
    cube.translate([1, 1, 1])
    print(cube)
    cube.rotate(90, [0, 1, 0])
    print(cube)