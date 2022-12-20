import pygame as pg
import random
import sys
import os

def alarm():
    pg.mixer.init(frequency = 44100)    # 初期設定
    pg.mixer.music.load("ex05/IT3_07_C0A21089.wav")     # 音楽ファイルの読み込み
    pg.mixer.music.play(5) #再生回数


class Screen:           #スクリーンの初期設定
    def __init__(self, title, wh, img_path):
        pg.display.set_caption(title) 
        self.sfc = pg.display.set_mode(wh)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(img_path)
        self.bgi_rct = self.bgi_sfc.get_rect() 

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct) 


class Bird:    #こうかとんの移動と画像の定義
    key_delta = {
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],
    }

    def __init__(self, img_path, ratio, xy):
        self.sfc = pg.image.load(img_path)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, ratio)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        key_dct = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_dct[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]  
            if check_bound(self.rct, scr.rct) != (+1, +1):
                self.rct.centerx -= delta[0]
                self.rct.centery -= delta[1]
        self.blit(scr)                    


class Bomb:       #ボムの初期設定
    def __init__(self, color, rad, vxy, scr:Screen):
        self.sfc = pg.Surface((2*rad, 2*rad)) 
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, color, (rad, rad), rad)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)


def check_bound(obj_rct, scr_rct): #こうかとんにボムが当たったかどうかの判定
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = (-1)*1.2

    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = (-1)*1.2
    return yoko, tate


def main():
    clock =pg.time.Clock()
    
    scr = Screen("逃げろ！こうかとん", (1600,900), "ex05/pg_bg.jpg")

    kkt = Bird("ex05/fig/6.png", 2.0, (900,400))
    kkt.update(scr)
    bombs = []
    colors = ["red","green","blue","yellow","magenta"]
    for i in range(5):
        color = colors[i]
        vx = random.choice([-1,1])
        vy = random.choice([-1,1])
        bombs.append(Bomb(color,10,(vx,vy),scr))

    while True:        
        scr.blit()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        kkt.update(scr)
        for i in range(len(bombs)):
            bombs[i].update(scr)
            if kkt.rct.colliderect(bombs[i].rct):

                #着弾後のこうかとんの画像の設置
                scr.sfc = pg.display.set_mode((1600,900))
                kkt.sfc = pg.transform.rotozoom(kkt.sfc,90,1.0)
                scr.sfc.blit(kkt.sfc,kkt.rct)
                jikan = pg.time.get_ticks()
                fonto = pg.font.Font(None,80)
                txt = fonto.render(f"{int(jikan/1000)}s escape",True,(255,0,0))
                scr.sfc.blit(txt,(400,200))

                #着弾後のテキスト表示
                fonto = pg.font.Font(None,80)
                txt = fonto.render("THE END",True,(255,0,0))
                scr.sfc.blit(txt,(1000,200))
                pg.display.update()
                pg.mixer.music.stop()
                clock.tick(0.5)
                return

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    alarm()
    main()
    pg.quit()
    sys.exit()

