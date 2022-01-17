from torch.nn import Model
class Model():
    def __init__(self, hidden_size, n_layers):
	self.hidden_size = hidden_size
 	self.n_layers = n_layers
	self.model = Model(self.n_layers, self.hidden_size)
    def fit(self, X, y):
	self.model.fit(X, y)

