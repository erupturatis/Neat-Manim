from manim import *
class OpeningManim(Scene):
    def construct(self):

        polys = RegularPolygon(5, radius=1, fill_opacity = 0.5, color=RED)
        self.play(DrawBorderThenFill(polys), run_time=2)
        self.play(
            polys.animate.shift(UP)
        )
        self.wait()


