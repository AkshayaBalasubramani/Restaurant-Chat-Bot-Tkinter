import torch.nn as nn

# # feed forward nn
# #bag of words as input,1 hidden layer pattern number,2 hidden layers and output size as the number of dii classes
# #softmax applied

class NeuralNets(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(NeuralNets, self).__init__()
        self.l1 = nn.Linear(input_size, hidden_size)
        self.l2 = nn.Linear(hidden_size, hidden_size)
        self.l3 = nn.Linear(hidden_size, output_size)
        self.relu=nn.ReLU()  # Adjust input_size to match the output size of the previous layer

    def forward(self, x):
        out = self.l1(x)
        out=self.relu(out)
        out = self.l2(out)
        out=self.relu(out)
        out = self.l3(out)
        return out
