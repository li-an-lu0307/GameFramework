import pygame
class Bullet(pygame.sprite.Sprite):

    def __init__(self, init_pos: tuple, is_player):
        super().__init__()
        self._init_pos = init_pos
        self._is_player = is_player
        self.rect = pygame.Rect(init_pos, (5, 8))
        self._y_speed = 10
        if self._is_player:
            self.color = "#21A1F1"
        else:
            self.color = "#FFA500"

    def update(self, *args, **kwargs) -> None:
        if self._is_player:
            self.rect.centery -= self._y_speed
        else:
            self.rect.centery += self._y_speed

    @property
    def game_object_data(self):
        return create_image_view_data(name = "bullet"
                                      , x = self.rect.x
                                      , y = self.rect.y
                                      , width = self.rect.width
                                      , height = self.rect.height
                                      , color = "#"
                                      , angle = 0)