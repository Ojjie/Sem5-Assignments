Data Preprocessing:
	-> The dataset was first analysed to see which columns were numerical and which were categorical, and a check was done to find and return the number of missing values in each column.
	-> Then the default pandas.interpolate() function was used to replace the missing values with those calculated by interpolation.
	-> For the numerical data (like Age,Weight,BP etc) were standardized by subtracting each entry by the mean of the column and divided by the standard deviation of the column (Gaussian Normalization)
	-> The categorical data (like Community,IFA etc.) were rounded to the nearest integer value
	-> An improvement that could be made is to use one hot encoding to represent the categorical data.
	-> The cleaned data was then exported to a new CSV

Descriptions of the code:
	-> df_cleaning: performs the cleaning process as described above
	-> class NN:
		1) __init__:
				* It is the constructor for the NN class.
				* Initializes the epoch, number of neurons in each layer, the learning rate and the beta value, based on the parameters passed.
				* It also initializes the weights and biases of the neural network based on the number of neurons in each layer. The weights are initialized randomly using the Xavier initialization method. The biases are initialized to 0
				* The weights attribute is a list of the weights of each layer of the network. Each layer's weights are represented by a 2D matrix of dimensions Ni X Ni-1 (where i is the current layer)
				* The biases attribute is a list of the biases of each layer of the neural network. Each layer's biases are represented by a 2D matrix of dimensions 1 x Ni (where i is the current layer)
				* The matrices for vdw and vdb (to calculate momentum) are also lists of their values for each layer and are initialized to 0 (having the same dimensions as the respective weights and biases)
		2) sigmoid:
				* implements the sigmoid activation function
		3) relu:
				* implements the relu activation function
		4) tanh:
				* implements the tanh activation function
		5) activate:
				* takes 2 parameters, z and act.
				* act is used to decide what activation function is to be used to calculate the activation values
				* z is an array of the z values
		6) sigmoid_back:
				* calculates the differential of the sigmoid activaion function.
		7) relu_back:
				* calculates the differential of the relu activaion function.
		8) tanh_back:
				* calculates the differential of tanh the activaion function.
		9) activate_back:
				* takes 2 parameters, z and act.
				* act is used to decide which activation function is to be used to calculate the derivative of the activation values
				* z is an array of the z values
		11) cross_entropy_back:
				* calculates the differential of the binary cross entropy function given the y and yhat values.
		12) mse_back:
				* calculates the differential of the mean squared error cost function given the y and yhat values
		13) forward_prop:
				* performs forward propagation given a row of input and stores the yhat values
		14) backward_prop:
				* performs backward propogation
				* it calculates and stores the appropriate derivatives in order to later update the weights and biases
		15) update_weight:
				* calculates momentum which is then used to update the weights and biases based on the derivatives calculated by the bacward_prop function
		16) CM: 
				*calculates the confusion matrix given the y and yhat values and prints the calculated accuracy
		17) fit:
				* runs forward and backward propogation for a given number of epochs on the training set.
				* it also updates the weights as it goes along, thus improving the weights and biases
		18) predict:
				given a set of X values (i.e. the testing set) it calculates and returns a list of the yhat values

Standout feature of our implementation of the design of the neural network:
	-> Xavier initialisation was used to initialize the weights 
	-> Momentum for faster convergence of gradient descent which allows us to have a higher learning rate

Hyperparameters used:
	
	-> Number of hidden layers used (we played around with this, but found just a single  hidden layer to give the best accuracy).
	-> Number of nodes in the hidden layers = 20
	-> learning rate (alpha) = 0.008
	-> beta (for momentum) = 0.9 
	-> number of epochs (iterations) = 3000

Future scope for improvement -

-> Since we had gotten decent accuracy using regular gradient descent, we did not look for implementing an optimizer class, but in the future different
optimizers like(Adam,RMSprop etc), can be used for improving the test accuracy.

-> Another possibility is to add more classes for different 'types' of layers, like 'Dense', 'Sequential' etc. so that a different combination of them can
be used to see how the train-test accuracy changes and also to make it more like a framework like Keras or Pytorch to improve modularity and give more control to the user to visualise the differences.

Detailed steps to run the files:
	-> Folders
		1) Src:
			* data_preprocessing.py - (The python file used to clean the csv file)
			* Assignment3.py (the code for the neural network)
		2) Data: 
			* Has the cleaned dataset - ‘LBW_Dataset_Cleaned.csv’
			* README.txt (you’re reading this now :P)
			* Run data_preprocessing.py to clean the dataset
			*  Include the csv in the ‘data’ folder in the path to the dataframe and 
			* Run the the file called ‘Assignment3.py’ in the src folder using the command - 
				'python3 Assignment3.py'
			* Voila! You have the output metrics like accuracy, precision,recall and F1 score for train and test which is computed using the ‘CM’ function predefined in the template.