import pygame
import random
import os

# Ekran boyutlarık
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Renkler
BEYAZ = (255, 255, 255)
SIYAH = (0, 0, 0)

# Oyun dosya dizini
oyun_klasoru = os.path.dirname(__file__)
img_klasoru = os.path.join(oyun_klasoru, "img")

class Oyuncu(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(img_klasoru, "01.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (100, SCREEN_HEIGHT // 2)
        self.yercekimi = 0.4
        self.ziplama_gucu = -10
        self.hizi = 0
        self.ates_gecikmesi = 250  # Ateş etme gecikmesi (milisaniye)
        self.son_ates = pygame.time.get_ticks()
        self.kursun_sayisi = 0  # Birden fazla atış için kurşun sayısı
        self.coklu_ates_gecikmesi = 500  # Birden fazla atış gecikmesi

    def update(self):
        self.hizi += self.yercekimi
        self.rect.y += self.hizi

        if self.rect.bottom >= YER_YUKSEKLIGI:
            self.rect.bottom = YER_YUKSEKLIGI
            self.hizi = 0

    def zipla(self):
        if self.rect.bottom == YER_YUKSEKLIGI:
            self.hizi = self.ziplama_gucu

    def ates_et(self):
        suan = pygame.time.get_ticks()
        if suan - self.son_ates > self.ates_gecikmesi:
            self.son_ates = suan
            kursun = Kursun(self.rect.right, self.rect.centery)
            tum_spritelist.add(kursun)
            kursunlar.add(kursun)
            self.kursun_sayisi += 1

            # Birden fazla atış için zaman geldiğinde daha fazla kurşun at
            if self.kursun_sayisi % 6 == 0:
                for _ in range(6):
                    kursun = Kursun(self.rect.right, self.rect.centery + random.randint(-20, 20))
                    tum_spritelist.add(kursun)
                    kursunlar.add(kursun)

            # Birden fazla atış sonrası kurşun sayısını sıfırla
            if self.kursun_sayisi % 12 == 0:
                self.kursun_sayisi = 0

class Engeller(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()   
        self.image = pygame.image.load(os.path.join(img_klasoru, "02.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH + 50, YER_YUKSEKLIGI - 30)
        self.hizi = -5

    def update(self):
        self.rect.x += self.hizi
        if self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH + random.randrange(100, 300)
            self.rect.bottom = YER_YUKSEKLIGI - random.randrange(30, 100)

class Kursun(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 5))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.centery = y
        self.hizx = 10

    def update(self):
        self.rect.x += self.hizx
        if self.rect.left > SCREEN_WIDTH:
            self.kill()

pygame.init()
ekran = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sonsuz Engellerden Atla")

saat = pygame.time.Clock()

tum_spritelist = pygame.sprite.Group()
engeller = pygame.sprite.Group()
kursunlar = pygame.sprite.Group()

oyuncu = Oyuncu()
tum_spritelist.add(oyuncu)

YER_YUKSEKLIGI = SCREEN_HEIGHT - 50

# Zemin
yer_resmi = pygame.image.load(os.path.join(img_klasoru, "03.png")).convert_alpha()
yer_resmi = pygame.transform.scale(yer_resmi, (SCREEN_WIDTH, 50))
yer_dikdortgen = yer_resmi.get_rect()
yer_dikdortgen.bottom = SCREEN_HEIGHT
             
# Arkaplan
arkaplan_resmi = pygame.image.load(os.path.join(img_klasoru, "04.jpg")).convert()
arkaplan_resmi = pygame.transform.scale(arkaplan_resmi, (SCREEN_WIDTH, SCREEN_HEIGHT))
arkaplan_dikdortgen = arkaplan_resmi.get_rect()

for _ in range(2):
    engel = Engeller()
    tum_spritelist.add(engel)
    engeller.add(engel)

puan = 0  # Puan değişkenini başlat
seviye = 1  # Seviye değişkenini başlat
seviye_atlamak_icin_puan = 5  # Seviye atlamak için gereken puan

# Puan ve seviye gösterimi için font
yazi_fontu = pygame.font.Font(None, 36)

calisiyor = False
menu = True

while menu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                calisiyor = True
                menu = False

    ekran.blit(arkaplan_resmi, arkaplan_dikdortgen)
    # Menü metni çizimi
    menu_yazi = yazi_fontu.render("Jeton atmak için* ENTERE BAS", True, BEYAZ)
    menu_yazi_dikdortgen = menu_yazi.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    ekran.blit(menu_yazi, menu_yazi_dikdortgen)
    
    pygame.display.flip()
    saat.tick(60)

while calisiyor:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            calisiyor = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                oyuncu.zipla()
            elif event.key == pygame.K_k:
                oyuncu.ates_et()
            elif event.key == pygame.K_a:  # 'a' tuşuna basarak sola hareket et
                oyuncu.rect.x -= 10
            elif event.key == pygame.K_d:  # 'd' tuşuna basarak sağa hareket et
                oyuncu.rect.x += 10

    tum_spritelist.update()

    engel_vurmalari = pygame.sprite.groupcollide(engeller, kursunlar, True, True)
    for vurus in engel_vurmalari:
        engel = Engeller()
        tum_spritelist.add(engel)
        engeller.add(engel)
        puan += 1  # Engeli vurunca puanı artır

        # Puan belirli bir seviyeye ulaştığında seviyeyi yükselt
        if puan % seviye_atlamak_icin_puan == 0:
            seviye += 1

            # Her 5 seviyede engel hızını ve sayısını artır
            if seviye % 5 == 0:
                for _ in range(2):
                    engel = Engeller()
                    tum_spritelist.add(engel)
                    engeller.add(engel)
                for eng in engeller:
                    eng.hizi -= 1

    # Puan belirli bir seviyeye ulaştığında seviyeyi yükselt
    if puan % seviye_atlamak_icin_puan == 0:
        # Her 5 seviyede oyuncunun kurşun hızını artır
        if seviye % 5 == 0:
            oyuncu.ates_gecikmesi -= 25

        # Her 6 seviyede birden fazla atış sıklığını artır
        if seviye % 6 == 0:
            oyuncu.ates_gecikmesi -= 25

    engel_vuruslari = pygame.sprite.spritecollide(oyuncu, engeller, False)
    if engel_vuruslari:
        calisiyor = False

    ekran.blit(arkaplan_resmi, arkaplan_dikdortgen)
    ekran.blit(yer_resmi, yer_dikdortgen)
    tum_spritelist.draw(ekran)

    # Puan ve seviye gösterimi
    puan_yazi = yazi_fontu.render("Toplanan boynuz: " + str(puan), True, BEYAZ)
    seviye_yazi = yazi_fontu.render("Boynuz gücü: " + str(seviye), True, BEYAZ)
    ekran.blit(puan_yazi, (10, 10))
    ekran.blit(seviye_yazi, (10, 40))

    pygame.display.flip()
    saat.tick(60)

pygame.quit()
