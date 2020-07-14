import string
counts = dict()
file = input("Enter file name")
if len(file) < 1: file = 'clown.txt'
fh = open(file)
for line in fh:
    wrds = line.rstrip().translate(line.maketrans('','',string.punctuation)).lower().split()
    for word in wrds:
        #print(word)
        #if key is not there, the count is 0
        counts[word] = counts.get(word,0) + 1
#print(counts) 

#now find most common word
largest = -1
theword = None
for k,v in counts.items():
    if counts[k] > 50:
        print(k,v)
    if v > largest:
        largest = v
        theword = k
print(f'The most common word is {theword} and it appears {largest} times.')

# find 10 most common word
newlst = []

for k,v in counts.items():
    newtup = (v,k)
    newlst.append(newtup)
#print(newlst)
newlst= sorted(newlst,reverse=True)
print(newlst)
print(len(newlst))
print("Top 10 most common words:\n")
for v,k in newlst[:10]: 
    print(f'{k.upper()} appears {v} times!')
print("\nTop 10 least common words:\n")
for v,k in newlst[4272:]: 
    print(f'{k.upper()} appears {v} time!')
    
