
from cProfile import label
from manim import *
class OpeningManim(Scene):
    def construct(self):
        ax = Axes(x_range=(-6,6), y_range=(-20,20))
        curve = ax.plot( lambda x: x**3)
        self.add(ax, curve)