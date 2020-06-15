import numpy as np
from bmtk.builder import NetworkBuilder
import pandas as pd

df = pd.read_csv("./some_neurons.csv")

net = NetworkBuilder("my_network")

for i in range(len(df)):
	net.add_nodes(N=1, pop_name = df['bodyId'][i])

net.build()
net.save_nodes(output_dir='network')

############################
#import numpy as np
#from bmtk.builder import NetworkBuilder

#neuron_list = [["123"], ["111"], ["211"]]

#net = NetworkBuilder("my_network")

#for i in range(len(neuron_list)):
#	name = neuron_list[i][0]
#	net.add_nodes(N=1, pop_name=name)

#net.build()
#net.save_nodes(output_dir='network')

# Create connections between pyr --> izh cells

for i in range(10):
	for j in range(i,10):
		net.add_edges(source={'pop_name': df['bodyId'][i]}, target={'pop_name': df['bodyId'][j]})

# Build and save our network
net.build()
net.save_edges(output_dir='network')
