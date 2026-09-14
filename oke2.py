import turtle
import random

# Mengatur layar
screen = turtle.Screen()
screen.bgcolor("lightblue")  # Latar belakang hijau seperti rumput
screen.setup(width=800, height=600)
screen.title("Serangkaian Bunga Banyak")

t = turtle.Turtle()
t.speed(0)  # Kecepatan maksimal agar cepat selesai

# Daftar warna bunga yang bervariasi
warna_kelopak = ["red", "pink", "orange", "yellow", "purple", "white", "lightblue"]

# Fungsi untuk menggambar satu bunga
def gambar_bunga(x, y, ukuran):
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    # Pilih warna acak untuk kelopak
    warna = random.choice(warna_kelopak)
    t.color(warna)
    
    # Menggambar 6 kelopak
    for _ in range(6):
        t.begin_fill()
        t.circle(ukuran, 60)
        t.left(120)
        t.circle(ukuran, 60)
        t.left(120)
        t.end_fill()
        t.left(60)
        
    # Menggambar bagian tengah bunga (putik kuning)
    t.penup()
    t.goto(x, y - (ukuran * 0.2))
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    t.circle(ukuran * 0.3)
    t.end_fill()

# Menggambar 25 bunga di lokasi acak
for _ in range(25):
    posisi_x = random.randint(-350, 350)
    posisi_y = random.randint(-250, 250)
    ukuran_acak = random.randint(20, 50)  # Ukuran bunga bervariasi
    gambar_bunga(posisi_x, posisi_y, ukuran_acak)

# Selesai
t.hideturtle()
turtle.done()
