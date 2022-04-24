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

    def move_left(self):
        pass

    def move_right(self):
        pass

    def move_up(self):
        print("moving")
        player = self.player()
        player[1].move(0, 1)

    def move_down(self):
        pass

    def __update__(self):
        game.screen.fill(self.background)
        game.screen.blit(self.player()[0], self.player()[1])

class Obstacle():
    def __init__(self):
        self.list = []

    def create_obstacle(self, x, y, width, height, img):
        print(x, y, width, height, img)
        img = pygame.image.load(img)
        img = pygame.transform.smoothscale(img, (width, height))
        obstacle = img.get_rect()
        self.list.append([img, obstacle])

game = Game()
obstacles = Obstacle()

obstacles.create_obstacle(200, 100, 30, 30, "ball2.png")
while game.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: exit()
        keys = pygame.key.get_pressed()
        if(keys[pygame.K_w]): game.move_up()

    game.__update__()
    pygame.display.flip()