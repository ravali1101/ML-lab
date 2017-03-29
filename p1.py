dataset = [[1,1,1], [-1,1,-1], [1,-1,-1], [-1,-1,-1]]
weight = [-1,1,1]
def predict(row,weight):
	activation = weight[0]
	for i in range(len(row)-1):
	   activation+= weight[i+1]*row[i]
	   return 1.0 if activation >= 0.0 else 0.0

for row in dataset:
	prediction = predict(row,weight)
	print("expected = %d,predicted = %d"%(row[-1],prediction))
def train_weights(train,I_rate,n_epoch):
	weights = [0.0 for i in range (len(train[0]))]
	for epoch in range(n_epoch):
	    sum_error = 0.0
	    for row in train:
	    	prediction=predict(row,weights)
	    	error=row[-1]-prediction
	    	sum_error+=error**2
	    	weights[0]=weights[0]+I_rate*error
	    	for i in range(len(row)-1):
	    		weights[i+1]=weights[i+1]+I_rate*error*row[i]
	    		print('>epoch=%d,irate=%.3f,error=%.3f'%(epoch,I_rate,sum_error))
	    		return weights
