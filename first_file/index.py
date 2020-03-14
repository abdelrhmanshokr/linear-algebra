import math
import numpy as np


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
        #we need to add a try block here to make usre we won't divide by 0
        try:
            direction_result = self.scale_mul(1 / magnitude)
        except ZeroDivisionError as error:
            return error

        return direction_result 


    def dot_product(self, v):
        dot_product_result = 0

        for i in range(len(self.coordinates)):
            dot_product_result += self.coordinates[i] * v.coordinates[i]

        return dot_product_result

    def angel(self, v, in_degrees = False):
        try:
            angel = 0

            dot_product = self.dot_product(v)
            total_magnitude = self.magnitude() * v.magnitude()

            angel = math.acos(dot_product / total_magnitude)

            #check if the angel is required by red or degrees
            if in_degrees:
                angel_in_rad = angel * 180 * 7 / 22 
                return angel_in_rad
            else:
                return angel
        except ZeroDivisionError as error:
            return error

    def is_parallel(self, v):
        try:
            parallel = True
            ratio = self.coordinates[0] / v.coordinates[0]
            for i in range(len(self.coordinates)):
                new_ratio = self.coordinates[i] / v.coordinates[i]
                if new_ratio != ratio:
                    parallel = False
                    break
            return parallel
        except ZeroDivisionError as error:
            return error 

    def is_orthognal(self, v):
        if self.dot_product(v) == 0:
            orthognal = True
        else:
            orthognal = False
        
        return orthognal

v1 = Vector([-7.579,-7.88])
v2 = Vector([22.737, 23.64])

print('addition', Vector.add(v1, v2))
print('subtraction', Vector.sub(v1, v2))
print('scale mulitblication', Vector.scale_mul(v1, 10))
print('magnitude', Vector.magnitude(v1))
print('direction', Vector.direction(v2))
print('dot poduct', Vector.dot_product(v1, v2))
print('angel of dot product', Vector.angel(v1, v2))
print('is it parallel', Vector.is_parallel(v1, v2))
print('is it orthognal', Vector.is_orthognal(v1, v2))
