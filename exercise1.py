import matplotlib
matplotlib.use('Agg') # Use a non-interactive backend
import matplotlib.pyplot as plt
import numpy as np
import neurolab as nl

# >>>>>> EXERCISE 1 >>>>>>>>>>>>
# set seed=1
np.random.seed = 1

# generate 2 sets of numbers
set1 = np.random.uniform(-0.6, 0.6, 10)
set2 = np.random.uniform(-0.6, 0.6, 10)

# combine two sets in input_norman
input_norman = np.column_stack((set1, set2))

# create target data : sum of set1, set2
output_norman = np.sum(input_norman, axis=1).reshape(10, 1)

# print("input array: \n", input_norman)
# print("output array: \n", output_norman)
# print("shapes : input ", input_norman.shape, "\noutput : shape ", output_norman.shape)

num_output = output_norman.shape[1]
# create a neural network with two inputs, 6 neurons in one layer with one output neuron: single layer neuron network
net1 = nl.net.newff([[-0.6, 0.6], [-0.6, 0.6]], [6, num_output])

error1 = net1.train(input_norman, output_norman, show=15, goal=0.00001)
output = net1.sim(input_norman)

# print("Input Data (input_norman):")
# print(input_norman)
# print("\nTarget Data (output_norman):")
# print(output_norman)
# print("\nOutput Data :")
# print(output)

# test data
# result #1
test_input = np.array([[0.1, 0.2]])
test_1 = net1.sim(test_input)
print("input test data:", test_input)
print("Output Test1 Data :", test_1)

# >>>>>> EXERCISE 2 >>>>>>>>>>>>

# create a feet-forward network with 5 neurons, 3 neurons in each layer, 1 output neuron
net2 = nl.net.newff([[-0.6, 0.6], [-0.6, 0.6]], [5, 3, 1])

# training algorithm set to gradient descent back propagation
net2.trainf = nl.train.train_gd

error2 = net2.train(input_norman, output_norman, epochs=1000, show=100, goal=0.00001)

test_2 = net2.sim(test_input)
print("input test data:", test_input)
print("Output of Test2 Data :", test_2)

# >>>>>> EXERCISE 3 >>>>>>>>>>>>

# generate 2 sets of numbers : 100 samples
set100 = np.random.uniform(-0.6, 0.6, 100)
set200 = np.random.uniform(-0.6, 0.6, 100)

# combine two sets in input_norman
input_norman = np.column_stack((set100, set200))

# create target data : sum of set100, set200
output_norman = np.sum(input_norman, axis=1).reshape(100, 1)

num_output = output_norman.shape[1]
# create a neural network with two inputs, 6 neurons in one layer with one output neuron: single layer neuron network
net3 = nl.net.newff([[-0.6, 0.6], [-0.6, 0.6]], [6, num_output])

error3 = net3.train(input_norman, output_norman, show=15, goal=0.00001)

# test data with net3
test_3 = net3.sim(test_input)
print("input test data:", test_input)
print("Output of Test3 Data :", test_3)

# >>>>>> EXERCISE 4 >>>>>>>>>>>>

# generate 2 sets of numbers : 100 samples
set100 = np.random.uniform(-0.6, 0.6, 100)
set200 = np.random.uniform(-0.6, 0.6, 100)

# combine two sets in input_norman
input_norman = np.column_stack((set100, set200))

# create target data : sum of set100, set200
output_norman = np.sum(input_norman, axis=1).reshape(100, 1)

# create a neural network , two layers ; 5 neurons in first layer, second with 3 neurons
net4 = nl.net.newff([[-0.6, 0.6], [-0.6, 0.6]], [5, 3, 1])
# set training algorithm to Gradient descent back-propagation
net4.trainf = nl.train.train_gd

error4 = net4.train(input_norman, output_norman, epochs=1000, show=100, goal=0.00001)

# test data with net4
test_4 = net4.sim(test_input)
print("input test data:", test_input)
print("Output of Test4 Data :", test_4)

# Plot the error training size graph
plt.plot(error4)
plt.xlabel('Epoch number')
plt.ylabel('Training error')
plt.title('Training error progress')
plt.savefig('training_error4.png')

# >>>>>> EXERCISE 5 >>>>>>>>>>>>
# repeat exercise 1 with 3 inputs >>>>>>>>>>>>
np.random.seed = 1
input_data = np.random.uniform(-0.6, 0.6, size=(10, 3))
output_data = np.sum(input_data, axis=1).reshape(10, 1)

num_output = output_data.shape[1]

# neural net with 3 inputs, two hidden layers (5 neurons and 3 neurons), and 1 output
net5 = nl.net.newff([[-0.6, 0.6], [-0.6, 0.6], [-0.6, 0.6]], [6, num_output])

error5 = net5.train(input_data, output_data, show=15, goal=0.00001)

# Test the network with the input values [0.2, 0.1, 0.2]
test_3_inputs = np.array([[0.2, 0.1, 0.2]])
test_5 = net5.sim(test_3_inputs)
print("input test data:", test_3_inputs)
print("Output of Test5 Data :", test_5)

# repeat exercise 4 with three inputs >>>>>>>>>>>>

input_data_100 = np.random.uniform(-0.6, 0.6, size=(100, 3))
output_data_100 = np.sum(input_data_100, axis=1).reshape(100, 1)

# create a neural network , two layers ; 5 neurons in first layer, second with 3 neurons
net6 = nl.net.newff([[-0.6, 0.6], [-0.6, 0.6], [-0.6, 0.6]], [5, 3, 1])
# set training algorithm to Gradient descent back-propagation
net6.trainf = nl.train.train_gd

error4 = net6.train(input_data_100, output_data_100, epochs=1000, show=100, goal=0.00001)

# test data with net6
test_6 = net6.sim(test_3_inputs)
print("input test data:", test_3_inputs)
print("Output of Test4 Data :", test_6)





