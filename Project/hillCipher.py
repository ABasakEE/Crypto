import numpy as np
import math

def breakIntoN(string,n)->list:
    count=n
    word=""
    words=list()
    for i in range(len(string)):
        ch=string[i]
        if (count==0):
            words.append(word)
            word=""
            count=n
        word=word+ch
        count-=1
    words.append(word)
    return words

def getCofactor(matrix):
    sign=1
    n=len(matrix)
    cofactor=[]
    for i in range(n):
        row=list()
        for j in range(n):
            if (i+j)%2==0:
                sign=1
            else:
                sign=-1     
            cof=sign*findDet(findMinor(matrix,i,j))
            row.append(cof)
        cofactor.append(row)
    return cofactor     

def findMinor(matrix,row,col):
    minor=list()
    n=len(matrix)
    for i in range(n):
        r=list()
        for j in range(n):
            if i!=row and j!=col:
                r.append(matrix[i][j])
        if len(r)!=0:
            minor.append(r) 
    return minor

def findDet(matrix)->int: #must be a 2D square list
    n=len(matrix)
    if n==2:#base case
        a1=matrix[0][0]
        a2=matrix[0][1]
        b1=matrix[1][0]
        b2=matrix[1][1]
        return (a1*b2-a2*b1) 
    
    det=0
    sign=1
    for i in range(n): #recurse over the first row
        m=findMinor(matrix,0,i)
        det+=matrix[0][i]*sign*findDet(m)
        sign*=-1
    return det

def encrypt(plain,key)->str:
    if (len(plain)==0):
        return ""
    
    n=3 #key size fixed as 3x3 here
    extra=len(plain)%n
    if (extra!=0):
        for i in range(n-extra):
            plain=plain+'X' #padding plain text
    
    #breaking into groups of n(=3) here
    words=breakIntoN(plain,n)
    
    #broken words into nx1 vectors
    
    #create the key matrix
    keyMatrix=[[0]*n for i in range(n)]
    
    keys=breakIntoN(key,n)
    
    for i in range(n):
        for j in range(n):
            ch=keys[i][j]
            num=ord(ch)-ord('A') #convert to a number
            keyMatrix[i][j]=num
    
    #converting to a numpy array
    keyVec=np.array(keyMatrix,dtype=int)
    det=round(np.linalg.det(keyVec))
    if (det==0 or det%2==0 or det%13==0): #no modular inverse exists if not coprime
        print("Non invertible key")
        return "" 
      
    sentence=""
    
    for word in words:
        numWord=list()
        for i in range(n): #convert each word into a vector of numbers 
           num=ord(word[i])-ord('A') #convert to a number based on the alphabet
           numWord.append(num)
        #perform matrix multiplication
        ans=np.dot(keyVec,numWord)%26 #final array
        for num in ans:
            ch=chr(num+ord('A'))
            sentence=sentence+ch
        
    return sentence    
            
        
def getKey(plain,cipher)->str:
    #assuming we get valid cipher text and their corresponding plain text
    n=3 #set key size as 3 here
    #note that we must need at least a nxn long cipher text and plain text 
    #in order to unqiuely determine the key
    
    if (len(plain)<n*n):
        print("Key cannot be uniquely determined")
        return None
    
    #pad the plain text if needed
    extra=len(plain)%n
    if (extra!=0):
        for i in range(n-extra):
            plain=plain+'X' #padding plain text
    
    #split the cipher and the key text into groups of nx1 vectors and choose only those first n vectors which give a determinable solution
    #so we must first find if the determinant of plainText matrix is invertible modulo 26
    start=0
    end=n
    determinant=0
    plainBreak=breakIntoN(plain,n)
    tot=len(plainBreak)
    #print(plainBreak,tot)
    plainList=list()
    plainMat=list()
    
    #get three 3x1 vectors such that they form an invertible 3x3 matrix modulo 26
    i1=0
    i2=0
    i3=0
    
    flagA=False
    flagB=False
    
    for a in range(tot-2):
        for b in range(a+1, tot-1):
            for c in range(b+1,tot):
                #print("A",a,"B",b,"C",c)
                rowA=plainBreak[a]
                rowB=plainBreak[b]
                rowC=plainBreak[c]
                plainMat.clear()
                
                numA=list()
                numB=list()
                numC=list()
                
                #convert them into numbers
                for i in range(len(rowA)):
                    numA.append(ord(rowA[i])-ord('A'))
                    numB.append(ord(rowB[i])-ord('A'))
                    numC.append(ord(rowC[i])-ord('A'))
                    #all rows are of same length
                    
                plainMat.append(numA)
                plainMat.append(numB)
                plainMat.append(numC)
                
                det=findDet(plainMat)
                if det!=0 and math.gcd(det,26)==1:
                    i1,i2,i3=a,b,c
                    determinant=det
                    flagA=True
                    flagB=True
                    break
            if flagB:
                break
        if flagA:
            break
    
    if determinant==0: #still didn't get a solvable matrix
        print("Key cannot be determined, too few unique equations")
        return ""
    
    #print("indices",i1,i2,i3)
        
    #get the cipher text vectors
    cipherBreak=breakIntoN(cipher,n)
    cipherList=list()
    cipherList.append(cipherBreak[i1])
    cipherList.append(cipherBreak[i2])
    cipherList.append(cipherBreak[i3])    
    
    #converting them into a nxn matrix
    cipherMat=list()
    
    for entry in cipherList:
        row=list()
        for ch in entry:
            num=ord(ch)-ord('A')
            row.append(num)
        cipherMat.append(row)
        
    #due to the nature of the cipher multiplication and how we formed the rows
    #we need to take the transpose of the cipher and plain text matrices
    
    plainMat=np.array(plainMat).T
    cipherMat=np.array(cipherMat).T
    
    #find modular inverse of the determinant of the plain text
    detPlain=pow(determinant,-1,26)
    
    
    #get the cofactor matrix and convert into numpy array
    cofactorPlain=np.array(getCofactor(plainMat))%26
    
    #take transpose to get the adjoint matrix
    adjointPlain=cofactorPlain.T
    
    #get the modular inverse of matrix
    inversePlain=(detPlain*adjointPlain)%26
    
    #get the key matrix
    #C=KP , so K= CP^(-1) [C=cipher, P=plain, K=key matrix] (all modulo 26)
    key=np.dot(cipherMat,inversePlain)%26
    
    #convert it back into a string
    keyString=""
    for row in key:
        for elem in row:
            keyString=keyString+chr(elem+ord('A'))
            
    return keyString  
 
plain="HILLCIPHERISFUN"
key="CIPHERING"
cipher=encrypt(plain=plain,key=key)
if len(cipher)==0:
    print("Encryption not possible")
else:
    print("Plain text:",plain,"\nKey:",key,"\nEncrypted text:",cipher)


plain="ANTCATDOG"
cipher="TIMFINWLY"

keyString=getKey(plain=plain,cipher=cipher)
print("Plain:",plain,"\nCipher:",cipher,"\nObtained key string:",keyString)
            
            
        
    
        
