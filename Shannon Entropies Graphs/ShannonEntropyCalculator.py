import math
def ShannonEntropyCalculator(frequency):
    '''
    This function is created to calculate sub values of the given 
    frequency which needs to be summed later with other frequencies 
    in order to calculat total Shannon Entropy for a column 
    '''
    logvalue= math.log2(pinum)
    elementofhvalue= pinum*logvalue*-1
    return elementofhvalue
def DomainAvarageCalculator(startresidue, endresidue, listofhvalues):
    '''
    This function is created to calculate the avarage of a given part in a list
    '''
    totalofdomain=0
    for a in range(startresidue, endresidue):
        totalofdomain+=listofhvalues[a]
    avarageofdomain=totalofdomain/(endresidue-startresidue)
    print("H value for the domain between",startresidue,"-",endresidue,"is:",avarageofdomain)
asd=[]
agh=[]
if __name__ == "__main__":      
    fileopener = open("new.fasta",'r')
    headerslist=[] 
    listofseq=[]
    count=0
    listofhvalues=[]
    for b in fileopener:
        b=b.strip()
        if b[0]==">":
            listofseq.append("")
            headerslist.append(b[1:]) #to append headers to list
            count+=1
        else:
            listofseq[count-1]+=b #to append sequences to list
    lengthofseq= len(listofseq[0])
    numberofseq= len(listofseq)
    counter=0
    for eachaa in range(lengthofseq):
        counterdict={}
        for seqs in range(numberofseq):
            sekans= listofseq[seqs]
            aa=sekans[eachaa]
            if aa in counterdict: 
                counterdict[aa]+=1 # if the residue is in the dictionary increments its value
            else:
                counterdict[aa]=1 # if not creates the residue as a key
        total=0
        for numbers in counterdict.values():
            total+=numbers # finds the total numbers of aa in a column
        hvalue=0
        for element in counterdict.keys():   
            pinum=counterdict[element]/total
            if counter==135:
                asd.append(element)
                agh.append(pinum)
            elementofhvalue= ShannonEntropyCalculator(pinum)
            hvalue+=elementofhvalue # to sum sub values that found with ShannonEntropyCalculator function
        counter+=1
        listofhvalues.append(hvalue)
    totalofdomain1=0
    DomainAvarageCalculator(0,22,listofhvalues)
    DomainAvarageCalculator(22,45,listofhvalues)
    DomainAvarageCalculator(45,76,listofhvalues)
    DomainAvarageCalculator(76,95,listofhvalues)
    DomainAvarageCalculator(95,130,listofhvalues)
    DomainAvarageCalculator(130,153,listofhvalues)
    DomainAvarageCalculator(153,191,listofhvalues)
    DomainAvarageCalculator(191,214,listofhvalues)
    DomainAvarageCalculator(214,283,listofhvalues)
    stringtocsv="aa, value, domain"
    for a in range(len(listofhvalues)): # this loop is written to turn foundings of the script to CSV file with respect to topological regions
        if 0<=a<=21:
            stringtocsv=stringtocsv+'\n'+str(a+1)+", "+str(listofhvalues[a])+ ", Topological domain 1"
        elif 22<=a<=44:
            stringtocsv=stringtocsv+'\n'+str(a+1)+", "+str(listofhvalues[a])+ ", Transmembrane 1"
        elif 45<=a<=75:
            stringtocsv=stringtocsv+'\n'+str(a+1)+", "+str(listofhvalues[a])+ ", Topological domain 2"
        elif 76<=a<=94:
            stringtocsv=stringtocsv+'\n'+str(a+1)+", "+str(listofhvalues[a])+ ", Transmembrane 2"
        elif 95<=a<=129:
            stringtocsv=stringtocsv+'\n'+str(a+1)+", "+str(listofhvalues[a])+ ", Topological domain 3"
        elif 130<=a<=152:
            stringtocsv=stringtocsv+'\n'+str(a+1)+", "+str(listofhvalues[a])+", Transmembrane 3"
        elif 153<=a<=190:
            stringtocsv=stringtocsv+'\n'+str(a+1)+", "+str(listofhvalues[a])+ ", Topological domain 4"
        elif 191<=a<=213:
            stringtocsv=stringtocsv+'\n'+str(a+1)+", "+str(listofhvalues[a])+ ", Transmembrane 4"
        elif 214<=a<=283:
            stringtocsv=stringtocsv+'\n'+str(a+1)+", "+str(listofhvalues[a])+ ", Topological domain 5"
    for a in range(len(asd)):
        print(asd[a], agh[a])
    # fo = open("entropyvalues.csv",'w')
    # fo.write(stringtocsv)


