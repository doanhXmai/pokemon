from core import config

pokemon_images = [f"assets/images/pieces{i}.png" for i in range(1, 20)]

icon_sound = ["assets/images/volume.png", "assets/images/volume-off.png"]

background = "assets/images/bgk.jpg"

sound_path = {config.CLICK:         f"assets/sounds/{config.CLICK}.wav",
              config.NOT_SELECTED:  f"assets/sounds/{config.NOT_SELECTED}.wav",
              config.MATCHED:       f"assets/sounds/{config.MATCHED}.wav",
              config.WIN:           f"assets/sounds/{config.WIN}.mp3",
              config.LOSE:          f"assets/sounds/{config.LOSE}.wav"}

button_path = {"pause":     "assets/images/pause.png",
               "hint":      "assets/images/hint.png",
               "shuffle":   "assets/images/shuffle.png"}

avatar_path = "assets/images/avt.png"