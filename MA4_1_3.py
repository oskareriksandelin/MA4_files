
"""
Solutions to module 4
Review date:
"""

student = "Oskar Sandelin"
reviewer = ""

import math as m
import random as r
import concurrent.futures as futures
from time import perf_counter as pc
import functools as functools

def sphere_volume(n, d):
    # n is a list of set of coordinates
    # d is the number of dimensions of the sphere 
    
    #Generate points inside hypersphere with HOF
    points = [[r.uniform(-1, 1) for _ in range(d)] for _ in range(n)]
    points_inside = list(filter(lambda point: functools.reduce(lambda x, y: x + y, map(lambda x: x**2, point)) <= 1**2, points))
    
    #Ratio of points times the cube volume equals the approx volume
    V_approx = (len(points_inside)/n)*(2**d)
    
    #Print V_approx
    #print(f"The approximated V is {V_approx}")

    return V_approx

def hypersphere_exact(n,d):
    V_real = (m.pi ** (d / 2)) / m.gamma((d / 2) + 1) * (1 ** d) 
    return V_real

# parallel code - parallelize for loop
def sphere_volume_parallel1(n,d,np):
     #using multiprocessor to perform 10 iterations of volume function 
    start = pc()
    result = []
    with futures.ProcessPoolExecutor() as ex:
        tasks = [ex.submit(sphere_volume, n, d) for _ in range(np)]
        for f in futures.as_completed(tasks):
            result.append(f.result())
    end = pc()
    print(f"Parallel version 1 took: {end - start} seconds")
    return sum(result) / np 

# parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel2(n,d,np):
    start = pc()
    split = n//np
    result = []
    with futures.ProcessPoolExecutor() as ex:
        tasks = [ex.submit(sphere_volume, split, d) for _ in range(np)]
        for f in futures.as_completed(tasks):
            result.append(f.result())
    end = pc()
    print(f"Parallel version 2 took: {end - start} seconds")
    return sum(result) / np

def main():
    # part 1 -- parallelization of a for loop among 10 processes 
    n = 100000
    d = 11
    np = 10
    
    # Non-parallel version (1.2)
    start = pc()
    for y in range (np):
        sphere_volume(n,d)
    print(f"Non-parallel version took: {pc()-start} seconds")

    #Parallel version (1.3)
    print(sphere_volume_parallel1(n,d,np))

    # part 2 -- parallelization of the actual computations by splitting the data
    #Parallel version (1.3)
    print(sphere_volume_parallel2(n,d,np))

if __name__ == '__main__':
	main()
