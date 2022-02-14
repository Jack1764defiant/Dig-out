import random
from time import *
WIDTH =800
HEIGHT=600
alive = True
startime = time()
terrains = []
player = Rect(0, 40, 40, 40)
bricks = []
numbers = []
BRICKX = int(WIDTH/40)
BRICKY = int(HEIGHT/40)
boulder = False
check = False
check2 = False
tmcheck = False
tm = 2
tmcheck2 = False
tm2 = 2
tmcheck3 = False
tm3 = 2
level = 0
tmcheck4 = False
tm4 = 2
tmcheck5 = False
tm5 = 2
tm6 = 2
tmcheck6 = False
tm7 = 2
tmcheck7 = False
lives = 5
falling = []
livecheck = []
checks = []
xvel = 3
yvel = 3
for x in range(0, BRICKX):
    for y in range(0, BRICKY):
        brick = Rect(x*40,y*40 , 40, 40)
        bricks.append(brick)
for x in range(0, BRICKX):
    for y in range(0, BRICKY):
        checks.append(False)
for x in range(0, BRICKX):
    for y in range(0, BRICKY):
        ran = random.randint(0,103)
        if ran < 81:
            terrain = "dirt"
        elif ran > 80 and ran < 91:
            terrain = "boulder"
        elif ran > 90 and ran < 97:
            terrain = "gem"
        else:
            terrain = "spike"
        terrains.append(terrain)
terrains[1] = "space2"
terrains[0] = "teleport"
terrains[int(HEIGHT/40)] = "space2"
terrains[int(HEIGHT/40)+1] = "space2"
def create():
    global terrains,player,bricks,BRICKX,BRICKY,boulder,check,check2,tmcheck,tm,tmcheck2,tm2,tmcheck3, tm3, level, startime, ghost, lives, livecheck, yvel, xvel
    level += 1
    if level % 2 == 0 and not(level in livecheck):
        lives += 1
        livecheck.append(level)
    startime = time()
    if level >= 3:
        ghost = Rect(0,0,30, 60)
    xvel = 3
    yvel = 3
    terrains = []
    player = Rect(0, 40, 40, 40)
    bricks = []
    BRICKX = int(WIDTH/40)
    BRICKY = int(HEIGHT/40)
    boulder = False
    check = False
    check2 = False
    tmcheck = False
    tm = 2
    tmcheck2 = False
    tm2 = 2
    tmcheck3 = False
    tm3 = 2
    alive = True
    for x in range(0, BRICKX):
        for y in range(0, BRICKY):
            brick = Rect(x*40,y*40 , 40, 40)
            bricks.append(brick)
    for x in range(0, BRICKX):
        for y in range(0, BRICKY):
            ran = random.randint(0,104)
            if ran < 81:
                terrain = "dirt"
            elif ran > 80 and ran < 91:
                terrain = "boulder"
            elif ran > 90 and ran < 97:
                terrain = "gem"
            elif ran > 100 and y != BRICKY and level >= 2:
                terrain = "tnt"
            else:
                terrain = "spike"
            terrains.append(terrain)
    terrains[1] = "space2"
    terrains[0] = "teleport"
    terrains[14] = "teleport"
    terrains[285] = "teleport"
    terrains[(int(HEIGHT/40)*int(WIDTH/40))-1] = "teleport"
    terrains[int(HEIGHT/40)] = "space2"
    terrains[int(HEIGHT/40)+1] = "space2"
    state = "playing"

score = 0
state = "playing"
create()
terrains[-2] = "space2"
def draw():
    global state
    global lives
    global player
    global boulder
    global ghost
    global tm
    global score
    global alive
    global level
    terrains[-2] = "space2"
    terrains[1] = "space2"
    terrains[13] = "space2"
    terrains[286] = "space2"
    terrains[0] = "teleport"
    terrains[(int(HEIGHT/40)*int(WIDTH/40))-1] = "teleport"
    terrains[14] = "teleport"
    terrains[285] = "teleport"
    terrains[int(HEIGHT/40)] = "space2"
    terrains[int(HEIGHT/40)+1] = "space2"
    colours = ["brown", "green", "red", "blue", "white", "gray", "yellow", "orange", "purple", "pink"]
    if state == "gamover":
        screen.clear()
        screen.draw.text("GAME OVER!", (200, 150), color = "red")
        screen.draw.text("Score: " + str(score), (10, 30), color="red")
    elif state == "win":
        screen.clear()
        screen.draw.text("You Win!", (200, 150), color = "red")
        create()
        state = "playing"
    elif state == "paused":
        screen.draw.text("Paused", (150, 150), color = "yellow")
        screen.draw.text("Score: " + str(score), (10, 30), color="red")
        if keyboard[keys.O] and state == "paused":
            state = "playing"
    if state == "playing":
        screen.clear()
        for i in range(0, len(bricks)):
            if terrains[i] == "dirt":
                screen.blit("soil", bricks[i])
            elif terrains[i] == "boulder":
                screen.blit("rock", bricks[i])
            elif terrains[i] == "spike":
                screen.draw.filled_rect(bricks[i], "white")
                #screen.draw.filled_circle(bricks[i].center, 10, "red")
                #screen.draw.filled_circle(bricks[i].center , 7.5, "green")
                screen.draw.filled_circle(bricks[i].center, 8, "black")
                #screen.draw.filled_circle(bricks[i].center, 2.5, "yellow")
            elif terrains[i] == "gem":
                screen.blit("gem", bricks[i])
            elif terrains[i] == "teleport":
                screen.draw.filled_rect(bricks[i], "blue")
                screen.draw.filled_circle(bricks[i].center, 8, "light blue")
            elif terrains[i] == "space":
                screen.draw.filled_rect(bricks[i], "black")
            elif terrains[i] == "space2":
                screen.draw.filled_rect(bricks[i], "black")
            elif terrains[i] == "laser":
                screen.draw.filled_rect(bricks[i], "grey")
                laser = Rect (bricks[i].x, bricks[i].y +7.5, 20, 5)
                screen.draw.filled_rect(laser, "blue")
                laser2 = Rect (bricks[i].x + 7.5, bricks[i].y, 5, 20)
                screen.draw.filled_rect(laser2, "blue")
            elif terrains[i] == "tnt":
                if level < 3 or level == 4 or level == 5:
                    screen.draw.filled_rect(bricks[i], "red")
                    tnt = Rect (bricks[i].x, bricks[i].y +8, 40, 4)
                    screen.draw.filled_rect(tnt, "black")
                    tnt = Rect (bricks[i].x, bricks[i].y + 28, 40, 4)
                    screen.draw.filled_rect(tnt, "black")
                else:
                    screen.draw.filled_circle(bricks[i].center, 20, "dark grey")
                    screen.draw.filled_circle(bricks[i].center, 8, "red")
            elif terrains[i] == "explosion":
                explo = Rect (bricks[i].x, bricks[i].y, 40, 40)
                screen.draw.filled_rect(explo, "orange")
                if i % int(HEIGHT/40) == 0:
                    terrains[i] = "space2"
                else:
                    terrains[i] = "space"
        if time() >= startime + 2.5 and level >=4 and level < 7:
            screen.draw.filled_circle((ghost.x+20, ghost.y+10), 15, "white")
            ghost2 = Rect(ghost.x+5, ghost.y+10, 30, 25)
            screen.draw.filled_rect(ghost2, "white")
            screen.draw.filled_circle((ghost.x+13,ghost.y+8), 5, "red")
            screen.draw.filled_circle((ghost.x+27,ghost.y+8), 5, "red")
        if time() >= startime + 2.5 and level >=7 and int(time())%2 == 0:
            screen.draw.filled_circle((ghost.x+20, ghost.y+10), 15, "white")
            ghost2 = Rect(ghost.x+5, ghost.y+10, 30, 25)
            screen.draw.filled_rect(ghost2, "white")
            screen.draw.filled_circle((ghost.x+13,ghost.y+8), 5, "red")
            screen.draw.filled_circle((ghost.x+27,ghost.y+8), 5, "red")
        if alive:
            screen.draw.filled_circle(player.center, 20, random.choice(colours))
        else:
            if boulder == True:
                player = Rect(player.x, player.y + 35, 40, 5)
                screen.draw.filled_rect(player, "red")
            elif boulder == "spike":
                player = Rect(player.x, player.y, 40, 40)
                screen.draw.filled_circle(player.center, 20, "red")
                screen.draw.filled_circle(player.center, 8, "black")
            elif boulder == "ghost":
                screen.draw.filled_circle((player.x+20, player.y+10), 15, "dark grey")
                player2 = Rect(player.x+5, player.y+10, 30, 25)
                screen.draw.filled_rect(player2, "dark grey")
                player2 = Rect(player.x + 18, player.y, 4, 30)
                screen.draw.filled_rect(player2, "black")
                player2 = Rect(player.x + 12, player.y + 6, 16, 4)
                screen.draw.filled_rect(player2, "black")
            else:
                player = Rect(player.x, player.y, 40, 40)
                screen.draw.filled_circle(player.center, 20, "red")
            state = "gameover"
        if keyboard[keys.P] and state == "playing":
            state = "paused"
        screen.draw.text("Score: " + str(score), (10, 30), color="red")
        if time() >= tm5 + 3.5 and level > 4:
            screen.draw.text("Teleport", (100, 30), color="red")
        if time() >= tm7 + 8:
            screen.draw.text("Laser", (175, 30), color="red")
        screen.draw.text("Level: " + str(level), (250, 30), color="red")
        screen.draw.text("Lives: " + str(lives), (350, 30), color="red")



def update():
    global state
    global score
    global alive
    act = 1
    global boulder
    global check
    global tmcheck
    global tm
    global tmcheck2
    global tm2
    global tmcheck3
    global tm3
    global check2
    global level
    global tmcheck4
    global tm4
    global tmcheck5
    global tm5
    global tmcheck6
    global tm6
    global tm7
    global tmcheck7
    global lives
    global falling
    global startime
    global numbers
    global xvel
    global yvel
    terrains[-2] = "space2"
    if state == "playing":
        explode = False
        val = "none"
        sx = player.x
        sy = player.y
        if keyboard[keys.D] and player.right < WIDTH and act == 1:
            if not tmcheck4:
                tm4 = time()
                tmcheck4 = True
            elif time() >= tm4 + 0.15:
                player.x = player.x + 31
                player.x = 20 * round(player.x/20)
                val = "right"
                tmcheck4 = False
        elif keyboard[keys.A] and player.left > 0 and act == 1:
            if not tmcheck4:
                tm4 = time()
                tmcheck4 = True
            elif time() >= tm4 + 0.15:
                player.x = player.x - 31
                player.x = 20 * round(player.x/20)
                val = "left"
                tmcheck4 = False
        elif keyboard[keys.W] and player.top > 0 and act == 1:
            if not tmcheck4:
                tm4 = time()
                tmcheck4 = True
            elif time() >= tm4 + 0.15:
                player.y = player.y - 40
                val = "up"
                tmcheck4 = False
        elif keyboard[keys.S] and player.bottom < HEIGHT and act == 1:
            if not tmcheck4:
                tm4 = time()
                tmcheck4 = True
            elif time() >= tm4 + 0.15:
                player.y = player.y + 31
                player.y = 20 * round(player.y/20)
                val = "down"
                tmcheck4 = False

        elif keyboard[keys.RIGHT] and player.right < WIDTH and act == 1:
            if not tmcheck4:
                tm4 = time()
                tmcheck4 = True
            elif time() >= tm4 + 0.15:
                player.x = player.x + 31
                player.x = 20 * round(player.x/20)
                val = "right"
                tmcheck4 = False
        elif keyboard[keys.LEFT] and player.left > 0 and act == 1:
            if not tmcheck4:
                tm4 = time()
                tmcheck4 = True
            elif time() >= tm4 + 0.15:
                player.x = player.x - 31
                player.x = 20 * round(player.x/20)
                val = "left"
                tmcheck4 = False
        elif keyboard[keys.UP] and player.top > 0 and act == 1:
            if not tmcheck4:
                tm4 = time()
                tmcheck4 = True
            elif time() >= tm4 + 0.15:
                player.y = player.y - 40
                val = "up"
                tmcheck4 = False
        elif keyboard[keys.DOWN] and player.bottom < HEIGHT and act == 1:
            if not tmcheck4:
                tm4 = time()
                tmcheck4 = True
            elif time() >= tm4 + 0.15:
                player.y = player.y + 31
                player.y = 20 * round(player.y/20)
                val = "down"
                tmcheck4 = False
        if keyboard[keys.SPACE] and level > 3 and level != 4:
            if time() >= tm5 + 4:
                ghost.x = random.randint(0, WIDTH)
                ghost.x = 40 * round(ghost.x/40)
                ghost.y = random.randint(0, HEIGHT)
                ghost.y = 40 * round(ghost.y/40)
                tmcheck5 = False
            if not tmcheck5:
                tm5 = time()
                tmcheck5 = True
        if keyboard[keys.X]:
            if time() >= tm7 + 10:
                tmcheck7 = False
                for i in range(0,len(bricks)):
                    if bricks[i].colliderect(player):
                        try:
                            terrains[i+1] = "explosion"
                        except:
                            pass
                        try:
                            terrains[i+2] = "explosion"
                        except:
                            pass
                        try:
                            terrains[i-1] = "explosion"
                        except:
                            pass
                        try:
                            terrains[i-2] = "explosion"
                        except:
                            pass
                        try:
                            terrains[i+int(HEIGHT/40)] = "explosion"
                        except:
                            pass
                        try:
                            terrains[i+int(HEIGHT/40)+int(HEIGHT/40)] = "explosion"
                        except:
                            pass
                        try:
                            terrains[i-int(HEIGHT/40)] = "explosion"
                        except:
                            pass
                        try:
                            terrains[(i-int(HEIGHT/40))-int(HEIGHT/40)] = "explosion"
                        except:
                            pass
            if not tmcheck7:
                tm7 = time()
                tmcheck7= True
        if level >= 4:
            if time() > startime + 4.5:
                if level > 4:
                    if ghost.x < player.x and (random.randint(1,5)%2 ==0):
                        ghost.x += (level - 2)/2
                    if ghost.x > player.x and (random.randint(1,5)%2 ==0):
                        ghost.x -= (level - 2)/2
                    if ghost.y < player.y and (random.randint(1,5)%2 ==0):
                        ghost.y += (level -2)/2
                    if ghost.y > player.y and (random.randint(1,5)%2 ==0):
                        ghost.y -= (level-2)/2
                if level == 4:
                    ghost.x = ghost.x + xvel
                    ghost.y = ghost.y + yvel
                    if ghost.right > WIDTH:
                        xvel = xvel * -1
                        #xvel += random.uniform(-2.5, 2.5)
                        #yvel += random.uniform(-1.5, 1.5)
                        ghost.x = ghost.x + xvel
                        ghost.y = ghost.y + yvel
                    if ghost.bottom > HEIGHT:
                        yvel = yvel * -1
                        #yvel += random.uniform(-2.5, 2.5)
                        #xvel += random.uniform(-1.5, 1.5)
                        ghost.x = ghost.x + xvel
                        ghost.y = ghost.y + yvel
                    if ghost.left < 0:
                        xvel = xvel * -1
                        #xvel += random.uniform(-2.5, 2.5)
                        #yvel += random.uniform(-1.5, 1.5)
                        ghost.x = ghost.x + xvel
                        ghost.y = ghost.y + yvel
                    if ghost.top < 0:
                        yvel = yvel * -1
                        #yvel += random.uniform(-2.5, 2.5)
                        #xvel += random.uniform(-1.5, 1.5)
                        ghost.x = ghost.x + xvel
                        ghost.y = ghost.y + yvel
                    #print(str(xvel) + " " + str(yvel))
        for i in range(0, len(bricks)):
            if bricks[i].colliderect(player):
                if (terrains[i] == "dirt" and player.y == 0) or (terrains[i] == "dirt" and i % int(HEIGHT/40) == 0):
                    terrains[i] = "space2"
                elif terrains[i] == "dirt":
                    terrains[i] = "space"
                elif terrains[i] == "teleport" and i == 0:
                    terrains[-2] = "space2"
                    player.x = WIDTH - 40
                    player.y = HEIGHT - 80
                elif terrains[i] == "teleport" and i == 14:
                    player.x = WIDTH - 40
                    player.y = 40
                elif terrains[i] == "teleport" and i == 285:
                    player.x = WIDTH - 40
                    player.y = 40
                    player.x = 0
                    player.y = HEIGHT - 80
                elif terrains[i] == "teleport":
                    player.x = 0
                    player.y = 40
                elif terrains[i] == "spike":
                    alive = False
                    boulder = "spike"
                    for b in range(0, len(bricks)-1):
                        terrains[i] == "spike"
                        terrain == "space"
                        alive = False
                elif terrains[i] == "gem":
                    if i % int(HEIGHT/40) == 0:
                        terrains[i] = "space2"
                    else:
                        terrains[i] = "space"
                    score += 10
                elif terrains[i] == "boulder":
                    try:
                        if val == "right" and (terrains[i+int(HEIGHT/40)] == "space" or terrains[i-int(HEIGHT/40)] == "space2"):
                            if player.y == 0 or i % int(HEIGHT/40) == 0:
                                terrains[i] = "space2"
                            else:
                                terrains[i] = "space"
                            terrains[i+int(HEIGHT/40)] = "boulder"
                        elif val == "left" and (terrains[i-int(HEIGHT/40)] == "space" or terrains[i-int(HEIGHT/40)] == "space2"):
                            if  player.y == 0 or i % int(HEIGHT/40) == 0:
                                terrains[i] = "space2"
                            else:
                                terrains[i] = "space"
                            terrains[i-int(HEIGHT/40)] = "boulder"
                        else:
                            player.x = sx
                            player.y = sy
                    except:
                        player.x = sx
                        player.y = sy
                elif terrains[i] == "tnt":
                    try:
                        if val == "right" and (terrains[i+int(HEIGHT/40)] == "space" or terrains[i-int(HEIGHT/40)] == "space2"):
                            if  player.y == 0 or i % int(HEIGHT/40) == 0:
                                terrains[i] = "space2"
                            else:
                                terrains[i] = "space"
                            terrains[i+int(HEIGHT/40)] = "tnt"
                        elif val == "left" and (terrains[i-int(HEIGHT/40)] == "space" or terrains[i-int(HEIGHT/40)] == "space"):
                            if player.y == 0 or i % int(HEIGHT/40) == 0:
                                terrains[i] = "space2"
                            else:
                                terrains[i] = "space"
                            terrains[i-int(HEIGHT/40)] = "tnt"
                        else:
                            player.x = sx
                            player.y = sy
                    except:
                        player.x = sx
                        player.y = sy
                val = "none"
            if level > 4 and bricks[i].colliderect(ghost) and terrains[i] == "tnt":
                number = i
                startime = time()
                explode = True
                ghost.x = random.randint(0, WIDTH)
                ghost.x = 40 * round(ghost.x/40)
                ghost.y = random.randint(0, HEIGHT)
                ghost.y = 40 * round(ghost.y/40)
                sounds.explosion.play()
                try:
                    terrains[i] = "explosion"
                    terrains[i+1] = "explosion"
                    terrains[i+2] = "explosion"
                    #terrains[i+3] = "explosion"
                except:
                    pass
                try:
                    terrains[i-1] = "explosion"
                    terrains[i-2] = "explosion"
                    #terrains[i-3] = "explosion"
                except:
                    pass
                try:
                    terrains[i+(int(HEIGHT/40)*1)] = "explosion"
                    terrains[i+(int(HEIGHT/40)*2)] = "explosion"
                    #terrains[i+(int(HEIGHT/40)*3)] = "explosion"
                except:
                    pass
                try:
                    terrains[i-(int(HEIGHT/40)*1)] = "explosion"
                    terrains[i-(int(HEIGHT/40)*2)] = "explosion"
                    #terrains[i-(int(HEIGHT/40)*3)] = "explosion"
                except:
                    pass

                if (bricks[i].y == player.y and player.x <= (bricks[i].x + 80) and player.x >= (bricks[i].x - 80)) or (bricks[i].x == player.x and player.y <= (bricks[i].y + 80) and player.y >= (bricks[i].y - 80)) and not(player.x == 0 and player.y ==40):
                    alive = False
            if level > 4 and bricks[i].colliderect(ghost) and terrains[i] == "explosion" and keyboard[keys.X]:
                startime = time()
                ghost.x = random.randint(0, WIDTH)
                ghost.x = 40 * round(ghost.x/40)
                ghost.y = random.randint(0, HEIGHT)
                ghost.y = 40 * round(ghost.y/40)
                pass

            try:
                if (terrains[i] == "gem" and (terrains[i+1] == "space" or terrains[i+1] == "spike" or terrains[i+1] == "tnt") and (player.y != (bricks[i].y + 40) or player.x != bricks[i].x)):
                    if not tmcheck2:
                        tm2 = time()
                        tmcheck2 = True
                    elif time() >= tm2 + 0.3:
                        if terrains[i+1] != "tnt":
                            if i % int(HEIGHT/40) == 0:
                                terrains[i] = "space2"
                            else:
                                terrains[i] = "space"
                            terrains[i+1] = "gem"
                            tmcheck2 = False
                        else:
                            explode = True
                            number = i+1
            except:
                pass
            try:
                if terrains[i] == "boulder" and (terrains[i+1] == "space" or terrains[i+1] == "spike" or terrains[i+1] == "tnt") and ((player.y != (bricks[i].y + 40) or player.x != bricks[i].x)or checks[i] == True):
                    if not tmcheck:
                        tm = time()
                        tmcheck = True
                    elif time() >= tm + 0.3:
                        if terrains[i+1] != "tnt":
                            if i % int(HEIGHT/40) ==0:
                                terrains[i] = "space2"
                            else:
                                terrains[i] = "space"
                            terrains[i+1] = "boulder"
                            tmcheck = False
                        else:
                            explode = True
                            number = i+1
                    checks[i+1] = True
                    check = True
                    if bricks[i+1].colliderect(player) and terrains[i+1] != "space2" and terrains[i+1] == "space":
                        terrains[i] = "space"
                        terrains[i+1] = "boulder"
                        boulder = True
                        alive = False
                elif terrains[i] == "boulder":
                    check = False
                    checks[i] = False
            except:
                pass
            try:
                if terrains[i] == "tnt" and (terrains[i+1] == "space" or terrains[i+1] == "spike") and ((player.y != (bricks[i].y + 40) or player.x != bricks[i].x)):
                    if not tmcheck3:
                        tm3 = time()
                        tmcheck3 = True
                    elif time() >= tm3 + 0.3:
                        if (terrains[i] == "dirt" and player.y == 0) or (terrains[i] == "dirt" and i % int(HEIGHT/40) == 0):
                            terrains[i] = "space2"
                        else:
                            terrains[i] = "space"
                        terrains[i+1] = "tnt"
                        number = i+1
                        tmcheck3 = False
                        explode = True
                elif (terrains[i] == "tnt" and terrains[i+1] != "space" and terrains[i+1] != "spike" and explode and ((player.y != (bricks[i].y + 40) or (player.x != bricks[i].x)) and number == i) or (bricks[i].colliderect(ghost) and level > 4) and terrains[i] == "tnt"):
                    sounds.explosion.play()
                    terrains[i] = "explosion"
                    terrains[i+1] = "explosion"
                    terrains[i+2] = "explosion"
                    #terrains[i+3] = "explosion"
                    terrains[i-1] = "explosion"
                    terrains[i-2] = "explosion"
                    #terrains[i-3] = "explosion"
                    terrains[i+(int(HEIGHT/40)*1)] = "explosion"
                    terrains[i+(int(HEIGHT/40)*2)] = "explosion"
                    #terrains[i+(int(HEIGHT/40)*3)] = "explosion"
                    terrains[i-(int(HEIGHT/40)*1)] = "explosion"
                    terrains[i-(int(HEIGHT/40)*2)] = "explosion"
                    #terrains[i-(int(HEIGHT/40)*3)] = "explosion"
                    if (bricks[i].y == player.y and player.x <= (bricks[i].x + 80) and player.x >= (bricks[i].x - 80)) or (bricks[i].x == player.x and player.y <= (bricks[i].y + 80) and player.y >= (bricks[i].y - 80)) and not(player.x == 0 and player.y ==40) and not(player.x == 0 and player.y ==40):
                        alive = False
                if (terrains[i] == "tnt" and terrains[i+1] != "space" and level >= 3 and level != 4 and level != 5 and (bricks[i-1].colliderect(player) or bricks[i+int(HEIGHT/40)].colliderect(player) or bricks[i-int(HEIGHT/40)].colliderect(player))) or timer:
                    timer = True
                    if not tmcheck6:
                        tm6 = time()
                        tmcheck6 = True
                    elif time() >= tm6 + 0.1:
                        sounds.explosion.play()
                        tmcheck6 = False
                        terrains[i] = "explosion"
                        terrains[i+1] = "explosion"
                        terrains[i+2] = "explosion"
                        #terrains[i+3] = "explosion"
                        terrains[i-1] = "explosion"
                        terrains[i-2] = "explosion"
                        #terrains[i-3] = "explosion"
                        terrains[i+(int(HEIGHT/40)*1)] = "explosion"
                        terrains[i+(int(HEIGHT/40)*2)] = "explosion"
                        #terrains[i+(int(HEIGHT/40)*3)] = "explosion"
                        terrains[i-(int(HEIGHT/40)*1)] = "explosion"
                        terrains[i-(int(HEIGHT/40)*2)] = "explosion"
                        #terrains[i-(int(HEIGHT/40)*3)] = "explosion"
                        if not (player.y >= 80 and player.x >= 80) and (bricks[i].y == player.y and player.x <= (bricks[i].x + 80) and player.x >= (bricks[i].x - 80)) or (bricks[i].x == player.x and player.y <= (bricks[i].y + 80) and player.y >= (bricks[i].y - 80)) and not(player.x == 0 and player.y ==40):
                            alive = False
            except:
                pass
            gems = 0
            for i in range(0, len(terrains)):
                if terrains[i] == "gem":
                    gems += 1
            if gems == 0:
                state = "win"# Write your code here :-)
    if keyboard[keys.R] and lives > 0 and alive == False:
        level -=1
        create()
        alive = True
        state = "playing"
        lives -= 1
        sleep(0.5)
    elif keyboard[keys.R] and lives > 0 and lives >= 1:
        level -=1
        create()
        alive = True
        state = "playing"
        sleep(0.5)
    elif keyboard[keys.R]:
        level = 0
        create()
        level = 0
        score = 0
        alive = True
        state = "playing"
        lives = 5
        sleep(0.5)
    if level >= 4:
        if (ghost.x <= player.x + 20) and (ghost.x >= player.x - 20) and (ghost.y >= player.y - 20) and (ghost.y <= player.y + 20) and time() > startime + 3.5:
            alive = False
            boulder = "ghost"
