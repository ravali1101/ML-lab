
def activation_function(yin):
	if yin <= 0:
		return 0
	elif yin < 0:
		return -1
	else:
		return 1

def train_model(learn_rate,data):
	weights = []
	bias = 0
	weight1 = 0
	weight2 = 0
	learn_rate = 1
	#print(len(data))
	for i in range(len(data)):
		x1 = data[i][0]
		print(x1)
		x2 = data[i][1]
		print(x2)
		y_actual = data[i][2]
		print(y_actual)
		yin = bias + x1 * weight1 + x2 * weight2
		print(yin)
		y_predicted = activation_function(yin)
		print(y_predicted)
		error = y_actual - y_predicted
		weight1 = weight1 + x1*learn_rate*error
		weight2 = weight2 + x2*learn_rate*error
		bias = bias + learn_rate* error 
		print(weight1,weight2,bias)	
	weights.append(bias)
	weights.append(weight1)
	weights.append(weight2)
	return(weights)


def predict_and(learn_rate,data,x1,x2):
	weights = train_model(learn_rate,data)
	bias = weights[0]
	w1 = weights[1]
	w2 = weights[2]
	yin = bias + x1 * w1 + x2 * w2
	target = activation_function(yin)
	if target >0:
		y_predicted = 1
	else:
		y_predicted = 0
	print(y_predicted)



def main():
	dataset = [[1,1,0],
			  [1,-1,1],
			  [-1,1,1],
			  [-1,-1,0]]
	l_rate = 1
	predict_and(l_rate,dataset,1,1)

main()