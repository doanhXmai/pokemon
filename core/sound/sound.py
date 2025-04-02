from assets import assets
from core import config, setting
from core.sound.soundmanager import SoundManager
from assets import assets


class Sound:
    sound_manager = SoundManager()
    @staticmethod
    def load_sound():
        Sound.sound_manager.load_sound(config.CLICK, assets.sound_path[config.CLICK])
        Sound.sound_manager.load_sound(config.NOT_SELECTED, assets.sound_path[config.NOT_SELECTED])
        Sound.sound_manager.load_sound(config.MATCHED, assets.sound_path[config.MATCHED])
        Sound.sound_manager.load_sound(config.WIN, assets.sound_path[config.WIN])
        Sound.sound_manager.load_sound(config.LOSE, assets.sound_path[config.LOSE])

    @staticmethod
    def stop_sound():
        Sound.sound_manager.stop_all()
    @staticmethod
    def play_music(name = config.CLICK, loop = 0):
        if setting.TURN_ON_VOLUME:
            Sound.sound_manager.play_sound(name, loop)