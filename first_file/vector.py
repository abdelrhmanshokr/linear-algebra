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
        orthognal = False
        if self.dot_product(v) == 0:
            orthognal = True
        
        return orthognal

    def projection(self, v_vector):
        #this function returns the projection vector of the v_vector into the base vector self
        #note that self is the base b vector and v_vector is the vector which is required to make projection into the base vector 
        try:
            base_vector_dot_v_vector = self.dot_product(v_vector)
            mag_of_v_vector = base_vector_dot_v_vector / self.magnitude()
            #dividing once more over mag of the base vector
            mag_of_v_vector = mag_of_v_vector / self.magnitude()
            v_parallel_result = self.scale_mul(mag_of_v_vector)
        except ZeroDivisionError as error:
            print(error)
        
        return v_parallel_result

    def v_orthognal(self, v_vector):
        #this function returns the orthognal vector as the v_vector is projected over the base vector self
        #the general form is v_vector = v_parallel + v_orthognal
        # v_parallel= self.projection(v_vector)
        # v_orthognal = Vector.sub(v_vector, v_parallel)

        # return v_orthognal
        return 'there is an issue with this function'

    def composing_a_vector_into_two_components(self, v_vector):
        #sovlv the above method first 
        return 'solve the above method first'
    
    def cross_product(self, v):
        #this function returns the cross product result for two dimension or three dimension vectors
        cross_product_result = []
        cross_product_result.append((self.coordinates[1] * v.coordinates[2]) - (self.coordinates[2] * v.coordinates[1]))
        cross_product_result.append((self.coordinates[2] * v.coordinates[0]) - (self.coordinates[0] * v.coordinates[2]))
        cross_product_result.append((self.coordinates[0] * v.coordinates[1]) - (self.coordinates[1] * v.coordinates[0]))

        return cross_product_result  

    def area_of_parallelgram(self, v):
        cross_product_result = self.cross_product(v)
        magnitude_result = 0
        
        for i in range(len(cross_product_result)):
            magnitude_result +=(math.pow(cross_product_result[i], 2))
        
        return math.sqrt(magnitude_result)    
    
    def area_of_triangle(self, v):
        return (self.area_of_parallelgram(v) / 2)
        
v1 = Vector([8.462, 7.893, -8.187])
v2 = Vector([6.984, -5.975, 4.778])

print('addition', Vector.add(v1, v2))
print('subtraction', Vector.sub(v1, v2))
print('scale mulitblication', Vector.scale_mul(v1, 10))
print('magnitude', Vector.magnitude(v1))
print('direction', Vector.direction(v2))
print('dot poduct', Vector.dot_product(v1, v2))
print('angel of dot product', Vector.angel(v1, v2))
print('is it parallel', Vector.is_parallel(v1, v2))
print('is it orthognal', Vector.is_orthognal(v1, v2))
print('this is the projection result', Vector.projection(v1, v2))
print('this is the orthognal vector on the base vector in projection', Vector.v_orthognal(v1, v2))
# print('this is decomposing of a vector v into two vectors one orthognal and the other parallel to the base vector b', Vector.decomposing_vector_into_a_parallel_and_an_orthognal_to_the_base(v1, v2))
print('this is the cross product result', Vector.cross_product(v1, v2))
print('this is the area of the parallelgram in the cross product', Vector.area_of_parallelgram(v1, v2))
print('this is the area of the triangle in the cross product', Vector.area_of_triangle(v1, v2))