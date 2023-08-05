import csv
import numpy as np
import PIL
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection
from matplotlib.backend_bases import MouseButton
from matplotlib.widgets import Button
import time as timepack
import random
import turtle
import matplotlib.pyplot
from PIL import Image, ImageOps
class plot_project:
    # This is the initialization function of the class
    def __init__(self):
        # Initialize the figure and set the size
        self.fig, self.ax = plt.subplots(figsize=(8, 8))

        # Set the axis limits
        self.ax.set(xlim=(-20, 20), ylim=(-20, 20))

        # Initialize the patches list
        self.patches = []
        # Set the background color of the plot
        self.ax.set_facecolor('indigo')
        # Initialize the drawing flag
        self.is_drawing = False
        self.drawn_points = []

        # Connect the mouse button press and release events
        self.fig.canvas.mpl_connect('button_press_event', self.left_click)
        self.fig.canvas.mpl_connect('button_release_event', self.release_left_click)
        self.fig.canvas.mpl_connect('motion_notify_event', self.while_holding_left_click)
        self.fig.canvas.mpl_connect('button_press_event', self.change_background_color)
        self.fig.canvas.mpl_connect('key_press_event', self.clear_markers)
    def draw_static_rectangle(self, x, y, height, width):
        # add a rectangle
        rect = mpatches.Rectangle((x, y), width, height, ec="none")
        self.patches.append(rect)

    def draw_rectangle(self): # Puts 4 rectangles to make a frame
        self.draw_static_rectangle(-10, -12, 2, 20)
        p = PatchCollection(self.patches, alpha=1)
        p.set_facecolor('black')
        self.ax.add_collection(p)
        self.patches = []

        self.draw_static_rectangle(-10, -12, 20, 2)
        p = PatchCollection(self.patches, alpha=1)
        p.set_facecolor('black')
        self.ax.add_collection(p)
        self.patches = []

        self.draw_static_rectangle(-10, 8, 2, 20)
        p = PatchCollection(self.patches, alpha=1)
        p.set_facecolor('black')
        self.ax.add_collection(p)
        self.patches = []

        self.draw_static_rectangle(8, -12, 20, 2)
        p = PatchCollection(self.patches, alpha=1)
        p.set_facecolor('black')
        self.ax.add_collection(p)
        self.patches = []

    def left_click(self, event):
        if event.button == MouseButton.LEFT:
            self.is_drawing = True
            self.drawn_points = [(event.xdata, event.ydata)]

    def release_left_click(self, event):
        if event.button == MouseButton.LEFT:
            self.is_drawing = False
            self.drawn_points = []

    def while_holding_left_click(self, event): # When user holds let click, markers will be added where the x and y coordinates are saved to the list in the previous 2 functions
        if self.is_drawing:
            self.drawn_points.append((event.xdata, event.ydata))
            x, y = zip(*self.drawn_points)
            self.ax.scatter(x, y, marker='*', s=100, color='yellow')
            self.fig.canvas.draw()

    def change_background_color(self, event):
        if event.button == MouseButton.RIGHT: # When user right clicks, the background will change color
            colors = ['red', 'green', 'blue', 'salmon', 'purple']
            color = random.choice(colors)
            self.ax.set_facecolor(color)
            self.fig.canvas.draw()

    def clear_markers(self, event):
        if event.key == 'x':
            self.ax.cla()  # Clear the plot
            self.ax.set(xlim=(-20, 20), ylim=(-20, 20))  # Set the axis limits
            self.draw_rectangle()  # Redraw the rectangle
            plt.imshow(My_Image, extent=(-8, 8, -10, 8))
            self.fig.canvas.draw()

if __name__ == '__main__':
    project = plot_project()
    project.draw_rectangle()
    FileName = 'Milo.jpg'
    My_Image = PIL.Image.open(FileName)  # Open image file into memory (doesn't display the picture)
    My_Image = ImageOps.exif_transpose(My_Image)
    plt.imshow(My_Image, extent=(-8, 8, -10, 8))  # Plot the image and set the extent to match the axis limits
    plt.title("Shrey Bosamia, Interactive Portrait")
    plt.show()
    project.fig.savefig('bosamia_portrait')  # Save the plot figure before showing it