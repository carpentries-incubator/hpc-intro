# -*- coding: utf-8 -*-

# This program generates a picture of the algorithm used to estimate the value
# of π by random sampling.

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as pltpatches

np.random.seed(14159625)

n = 128
x = np.random.uniform(size=n)
y = np.random.uniform(size=n)

with plt.xkcd():

    plt.figure(figsize=(5,5))
    plt.axis("equal")
    plt.xlim([-0.0125, 1.0125])
    plt.ylim([-0.0125, 1.0125])

    for d in ["left", "top", "bottom", "right"]:
        plt.gca().spines[d].set_visible(False)

    plt.xlabel("x", position=(0.8, 0))
    plt.ylabel("y", rotation=0, position=(0, 0.8))

    plt.xticks([0, 0.5, 1], ["0", "1/2", "1"])
    plt.yticks([0, 0.5, 1], ["0", "1/2", "1"])

    plt.scatter(x, y, s=8, c=np.random.uniform(size=(n,3)))

    circ = pltpatches.Arc((0, 0), width=2, height=2, angle=0, theta1=0, theta2=90, color="black", linewidth=3)
    plt.gca().add_artist(circ)
    squa = plt.Rectangle((0, 0), width=1, height=1, fill=None, linewidth=3)
    plt.gca().add_artist(squa)

    plt.savefig("pi.png", bbox_inches="tight", dpi=400)
