from random import randint
import pygame



class PlayFrame:
    def __init__(self):
        self.area = []


class Ball:
    def __init__(self):
        self.whichMove = 1
        self.yVelocity = -2
        self.xVelocity = 1
        self.x = 270
        self.y = 368
        self.size = 4
        self.color = (128, 128, 0)

    def move(self):
        self.y += self.yVelocity
        self.x += self.xVelocity

    def move2(self):
        if self.y % 2 == 0:
            self.x += self.xVelocity
        self.y += self.yVelocity

    def move3(self):
        if self.y % 3 == 0:
            self.x += self.xVelocity
        self.y += self.yVelocity

    def changeDirectionY(self):
        self.yVelocity *= -1

    def changeDirectionX(self):
        self.xVelocity *= -1


class Block:
    length = 50
    width = 10
    def __init__(self, x):
        self.x = x
        self.y = 10
        self.punchesLeft = 2
        self.color = (200, 50, 20)
        self.area = []
        for p in range(Block.length):
            self.area.append(self.x + p)

    def decreasePunches(self):
        self.punchesLeft -= 1
        if self.punchesLeft == 1:
            self.color = (50, 50, 200)
        if self.punchesLeft == 0:
            self.color = (200, 200, 50)


class Paddle:
    def __init__(self):
        self.jumpsize = 2
        self.x = 270
        self.y = 370
        self.length = 60
        self.height = 10
        self.color = (64, 255, 32)
        self.area = []

    def calculatePosition(self):
        self.area = []
        for p in range(self.length):
            self.area.append(self.x + p)


#Initialize objects
done = False
ball = Ball()
paddle = Paddle()
blocks = []
for b in range(10):
    block = Block(b*60)
    blocks.append(block)


#Initialize some more needed variables and the main loop
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((600, 400))


## mainloop ##
while not done:
    pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((0,0,0))

    for b in blocks:
        pygame.draw.rect(screen, b.color, pygame.Rect(b.x, b.y, b.length, b.width))

    pygame.draw.rect(screen, paddle.color, pygame.Rect(paddle.x, paddle.y, 60, 10))
    if pressed[pygame.K_LEFT]: paddle.x -= paddle.jumpsize
    if pressed[pygame.K_RIGHT]: paddle.x += paddle.jumpsize


    pygame.draw.circle(screen, ball.color, (ball.x, ball.y), ball.size)

    paddle.calculatePosition()

    if ball.whichMove == 1:
        ball.move()
    elif ball.whichMove == 2:
        ball.move2()
    elif ball.whichMove == 3:
        ball.move3()
    if (ball.y == paddle.y and ball.x in paddle.area):
        if ball.x >= paddle.area[0] and ball.x < paddle.area[10]:
            ball.xVelocity = -1
            ball.whichMove = 2
        elif ball.x >= paddle.area[10] and ball.x < paddle.area[25]:
            ball.xVelocity = -1
            ball.whichMove = 3
        elif ball.x >= paddle.area[25] and ball.x < paddle.area[35]:
            ball.xVelocity = 0
            ball.whichMove = 1
        elif ball.x >= paddle.area[35] and ball.x < paddle.area[49]:
            ball.xVelocity = 1
            ball.whichMove = 3
        elif ball.x >= paddle.area[40] and ball.x < paddle.area[59]:
            ball.xVelocity = 1
            ball.whichMove = 2
        ball.changeDirectionY()

    if(ball.y == 0):
        ball.changeDirectionY()

    if(ball.y == 18):
        for b in blocks:
            if ball.x in b.area:
                if b.punchesLeft == 0:
                    blocks.remove(b)
                b.decreasePunches()
                ball.changeDirectionY()

    if (ball.x == 0 or ball.x == 600):
        ball.changeDirectionX()


    clock.tick(200)
    pygame.display.flip()
