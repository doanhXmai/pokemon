import pygame

from core.ui import UI


class AvatarScore(UI):
    def __init__(self, image_path, position, score, font, name = "player"):
        super().__init__(image_path, position)
        self.name, self.score, self.font = name, score, font
        self.name_surface, self.score_surface = None, None

        self.image = pygame.image.load(self.image_path).convert_alpha()
        self.scope_rect(position)
        self.scale((64, 64))
        self.update_text()

    def update_score(self, score):
        self.score = score
        self.score_surface = self.font.render(f"Score: {self.score}", True, (255, 255, 255))

    def update_text(self):
        # Create surface of text
        self.name_surface = self.font.render(self.name, True, (255, 255, 255))
        self.score_surface = self.font.render(f"Score: {self.score}", True, (255, 255, 255))

    def scale(self, size):
        # Resize avatar
        self.image = pygame.transform.scale(self.image, size)
        self.rect.size = size


    def scope_rect(self, position):
        if self.rect:
            self.rect.topleft = position
        else:
            self.rect = pygame.Rect(position[0], position[1], 0, 0)

    def draw(self, screen):
        # Draw avatar
        screen.blit(self.image, self.rect.topleft)

        # Tọa độ để vẽ chữ bên phải
        text_x = self.rect.right + 10
        text_y = self.rect.top

        # Draw name
        screen.blit(self.name_surface, (text_x, text_y + 5))

        # Draw score
        screen.blit(self.score_surface, (text_x, text_y + 35))

def create_rounded_avatar(image, radius):
    size = image.get_size()
    circle_surface = pygame.Surface(size, pygame.SRCALPHA)

    pygame.draw.circle(circle_surface, (255, 255, 255, 255), (size[0] // 2, size[1] // 2), radius)

    rounded_image = pygame.Surface(size, pygame.SRCALPHA)
    rounded_image.blit(image, (0, 0))
    rounded_image.blit(circle_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)

    return rounded_image