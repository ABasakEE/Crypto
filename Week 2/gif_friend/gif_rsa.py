import binascii
import base64
import math

def primeFactors(n): #helper function to get the prime factors
    primes=[]
     
    while n % 2 == 0:
        #print(2)
        primes.append(2)
        n = n // 2
         
    #skip by 2 and check if prime
    for i in range(3,int(math.sqrt(n))+1,2):
         
        while n % i== 0:
            #print(i)
            primes.append(i)
            n = n // i
             
    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        #print(n)
        primes.append(n)

    return primes

def shiftCaesar(cipher,key):
    s=""
    for i in range(len(cipher)):
        ch=ord(cipher[i])-ord('a') #convert to number
        newCh=(ch+key)%26+ord('a')
        newCh=chr(newCh)
        s+=newCh     
    return s

def rot(cipher,ind):
    s=""
    for ch in cipher:
        char=(ord(ch)+ind)%127
        s=s+chr(char)
    return s

#check the above function

s1a='?`labaf_haf'
s1b='?al``hfd_c_b'
s2a='6`leddbf'
s2b='6aladf'
s3a='4`lbgfaegf'
s3b='4aldgd`hhce'
strings=[s1a,s2a,s3a,s1b,s2b,s3b]
st=''
for s in strings:
    st=st+s
for string in strings:
    print("Shift=",-47,"OP=",rot(string,-47))

#used trial and error to get the shift of 47
#can now use RSA decryption on it
nums=[]
for s in strings:
    shift=rot(s,-47)
    nums.append(int(shift[shift.find('=')+1:]))
p1=nums[0]
p2=nums[3]
f1=primeFactors(p1)
f2=primeFactors(p2)
print(f1,f2)
phi1=(f1[0]-1)*(f1[1]-1)
phi2=(f2[0]-1)*(f2[1]-1)

e1=nums[1]
e2=nums[4]
d1=pow(e1,-1,phi1)
d2=pow(e2,-1,phi2)
print(d1,d2)

#encode it back into utf-8 to get the flag
cipher1=nums[2]
cipher2=nums[5]
plain1=pow(cipher1,d1,p1)
plain2=pow(cipher2,d2,p2)
print("Plain 1",plain1)
print("Plain 2",plain2)
print((plain1.to_bytes(4,'big')+plain2.to_bytes(4,'big')).decode('utf-8'))
    
        
