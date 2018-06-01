from random import randint
import pygame



class PlayFrame:
    def __init__(self):
        self.area = []


class Ball:
    def __init__(self):
        self.yVelocity = -2
        self.xVelocity = 1
        self.x = 270
        self.y = 368
        self.size = 4
        self.color = (128, 128, 0)

    def move(self, direction):
        self.y += self.yVelocity
        self.x += self.xVelocity

    def changeDirectionY(self):
        self.yVelocity *= -1

    def changeDirectionX(self):
        self.xVelocity *= -1


class Block:
    length = 50
    width = 10
    color = (200, 50, 20)
    def __init__(self, x):
        self.x = x
        self.y = 10
        self.area = []
        for p in range(Block.length):
            self.area.append(self.x + p)


class Paddle:
    def __init__(self):
        self.jumpsize = 5
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



while not done:
    pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((0,0,0))

    for b in blocks:
        pygame.draw.rect(screen, b.color, pygame.Rect(b.x, b.y, b.length, b.width))

    pygame.draw.rect(screen, paddle.color, pygame.Rect(paddle.x, paddle.y, 60, 10))
    paddle.calculatePosition()
    if pressed[pygame.K_LEFT]: paddle.x -= paddle.jumpsize
    if pressed[pygame.K_RIGHT]: paddle.x += paddle.jumpsize


    pygame.draw.circle(screen, ball.color, (ball.x, ball.y), ball.size)

    ball.move(ball.yVelocity)
    if (ball.y == paddle.y and ball.x in paddle.area):
        ball.changeDirectionY()

    if(ball.y == 18):
        ball.changeDirectionY()

    if (ball.x == 0 or ball.x == 600):
        ball.changeDirectionX()


    clock.tick(200)
    pygame.display.flip()
