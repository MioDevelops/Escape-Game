import pygame
pygame.init()

class Game():
    def __init__(self):
        self.background = (100, 0, 150)
        self.running = True
        self.screen = pygame.display.set_mode([500,400])

    def player(self):
        png = pygame.image.load("ball.png")
        png = pygame.transform.smoothscale(png, (40, 40))
        ball = png.get_rect()
        return png, ball

class Obstacle():
    def __init__(self):
        self.list = []

    def create_obstacle(self, x, y, width, height, img):
        print(x, y, width, height, img)
        img = pygame.image.load(img)
        img = pygame.transform.smoothscale(img, (width, height))
        obstacle = img.get_rect()
        obstacle.move(x, y)
        self.list.append([img, obstacle])

game = Game()
obstacles = Obstacle()

obstacles.create_obstacle(100, 100, 30, 30, "ball2.png")
while game.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: exit()

    game.screen.fill(game.background)
    for i in obstacles.list:
        game.screen.blit(i[0], i[1])
    game.screen.blit(game.player()[0], game.player()[1])
    pygame.display.flip()