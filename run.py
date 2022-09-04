import os
import pickle
import neat
import NeatManim

if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config3.txt')

    winner_name = "winner"
 
    NeatManim.visualize_network("winner", config_path = config_path)
    