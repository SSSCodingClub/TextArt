import cv2
import numpy as np

density = '@#O%+=|i-:.        '
density_length = len(density)

scale = 5

def find_index(num, old_min, old_max, new_min, new_max):
    return (num - old_min) * (new_max - new_min) / (old_max - old_min) + new_min

def get_average(image, x, y):
    total = 0
    height, width = image.shape
    
    for j in range(y, min(y + scale, height)):
        for k in range(x, min(x + scale, width)):
            total += image[j, k]
    return total // pow(scale, 2)
            

def text_art_image(path):
    image = cv2.imread(path, 0) # grayscale image
    height, width = image.shape
    
    line = ""
    for index, i in np.ndenumerate(image):
        y, x = index
        
        if x % scale != 0 or y % scale != 0 or (x == 0 and y == 0):
            continue
        
        # GRAYSCALE 0 - 255
        # DENSITY 0 - 16

        line += density[int(find_index(get_average(image, x, y), 0, 255, 0, density_length - 1))]
        if x == 0 and y > 0:
            line += '\n'

    line += density[int(find_index(get_average(image, width//scale * scale, height//scale * scale), 0, 255, 0, density_length - 1))]

    with open("output.txt", "w") as f:
        f.write(line)        


text_art_image("input.png")