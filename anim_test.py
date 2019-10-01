"""
========================================
An animated image using a list of images
========================================

This examples demonstrates how to animate an image from a list of images (or
Artists).
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from a_game import unimaker

fig = plt.figure()

gsize = 200
bsize = gsize - 1
# ims is a list of lists, each row is a list of artists to draw in the
# current frame; here we are just animating one artist, the image, in
# each frame

universe = np.zeros((gsize, gsize))

beacon = np.zeros((gsize, gsize))
for i in range(0,bsize):
    for j in range(0,bsize):
        if i == 50 or j == 50 or i==j or i==bsize-j:
            beacon[i,j]=1

beacon = np.random.randint(2, size=(gsize, gsize))
universe[1:bsize, 1:bsize] = beacon[1:bsize, 1:bsize]

ims = []
for i in range(200):
    new_universe = unimaker(universe)
    #new_universe = unimaker(new_universe)
    universe = new_universe
    im = plt.imshow(new_universe, animated=True)
    ims.append([im])

ani = animation.ArtistAnimation(fig, ims, interval=1, blit=True,
                                repeat_delay=1000)

# Set up formatting for the movie files
Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)

ani.save('a_game.mp4', writer=writer)
# plt.show()

