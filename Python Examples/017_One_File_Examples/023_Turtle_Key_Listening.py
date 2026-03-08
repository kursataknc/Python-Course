import turtle as turtle_m
import random

# --- SABİTLER ---
MOVE_DISTANCE = 15
TURN_ANGLE = 10
WIDTH, HEIGHT = 800, 600

# --- KURULUM ---
screen = turtle_m.Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.title("Gelişmiş Turtle Çizim | W,A,S,D: Hareket | Space: Kalem | R: Renk | C: Temizle")

tim = turtle_m.Turtle()
tim.shape("turtle")
tim.color("blue")
tim.speed("fast")

# --- FONKSİYONLAR ---
def move_forwards():
    """Turtle'ı ileri hareket ettirir."""
    tim.forward(MOVE_DISTANCE)

def move_backwards():
    """Turtle'ı geri hareket ettirir."""
    tim.backward(MOVE_DISTANCE)

def turn_left():
    """Turtle'ı sola döndürür."""
    tim.left(TURN_ANGLE)

def turn_right():
    """Turtle'ı sağa döndürür."""
    tim.right(TURN_ANGLE)

def reset_screen():
    """Ekranı temizler ve turtle'ı başlangıç konumuna getirir."""
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

def toggle_pen():
    """Kalemi kaldırır veya indirir."""
    if tim.isdown():
        tim.penup()
    else:
        tim.pendown()

def change_color():
    """Turtle'ın rengini rastgele değiştirir."""
    r = random.random()
    g = random.random()
    b = random.random()
    tim.color(r, g, b)

def setup_controls():
    """Klavye kontrollerini ayarlar."""
    screen.listen()
    screen.onkeypress(move_forwards, "w")
    screen.onkeypress(move_backwards, "s")
    screen.onkeypress(turn_left, "a")
    screen.onkeypress(turn_right, "d")
    screen.onkey(reset_screen, "c")
    screen.onkey(toggle_pen, "space")
    screen.onkey(change_color, "r")

# --- ANA PROGRAM ---
print("Turtle ekranına tıklayın ve tuşları kullanın!")
print("-------------------------------------------------")
print("W: İleri, S: Geri, A: Sol, D: Sağ")
print("Space: Kalemi kaldır/indir")
print("R: Rastgele renk")
print("C: Ekranı temizle")
print("-------------------------------------------------")

setup_controls()
screen.mainloop()