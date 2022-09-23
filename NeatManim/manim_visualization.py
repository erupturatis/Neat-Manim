from operator import ne
from manim import *
import utils

def get_corresponding_anchors(circle1:Circle, circle2:Circle):
        '''
        return the anchors corresponding to the minimal distance
        between 2 circles
        '''
        anchors_input = circle1.get_anchors()
        distances = np.linalg.norm(anchors_input-circle2.get_center(), axis=1)
        min_index_input = np.argmin(distances)

        anchors_output = circle2.get_anchors()
        distances = np.linalg.norm(anchors_output-circle1.get_center(), axis=1)
        min_index_output = np.argmin(distances)

        return anchors_input[min_index_input],anchors_output[min_index_output]

class VisualizeNetworks(Scene):

    ''' this class can be used for any network as long as the 
    network layers and the connections are provided by the user'''
    def construct(self):
       
        winners = utils.animate_winners()
        winners_inner_neuron_layers = list()
        winners_line_connections = list()
        
        # All the winners should have the same config therefore the same inputs and outputs
      
 
        for winner_index,winner in enumerate(winners):

            network_layers = winner['network_layers']
            # eliminating redundant layers that appear sometimes
            network_layers = [layer for layer in network_layers if len(layer) > 0] 
            connections = winner["connections"]
            print(network_layers)
            # mapping the neurons to the corresponding layers and index in that layer
            neurons_map = {

            }
            for layer_num,layer in enumerate(network_layers):
                for pos,neuron in enumerate(layer):
                    neurons_map[neuron] = [layer_num,pos]

            # drawing the initial network with no connections
            num_layers = len(network_layers)

            # change this based on the number of layers you have
            

            # divides the distance into equal steps
            distance = 1
            step = distance * RIGHT
            
            start_layer_munit =  -step / 2 *(num_layers - 1)
            end_layer_munit = step / 2 *(num_layers - 1)
            neurons_layers = list()
            
            

            for layer_num,layer in enumerate(network_layers):
                num_neurons = len(layer)
                # creating the neurons batch for each layer
                neurons = VGroup(*[Circle(color=WHITE).set_stroke(width=1.5) for _ in range(num_neurons)])
                neurons.arrange_in_grid(num_neurons, 1, buff= .7).scale(.07)

                neurons.shift(start_layer_munit * RIGHT)
                neurons.shift(step * layer_num)

                if winner_index == 0:
                    self.add(neurons)

                neurons_layers.append(neurons)
                
            winners_inner_neuron_layers.append(VGroup(*neurons_layers[:]))

            
            

            # drawing the connections between neurons
            line_connections = list()

            maximal_weight = 0
            for connection in connections:
                input, output, weight = connection
                maximal_weight = max(maximal_weight,abs(weight))

            for connection in connections:
           
                input, output, weight = connection
                input_layer, input_pos = neurons_map[input]
                output_layer, output_pos = neurons_map[output]

                circle1 = neurons_layers[input_layer][input_pos]
                circle2 = neurons_layers[output_layer][output_pos]
                opacity = min(abs(weight) / maximal_weight, 1)
                line_color = BLUE if weight > 0 else RED
                start, end = get_corresponding_anchors(circle1, circle2)
                line = Line(start, end)
                line.set_opacity(opacity)
                line.set_stroke(line_color,1)
                
                line_connections.append(line)
            
            line_connections = VGroup(*line_connections)
            winners_line_connections.append(line_connections)

            
            if winner_index != 0 :
                
                self.play(ReplacementTransform(winners_inner_neuron_layers[winner_index-1],winners_inner_neuron_layers[winner_index]))

            if winner_index != 0 :
                self.play(ReplacementTransform(VGroup(winners_line_connections[winner_index-1],winners_inner_neuron_layers[winner_index-1]),VGroup(winners_line_connections[winner_index],winners_inner_neuron_layers[winner_index])))
            else:
                self.play(AnimationGroup(*[Create(line) for line in line_connections],run_time= 1))  
            self.wait()

class VisualizeNetworksRefactored(Scene):

    def update_line(self,line:Line, neuron1:Circle, neuron2:Circle):
        # sets and updater for connections passed
        def shifter(mob, dt):
            mob.put_start_and_end_on(get_corresponding_anchors(neuron1,neuron2))
        line.add_updater(shifter)

    def construct(self):
        winners = utils.animate_winners()
        winners_inner_neuron_layers = list()
        winners_line_connections = list()
        winners_networks_layers = list()
        neurons_maps = list()
        # All the winners should have the same config therefore the same inputs and outputs
      
 
        for winner_index,winner in enumerate(winners):

            network_layers = winner['network_layers']
            # eliminating redundant layers that appear sometimes
            network_layers = [layer for layer in network_layers if len(layer) > 0] 
            connections = winner["connections"]
            print(network_layers)
            # mapping the neurons to the corresponding layers and index in that layer
            neurons_map = {

            }
            for layer_num,layer in enumerate(network_layers):
                for pos,neuron in enumerate(layer):
                    neurons_map[neuron] = [layer_num,pos]

            neurons_maps.append(neurons_map)
            # drawing the initial network with no connections
            num_layers = len(network_layers)

            # change this based on the number of layers you have
            

            # divides the distance into equal steps
            distance = 1
            step = distance * RIGHT
            
            start_layer_munit =  -step / 2 *(num_layers - 1)
            end_layer_munit = step / 2 *(num_layers - 1)
            neurons_layers = list()
            
            
   
            for layer_num,layer in enumerate(network_layers):
                num_neurons = len(layer)
                # creating the neurons batch for each layer
                neurons = VGroup(*[Circle(color=WHITE).set_stroke(width=1.5) for _ in range(num_neurons)])
                neurons.arrange_in_grid(num_neurons, 1, buff= .7).scale(.07)

                neurons.shift(start_layer_munit * RIGHT)
                neurons.shift(step * layer_num)

                if winner_index == 0:
              
                    self.add(neurons)

                neurons_layers.append(neurons)
                
            winners_inner_neuron_layers.append(VGroup(*neurons_layers))
            winners_networks_layers.append(network_layers)

            new_layers = winners_networks_layers[winner_index]
            old_layers = winners_networks_layers[winner_index-1]

            new_linear = list()
            for layer in new_layers:
                for neuron in layer:
                    new_linear.append(neuron)

            old_linear = list()
            for layer in old_layers:
                for neuron in layer:
                    old_linear.append(neuron)
            
            common = list()
            uncommon = list()

            for neuron in new_linear:
                if neuron in old_linear:
                    common.append(neuron)
                else:
                    uncommon.append(neuron)

            anims = list()
            print(winners_inner_neuron_layers)
            if winner_index != 0:
                for layer in network_layers:
                    for neuron in layer:
                        if neuron in common:
                            # makes animations for all common neurons
                            layer_old, pos_old = neurons_maps[winner_index-1][neuron]
                            layer_new, pos_new = neurons_maps[winner_index][neuron]
                           

                            circle = winners_inner_neuron_layers[winner_index-1][layer_old][pos_old]
                            target = winners_inner_neuron_layers[winner_index][layer_new][pos_new]

                            circle.generate_target()
                            circle.target = target
                            anims.append(MoveToTarget(circle))
            
                self.play(AnimationGroup(*anims))
            

        
class Test(Scene):

    def update_line(self,line:Line, neuron1:Circle, neuron2:Circle):
        def shifter(mob, dt):
            mob.put_start_and_end_on(get_corresponding_anchors(neuron1,neuron2))
        line.add_updater(shifter)

    def construct(self):
        circle1 = Circle(radius=.2)
        pass
    
# the format of the old layer (layernum and pos for each neuron)
# the format of the new layer (layernum and pos for each neuron)
# list on neurons for first network
# list of neurons for second network
# common and uncommon neurons
# the common neurons are moved to the new ones with target
# the uncommon neuron are destroyed and the missing ones are created


            


