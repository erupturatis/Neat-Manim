import os
import NeatManim


if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, r'exampleWinner\config3.txt')

    winner_name = r"exampleWinner\winner"
 
    NeatManim.animate_winners([f"{winner_name}"], config_path = config_path)
    