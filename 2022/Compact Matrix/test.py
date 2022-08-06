import sys
import copy


from manim import *
config.background_color='#170526'
from manim_fonts import *
import itertools as it
from tkinter import font
from turtle import bgcolor
from numpy import array
from color import*

######

'''
class RiemannRectanglesAnimation(GraphScene):
    CONFIG = {
        "y_max": 8,
        "y_axis_height": 5,
        "init_dx":0.5,
    }
    def construct(self):
        self.setup_axes()
        def func(x):
            return 0.1 * (x + 3-5) * (x - 3-5) * (x-5) + 5

        graph=self.get_graph(func,x_min=0.3,x_max=9.2)
        kwargs = {
            "x_min" : 2,
            "x_max" : 8,
            "fill_opacity" : 0.75,
            "stroke_width" : 0.25,
        }
        flat_rectangles = self.get_riemann_rectangles(
                                self.get_graph(lambda x : 0),
                                dx=self.init_dx,
                                start_color=invert_color(PURPLE),
                                end_color=invert_color(ORANGE),
                                **kwargs
        )
        riemann_rectangles_list = self.get_riemann_rectangles_list(
                                graph,
                                6,
                                max_dx=self.init_dx,
                                power_base=2,
                                start_color=PURPLE,
                                end_color=ORANGE,
                                 **kwargs
        )
        self.add(graph)
        # Show Riemann rectangles
        self.play(ReplacementTransform(flat_rectangles,riemann_rectangles_list[0]))
        self.wait()
        for r in range(1,len(riemann_rectangles_list)):
            self.transform_between_riemann_rects(
                    riemann_rectangles_list[r-1],
                    riemann_rectangles_list[r],
                    replace_mobject_with_target_in_scene = True,
                )
        self.wait()
'''

class IntegerTableExample(Scene):
    def construct(self):
        t0 = IntegerTable(
            [[0,30,45,60,90],
            [90,60,45,30,0]],
            col_labels=[
                MathTex("\\frac{\sqrt{0}}{2}"),
                MathTex("\\frac{\sqrt{1}}{2}"),
                MathTex("\\frac{\sqrt{2}}{2}"),
                MathTex("\\frac{\sqrt{3}}{2}"),
                MathTex("\\frac{\sqrt{4}}{2}")],
            row_labels=[MathTex("\sin"), MathTex("\cos")],
            h_buff=1,
            element_to_mobject_config={"unit": "^{\circ}"})
        t0.set_color_by_gradient(REANLEA_WARM_BLUE,REANLEA_GREEN_LIGHTER,REANLEA_CHARM,REANLEA_WARM_BLUE_DARKER,REANLEA_VIOLET,REANLEA_PURPLE_DARK_FILL)
        self.play(
            Create(t0, run_time=5)
        )
        self.wait()


