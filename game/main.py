import traceback
import sys
try:
    from game import Game

    game = Game()
    game.run()

except Exception as e:
    print("Exception occurred:", e)
    traceback.print_exc()
    input("Press Enter to exit...")  # Keeps console open
    sys.exit(1)
