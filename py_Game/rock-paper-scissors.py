import pygame, sys, random
from PIL import Image

def resize():
    # Image.open() can also open other image types
    goruntu1 = Image.open("kırmızı_makas.png")
    goruntu2 = Image.open("taş.png")
    goruntu3 = Image.open("kagıt.png")
    # WIDTH and HEIGHT are integers
    scissor = goruntu1.resize((200, 200))
    scissor.save("resized_scissor.png")
    rock = goruntu2.resize((200, 200))
    rock.save("resized_rock.png")
    paper = goruntu3.resize((200, 200))
    paper.save("resized_paper.png")
# "dogru" ve "yanlis"taki sesleri farkli kanalda acmam seslerin birbirini sonlandirmasini onlemektedir.
# Varsayalım ki aynı kanalda olsunlar; arka planda muzik calarken secim yapmaniz ile birlikte
# dogru ses efekti oynatilirsa arkaplandaki muzik sonlandirilir, yerine dogru ses efekti oynatilir.
def dogru():
    kanal = pygame.mixer.Channel(5)
    kanal.play(pygame.mixer.Sound(musicTrue))
def yanlis():
    kanal = pygame.mixer.Channel(5)
    kanal.play(pygame.mixer.Sound(musicFalse))
def oyun(a):
   # Taş = 0
   # Kağıt = 1
   # Makas = 2

    b = random.randint(0,2)
    if b == 0:
       if a == 0:
           print("berabere")
           return pencere.fill((0, 0, 0)), pencere.blit(berabere, (500, 170))
       elif a == 1:
           print("kazandınız")
           dogru()
           return pencere.fill((0, 250, 250)), pencere.blit(kazandiniz, (500, 170))

       else:
           print("kaybettiniz")
           yanlis()
           return pencere.fill((255, 0, 0)), pencere.blit(kaybettiniz, (500, 170))

    if b == 1:
        if a == 0:
            print("kaybettiniz")
            yanlis()
            return pencere.fill((255, 0, 0)), pencere.blit(kaybettiniz, (500, 170))
        elif a == 1:
            print("berabere")
            return pencere.fill((0, 0, 0)), pencere.blit(berabere, (500, 170))
        else:
            print("kazandınız")
            dogru()
            return pencere.fill((0, 250, 250)), pencere.blit(kazandiniz, (500, 170))
    if b == 2:
        if a == 0:
            print("kazandınız")
            dogru()
            return pencere.fill((0, 250, 250)), pencere.blit(kazandiniz, (500, 170))
        elif a == 1:
            print("kaybettiniz")
            yanlis()
            return pencere.fill((255, 0, 0)), pencere.blit(kaybettiniz, (500, 170))
        else:
            print("berabere")
            return pencere.fill((0, 0, 0)), pencere.blit(berabere, (500, 170))
def secim_rps():
    if event.type == pygame.MOUSEBUTTONDOWN:
        if 50 < x < 250 and 420 < y < 620 and event.button == 1:
            print("Taşa tıkladın")
            oyun(0)
            pygame.display.update()
        if 500 < x < 700 and 420 < y < 620 and event.button == 1:
            print("kağıda tıkladınız")
            oyun(1)
            pygame.display.update()
        if 1000 < x < 1200 and 420 < y < 620 and event.button == 1:
            print("makasa tıkladınız")
            oyun(2)
            pygame.display.update()
def muzikFonk():
    global a
    global pause
    if event.type == pygame.KEYDOWN:
        # Enterla kullanabilecegimiz sart yapısı
        if event.key == pygame.K_RETURN:

            a += 1
            if a == 1:
                pygame.mixer.music.load(musicName_1)
                pygame.mixer.music.play()
            elif a == 2:
                pygame.mixer.music.load(musicName_2)
                pygame.mixer.music.play()
            elif a == 3:
                pygame.mixer.music.load(musicName_3)
                pygame.mixer.music.play()
            elif a == 4:
                pygame.mixer.music.load(musicName_4)
                pygame.mixer.music.play()
            elif a == 5:
                pygame.mixer.music.load(musicName_5)
                pygame.mixer.music.play()
            else:
                pygame.mixer.music.stop()
                a = 0
        if event.key == pygame.K_p:
            # Durdurma ve devam ettirme.
            if pause:
                pygame.mixer.music.unpause()
                pause = False
            else:
                pygame.mixer.music.pause()
                pause = True
def cıkıs():
    # sag ustteki carpı ile cıkıs yapabilmek icin
    if event.type == pygame.QUIT:
        sys.exit()

# ---------------------------------------------------------------------------------------------------------
pygame.init()

boyutu = (1280,720)

resize()
scissor = pygame.image.load("resized_scissor.png")
rock = pygame.image.load("resized_rock.png")
paper = pygame.image.load("resized_paper.png")

musicName_1 = "Carol of the bells.mp3"
musicName_2 = "Cinematic Violin.mp3"
musicName_3 = "royalty-free-music-no-copyright-winner-violin-hip-hop-beat.mp3"
musicName_4 = "Guitar  Violin - (Royalty Free  No Copyright) Background Music - Sweet Bright Achievement Light.mp3"
musicName_5 = "Telifsiz Müzik 3- No Copyright Song 3 - Red Violin.mp3"

musicTrue = "dogru.mp3"
musicFalse = "yanlis.mp3"


font = pygame.font.SysFont("Arial", 40)
rock_paper_scissors = font.render("Taş, kağıt, makas Oyununa Hoşgeldiniz. Cat-Dos Inc. sunar", True, (160, 120, 255), (60, 50, 160))
gecis = font.render("Geçmek için Enter'a bas", True, (160, 120, 255), (60, 50, 160))
kazandiniz = font.render(" Kazandınız ", True, (100, 250, 170), (20, 120, 100))
berabere = font.render(" Berabere kaldınız ", True, (0, 0, 0), (60, 50, 160))
kaybettiniz = font.render(" Kaybettiniz ", True, (255, 0, 0), (50, 50, 70))
enterFonksiyon = font.render(" Enter = müzik değiştirir. ", True, (50, 100, 200), (20, 40,15))
pFonksiyon = font.render(" p = müziği duraklat/devam ettir.", True, (50, 100, 200), (20, 40,15))
pencere = pygame.display.set_mode(boyutu)
a = 0
pause = False

clock = pygame.time.Clock()

pygame.display.update()

while True:
    pencere.blit(rock, (50, 420))
    pencere.blit(paper, (500, 420))
    pencere.blit(scissor, (1000, 420))
    pencere.blit(rock_paper_scissors, (200, 100))
    pencere.blit(enterFonksiyon, (400, 255))
    pencere.blit(pFonksiyon, (400, 300))
    pygame.display.update()

    for event in pygame.event.get():
        #  mouse pozisyonu x, y
        x, y = pygame.mouse.get_pos()
        # Buradaki mouse pozisyonları sadece yorumlayıcıda gorunur, ayrıca acılan pencerede goruntulenmez.
        print(x, y)
        cıkıs()
        muzikFonk()
        secim_rps()