import pygame
import random
import color_blocks as cb
import time
 
colors = [
    "red", 
    "green", 
    "yellow", 
    "blue",
    ]
count_of_computer = 0
count_wanted = 4
pattern = []

while True:
    while count_wanted >= count_of_computer:
        random_color = random.choice(colors)
        pattern.append(random_color)
        count_of_computer += 1
        print(pattern)

