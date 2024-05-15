import turtle
import math

# Pencere oluşturma
window = turtle.Screen()
window.title("Çemberler Arası Çizgiler")
window.setup(width=400, height=400)

# Turtle objelerini oluşturma
pen = turtle.Turtle()
pen.speed(0)
pen.width(2)

# İki çemberin merkezi
x1, y1 = 0, 0

# İlk çemberi çizme (20 birim çap)
radius1 = 20 * 15
pen.penup()
pen.goto(x1, y1 - radius1)
pen.pendown()
pen.circle(radius1)

# İkinci çemberin merkezi
x2, y2 = 0, 0

# İkinci çemberi çizme (18 birim çap)
radius2 = 18 * 15
pen.penup()
pen.goto(x2, y2 - radius2)
pen.pendown()
pen.circle(radius2)

# Çizgileri çizme
num_lines = 40
for i in range(num_lines):
    angle = (360 / num_lines) * i
    x1_new = x1 + radius1 * math.cos(math.radians(angle))
    y1_new = y1 + radius1 * math.sin(math.radians(angle))
    x2_new = x2 + radius2 * math.cos(math.radians(angle))
    y2_new = y2 + radius2 * math.sin(math.radians(angle))
    pen.penup()
    pen.goto(x1_new, y1_new)
    pen.pendown()
    pen.goto(x2_new, y2_new)

# Çizimi tamamlama
pen.hideturtle()
window.mainloop()
