import numpy
import random

from config import LEARNING_RATE
from formulas import sig, inv_sig, inv_err

curr_node_id = 0


class Layer:
    def __init__(self, num_nodes, input_vals, layer_num):
        self.num_nodes = num_nodes
        self.input_vals = input_vals
        self.layer_num = layer_num
        self.weight = [[random.random() for col in range(len(input_vals))] for row in range(num_nodes)]
        self.weight_delta = [[0 for col in range(len(input_vals))] for row in range(num_nodes)]
        self.layer_net = [0 for col in range(num_nodes)]
        self.layer_out = [0 for col in range(num_nodes)]
        self.bias = (random.random() * 2) - 1

    def eval(self):
        #  evaluation part
        #  Get input, compute the output of layer nodes.
        for i in range(self.num_nodes):
            x = 0.0
            j = 1
            for j in range(len(self.input_vals)):
                x += self.weight[i][j] * self.layer_out[i]
            self.layer_out[i] = sig(x)

    def backprop(self, other):
        #  use backpropagation method to update weights
        for i in range(self.num_nodes):
            for j in range(len(self.input_vals)):
                #  preform gradient descent using the actual and target outputs
                self.weight_delta[i][j] = self.weight[i][j] - (LEARNING_RATE*inv_err(self.layer_out[i],
                                                                                     self.layer_net[i]))

