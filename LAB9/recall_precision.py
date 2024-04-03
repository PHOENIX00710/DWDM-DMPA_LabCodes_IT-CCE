predicted=[]
actual=[]

#Input predicted and actual values to compare
predicted=list(input('Enter the list of predicted values seperated by a space: ').split(' '))
actual=list(input('Enter the list of actual values seperated by a space: ').split(' '))

if(len(predicted)!=len(actual)):
    print("The number of predicted and actual values are not equal")
    exit(0)


#Calculate true negative/positive and false negative/positive
TP=0 
FP=0
TN=0
FN=0

for i in range(0,len(predicted)):
    if(predicted[i] == '1' and actual[i] == '1'):
        TP+=1
    elif(predicted[i] == '1' and actual[i] == '0'):
        FP+=1
    elif(predicted[i] == '0' and actual[i] == '1'):
        FN+=1
    elif(predicted[i] == '0' and actual[i] == '0'):
        TN+=1

print(f"\n\nTrue Positives:{TP}\nFalse Positives:{FP}\nFalse Negatives: {FN}\nTrue Negatives: {TN}")

#Calculate the desired values
Accuracy=(TP+TN)/(TP+TN+FP+FN)
Error_rate= (FP+FN)/(TP+TN+FP+FN) 
Precision=TP/(TP+FP)
Recall=TP/(TP+FN)

print(f"\n\nAccuracy: {Accuracy} \nPrecision: {Precision} \nRecall: {Recall}")


''' 
Predicted: 1 1 0 0 1 1 0 0 1 1 1 1 0 1
Actual: 1 1 0 1 0 1 0 0 0 1 1 1 0 0 
'''