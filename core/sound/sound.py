from core import config
from core.sound.soundmanager import SoundManager


class Sound:
    sound_manager = SoundManager()
    @staticmethod
    def load_sound():
        Sound.sound_manager.load_sound(config.CLICK, "assets/sounds/click.wav")
        Sound.sound_manager.load_sound(config.NOT_SELECTED, "assets/sounds/notselected.wav")
        Sound.sound_manager.load_sound(config.MATCHED, "assets/sounds/matched.wav")
        Sound.sound_manager.load_sound(config.WIN, "assets/sounds/win.mp3")
        Sound.sound_manager.load_sound(config.LOSE, "assets/sounds/lose.wav")

    @staticmethod
    def stop_sound():
        Sound.sound_manager.stop_all()