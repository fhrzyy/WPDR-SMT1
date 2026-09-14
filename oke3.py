import turtle
import time
import random

# Mengatur layar jendela baru
screen = turtle.Screen()
screen.setup(width=800, height=400)
screen.bgcolor("#1e1e24") # Latar belakang abu-abu gelap agar warna teks menyala
screen.title("Animasi Teks JTI POLIJE")

t = turtle.Turtle()
t.hideturtle()
t.penup()

# Daftar warna-warni untuk setiap huruf
warna_list = ["#FF5733", "#33FF57", "#3357FF", "#F3FF33", "#FF33F3", "#33FFF0", "#FFAF33", "#B233FF", "#33FFA8", "#FF3333"]

teks_target = "JTI POLIJE"

# Mengatur posisi awal teks agar berada di tengah layar
start_x = -300
y_position = -30 # Sedikit di bawah 0 agar pas di tengah vertikal
jarak_antar_huruf = 60

# Menampilkan huruf satu per satu dengan jeda waktu
for index, huruf in enumerate(teks_target):
    # Pindah ke posisi huruf berikutnya
    t.goto(start_x + (index * jarak_antar_huruf), y_position)
    
    # Pilih warna acak untuk huruf ini
    t.color(random.choice(warna_list))
    
    # Tulis hurufnya ke layar
    t.write(huruf, font=("Arial", 50, "bold"))
    
    # Efek jeda waktu (animasi) sebelum huruf berikutnya muncul
    time.sleep(0.4)

# Menjaga agar jendela tidak langsung tertutup saat animasi selesai
turtle.done()
