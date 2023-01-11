import pygame

class Neron(pygame.sprite.Sprite):
    """ Один прищелец """

    def __init__(self, screen):
        """ Инициализация на начальную позицию прищельцев """
        super(Neron, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/nerons.png')
        self.rect = self.image.get_rect()
        self.rect.y = self.rect.width
        self.rect.x = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """ Вывод иноприщеленца """
        self.screen.blit(self.image, self.rect)

    def update(self):

        self.y += 0.1
        self.rect.y = self.y



