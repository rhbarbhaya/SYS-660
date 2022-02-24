import numpy as np
from matplotlib import pyplot as plt

###############################################################################
# The data (change all of this to your actual data, this is just a mockup)
variables = [
    'apple',
    'juice',
    'orange',
    'peach',
    'gum',
    'stones',
    'bags',
    'lamps',
]

base = 3000

lows = np.array([
    base - 246 / 2,
    base - 1633 / 2,
    base - 500 / 2,
    base - 150 / 2,
    base - 35 / 2,
    base - 36 / 2,
    base - 43 / 2,
    base - 37 / 2,
])

values = np.array([
    246,
    1633,
    500,
    150,
    35,
    36,
    43,
    37,
])

###############################################################################
# The actual drawing part

# The y position for each variable
ys = range(len(values))[::-1]  # top to bottom

# Plot the bars, one by one
for y, low, value in zip(ys, lows, values):
    # The width of the 'low' and 'high' pieces
    low_width = base - low
    high_width = low + value - base

    # Each bar is a "broken" horizontal bar chart
    plt.broken_barh(
        [(low, low_width), (base, high_width)],
        (y - 0.4, 0.8),
        facecolors=['white', 'white'],  # Try different colors if you like
        edgecolors=['black', 'black'],
        linewidth=1,
    )