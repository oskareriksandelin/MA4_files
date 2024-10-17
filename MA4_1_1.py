
"""
Solutions to module 4
Review date:
"""

student = "Oskar Sandelin"
reviewer = ""


import random as r
import matplotlib.pyplot as plt 
import math

def approximate_pi(n, plot = False):
    random_points = [(r.uniform(-1,1),r.uniform(-1,1)) for _ in range(n)]
    
    #Classify the points
    cirkle_points = [(x,y) for (x,y) in random_points if x**2 + y**2 <= 1]
    outside_points = [(x,y) for (x,y) in random_points if x**2 + y**2 >= 1]
    
    #Approximate pi
    approx_pi = (4*len(cirkle_points))/len(random_points)
    real_pi = math.pi

    print(f"Approximation of pi with {n} points: {approx_pi}")
    print(f"Real pi: {real_pi}")

    if plot: 
        #Plots for points inside and outside the cirkle
        #HOF zip is used to unpack the coordinates from the lists
        plt.scatter(*zip(*cirkle_points), color='red', label='Inside Circle', s=10)
        plt.scatter(*zip(*outside_points), color='blue', label='Outside Circle', s=10)

        #To make the cirkle look like a cirkle
        plt.gca().set_aspect('equal', adjustable='box')

        plt.title('Monte carlo sim of points outside and inside cirkle')
        plt.xlabel('X coord')
        plt.ylabel('Y coord')
        plt.legend()
        plt.show()

    return approx_pi
    
def main():
    dots = [1000, 10000, 100000]
    for n in dots:
        approximate_pi(n, True)

if __name__ == '__main__':
	main()
