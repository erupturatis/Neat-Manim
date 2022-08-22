
from cProfile import label
from tokenize import Number
from turtle import circle
from manim import *
class OpeningManim(Scene):
    def construct(self):
        inputs = VGroup(*[Circle(radius=0.05, ) for _ in range(5)])
        inputs.arrange(UP, buff=0.05)
        inputs2 = VGroup(*[Circle(radius=0.05, ) for _ in range(5)])
        inputs2.arrange(LEFT, buff=0.05)
        inputs3 = VGroup(*[Circle(radius=0.05, ) for _ in range(10)])
        inputs3.arrange(LEFT)
        inputs.to_edge(UP, buff=0.5)
        inputs2.to_edge(LEFT, buff=0.5)
        inputs4 = VGroup(inputs, inputs2)
        self.add(inputs4, inputs3)
        
        self.play(Transform(inputs4, inputs3))

        self.wait()


