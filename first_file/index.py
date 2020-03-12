import math 

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def add(self, v):
        addition_result = []

        for i in range(len(self.coordinates)):
            addition_result.append(self.coordinates[i] + v.coordinates[i])
        
        return addition_result

    def sub(self, v):
        subtration_result = []

        for i in range(len(self.coordinates)):
            subtration_result.append(self.coordinates[i] - v.coordinates[i])

        return subtration_result

    def scale_mul(self, scalar):
        scale_mul_result = []

        for i in range(len(self.coordinates)):
            scale_mul_result.append(self.coordinates[i] * scalar)

        return scale_mul_result 

    def magnitude(self):
        magnitude_result = 0
        
        for i in range(len(self.coordinates)):
            magnitude_result +=(math.pow(self.coordinates[i], 2))
        
        return math.sqrt(magnitude_result)

    def direction(self):
        magnitude = self.magnitude()
        direction_result = self.scale_mul(1 / magnitude)
        return direction_result 


v1 = Vector([-0.221, 7.437])
v2 = Vector([5.581, -2.136])

print('addition', Vector.add(v1, v2))
print('subtraction', Vector.sub(v1, v2))
print('scale mulitblication', Vector.scale_mul(v1, 10))
print('magnitude', Vector.magnitude(v1))
print('directoin', Vector.direction(v2))