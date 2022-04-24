import pygame
pygame.init()

class Game():
    def __init__(self):
        self.background = (100, 0, 150)
        self.running = True
        self.screen = pygame.display.set_mode([500,400])
        self.player = pygame.rect.Rect((64, 54, 25, 25))

    def __update__(self):
        self.screen.fill(self.background)
        pygame.draw.rect(self.screen, (0, 0, 0), self.player)

#class Obstacle():
#    def __init__(self):
#        self.list = []
#
#    def create_obstacle(self, x, y, width, height, img):
#        print(x, y, width, height, img)
#        img = pygame.image.load(img)
#        img = pygame.transform.smoothscale(img, (width, height))
#        obstacle = img.get_rect()
#        self.list.append([img, obstacle])
#obstacles = Obstacle()
#obstacles.create_obstacle(200, 100, 30, 30, "ball2.png")

game = Game()
while game.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: exit()
        keys = pygame.key.get_pressed()
        if(keys[pygame.K_w]): game.player.move_ip(0, -2)
        elif(keys[pygame.K_a]): game.player.move_ip(-2, 0)
        elif(keys[pygame.K_s]): game.player.move_ip(0, 2)
        elif(keys[pygame.K_d]): game.player.move_ip(2, 0)

    game.__update__()
    pygame.display.flip()