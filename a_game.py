import numpy as np

gsize = 200
bsize = gsize-1



def unimaker(universe):

    new_universe = np.zeros((gsize, gsize))


    new_universe[1:bsize, 1:bsize] = universe[1:bsize, 1:bsize]


    def num_neighbours(x, y):
        num = 0

        if x>=1 and x<=bsize and y>=1 and y<=bsize:
            if universe[x - 1, y - 1] != 0:
                num = num + 1

            if universe[x - 1, y] != 0:
                num = num + 1

            if universe[x - 1, y + 1] != 0:
                num = num + 1

            if universe[x, y - 1] != 0:
                num = num + 1

            if universe[x, y + 1] != 0:
                num = num + 1

            if universe[x + 1, y - 1] != 0:
                num = num + 1

            if universe[x + 1, y] != 0:
                num = num + 1

            if universe[x + 1, y + 1] != 0:
                num = num + 1

        return num

    def pow_neighbours(x, y):
        l = universe[x - 1, y - 1] + universe[x - 1, y] + \
              universe[x - 1, y + 1] + universe[x, y - 1] + \
              universe[x, y + 1] + universe[x + 1, y - 1] + \
              universe[x + 1, y] + universe[x + 1, y + 1]
        return l


    for x in range(0, bsize):
        for y in range(0, bsize):

            if not 2 <= num_neighbours(x,y) <= 3 and universe[x, y]:
                new_universe[x, y] = 0
            elif not universe[x, y] and num_neighbours(x, y) == 3:
                new_universe[x, y] = 1

    #import matplotlib.pyplot as plt
    #plt.imshow(universe, cmap='binary')
    #plt.show()

    return new_universe

