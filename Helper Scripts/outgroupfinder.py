def fastareader(filename):
    sequences = open(filename,'r')
    lines = sequences.readlines()
    seqDict = {}
    for line in lines:
        if line.startswith(">"):
            header = line[1:].strip()
            seqDict[header] =""
        else:
            seqDict[header] += line.strip()

    return seqDict

filename = 'mafft_aligned.fasta'
seqdict = fastareader(filename)
matrix = {}
length = len(list(seqdict.values())[0])
seqnum = len(list(seqdict.values()))
for header in seqdict.keys():
    sequence = seqdict[header]
    for i in range(length):
        aa = sequence[i]
        if aa not in matrix:
            matrix[aa]= []
            for y in range(length):
                matrix[aa].append(0)
            matrix[aa][i]+=1
        else:
            matrix[aa][i]+=1

for aa in matrix.keys():
    list1 = matrix[aa]
    for i in range(length):
        list1[i]=(list1[i])/seqnum
best = 0
worst = 1
besthit=''
worsthit=''
prob = {}
for header in seqdict.keys():
    sequence = seqdict[header]
    prob[header] = 1
    for i in range(length):
        aa = sequence[i]
        prob[header]= prob[header]*matrix[aa][i]
        
for header in prob.keys():
    if prob[header]>best:
        best = prob[header]
        besthit= header
    elif prob[header]<worst:
        worst = prob[header]
        worsthit= header
list2 = []
for header in prob.keys():
    list2.append(prob[header])
list2 = sorted(list2)
list3 = []
list3.append(list2[-1])
list3.append(list2[-2])
list3.append(list2[-3])
for i in list3:
    for header in prob.keys():
        if prob[header]==i:
            print(header)


print("best hit is: "+besthit)
print ("worst hit is: " + worsthit)
print(worst)
print(best)
