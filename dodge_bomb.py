import random
import sys
import pygame as pg


WIDTH, HEIGHT = 1600, 900
delta = {
    pg.K_UP: (0, -5),
    pg.K_DOWN: (0, +5),
    pg.K_LEFT: (-5, 0),
    pg.K_RIGHT: (+5, 0),
}

vector ={
    sum_v[0, -5]: pg.transform.rotozoom(kk_img,90,1.0),

    }


def check_bound(rect: pg.Rect) -> tuple[bool,bool]:
    yoko, tate = True, True
    if rect.left < 0 or WIDTH < rect.right:  # 横方向判定
        yoko = False
    if rect.top < 0 or HEIGHT < rect.bottom:  # 縦方向判定
        tate = False
    return yoko, tate


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 900, 400
    bm_img = pg.Surface((20,20))
    pg.draw.circle(bm_img,(255,0,0),(10,10),10)
    x = random.randint(0,WIDTH)
    y = random.randint(0,HEIGHT)
    bm_rct = bm_img.get_rect() #爆弾Surfaceを抽出する
    bm_rct.center = x, y       #爆弾の初期座標
    bm_img.set_colorkey((0,0,0))#円を囲う四角の四隅を透明に
    vx, vy = +5, +5
    clock = pg.time.Clock()
    tmr = 0


    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
            
        if kk_rct.colliderect(bm_rct):
            print("ゲームオーバー")
            return   # ゲームオーバー 
        
        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]
        for k, mv in delta.items():
            if key_lst[k]:
                sum_mv[0] += mv[0]
                sum_mv[1] += mv[1]
        kk_rct.move_ip(sum_mv)
        if check_bound(kk_rct) != (True,True):
            kk_rct.move_ip(-sum_mv[0],-sum_mv[1])

        sum_mv = [0, 0]
        for l,mv in vector.items():
            if key_lst[l]:
                sum_mv[0] += mv[0]
                sum_mv[1] += mv[1]

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rct)
        bm_rct.move_ip(vx,vy)
        yoko, tate = check_bound(bm_rct)
        if not yoko:
            vx *= -1
        if not tate:
            vy *= -1
        screen.blit(bm_img,bm_rct)
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()


"""
pg.transform.rotozoom(kk_img,45,1.0),
    pg.transform.flip(kk_img, True, False),
    pg.transform.rotozoom(kk_img,-45,1.0),
    pg.transform.rotozoom(kk_img,90,1.0),
    pg.transform.rotozoom(kk_img,-90,1.0),
    pg.transform.rotozoom(kk_img,135,1.0),
    pg.transform.rotozoom(kk_img,-135,1.0)
"""