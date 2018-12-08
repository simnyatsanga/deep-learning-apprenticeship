import numpy as np


# Input vector for the input layer
x = np.array([1.5, 2.0, 3.0])

# weights originating from the first 3-node layer
w1 = np.array([[0.2, 0.2, 0.2], [0.4, 0.4, 0.4], [0.6, 0.6, 0.6]])

# weights originating from the second/hidden 3-node layer
w2 = np.zeros((1,3))
w2[0, :] = np.array([0.5, 0.5, 0.5])

# bias vector originating from the first 3-node layer
b1 = np.array([0.8, 0.8, 0.8])

# bias scalar originating from the second/hidden 3-node layer
b2 = np.array([0.2])


# Sigmoid activation functions
def f(x):
    return 1 / (1 + np.exp(-x))


# This loops for every node in every layer:
# Operation: Does a dot product of the input weights and the input vector from the previous layer
def simple_loop_feed_foward(num_of_layers, x, w_arr, b_arr):
    h_arr = []
    result = {}
    for layer in xrange(num_of_layers - 1): # ignore the first/input layer for the calculation
        if layer == 0: # second/hidden layer
            node_num = 3
            node_input = x
        if layer == 1: # third/output layer
            node_num = 1
            node_input = h_arr
        for node in xrange(node_num):
            sum = w_arr[layer][node].dot(node_input) + b_arr[layer][node] # w*x + b
            if layer == 0:
                h_arr.append(f(sum))
                result["layer_{}".format(layer)] = h_arr
            if layer == 1:
                result["layer_{}".format(layer)] = f(sum)
    return result


# This loops for every layer:
# Operation: Does a matrix dot product of all the weights of all the nodes in that layer
# and the input vector from the previous layer
def matrix_feed_foward(num_of_layers, x, w_arr, b_arr):
    result_dict = {}
    for layer in xrange(num_of_layers - 1):
        if layer == 0:
            node_input = x
        else:
            node_input = res
        matrix_sum = w_arr[layer].dot(node_input) + b_arr[layer]
        res = f(matrix_sum)
        result_dict["layer_{}".format(layer)] = res
    return result_dict



w_arr = [w1, w2]
b_arr = [b1, b2]
print "Using simple loop -> {}".format(simple_loop_feed_foward(3, x, w_arr, b_arr))
print "Using matrix vectorization -> {}".format(matrix_feed_foward(3, x, w_arr, b_arr))
