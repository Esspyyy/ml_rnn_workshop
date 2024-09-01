def sigmoid(x):
    return 1.0 / (1.0 + exp(-x))

def tanh(x):
    return (exp(x) - exp(-x)) / (exp(x) + exp(-x))

def leaky_relu(x):
    return max(0.1 * x, x)

def softmax(x):
    return exp(x) / exp(x).sum()




def function(x):
    return x**2 + 4*x + 4

# Define the gradient of the function
def gradient(x):
    return 2*x + 4

for i in range(iterations):
    x_values.append(x)
    f_values.append(function(x))
    x = x - learning_rate * gradient(x)