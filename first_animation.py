
from manim import *
import numpy as np

config.pixel_width = 720
config.pixel_height = 1280
config.frame_width = 7.2
config.frame_height = 12.8
config.background_color = "#0B1020"

# Colour palette
WHITE = "#F1F5F9"
BLUE = "#38BDF8"
PURPLE = "#A78BFA"
GOLD = "#FBBF24"
GREEN = "#34D399"
PINK = "#FB7185"


class PythagoreanProof(Scene):

    def construct(self):
        title = Text(
            "PYTHAGOREAN THEOREM",
            font_size=35,
            color=WHITE,
            weight=BOLD
        ).to_edge(UP, buff=0.8)

        subtitle = Text(
            "A proof using only a square",
            font_size=26,
            color=BLUE
        ).next_to(title, DOWN, buff=0.25)

        self.play(
            FadeIn(title, shift=DOWN),
            FadeIn(subtitle, shift=DOWN),
            run_time=1
        )

        self.wait(0.6)

        hook = Text(
            "Can a square prove this?",
            font_size=31,
            color=GOLD,
            weight=BOLD
        ).move_to(ORIGIN)

        self.play(
            FadeOut(subtitle),
            FadeIn(hook, scale=0.9),
            run_time=0.6
        )

        self.wait(0.8)
        self.play(FadeOut(hook))


        a = 2
        b = 4
        L = a + b

        scale = 0.62
        center = DOWN * 0.3

        def P(x, y):
            return center + scale * np.array([
                x - L / 2,
                y - L / 2,
                0
            ])

        triangle = Polygon(
            P(0, 0),
            P(a, 0),
            P(0, b),
            color=BLUE,
            fill_color=BLUE,
            fill_opacity=0.45,
            stroke_width=4
        )

        side_a = Line(P(0, 0), P(a, 0), color=GOLD)
        side_b = Line(P(0, 0), P(0, b), color=PURPLE)
        side_c = Line(P(a, 0), P(0, b), color=GREEN)

        label_a = Text("a", font_size=27, color=GOLD)
        label_a.next_to(side_a, DOWN, buff=0.1)

        label_b = Text("b", font_size=27, color=PURPLE)
        label_b.next_to(side_b, LEFT, buff=0.1)

        label_c = Text("c", font_size=27, color=GREEN)
        label_c.move_to(
            side_c.get_center() + RIGHT * 0.25
        )

        right_angle = Square(
            side_length=0.22,
            color=WHITE,
            stroke_width=2
        ).move_to(P(0.11, 0.11))

        triangle_text = Text(
            "A right-angled triangle",
            font_size=27,
            color=WHITE
        ).next_to(title, DOWN, buff=0.35)

        self.play(
            FadeIn(triangle_text),
            Create(triangle),
            run_time=0.8
        )

        self.play(
            Create(side_a),
            Create(side_b),
            Create(side_c),
            FadeIn(label_a),
            FadeIn(label_b),
            FadeIn(label_c),
            FadeIn(right_angle),
            run_time=0.8
        )

        self.wait(0.7)

        self.play(
            FadeOut(triangle_text),
            FadeOut(triangle),
            FadeOut(side_a),
            FadeOut(side_b),
            FadeOut(side_c),
            FadeOut(label_a),
            FadeOut(label_b),
            FadeOut(label_c),
            FadeOut(right_angle),
            run_time=0.5
        )

        outer = Polygon(
            P(0, 0),
            P(L, 0),
            P(L, L),
            P(0, L),
            color=WHITE,
            stroke_width=4
        )

        square_title = Text(
            "Construct a square of side a + b",
            font_size=27,
            color=BLUE
        ).next_to(title, DOWN, buff=0.35)

        self.play(
            FadeIn(square_title),
            Create(outer),
            run_time=0.8
        )


        top_label = Text(
            "a + b",
            font_size=25,
            color=GOLD
        ).next_to(outer.get_top(), UP, buff=0.12)

        bottom_label = Text(
            "a + b",
            font_size=25,
            color=GOLD
        ).next_to(outer.get_bottom(), DOWN, buff=0.12)

        left_label = Text(
            "a + b",
            font_size=23,
            color=GOLD
        ).next_to(outer.get_left(), LEFT, buff=0.12)

        right_label = Text(
            "a + b",
            font_size=23,
            color=GOLD
        ).next_to(outer.get_right(), RIGHT, buff=0.12)

        self.play(
            FadeIn(top_label),
            FadeIn(bottom_label),
            FadeIn(left_label),
            FadeIn(right_label),
            run_time=0.5
        )

        self.wait(0.4)


        triangles = VGroup(

            # Bottom-left
            Polygon(
                P(0, 0), P(a, 0), P(0, b),
                color=BLUE,
                fill_color=BLUE,
                fill_opacity=0.5,
                stroke_width=2
            ),

            # Bottom-right
            Polygon(
                P(L, 0), P(L, a), P(L-b, 0),
                color=PURPLE,
                fill_color=PURPLE,
                fill_opacity=0.5,
                stroke_width=2
            ),

            # Top-right
            Polygon(
                P(L, L), P(L-a, L), P(L, L-b),
                color=GOLD,
                fill_color=GOLD,
                fill_opacity=0.5,
                stroke_width=2
            ),

            # Top-left
            Polygon(
                P(0, L), P(0, L-a), P(b, L),
                color=PINK,
                fill_color=PINK,
                fill_opacity=0.5,
                stroke_width=2
            )
        )

        self.play(
            LaggedStart(
                *[FadeIn(t) for t in triangles],
                lag_ratio=0.12
            ),
            run_time=1
        )


        center_square = Polygon(
            P(a, 0),
            P(0, b),
            P(b, L),
            P(L, a),
            color=GREEN,
            fill_color=GREEN,
            fill_opacity=0.65,
            stroke_width=3
        )

        self.play(
            Create(center_square),
            run_time=0.8
        )

        center_label = Text(
            "c²",
            font_size=35,
            color=WHITE,
            weight=BOLD
        ).move_to(center_square.get_center())

        self.play(FadeIn(center_label, scale=1.2))



        self.wait(0.5)

        area_text = Text(
            "Area of the large square:",
            font_size=27,
            color=WHITE
        ).move_to(DOWN * 3.7)

        equation1 = Text(
            "(a + b)² = a² + 2ab + b²",
            font_size=29,
            color=GOLD
        ).next_to(area_text, DOWN, buff=0.25)

        self.play(
            FadeIn(area_text),
            Write(equation1),
            run_time=1
        )

        self.wait(0.8)

 
        self.play(
            FadeOut(area_text),
            FadeOut(equation1),
            run_time=0.4
        )

        area_text2 = Text(
            "Same square, different pieces:",
            font_size=27,
            color=WHITE
        ).move_to(DOWN * 3.7)

        equation2 = Text(
            "4 × (1/2 ab) + c²",
            font_size=30,
            color=GREEN
        ).next_to(area_text2, DOWN, buff=0.25)

        explanation = Text(
            "(4 triangles + central square)",
            font_size=22,
            color=WHITE
        ).next_to(equation2, DOWN, buff=0.15)

        self.play(
            FadeIn(area_text2),
            Write(equation2),
            FadeIn(explanation),
            run_time=0.8
        )

        self.wait(0.8)

     

        self.play(
            FadeOut(area_text2),
            FadeOut(equation2),
            FadeOut(explanation),
            run_time=0.4
        )

        compare = Text(
            "Both expressions equal the same area!",
            font_size=26,
            color=BLUE
        ).move_to(DOWN * 3.7)

        equation3 = Text(
            "a² + 2ab + b² = 2ab + c²",
            font_size=27,
            color=WHITE
        ).next_to(compare, DOWN, buff=0.3)

        self.play(
            FadeIn(compare),
            Write(equation3),
            run_time=0.8
        )

        self.wait(0.8)

  
        self.play(
            FadeOut(compare),
            FadeOut(equation3),
            run_time=0.4
        )

        final_title = Text(
            "Subtract 2ab from both sides",
            font_size=26,
            color=WHITE
        ).move_to(DOWN * 3.7)

        final_equation = Text(
            "a² + b² = c²",
            font_size=52,
            color=GREEN,
            weight=BOLD
        ).next_to(final_title, DOWN, buff=0.4)

        final_box = SurroundingRectangle(
            final_equation,
            color=GREEN,
            buff=0.25,
            stroke_width=3
        )

        self.play(
            FadeIn(final_title),
            Write(final_equation),
            Create(final_box),
            run_time=1
        )

        self.wait(1.5)

        ending = Text(
            "Hence proved.",
            font_size=30,
            color=GOLD,
            weight=BOLD
        ).next_to(final_box, DOWN, buff=0.35)

        self.play(
            FadeIn(ending, shift=UP),
            run_time=0.5
        )

        self.wait(1)
