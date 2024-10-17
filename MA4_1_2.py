
"""
Solutions to module 4
Review date:
"""

student = ""
reviewer = ""

import math as m
import random as random
import functools as functools

# def sphere_volume_first_try(n, d, r=1):
#     # n is a list of set of coordinates
#     # d is the number of dimensions of the sphere 
#     inside_point = 0
#     cube_volume = 2**d
#     #Generate points inside hypersphere
#     for _ in range(n):
#         point = [random.uniform(-1,1) for _ in range(d)]
#         if sum(x**2 for x in point) <= r:
#             inside_point += 1
    
#     #Ratio of points times the cube volume equals the approx volume
#     V_approx = (inside_point/n)*cube_volume
    
#     #Print V_approx
#     print(f"The approximated V is {V_approx}")

#     return V_approx

#Improved with HOF
def sphere_volume(n, d, r=1):
    # n is a list of set of coordinates
    # d is the number of dimensions of the sphere 
    
    #Generate points inside hypersphere with HOF
    points = [[random.uniform(-r, r) for _ in range(d)] for _ in range(n)]
    points_inside = list(filter(lambda point: functools.reduce(lambda x, y: x + y, map(lambda x: x**2, point)) <= r**2, points))
    
    #Ratio of points times the cube volume equals the approx volume
    V_approx = (len(points_inside)/n)*(2**d)
    
    #Print V_approx
    print(f"The approximated V is {V_approx}")

    return V_approx

def hypersphere_exact(n,d,r=1):
    V_real = (m.pi ** (d / 2)) / m.gamma((d / 2) + 1) * (r ** d) 
    return V_real
     
def main():
    n = 100000
    d = 11
    sphere_volume(n,d)


if __name__ == '__main__':
	main()
