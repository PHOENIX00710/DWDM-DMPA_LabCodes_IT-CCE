#Initial Declaration
transactions = {
    'positive': {'total': 0},
    'negative': {'total': 0},
    'total': 0
}

#mapping of label1 assuming positive responses
positive_no = int(input('Enter the number of positive comments: '))
for i in range(positive_no):
    print("Enter all words for positive comment consideration with spaces separating them")
    columns = input().split(' ')
    print(columns)
    for j in columns:
        if j.lower() not in transactions['positive']:
            transactions['positive'][j.lower()] = 1
            transactions['total']+=1
        else:
            transactions['positive'][j.lower()] += 1
        transactions['positive']['total']+=1
            
#mapping of label1 assuming negative responses            
negative_no = int(input('Enter the number of negative comments: '))
for i in range(negative_no):
    print("Enter all words for negative comment consideration with spaces separating them")
    columns = input().split(' ')
    print(columns)
    for j in columns:
        if j.lower() not in transactions['positive']:
            transactions['total']+=1
        if j.lower() not in transactions['negative']:
            transactions['negative'][j.lower()] = 1
        else:
            transactions['negative'][j.lower()] += 1
        transactions['negative']['total']+=1

print(transactions)

#Take input for attributes to be predicted
wordTest=input("Sentence to classify: ").split(' ')
print(wordTest)
    
#probability of labels
prob_pos=positive_no/(positive_no+negative_no)
prob_neg=1-prob_pos

#probabilty of words of test given label
wordTest_map={}
final_map = {'negative': {}, 'positive': {}}
for i in wordTest:
    word_lower = i.lower()
    wordTest_map[word_lower]=wordTest_map.get(word_lower,0)+1
    final_map['positive'][word_lower] = (transactions['positive'].get(word_lower, 0) + 1) / (transactions['positive']['total'] + transactions['total'])
    final_map['negative'][word_lower] = (transactions['negative'].get(word_lower, 0) + 1) / (transactions['negative']['total'] + transactions['total'])
    
print(prob_pos,prob_neg)
print(final_map, wordTest_map)

for key in wordTest_map.keys():
    prob_pos*=pow(final_map['positive'][key],wordTest_map[key])
    prob_neg*=pow(final_map['negative'][key],wordTest_map[key])
    
print(prob_pos,prob_neg)

if(prob_pos > prob_neg):
    print(f"The sentence is of positive sentiment")
else:
    print(f"The sentence is of negative sentiment")

'''
3
I liked the movie 
Its a good movie Nice story
Heros acting is bad but heroine looks good Overall nice movie

2
Nice songs But sadly boring ending
Sad boring movie
    
overall liked the movie

Test Case 2:-

3(+ve)
Chinese Beijing Chinese
Chinese Chinese Sanghai
Chinese Macao
1(-v2)
Tokoyo Japan Chinese

Test: - Chinese Chinese Chinese Tokoyo Japan (+ve)
    
'''