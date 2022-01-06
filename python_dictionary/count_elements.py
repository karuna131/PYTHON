dict =  {
   'Alex': ['subj1', 'subj2', 'subj3'], 
   'David': ['subj1', 'subj2']}
count=0
for i in dict:
    if isinstance(dict[i], list):
        count+=len(dict[i])
print(count)
    
