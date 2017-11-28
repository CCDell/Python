import math
import turtle
import sys
import random
import argparse
import numpy as np
from PIL import Image
from datetime import datetime
from fractions import gcd


'''
Noah Sanci
The Koch snowflake
This program will recursively craete a Koch snowflake. 

'''

def main():
    print("Generating the snowflake")
    turtle.title("Snowflake!")
    
    print("Please enter the recursive depth that will be reached, '1' being simply a triangle")
    depth = 0
    while depth <=0:
       depth = int(input())
    
    flake = Snowflake(depth)
    

'''

Every triangle is equilateral, meaning that the angles are 60 = degrees


'''


class Snowflake:
    def __init__(self, depth):
        self.maxDepth = depth
        self.t = turtle.Turtle()
        self.t.up()
        self.t.shape = ('arrow')
        
        self.sideLength = turtle.window_width()/8
        height = math.sin(math.radians(60)) * self.sideLength

        self.t.setx(0-self.sideLength/2);
        self.t.sety(0-height/2);
        self.t.down()
        self.draw(self.sideLength,self.maxDepth)

    def draw(self, sideLength,depth):
        sideLength = sideLength*(1/(3*self.maxDepth))
        
        for i in range(0,3):
            self.rdraw(sideLength, depth)
            self.t.forward(sideLength)
            self.t.left(120)
            
    def rdraw(self,sideLength,depth):
        
        if depth == 0:
            return
        
        self.rdraw(sideLength,depth-1)
        self.t.forward(sideLength)
        self.t.right(60)
        self.rdraw(sideLength,depth-1)
        self.t.forward(sideLength)
        self.t.right(240)
        self.rdraw(sideLength,depth-1)
        self.t.forward(sideLength)
        self.t.right(60)
        self.rdraw(sideLength,depth-1)
        
            
if __name__=='__main__':
    main()
