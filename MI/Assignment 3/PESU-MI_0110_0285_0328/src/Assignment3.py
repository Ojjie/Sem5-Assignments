import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

class NN:

	def __init__(self, inp, n1, out, epoch, lr, beta):
		self.epoch = epoch
		self.weights = []
		self.biases = []
		self.output = []
		self.vdw = []
		self.vdb = []
		self.l0 = inp
		self.l1 = n1
		self.l2 = out
		self.lr = lr
		self.beta = beta
		self.weights.append(np.random.randn(inp, n1)*np.sqrt(1/n1))
		#self.weights.append(np.zeros((inp, n1)))
		self.vdw.append(np.zeros((inp,n1)))
		self.biases.append(np.zeros((1,n1)))
		self.vdb.append(np.zeros((1,n1)))
		self.weights.append(np.random.randn(n1, out)*np.sqrt(1/out))
		#self.weights.append(np.zeros((n1, out)))
		self.vdw.append(np.zeros((n1,out)))
		self.biases.append(np.zeros((1, out)))
		self.vdb.append(np.zeros((1,out)))

	def sigmoid(self, z):
		z = 1/(1+np.exp(-z))
		return z

	def relu(self, z):
		z = np.maximum(0,z)
		return z

	def tanh(self, z):
		z = np.tanh(z)
		return z

	def activate(self, act, z):
		if(act == 0):
			z = self.sigmoid(z)
		elif(act == 1):
			z = self.relu(z)
		else:
			z = self.tanh(z)
		return z

	def sigmoid_back(self, z):
		s = 1/(1+np.exp(-z))
		return s*(1-s)

	def relu_back(self, z):
		#print(z.shape)
		s = np.empty(z.shape)
		for i in range(len(z[0])):
			if(z[0][i] > 0):
				s[0][i] = 1
			else:
				s[0][i] = 0
		return s

	def tanh_back(self, z):
		return 1-(np.tanh(z)**2)

	def activate_back(self, act, z):
		if(act == 0):
			z = self.sigmoid_back(z)
		elif(act == 1):
			z = self.relu_back(z)
		else:
			z = self.tanh_back(z)
		return z

	def cross_entropy(yhat, y):
		if y==1:
			return -np.log2(yhat)
		else:
			return -np.log2(1-yhat)

	def cross_entropy_back(self, yhat,y):
		epsilon = 10**(-7)
		return ((-y/(np.log(yhat+epsilon)) + (1-y)/(-np.log(1-yhat+epsilon))))

	def mse_back(self, yhat, y):
		return ((y-yhat))

	def forward_prop(self):
		self.layer = self.activate(1, np.dot(self.inp, self.weights[0]) + self.biases[0])
		self.activs.append(self.layer)		#self.layers
		self.layer = self.activate(0, np.dot(self.layer, self.weights[1]) + self.biases[1])
		self.activs.append(self.layer)
		self.act = self.layer

	def backward_prop(self):
		d = []		#differentials
		de_dy = self.activate_back(0, self.act) * self.cross_entropy_back(self.act, self.y)
		d.append(de_dy)
		de_dhi = np.dot(d[-1], self.weights[1].T) * self.activate_back(1, self.activs[1])
		d.append(de_dhi)
		return d

	def update_weight(self, d, lr):
		self.vdw[0] = (self.beta * self.vdw[0]) + ((1 - self.beta) * np.dot(self.activs[0].T, d[1]))
		self.weights[0] = self.weights[0] - lr * self.vdw[0]
		self.vdb[0] = (self.beta * self.vdb[0]) + ((1 - self.beta) * d[1])
		self.biases[0] = self.biases[0] - lr * self.vdb[0]
		self.vdw[1] = (self.beta * self.vdw[1]) + ((1 - self.beta) * np.dot(self.activs[1].T, d[0]))
		self.weights[1] = self.weights[1] - lr * self.vdw[1]
		self.vdb[1] = (self.beta * self.vdb[1]) + ((1 - self.beta) * d[0])
		self.biases[1] = self.biases[1] - lr * self.vdb[1]

	def CM(self, y_test, y_test_obs):
		for i in range(len(y_test_obs)):
			if(y_test_obs[i][0]>0.6):
				y_test_obs[i][0]=1
			else:
				y_test_obs[i][0]=0
		fp=0
		fn=0
		tp=0
		tn=0
		for i in range(len(y_test)):
			if(y_test[i]==1 and y_test_obs[i][0]==1):
				tp=tp+1
			if(y_test[i]==0 and y_test_obs[i][0]==0):
				tn=tn+1
			if(y_test[i]==1 and y_test_obs[i][0]==0):
				fp=fp+1
			if(y_test[i]==0 and y_test_obs[i][0]==1):
				fn=fn+1
		
		#Added part- finding accuracy by taking all correct predictions upon all predictions
		accuracy=(tn+tp)/(tn+tp+fn+fp)*100
		# print("false +ve:",fp,"false -ve:",fn,"true +ve", tp,"true -ve",tn)
		p = tp/(tp+fp)
		r=tp/(tp+fn)
		f1=(2*p*r)/(p+r)
		print("precision:", p)
		print("recall:", r)
		print("f1 score:",f1)
		print("Accuracy: ", accuracy)
		return accuracy

	def fit(self, X, Y):
		for z in range(self.epoch):
			self.yhats = []
			for row in range(X.shape[0]):
				self.inp = X[row][:].reshape((1, self.l0))
				self.y = Y[row]		#self.op
				self.activs = [self.inp] #self.layers
				self.forward_prop()
				self.yhats.append(self.act[:])
			d = self.backward_prop()
			self.update_weight(d, self.lr)
		print("_____________________________")
		print("Train accuracy: ")
		self.accuracy = self.CM(Y, self.yhats)
		print("_____________________________")
		#print("Train Accuracy: ", accuracy, "using tanh, sigmoid")
	def predict(self, X):
		yhat = []
		for z in range(X.shape[0]):
			input_ = X[z][:].reshape((1,X.shape[1]))
			layer = self.activate(1,np.dot(input_, self.weights[0]) + self.biases[0])
			out = self.activate(0,np.dot(layer, self.weights[1]) + self.biases[1])
			yhat.append(out)
		return yhat

fname = r"LBW_Dataset_Cleaned.csv"
df = pd.read_csv(fname)
df = df.drop(columns=['Unnamed: 0'])
df = df.values

np.random.seed(7)
X_train, X_test, Y_train, Y_test = train_test_split(df[:,0:8], df[:,8], test_size = 0.1, stratify = df[:,8], random_state = 42)
n = NN(X_train.shape[1],20,1,3000,0.008, 0.9)
n.fit(X_train,Y_train)
yhat = n.predict(X_test)
print("_____________________________")
print("Test accuracy: ")
n.CM(Y_test, yhat)
print("_____________________________")