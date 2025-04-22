'''
    LEVEL_OF_SCREEN = 0 menu: start
    LEVEL_OF_SCREEN = 1 menu: select game mode
    LEVEL_OF_SCREEN = 2 mode: solo
    LEVEL_OF_SCREEN = 3 battle bot
    LEVEL_OF_SCREEN = 4 pause
    LEVEL_OF_SCREEN = 5 WIN
    LEVEL_OF_SCREEN = 6 LOSE
    LEVEL_OF_SCREEN = 7 Training
    LEVEL_OF_SCREEN = 8 Game Over
'''
import os.path

LEVEL_OF_SCREEN = 0

'''
    TURN_ON_VOLUME = True bật âm thanh
    TURN_ON_VOLUME = False tắt âm thanh
'''
TURN_ON_VOLUME = True

'''
    TURN_ON_PAUSE = False vẫn chơi được
    TURN_ON_PAUSE = True tạm dừng
'''
TURN_ON_PAUSE = False

'''
    WIN:  True-you win
    LOSE: True-you lose
'''
WIN = False
LOSE = False

'''
    PAUSE: Dừng giảm time
'''
PAUSE = False

FONT_PATH = os.path.join("assets", "fonts", "timesnewroman.ttf")

'''
    DELAY: 3s
'''
DELAY = 100