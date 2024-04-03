# We take input for the transactions
n = int(input('Enter the number of transactions: '))
transactions = {}
columns=['Weather','Temperature','Humidity','Wind','Outcome']
for i in range(0, n):
    temp={}
    for j in columns:
        temp[j]=input(f"Enter {j} value for transaction {i}: ")
    transactions[i]=temp
 
print(transactions)
 
#Take input for attributes to be predicted
print("The values of attriutes for which you have to classify")
test={}
for j in columns:
    if(j == 'Outcome'):
        break
    test[j]=input(f"Enter {j} value: ")
 
# Calculate total probability of yes and No of the outcome
no_of_yes=0
for key,value in transactions.items():
    if(value['Outcome'] == "yes"):
        no_of_yes+=1
no_of_no=n-no_of_yes
prob_yes=no_of_yes/n
prob_no=no_of_no/n
 
print(f"Probability of yes: {prob_yes} Probability of no: {prob_no} for the whole datset")
 
 
# Probability for yes/positive/1
p_final_yes=1
 
for key1,value1 in test.items():
    p_temp=1
    count=0
    for value2 in transactions.values():
        if(value2['Outcome'] == "yes" and value2[f"{key1}"] == value1):
            count+=1
    p_temp=float(count/no_of_yes)
    p_final_yes=float(p_final_yes*p_temp)
 
print(f"Probabilty of yes given the conditions: {p_final_yes}")
 
# Probability for no/negative/0
p_final_no=1
 
for key1,value1 in test.items():
    p_temp=1
    count=0
    for value2 in transactions.values():
        if(value2['Outcome'] == "no" and value2[f"{key1}"] == value1):
            count+=1
    p_temp=float(count/no_of_no)
    p_final_no=float(p_final_no*p_temp)
 
print(f"Probabilty of no given the conditions: {p_final_no}")
 
if(p_final_yes >= p_final_no):
    print("The tuple is classified to have outcome True")
else:
    print("The tuple is classified to have outcome False")
 
 
'''
 
Train Data (13) :
 
Sunny
Hot
High
Weak
no
Sunny
Hot
High
Strong
no
Cloudy
Hot
High
Weak
yes
Rain
Mild
High
Weak
yes
Rain
Cool
Normal
Weak
yes
Rain
Cool
Normal
Strong
no
Cloudy
Cool
Normal
Strong
yes
Sunny
Mild
High
Weak
no
Sunny
Cool
Normal
Weak
yes
Rain
Mild
Normal
Weak
yes
Sunny
Mild
Normal
Strong
yes
Cloudy
Mild
High
Strong
yes
Cloudy
Hot
Normal
Weak
yes
 
I/0: (Manually enter each value for I/O)
 
Rain
Mild
High
Strong
no
 
'''