import pygame


class btnTXT:
    def __init__(self, btn_name, font, color, text_color, rect):
        self.btn_name = btn_name
        self.font = font
        self.btn = {"text": btn_name, "color": color, "text_color": text_color, "rect": rect}
    def draw(self, screen):
        pygame.draw.rect(screen, self.btn["color"], self.btn["rect"], border_radius=10)
        text_surface = self.font.render(self.btn["text"], True, self.btn["text_color"])
        text_rect = text_surface.get_rect(center=self.btn["rect"].center)
        screen.blit(text_surface, text_rect)