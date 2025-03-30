import os

import pygame


class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.sounds = {}
    def load_sound(self, name, file_path):
        """Tải âm thanh từ file và lưu vào dictionary."""
        sound_path = os.path.abspath(file_path)
        # print(f"Đường dẫn tuyệt đối: {sound_path}")
        if os.path.exists(file_path):
            self.sounds[name] = pygame.mixer.Sound(sound_path)
            print(f"Tìm thấy")
        else:
            print(f"⚠️ Không tìm thấy file âm thanh: {file_path}")

    def stop_all(self):
        """Dừng tất cả âm thanh."""
        pygame.mixer.stop()

    def stop_sound(self, name):
        """Dừng phát âm thanh."""
        if name in self.sounds:
            self.sounds[name].stop()

    def play_sound(self, name, loop=0):
        """Phát âm thanh với số lần lặp (loop=0 là 1 lần, -1 là vô hạn)."""
        if name in self.sounds:
            self.sounds[name].play(loops=loop)
        else:
            print(f"⚠️ Âm thanh '{name}' chưa được load.")

    def set_volume(self, name, volume):
        """Chỉnh âm lượng (0.0 đến 1.0)."""
        if name in self.sounds:
            self.sounds[name].set_volume(volume)