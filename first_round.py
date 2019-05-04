import numpy as np

def sig(x):
    a = 1
    b = 2.5
    return np.exp(a*x-b)/(np.exp(a*x-b) +1)
input_cards = np.zeros(52)
print(input_cards)


first_layer = np.zeros(52+0)
second_layer = np.zeros(52)
third_layer= np.zeros(12)
output_layer = np.zeros(4)


layers = []
weights = []
biases = []

input_layers = [52,52,12,4]

for i in range(len(input_layers)):
    layers.append(np.zeros(input_layers[i]))
for i in range(1,len(layers)):
    weights.append(np.random.rand(input_layers[i],input_layers[i-1]))
    biases.append(np.random.rand(input_layers[i]))


for i in range(1,len(layers)):
    layers[i] = sig(np.dot(weights[i-1]/layers[i-1].shape[0],layers[i-1]) + biases[i-1])



for i in layers:
    print("hi")
    print(i)

#first_weights = np.random.rand(first_layer.shape[0],second_layer.shape[0])
#first_bias = np.random.rand(second_layer.shape[0])
#
#second_weights = np.random.rand(second_layer.shape[0],third_layer.shape[0])
#second_bias = np.random.rand(third_layer.shape[0])
#
#third_weights = np.random.rand(third_layer.shape[0],output_layer.shape[0])
#third_bias = np.random.rand(output_layer.shape[0])
#
#second_layer = sig(np.dot(first_weights,first_layer) + first_bias)
#print(second_layer)
