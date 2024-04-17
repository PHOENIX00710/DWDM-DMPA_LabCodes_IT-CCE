import math

def entropy(transactions,attribute,val):
    e=0
    total=0
    count_yes=count_no=0
    for value in transactions.values():
        if(value[attribute] == val): 
            if(value['Outcome'] == 'yes'):
                count_yes+=1
            else:
                count_no+=1
            total+=1
    ratio_yes=(count_yes/total) if (count_yes != 0) else 1
    ratio_no=(count_no/total) if (count_no != 0) else 1
    e=-(ratio_yes)*math.log2(ratio_yes)-(ratio_no)*math.log2(ratio_no)
    return e,total
    
def information_gain(transactions,attribute,entropy_total):
    temp=[]
    for value in transactions.values():
        temp.append(value[attribute])
    distinct_values=set(temp)
    ig=entropy_total
    for value in distinct_values:  
        e,total=entropy(transactions,attribute,value)
        ig-=(total/len(transactions))*e
    return round(ig,3)

#Calculate the node to split about
def splitting_node(transactions,columns,entropy_total):
    max_ig=0
    split='Outcome'
    for col in columns:
        if(col == 'Outcome'):
            break
        ig=information_gain(transactions,col,entropy_total)
        if ig>max_ig:
            max_ig=ig
            split=col
    return split

n = int(input('Enter the number of transactions: '))
transactions = {}
columns=['Weather','Temperature','Humidity','Wind','Outcome']
for i in range(0, n):
    temp={}
    for j in columns:
        temp[j]=input(f"Enter {j} value for transaction {i}: ")
    transactions[i]=temp
        
# Calculate overall entropy of the entire datset        
count_yes=count_no=0
for value in transactions.values():
        if(value['Outcome'] == 'yes'): 
            count_yes+=1
        else:
            count_no+=1
ratio_yes=(count_yes/n) if (count_yes != 0) else 1
ratio_no=(count_no/n) if (count_no != 0) else 1
entropy_total=-(ratio_yes)*math.log2(ratio_yes)-(ratio_no)*math.log2(ratio_no)


node=splitting_node(transactions,columns,entropy_total)
temp=[]
for value in transactions.values():
    temp.append(value[node])
distinct_values=set(temp)  
 
for value in distinct_values:
    newTransaction={}
    j=0
    columns_new=columns.copy()
    columns_new.remove(node)
    split_new=''
    for key,transaction in transactions.items():
        # print(f"{key} -> {transaction}")
        if(transaction[node] == value):
            newTransaction[j]=transactions[key]
            split_new=splitting_node(newTransaction,columns_new,entropy(transactions,node,value)[0])
            j+=1
    print(f"We split {value} about {split_new}")

