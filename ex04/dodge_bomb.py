import pygame as pg
import sys

def main():
    clock = pg.time.Clock()
    pg.display.set_caption("逃げろ!こうかとん")
    scrn_sfc = pg.display.set_mode((1600,900))
    pgbg_sfc = pg.image.load("ex04/pg_bg.jpg")
    pgbg_rct = pgbg_sfc.get_rect()

    tori_sfc = pg.image.load("ex04/fig/0.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc,0,2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900,400
    scrn_sfc.blit(tori_sfc,tori_rct)

    while True:
        scrn_sfc.blit(pgbg_sfc,pgbg_rct)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            
        key_dct = pg.key.get_pressed()
        if key_dct[pg.K_UP]:
            tori_rct.centery -= 1
        
        if key_dct[pg.K_DOWN]:
            tori_rct.centery += 1
        
        if key_dct[pg.K_LEFT]:
            tori_rct.centerx -= 1

        if key_dct[pg.K_RIGHT]:
            tori_rct.centerx += 1

        scrn_sfc.blit(tori_sfc,tori_rct)
        pg.display.update()
        clock.tick(1000)





if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit() 
"""def main():
    pg.display.set_caption("逃げろ!こうかとん")
    screen = pg.display.set_mode((1600,900))
    img = pg.image.load("pg_bg_ipg")
    tri_sfc = pg.image.load("fig/0.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc,0,2.0)
    tori_rect = tori_sfc.get_rect()
    tori_rect.center =400,900

    while True:
        screen.blit(tori_sfc,tori_rect)
        pg.display.update()
        clock = pg.time.Clock()
        clock.tick(1000)
        for event in pg.event.get():
            if event.type ==pg.QUIT:  # 閉じるボタンが押されたら終了
                return      # Pygameの終了(画面閉じられる)



            if event.type == pg.KEYDOWN and event.key == pg.K_F1:
                screen == pg.display.set_mode((800,600),pg.FULLSCREEN)
            
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                screen = pg.display.set_mode((800,600))"""



   

    



