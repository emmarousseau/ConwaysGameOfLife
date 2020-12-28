
import numpy as np
import glob
from PIL import Image
import imageio


columns = 100
rows = 100
time_steps = 100

array = np.random.randint(2, size=[columns, rows], dtype=np.uint8)
filenames = []

cur_plan = np.random.randint(2, size=(columns, rows))
next_plan = np.random.randint(1, size=(columns, rows))


# Determining the state of the each cell in the next time-step
for step in range(time_steps):
    for y, i in enumerate(cur_plan):
        for x, j in enumerate(i):
            on_neighbors = 0
            
            for verti in range(y-1, y+2) :
                for horiz in range(x-1, x+2) :
                    on_neighbors += cur_plan[(verti+columns)%columns][(horiz+rows)%rows]
            on_neighbors -= cur_plan[y][x]

            # Game of life original rules
            if ((cur_plan[y,x] == 1) and (on_neighbors < 2)):
                next_plan[y,x]=0 
            elif ((cur_plan[y,x] == 1) and (on_neighbors > 3)):
                next_plan[y,x]=0 
            elif ((cur_plan[y,x] == 0) and (on_neighbors == 3)):
                next_plan[y,x]=1 
            # else the state doesn't change

    # convert to image and save in C:/Users/emmar_/ConwaysGameOfLifeimage_*.png
    image = Image.fromarray(np.uint8(next_plan*255)).convert('1')
    name = "ConwaysGameOfLife_"+str(step)+".png"
    image = image.resize((columns*10, rows*10), Image.ANTIALIAS)
    image.save("images/"+name, format="png")
    filenames.append("images/"+name)
    cur_plan = next_plan.copy()


# Code by @Amar https://stackoverflow.com/a/35943809
# Saving series of images as a GIF
gif_file = "C:/Users/emmar_/ConwaysGameOfLife/life_output.gif"
images = []
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave(gif_file, images)
