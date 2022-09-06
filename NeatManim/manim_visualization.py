from manim import *
import utils

class VisualizeNetwork(Scene):

    ''' this class can be used for any network as long as the 
    network layers and the connections are provided by the user'''

    def get_corresponding_anchors(self, circle1:Circle, circle2:Circle):
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

    def construct(self):
        winners = utils.animate_winners()
        winner = winners[0]

        network_layers = winner['network_layers']
        connections = winner["connections"]

       # mapping the neurons to the corresponding layers and index in that layer
        neurons_map = {

        }
        for layer_num,layer in enumerate(network_layers):
            for pos,neuron in enumerate(layer):
                neurons_map[neuron] = [layer_num,pos]

        # drawing the initial network with no connections
        num_layers = len(network_layers)

        # change this based on the number of layers you have
        start_layer_munit =  -2
        end_layer_munit = 2

        # divides the distance into equal steps

        step = (end_layer_munit - start_layer_munit) / num_layers * RIGHT
        neurons_layers = list()

        for layer_num,layer in enumerate(network_layers):
            num_neurons = len(layer)
            # creating the neurons batch for each layer
            neurons = VGroup(*[Circle(color=WHITE).set_stroke(width=1.5) for _ in range(num_neurons)])
            neurons.arrange_in_grid(num_neurons, 1, buff= .7).scale(.07)

            neurons.shift(start_layer_munit * RIGHT)
            neurons.shift(step * layer_num)
            self.add(neurons)
            neurons_layers.append(neurons)

        

        # drawing the connections between neurons

        line_connections = list()
    
        for connection in connections:
            input, output, weight = connection
            print(f"{input} {output} {weight}")
            input_layer, input_pos = neurons_map[input]
            output_layer, output_pos = neurons_map[output]

            circle1 = neurons_layers[input_layer][input_pos]
            circle2 = neurons_layers[output_layer][output_pos]
            opacity = min(abs(weight),1)
            line_color = BLUE if weight > 0 else RED
            start, end = self.get_corresponding_anchors(circle1, circle2)
            line = Line(start, end)
            line.set_opacity(opacity)
            line.set_stroke(line_color,1)
            
            line_connections.append(line)
        
        line_connections = VGroup(*line_connections)
        self.play(AnimationGroup(*[Create(line) for line in line_connections],lag_ratio=.005))  
        self.wait()


