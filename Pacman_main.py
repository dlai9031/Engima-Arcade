from gamelibwillh2 import*
import random
#this code will give us a cover and lets us click space to start
def start():
    game = Game(800,800,"Pacman")

    cover=Image("PacMan_Files\\cover.png",game)

    cover.resizeTo(800,800)

    while not game.over:
        game.processInput()
        cover.draw()
        f1 = Font (blue,40,black,"Comic Sans Ms")
        game.drawText("Press Space bar to Play",300,740,f1)
        #When pressed the game starts and runs
        if keys.Pressed[K_SPACE]:
            game.over=True
            rundown()
        #if clicked you leave the game
        if keys.Pressed[K_ESCAPE]:
            game.over = True
            game.quit()
            quit()
    
        game.update(60)
#start of lvl 1 and in this game it shows how pacman has to go around collecting
#balls which are dots and get enough points to win. While doing that a ghost
#will be following you and trying to make you lose. The ghost is another player.
def rundown():
    game = Game(1000,800,"Pac Man",50)

    bk = Image("PacMan_Files\\Background.png",game)
    pacman = Animation("PacMan_Files\\pacman.png",16,game,128/4,128/4)
    ghost= Animation("PacMan_Files\\ghost.png",4,game,80/4,20)
    song = Sound("PacMan_Files\\song.wav",1)

    #dots list
    dot=[]
    for index in range(100):
        dot.append(Animation("PacMan_Files\\dot.png",4,game,64/2,64/2))
        dot[index].resizeBy(5)
    for index in range(100):
        dot[index].draw()
        x = randint(10,1000)
        y = randint(10,800)
        dot[index].moveTo(x,y)

    #apple list
    apple=[]
    for index in range(3):
        apple.append(Image("PacMan_Files\\apple.png",game))
        apple[index].resizeBy(-80)
    for index in range(3):
        apple[index].draw()
        x = randint(10,1000)
        y = randint(10,800)
        apple[index].moveTo(x,y)
    
    game.setBackground(bk)
    bk.resizeTo(1000,800)

    pacman.resizeBy(80)
    pacman.moveTo(100,390)

    ghost.resizeBy(70)
    ghost.moveTo(500,390)

    while not game.over:
        game.processInput()
        bk.draw()
        ghost.draw()
        pacman.draw()
        song.play()
        #apple points
        for index in range(3):
            apple[index].draw()
            if apple[index].collidedWith(pacman):
                apple[index].visible=False
                game.score+=500
        #dot/ghost points
        for index in range(100):
            dot[index].draw()
            if dot[index].collidedWith(pacman):
                dot[index].visible=False
                game.score+=100
            if ghost.collidedWith(pacman):
                game.score-=500
                ghost.moveTo(x,y)
        #pacman movement
        if keys.Pressed[K_ESCAPE]:
            game.over = True
            game.quit()
            quit()
        if keys.Pressed[K_DOWN]:
            pacman.y+=10
        if keys.Pressed[K_UP]:
            pacman.y-=10
        if keys.Pressed[K_LEFT]:
            pacman.x-=10
        if keys.Pressed[K_RIGHT]:
            pacman.x+=10
        #top pacman
        if pacman.y<=20:
            pacman.y+=50
            game.score-=50
        #bottom pacman
        if pacman.y>=780:
            pacman.y-=25
            game.score-=50
        #right pacman
        if pacman.x>980:
            pacman.moveTo(25,390)
        #left pacman
        if pacman.x<=0:
            pacman.moveTo(970,390)
        #ghost code now
        if keys.Pressed[K_s]:
            ghost.y+=11
        if keys.Pressed[K_w]:
            ghost.y-=11
        if keys.Pressed[K_a]:
            ghost.x-=11
        if keys.Pressed[K_d]:
            ghost.x+=11
        #top ghost
        if ghost.y<=20:
            ghost.y+=50
        #bottom ghost
        if ghost.y>=780:
            ghost.y-=25
        #right ghost
        if ghost.x>=980:
            ghost.moveTo(25,390)
        #left ghost
        if ghost.x<=0:
            ghost.moveTo(970,390)
        #pacman and ghost
        if ghost.collidedWith(pacman):
            game.score-=500
            ghost.moveTo(500,390)
        #game over
        if game.time<=0 or game.score<=-1000:
            game.over=True
            ending()
        if game.score>=7000:
            game.over=True
            ending_2()
        game.displayScore(10,10)
        game.displayTime(110,10)
        game.update(20)
    game.quit()
#when you lose the game because the time ran out or u got a certain negative
#points.After you lose the game over screen pops up and u can either replay or
#leave the game
def ending():
    game=Game(1000,800,"The End")
    gg = Image("PacMan_Files\\gg.jpg",game)
    gg.resizeTo(1000,800)
    while not game.over:
        game.processInput()
        gg.draw()
        #pressed and u leave the game
        if keys.Pressed[K_ESCAPE]:
            game.over = True
            game.quit()
            quit()
        f1 = Font (blue,80,black,"Comic Sans Ms")
        game.drawText("Press R to Replay lvl 1",100,30,f1)
        #pressed amd you can replay the game
        if keys.Pressed[K_r]:
            game.over=True
            rundown()
        game.update(30)
    game.quit()
#if the pacman win the game because u got a certain points than a win screen
#pops up and you can either replay the first level or go on to the next.
def ending_2():
    game=Game(1000,800,"The End")
    gg2 = Image("PacMan_Files\\gg2.png",game)
    win = Image("PacMan_Files\\win.png",game)
    gg2.resizeTo(1000,800)
    win.resizeBy(10)
    win.moveTo(500,700)
    while not game.over:
        game.processInput()
        gg2.draw()
        win.draw()
        #pressed and u leave the game
        if keys.Pressed[K_ESCAPE]:
            game.over = True
            game.quit()
            quit()
        f1 = Font (blue,50,black,"Comic Sans Ms")
        game.drawText("Press R to Replay lvl 1",255,30,f1)
        game.drawText("Press N to play lvl 2",280,-10,f1)
        #pressed r and u can play lvl 1 again
        if keys.Pressed[K_r]:
            game.over=True
            rundown()
        #pressed n and u can go to next lvl and play it
        if keys.Pressed[K_n]:
            game.over=True
            pt2()
        game.update(30)
    game.quit()

#this is the second level of the game where it is the same code of rundown
#but a few things are u need higher points and the ghostis bigger
def pt2():
    game = Game(1000,800,"Pac Man",40)

    bk = Image("PacMan_Files\\Background.png",game)
    pacman = Animation("PacMan_Files\\pacman.png",16,game,128/4,128/4)
    ghost= Animation("PacMan_Files\\ghost.png",4,game,80/4,20)
    song = Sound("PacMan_Files\\song.wav",1)

    #dots list
    dot=[]
    for index in range(100):
        dot.append(Animation("PacMan_Files\\dot.png",4,game,64/2,64/2))
        dot[index].resizeBy(5)
    for index in range(100):
        dot[index].draw()
        x = randint(10,1000)
        y = randint(10,800)
        dot[index].moveTo(x,y)

    #apple list
    apple=[]
    for index in range(3):
        apple.append(Image("PacMan_Files\\apple.png",game))
        apple[index].resizeBy(-80)
    for index in range(3):
        apple[index].draw()
        x = randint(10,1000)
        y = randint(10,800)
        apple[index].moveTo(x,y)
    
    game.setBackground(bk)
    bk.resizeTo(1000,800)

    pacman.resizeBy(80)
    pacman.moveTo(100,390)

    ghost.resizeBy(400)
    ghost.moveTo(500,390)

    while not game.over:
        game.processInput()
        bk.draw()
        ghost.draw()
        pacman.draw()
        song.play()
        #apple points
        for index in range(3):
            apple[index].draw()
            if apple[index].collidedWith(pacman):
                apple[index].visible=False
                game.score+=750
        #dot/ghost points
        for index in range(100):
            dot[index].draw()
            if dot[index].collidedWith(pacman):
                dot[index].visible=False
                game.score+=150
            if ghost.collidedWith(pacman):
                game.score-=650
                ghost.moveTo(x,y)
        #pacman movement
        if keys.Pressed[K_DOWN]:
            pacman.y+=10
        if keys.Pressed[K_UP]:
            pacman.y-=10
        if keys.Pressed[K_LEFT]:
            pacman.x-=10
        if keys.Pressed[K_RIGHT]:
            pacman.x+=10
        if keys.Pressed[K_ESCAPE]:
            game.over = True
            game.quit()
            quit()
        #top pacman
        if pacman.y<=20:
            pacman.y+=50
            game.score-=50
        #bottom pacman
        if pacman.y>=780:
            pacman.y-=25
            game.score-=50
        #right pacman
        if pacman.x>980:
            pacman.moveTo(25,390)
        #left pacman
        if pacman.x<=0:
            pacman.moveTo(970,390)
        #ghost code now
        if keys.Pressed[K_s]:
            ghost.y+=10
        if keys.Pressed[K_w]:
            ghost.y-=10
        if keys.Pressed[K_a]:
            ghost.x-=10
        if keys.Pressed[K_d]:
            ghost.x+=10
        #top ghost
        if ghost.y<=20:
            ghost.y+=50
        #bottom ghost
        if ghost.y>=780:
            ghost.y-=25
        #right ghost
        if ghost.x>=980:
            ghost.moveTo(25,390)
        #left ghost
        if ghost.x<=0:
            ghost.moveTo(970,390)
        #pacman and ghost
        if ghost.collidedWith(pacman):
            game.score-=500
            ghost.moveTo(500,390)
        #game over
        if game.time<=0 or game.score<=-1000:
            game.over=True
            ending()
        if game.score>=10000:
            game.over=True
            ending_3()
        game.displayScore(10,10)
        game.displayTime(110,10)
        game.update(20)
    game.quit()
#if you win in lvl 2
def ending_3():
    game=Game(1000,800,"The End")
    gg2 = Image("PacMan_Files\\gg2.png",game)
    win = Image("PacMan_Files\\win.png",game)
    gg2.resizeTo(1000,800)
    win.resizeBy(10)
    win.moveTo(500,700)
    while not game.over:
        game.processInput()
        gg2.draw()
        win.draw()
        #pressed and u leave the game
        if keys.Pressed[K_ESCAPE]:
            game.over = True
            game.quit()
            quit()
        f1 = Font (blue,50,black,"Comic Sans Ms")
        game.drawText("Press R to Replay lvl 1",255,20,f1)
        #press r to replay the game from level 1.
        if keys.Pressed[K_r]:
            game.over=True
            rundown()
        game.update(30)
    game.quit()
start() 
