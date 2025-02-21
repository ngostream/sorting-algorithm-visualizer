# ui.py

import matplotlib.pyplot as plot
import time

def visualize_sorting(array, sort_function, speed, title):
    plot.ion()
    fig, ax = plot.subplots()
    bars = ax.bar(range(len(array)), array, color='blue')

    def visualize(array):
        for bar, height in zip(bars, array):
            bar.set_height(height)
        plot.pause(speed)
        ax.clear()
        ax.bar(range(len(array)), array, color='blue')
    
    sort_function(array, visualize)
    plot.title(title)
    plot.show()
    plot.ioff()
