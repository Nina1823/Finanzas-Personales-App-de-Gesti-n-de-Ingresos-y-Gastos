import tkinter as tk

class RoundedButton(tk.Canvas):
    def __init__(self, parent, text, command, radius=20, padding=10,
                 bg_color="#5CA8D1", fg_color="white", font=("Arial", 12, "bold")):

        tk.Canvas.__init__(self, parent, borderwidth=0,
                           highlightthickness=0, bg=parent["bg"])

        self.command = command
        self.radius = radius
        self.bg_color = bg_color

        self.text_id = None

        # Dibujar botón
        self.draw_button(text, font, fg_color, padding)

        # Evento click
        self.bind("<Button-1>", lambda e: self.command())

    def draw_button(self, text, font, fg_color, padding):
        width = 150
        height = 40

        r = self.radius
        self.create_round_rect(0, 0, width, height, r, fill=self.bg_color, outline=self.bg_color)

        self.text_id = self.create_text(
            width // 2, height // 2,
            text=text, fill=fg_color, font=font
        )
        self.config(width=width, height=height)

    def create_round_rect(self, x1, y1, x2, y2, r, **kwargs):
        points = [
            x1+r, y1,
            x2-r, y1,
            x2, y1,
            x2, y1+r,
            x2, y2-r,
            x2, y2,
            x2-r, y2,
            x1+r, y2,
            x1, y2,
            x1, y2-r,
            x1, y1+r,
            x1, y1,
        ]
        return self.create_polygon(points, smooth=True, **kwargs)
