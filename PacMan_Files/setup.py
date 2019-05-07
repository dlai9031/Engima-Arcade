from gamelib import*
import random


def rundown():
    game = Game(1000,800,"Pac Man",50)

    bk = Image("Background.png",game)
    pacman = Animation("pacman.png",16,game,128/4,128/4)
    ghost= Animation("ghost.png",4,game,80/4,20)
    song = Sound("song.wav",1)

    #dots list
    dot=[]
    for index in range(100):
        dot.append(Animation("dot.png",4,game,64/2,64/2))
        dot[index].resizeBy(5)
    for index in range(100):
        dot[index].draw()
        x = randint(10,1000)
        y = randint(10,800)
        dot[index].moveTo(x,y)

    #apple list
    apple=[]
    for index in range(3):
        apple.append(Image("apple.png",game))
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
    
def ending():
    game=Game(1000,800,"The End")
    gg = Image("gg.jpg",game)
    gg.resizeTo(1000,800)
    while not game.over:
        game.processInput()
        gg.draw()
        f1 = Font (blue,80,black,"Comic Sans Ms")
        game.drawText("Press R to Replay lvl 1",100,30,f1)
        if keys.Pressed[K_ESCAPE]:
            game.over = True
        if keys.Pressed[K_r]:
            game.over=True
            rundown()
        game.update(30)
    game.quit()
def ending_2():
    game=Game(1000,800,"The End")
    gg2 = Image("gg2.png",game)
    win = Image("win.png",game)
    gg2.resizeTo(1000,800)
    win.resizeBy(10)
    win.moveTo(500,700)
    while not game.over:
        game.processInput()
        gg2.draw()
        win.draw()
        f1 = Font (blue,50,black,"Comic Sans Ms")
        game.drawText("Press R to Replay lvl 1",255,30,f1)
        game.drawText("Press N to play lvl 2",280,-10,f1)
        if keys.Pressed[K_ESCAPE]:
            game.over = True
        if keys.Pressed[K_r]:
            game.over=True
            rundown()
        if keys.Pressed[K_n]:
            game.over=True
            pt2()
        game.update(30)
    game.quit()

def pt2():
    game = Game(1000,800,"Pac Man",40)

    bk = Image("Background.png",game)
    pacman = Animation("pacman.png",16,game,128/4,128/4)
    ghost= Animation("ghost.png",4,game,80/4,20)
    song = Sound("song.wav",1)

    #dots list
    dot=[]
    for index in range(100):
        dot.append(Animation("dot.png",4,game,64/2,64/2))
        dot[index].resizeBy(5)
    for index in range(100):
        dot[index].draw()
        x = randint(10,1000)
        y = randint(10,800)
        dot[index].moveTo(x,y)

    #apple list
    apple=[]
    for index in range(3):
        apple.append(Image("apple.png",game))
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
        if keys.Pressed[K_ESCAPE]:
            game.over = True
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

def ending_3():
    game=Game(1000,800,"The End")
    gg2 = Image("gg2.png",game)
    win = Image("win.png",game)
    gg2.resizeTo(1000,800)
    win.resizeBy(10)
    win.moveTo(500,700)
    while not game.over:
        game.processInput()
        gg2.draw()
        win.draw()
        f1 = Font (blue,50,black,"Comic Sans Ms")
        game.drawText("Press R to Replay lvl 1",255,20,f1)
        if keys.Pressed[K_ESCAPE]:
            game.over = True
        if keys.Pressed[K_r]:
            game.over=True
            rundown()
        game.update(30)
    game.quit()

