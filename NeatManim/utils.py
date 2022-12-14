
import pickle
import neat
import os

def process_network(winner_name:str, config_path:str) -> None:

    with open(f"winners\winners_list\{winner_name}", "rb") as f:
            genome = pickle.load(f)

    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                            neat.DefaultSpeciesSet, neat.DefaultStagnation,
                            config_path)
    # genome[0] is the index of the genome
    try:
        genome = genome[1]
    except:
        pass
    # the nodes numbers are very big eg 2053 despite being only 40 nodes
    used_nodes = {}
    for i,node in enumerate(genome.nodes.keys()):
        used_nodes[node] = i
 
    network_layers, layers, connections = process_layers(config.genome_config.input_keys, config.genome_config.output_keys, genome.connections.values(), used_nodes)
    #filtering connections
    connections = [(conn.key[0], conn.key[1], conn.weight) for conn in connections if conn.enabled]
    winner = {
        "network_layers": network_layers,
        "layers_index": layers,
        "connections": connections
    }
    return winner

def process_layers(inputs:list, outputs:list, connections:list, used_nodes:hash) -> list:
    '''Return a list with each layer and its corresponding nodes'''
    # inputs from -len to -1
    # outputs from 0 to len(outputs)-1

    # total number of nodes used
    length = len(used_nodes)
    layers = list()

    for i in range(length):
        layers.append(1)

    layer_num = 1

    changes = True
    # processing connections and turn values like 4003 in the corresponding index
    for conn in connections:
        if conn.enabled:
            input, output = conn.key
            if(input >= 0):
                inp_index = used_nodes[input]
            else:
                inp_index = input
            out_index = used_nodes[output]
            conn.key = (inp_index, out_index) 
    
    # defining the nodes layers, this is will always work since 
    # the graph doesn't have any cycles
    while changes:
        changes = False
        for conn in connections:
            if conn.enabled:
                input, output = conn.key
                if input < 0:
                    continue
                if layers[input] >= layers[output]:
                    layers[output] += 1
                    changes = True

    
    num_layers = 1

    # finds the last layer (the output layer)
    for i in range(length):
        num_layers = max(num_layers, layers[i])
    
    # the outputs will always come first in the layers list
    # makes the outputs into the last layer of the network
    for i in range(len(outputs)):
        layers[i] = num_layers 
        
    
    # creates the layers list
    network_layers = list()

    for i in range(num_layers+1):
        network_layers.append([])
    
    for i in range(length):
        network_layers[layers[i]].append(i)

    for input in inputs:
        network_layers[0].append(input)
    
    return network_layers, layers, connections
    

def animate_winners():
    ''' animates the winners int the folder winners/winners_list/...
    whose names are found in the file winners/winners_names.txt'''

    # winners_names:list, config_path:str
    with open('winners/winners_names.txt','r') as f:
        lines = f.readlines()

    winners_names = list()
    for i in lines:
        i = i.replace('\n','')
        winners_names.append(i)

    winners = list()
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, r'winners\config.txt')

    for winner_name in winners_names:
        winner = process_network(winner_name, config_path)
        winners.append(winner)

    return winners
