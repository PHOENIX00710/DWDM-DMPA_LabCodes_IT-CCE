from collections import OrderedDict

def prune(ck,min_support):
    return {i:ck[i] for i in ck if ck[i] >= min_support}

def join(C1, transactions, k):
    Ck = {}
    items = list(C1.keys())
    len_items = len(items)

    for i in range(len_items):
        for j in range(i + 1, len_items):
            item1, item2 = items[i], items[j]
            if len(item1) == 1 or item1[:-1] == item2[:-1]:
                new_tuple = tuple(sorted(set(item1 + item2)))
                Ck[new_tuple] = 0

    # Calculate the frequency of each itemset in Ck
    for itemset in Ck.keys():
        for transaction in transactions.values():
            if set(itemset).issubset(set(transaction)): 
                Ck[itemset] += 1

    return Ck
            

transactions={}
no_of_transactions=int(input("Enter the number of transactions: "))
for i in range(no_of_transactions):
    element=int(input(f"Value in transaction {i}, -1 to stop: "))
    temp=[]
    while(element != -1):
        temp.append(element)
        element=int(input(f"Value in transaction {i}, -1 to stop: "))
    transactions[i]=temp

print(transactions)

ck={}
for value in transactions.values():
    for i in value:
        curr=(i,)
        if curr not in ck:     #Important
            ck[curr]=1
        else:
            ck[curr]+=1
            
ck=OrderedDict(sorted(ck.items()))
min_support=int(input("Enter the minimum support: "))
ck=prune(ck,min_support)
ck=OrderedDict(sorted(ck.items()))

prevCk={}
k=1
while(ck):
    prevCk=ck
    ck=join(ck,transactions,k)
    ck=prune(ck,min_support)
    k+=1

print("Frequent item set: \n",prevCk)

'''
9
1 
2 
5 
-1
2 
4 
-1
2 
3 
-1
1 
2 
4 
-1
1 
3 
-1
2 
3 
-1
1 
3 
-1
1 
2 
3 
5 
-1
1 
2 
3
-1
2
'''
