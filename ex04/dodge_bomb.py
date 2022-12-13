import pygame as pg
import sys
import random

def check_bound(obj_rct,scr_rct):
    yoko,tate = 1,1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1*1.2
    
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1*1.2
    return yoko,tate



def main():
    clock = pg.time.Clock()
    pg.display.set_caption("逃げろ!こうかとん")
    scrn_sfc = pg.display.set_mode((1600,900))
    scrn_rct = scrn_sfc.get_rect()
    pgbg_sfc = pg.image.load("ex04/pg_bg.jpg")
    pgbg_rct = pgbg_sfc.get_rect()

    tori_sfc = pg.image.load("ex04/fig/0.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc,0,2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900,400
    scrn_sfc.blit(tori_sfc,tori_rct)

    bomb_sfc = pg.Surface((20,20))
    bomb_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bomb_sfc,(255,0,0),(10,10),10)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = random.randint(0,1600)
    bomb_rct.centery = random.randint(0,900)
    scrn_sfc.blit(bomb_sfc,bomb_rct)


    

    
    vx,vy = 1,1
    
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

        if check_bound(tori_rct,scrn_rct) != (1,1):
            if key_dct[pg.K_UP]:
                tori_rct.centery += 1
        
            if key_dct[pg.K_DOWN]:
                tori_rct.centery -= 1
            
            if key_dct[pg.K_LEFT]:
                tori_rct.centerx += 1

            if key_dct[pg.K_RIGHT]:
                tori_rct.centerx -= 1


        scrn_sfc.blit(tori_sfc,tori_rct)
        bomb_rct.move_ip(vx,vy)
        scrn_sfc.blit(bomb_sfc,bomb_rct)
        yoko,tate = check_bound(bomb_rct, scrn_rct)
        vx *= yoko
        vy *= tate
        if tori_rct.colliderect(bomb_rct):
            scrn_sfc = pg.display.set_mode((1600,900))
            tori_sfc = pg.transform.rotozoom(tori_sfc,90,1.0)
            scrn_sfc.blit(tori_sfc,tori_rct)
            jikan = pg.time.get_ticks()
            fonto = pg.font.Font(None,80)
            txt = fonto.render(f"{int(jikan/1000)}s escape",True,(255,0,0))
            scrn_sfc.blit(txt,(400,200))

            fonto = pg.font.Font(None,80)
            txt = fonto.render("THE END",True,(255,0,0))
            scrn_sfc.blit(txt,(1000,200))
            pg.display.update()
            clock.tick(0.5)
            
            return
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



   

    



