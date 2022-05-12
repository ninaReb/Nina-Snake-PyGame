# Snake Game!
import pygame, random, sys, time

# Errors
check_errors = pygame.init()
if check_errors[1] > 0:
    print("(!) Had {0} errors, exiting...".format(check_errors[1]))
    sys.exit(-1)
else:
    print("(+) PyGame successfully initialized")

# Interface
playSurface = pygame.display.set_mode((720, 460))
pygame.display.set_caption("Snake Game!")
red = pygame.Color(255, 0, 0) #game over
green = pygame.Color(12, 108, 7 ) #snake
blue = pygame.Color(0, 0, 255) 
black = pygame.Color(0, 0, 0)#score
cream = pygame.Color(225, 221, 146 ) #bg
brown = pygame.Color(81, 20, 7) #food

# Snake
fpsController = pygame.time.Clock()

snakePos = [110, 50]
snakeBody = [[100, 50], [90, 50], [80, 50]]
direction = 'RIGHT'
changeto = direction

score = 0

# Food
randomX = random.randrange(1,72)*10
randomY = random.randrange(1,46)*10

foodPos = [randomX, randomY]
foodSpawn = True

#game over
def gameOver():
    myFont = pygame.font.SysFont('monaco', 72)
    GOsurface = myFont.render('Game Over!', True, red)
    GOrectangle = GOsurface.get_rect()
    GOrectangle.midtop = (360, 15)
    playSurface.blit(GOsurface, GOrectangle)
    pygame.display.flip()
    showScore(0)
    time.sleep(5)
    pygame.quit()
    sys.exit()

#Score Board
def showScore(choice = 1):
        scoreFont = pygame.font.SysFont('monaco', 30)
        scoreSurface = scoreFont.render('Score: {0}'.format(score), True, black)
        scoreRect  = scoreSurface.get_rect()
        if choice == 1:
            scoreRect.midtop = (80, 10)
        else:
            scoreRect.midtop = (360, 120)
        playSurface.blit(scoreSurface, scoreRect)
        pygame.display.flip()
        

# Events
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changeto = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changeto = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                changeto = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changeto = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
                
    if changeto == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changeto == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changeto == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changeto == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'
    
    # updtae positions
    if direction == 'RIGHT':
        snakePos[0] += 10
    if direction == 'LEFT':
        snakePos[0] -= 10        
    if direction == 'UP':
        snakePos[1] -= 10        
    if direction == 'DOWN':
        snakePos[1] += 10        

    # body mechanism
    snakeBody.insert(0, list(snakePos))
    
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        score += 1
        foodSpawn = False
    else:
        snakeBody.pop()
        
    if foodSpawn == False:
        foodPos = [random.randrange(1,72)*10, random.randrange(1,46)*10]
    foodSpawn = True
    
     
    #Drawing
    playSurface.fill(cream)
    for pos in snakeBody:
        pygame.draw.rect(playSurface, green, pygame.Rect(pos[0], pos[1], 10, 10))
    
    pygame.draw.rect(playSurface, brown, pygame.Rect(foodPos[0], foodPos[1], 10, 10))
    
    if snakePos[0] > 710 or snakePos[0] < 0:
        gameOver()
    if snakePos[1] > 450 or snakePos[1] < 0:
        gameOver()
    
    for block in snakeBody[1:]:
        if snakePos[0] == block[0] and snakePos[1] == block[1]:
            gameOver()
        
        
       
    pygame.display.flip()
    showScore()
    fpsController.tick(12)

    