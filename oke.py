import turtle

# Mengatur layar dan kura-kura
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Simbol Love Python")

t = turtle.Turtle()
t.color("red")
t.fillcolor("red")
t.speed(1)

# Mulai mewarnai objek
t.begin_fill()

# Menggambar sisi kiri hati
t.left(140)
t.forward(180)

# Menggambar lengkungan kiri
t.circle(-90, 200)

# Menggambar lengkungan kanan
t.left(120)
t.circle(-90, 200)

# Menggambar sisi kanan hati
t.forward(180)

# Selesai mewarnai
t.end_fill()

# Menyembunyikan kura-kura dan mempertahankan jendela terbuka
t.hideturtle()
turtle.done()
