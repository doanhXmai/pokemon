from core import config

pokemon_images = [f"assets/images/pieces{i}.png" for i in range(1, 20)]

icon_sound = ["assets/images/volume.png", "assets/images/volume-off.png"]

background = [f"assets/images/background{i}.jpg" for i in range(1, 5)]

sound_path = {config.CLICK:         f"assets/sounds/{config.CLICK}.wav",
              config.NOT_SELECTED:  f"assets/sounds/{config.NOT_SELECTED}.wav",
              config.MATCHED:       f"assets/sounds/{config.MATCHED}.wav",
              config.WIN:           f"assets/sounds/{config.WIN}.mp3",
              config.LOSE:          f"assets/sounds/{config.LOSE}.wav"}

button_path = {"pause":             "assets/images/pause.png",
               "hint":              "assets/images/hint.png",
               "shuffle":           "assets/images/shuffle.png",
               "button_play":       "assets/images/button_play.png",
               "button_exit":       "assets/images/button_exit.png",
               "btn_training":      "assets/images/btn_training.png",
               "btn_playervsbot":   "assets/images/btn_playervsbot.png",
               "btn_multiplayer":   "assets/images/btn_multiplayer.png",
               "btn_back1":         "assets/images/btn_back1.png",
               "btn_back2":         "assets/images/btn_back2.png",
               "btn_replay":        "assets/images/btn_replay.png",
               "btn_tryagain":      "assets/images/btn_tryagain.png"}

avatar_path = "assets/images/avt.png"