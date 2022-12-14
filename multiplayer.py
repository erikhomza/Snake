import pygame as pg
import random


pg.init()

clock = pg.time.Clock()
fps = 30
control = 3
control2 = 3
cooldown = 5
score1 = 0
score2 = 0
highscore1 = 0
highscore2 = 0
win1 = 0
win2 = 0


screen_width = 800
screen_height = 800

screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Snake")

tile_size = 50
snake = [[4,4]]
snake2 = [[10,4]]
map = []
map_row = []
for i in range(16):
    map_row.append(1)
for i in range(16):
    map.append(map_row[:])
map[snake[0][0]][snake[0][1]] = 2
map[snake2[0][0]][snake2[0][1]] = 4



yellow = (255, 255, 0)
score_font = pg.font.Font("Turok.ttf", 30)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))



class World():
    def __init__(self, data):
        self.tile_list = []

        ground = pg.image.load('castleCenter.png').convert_alpha()
        snake = pg.image.load('liquidLava.png').convert_alpha()
        snake2 = pg.image.load('grassCenter.png').convert_alpha()
        food = pg.image.load('cakeCenter.png').convert_alpha()

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pg.transform.scale(ground, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pg.transform.scale(snake, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 3:
                    img = pg.transform.scale(food, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 4:
                    img = pg.transform.scale(snake2, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])


def pause():
    game_paused = True
    while game_paused:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_p:
                    game_paused = False
                if event.type == pg.QUIT:
                    pg.quit()


run = True
while run:

    clock.tick(fps)

    if score1 > highscore1:
        highscore1 = score1
    if score2 > highscore2:
        highscore2 = score2

    food_in_map = False
    for i in map:
        for e in i:
            if e == 3:
                food_in_map = True

    if food_in_map == False:
        y = random.randint(0, 15)
        for i in map:
            if map.index(i) == y:
                x = random.randint(0, 15)
                if i[x] == 1:
                    map[map.index(i)][x] = 3


    world = World(map)

    world.draw()
    draw_text("p1 score " + str(score1), score_font, yellow, 20, 20)
    draw_text("p1 highscore " + str(highscore1), score_font, yellow, 20, 50)
    draw_text("p2 score " + str(score2), score_font, yellow, 600, 20)
    draw_text("p2 highscore " + str(highscore2), score_font, yellow, 600, 50)
    draw_text("p1 wins " + str(win1), score_font, yellow, 20, 80)
    draw_text("p2 wins " + str(win2), score_font, yellow, 600, 80)



    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_p:
                pause()



    key = pg.key.get_pressed()
    if key[pg.K_DOWN]:
        if control != 2:
            control = 1
    if key[pg.K_UP]:
        if control != 1:
            control = 2
    if key[pg.K_RIGHT]:
        if control != 4:
            control = 3
    if key[pg.K_LEFT]:
        if control != 3:
            control = 4

    if key[pg.K_s]:
        if control2 != 2:
            control2 = 1
    if key[pg.K_w]:
        if control2 != 1:
            control2 = 2
    if key[pg.K_d]:
        if control2 != 4:
            control2 = 3
    if key[pg.K_a]:
        if control2 != 3:
            control2 = 4


    cooldown-=1
    if cooldown == 0:


        if control == 3:
            temp = snake[-1]
            snake.append(temp[:])
            snake[-1][1] += 1

        if control == 4:
            temp = snake[-1]
            snake.append(temp[:])
            snake[-1][1] -= 1

        if control == 1:
            temp = snake[-1]
            snake.append(temp[:])
            snake[-1][0] += 1

        if control == 2:
            temp = snake[-1]
            snake.append(temp[:])
            snake[-1][0] -= 1

        if control2 == 3:
            temp = snake2[-1]
            snake2.append(temp[:])
            snake2[-1][1] += 1

        if control2 == 4:
            temp = snake2[-1]
            snake2.append(temp[:])
            snake2[-1][1] -= 1

        if control2 == 1:
            temp = snake2[-1]
            snake2.append(temp[:])
            snake2[-1][0] += 1

        if control2 == 2:
            temp = snake2[-1]
            snake2.append(temp[:])
            snake2[-1][0] -= 1

        if snake[-1][0] == 16:
            snake[-1][0] -= 16
        if snake[-1][1] == 16:
            snake[-1][1] -= 16
        if snake[-1][0] == -1:
            snake[-1][0] = 15
        if snake[-1][1] == -1:
            snake[-1][1] = 15

        if snake2[-1][0] == 16:
            snake2[-1][0] -= 16
        if snake2[-1][1] == 16:
            snake2[-1][1] -= 16
        if snake2[-1][0] == -1:
            snake2[-1][0] = 15
        if snake2[-1][1] == -1:
            snake2[-1][1] = 15


        eating = False
        if map[snake[-1][0]][snake[-1][1]] == 2 or map[snake[-1][0]][snake[-1][1]] == 4:
            map = []
            map_row = []
            for i in range(16):
                map_row.append(1)
            for i in range(16):
                map.append(map_row[:])
            snake = [[4, 4], [4, 5]]
            snake2 = [[10, 4], [10, 5]]
            score1 = 0
            win2 += 1
            map[snake[0][0]][snake[0][1]] = 2
            map[snake[1][0]][snake[1][1]] = 2
        if map[snake[-1][0]][snake[-1][1]] == 3:
            eating = True
            score1 += 1
        map[snake[-1][0]][snake[-1][1]] = 2
        if eating == False:
            map[snake[0][0]][snake[0][1]] = 1
            snake.pop(0)
        cooldown = 5

        eating2 = False
        if map[snake2[-1][0]][snake2[-1][1]] == 2 or map[snake2[-1][0]][snake2[-1][1]] == 4:
            map = []
            map_row = []
            for i in range(16):
                map_row.append(1)
            for i in range(16):
                map.append(map_row[:])
            snake = [[4, 4]]
            snake2 = [[10, 4], [10, 5]]
            score2 = 0
            win1 += 1
            map[snake2[0][0]][snake2[0][1]] = 4
            map[snake2[1][0]][snake2[1][1]] = 4
        if map[snake2[-1][0]][snake2[-1][1]] == 3:
            eating2 = True
            score2 += 1
        map[snake2[-1][0]][snake2[-1][1]] = 4
        if eating2 == False:
            map[snake2[0][0]][snake2[0][1]] = 1
            snake2.pop(0)
        cooldown = 5



    pg.display.update()

pg.quit()