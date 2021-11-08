#PART E
#Menggunakan library pygame dan import time dari local library
import pygame, sys
from pygame import rect
from pygame.locals import *
import time

WIDTH, HEIGHT = 600, 480            #Mengatur ukuran layar
TITLE = "Tugas 4(Prak.Game Dev)"    #Membuat variabel TITLE sebagai nama jendela

pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))  #Mengatur ukuran layar dari kotak dialog program
pygame.display.set_caption(TITLE)               #Menampilkan nilai dari variabel TITLE
clock = pygame.time.Clock()

#Membuat variabel warna dengan hexcode
BLACK = ("#000000")
RED = ("#ff0000")
GREEN = ("#01B050")
BLUE = ("#01B0F0")
DARKBLU = ("#1F4E78")

#PART D
#Membuat class Player. Terdapat pengaturan sumbu x dan y.
#Pergerakan player sendiri berkondisi False agar objek tidak berjalan otomatis tanpa adanya kontrol dari pemain.
class Player:
    def __init__(self, x, y):                            #Membuat fungsi untuk objek => jarak, warna dan ukuran(x,y)
        self.x = int(x)
        self.y = int(y)
        self.rect = pygame.Rect(self.x, self.y, 32, 32)
        self.color = (1, 176, 80)
        self.velX = 0
        self.velY = 0
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.speed = 4

    #PART F
    #Membuat fungsi draw
    def draw(self, win): 
        pygame.draw.rect(win, self.color, self.rect)

    #PART A
    #Membuat fungsi update dengan paramater self untuk mengatur tombol keyboard dan batas objek
    def update(self):
        self.velX = 0
        self.velY = 0
        if self.left_pressed and not self.right_pressed and self.x > 0 :
            self.velX = -self.speed
        if self.right_pressed and not self.left_pressed and self.x < 570 :
            self.velX = self.speed
        if self.up_pressed and not self.down_pressed and self.y > 0 :
            self.velY = -self.speed
        if self.down_pressed and not self.up_pressed and self.y < 450 :
            self.velY = self.speed

        self.x += self.velX
        self.y += self.velY

        self.rect = pygame.Rect(int(self.x), int(self.y), 32, 32)

#PART B
#Var player untuk menyimpan yang dibutuhkan objek dr fungsi Player 
player = Player(WIDTH/2, HEIGHT/2)
# Menampilkan teks pada program
font_color = (BLACK)
font_obj = pygame.font.Font("C:\Windows\Fonts\ARLRDBD.TTF", 25)     #Mengambil jenis font yg ada pada komputer dan ukuran 25 
text = "Isnan Nur Ahmad Wijayakusuma"
img = font_obj.render(text, True, (BLUE))                          #Warna teks, dan teks disimpan dlm var img

rect = img.get_rect()
rect.topleft = (20, 20)
cursor = Rect(rect.topright, (3, rect.height))

#Perulangan untuk menggerakkan objek dengan menggunakan tombol arrow pada keyboard 
while True:
    #Mengatur keluar game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        #Mengatur keyboard agar bisa berjalan
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.left_pressed = True
            if event.key == pygame.K_RIGHT:
                player.right_pressed = True
            if event.key == pygame.K_UP:
                player.up_pressed = True
            if event.key == pygame.K_DOWN:
                player.down_pressed = True

         #Pengaturan keyboard yang tidak bisa berjalan bersamaan
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.left_pressed = False
            if event.key == pygame.K_RIGHT:
                player.right_pressed = False
            if event.key == pygame.K_UP:
                player.up_pressed = False
            if event.key == pygame.K_DOWN:
                player.down_pressed = False

            if event.type == QUIT:
                running = False

            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    if len(text) > 0:
                        text = text[:-1]

                else:
                    text += event.unicode
                    img = font_obj.render(text, True, BLUE)
                    rect.size = img.get_size()
                    cursor.topleft = rect.topright

    #PART C
    #Untuk mengatur hal-hal penting agar bisa menampilkan program
    win.fill((DARKBLU))
    pygame.draw.rect(win, (GREEN), player)

    win.blit(img, rect)
    if time.time() % 1 > 0.5:
        pygame.draw.rect(win, BLUE, cursor)
    pygame.display.update()

    player.update()
    pygame.display.flip()

    clock.tick(120)
    pygame.display.update()

pygame.quit()