from core import config, setting
from core.sound.soundmanager import SoundManager


class Sound:
    sound_manager = SoundManager()
    @staticmethod
    def load_sound():
        Sound.sound_manager.load_sound(config.CLICK, f"assets/sounds/{config.CLICK}.wav")
        Sound.sound_manager.load_sound(config.NOT_SELECTED, f"assets/sounds/{config.NOT_SELECTED}.wav")
        Sound.sound_manager.load_sound(config.MATCHED, f"assets/sounds/{config.MATCHED}.wav")
        Sound.sound_manager.load_sound(config.WIN, f"assets/sounds/{config.WIN}.mp3")
        Sound.sound_manager.load_sound(config.LOSE, f"assets/sounds/{config.LOSE}.wav")

    @staticmethod
    def stop_sound():
        Sound.sound_manager.stop_all()
    @staticmethod
    def play_music(name = config.CLICK, loop = 0):
        if setting.TURN_ON_VOLUME:
            Sound.sound_manager.play_sound(name, loop)