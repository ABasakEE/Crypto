# import the necessary libraries here
from Crypto.Util.number import getPrime,long_to_bytes,bytes_to_long
import math

class RSA:
    """Implements the RSA public key encryption / decryption."""

    def __init__(self, key_length):
        # define self.p, self.q, self.e, self.n, self.d here based on key_length
        
        # p and q must be declared as private members
        self.__p=getPrime(key_length)
        self.__q=getPrime(key_length)
        self.e=65537 #usually 2^16+1 chosen as public exponent
        self.n=self.__p*self.__q
        
        #generate the private key
        totient=(self.__p-1)*(self.__q-1)
        
        #private key can also not be accessed outside this class
        self.__d=pow(self.e,-1,totient)

    def encrypt(self, binary_data):
        # return encryption of binary_data here
        # encryption is defined as m^e (modulo n)
        print("Binary",binary_data)
        return pow(bytes_to_long(binary_data),self.e,self.n)
        pass

    def decrypt(self, encrypted_int_data):
        # return decryption of encrypted_binary_data here
        # decryption defined as c^d (modulo n)
        
        return pow(encrypted_int_data,self.__d,self.n)
        pass

class RSAParityOracle(RSA):
    """Extends the RSA class by adding a method to verify the parity of data."""

    def is_parity_odd(self, encrypted_int_data):
        # Decrypt the input data and return whether the resulting number is odd
        
        
        return bool(self.decrypt(encrypted_int_data) & 1)
        
        pass


def parity_oracle_attack(ciphertext, rsa_parity_oracle):
    # implement the attack and return the obtained plaintext
    
    # the public n is always available
    N=rsa_parity_oracle.n
    e=rsa_parity_oracle.e
    
    upper=rsa_parity_oracle.n
    lower=0
    
    # we know that RSA is homeomorphic
    # to find out the limits of the input binary message we can multiple the cipher text by powers of 2^e (modulo N)
    # this will decrypt to 2*m ,4*m, 8*m and so on 
    
    # if 2*m>n, it will return 1 -> m>n/2 (increase lower limit), else 0 -> m<n/2 (reduce upper limit)
    
    
    # based on if the output is even or odd we can shrink the bounds
    # this is basically similar to a binary search
    
    i=1
    print("Started search")
    bitLength=round(math.log(N,2))+1
    while lower<upper: #bit length of primes
        flag=rsa_parity_oracle.is_parity_odd((ciphertext*pow(2,i*e,N))%N) #returned True
        if flag:
            lower=(lower+upper)//2
        else:
            upper=(lower+upper)//2
        i+=1
        
        if i%10==0:
            print(".",end=' ')
    print()
    print("Search complete")
    
    #due to rounding errors we may have to look for a few values > and < upper
    #bound should be log2N=log2(1024)=10
    
    check=int(math.log(N,2)) #worst case error, but the error is usually much smaller
    plainBytes=upper
    for i in range(check+1):
        #try out the encryption using public key
        msg1=upper+i
        msg2=upper-i
        encrypt1=pow(msg1,e,N)
        encrypt2=pow(msg2,e,N)
        if encrypt1==ciphertext:
            plainBytes=msg1
            break
        if encrypt2==ciphertext:
            plainBytes=msg2
            break
        
        
        
    
    plain=long_to_bytes(plainBytes).decode('utf-8')
    return plain #they have now converged and we have the input message
    
    


def main():
    input_bytes = input("Enter the message: ")

    # Generate a 1024-bit RSA pair    
    rsa_parity_oracle = RSAParityOracle(1024)

    # Encrypt the message
    ciphertext = rsa_parity_oracle.encrypt(input_bytes.encode('utf-8'))
    print("Encrypted message is: ",ciphertext)
    # print("Decrypted text is: ",rsa_parity_oracle.decrypt(ciphertext))

    # Check if the attack works
    plaintext = parity_oracle_attack(ciphertext, rsa_parity_oracle)
    print("Obtained plaintext: ",plaintext)
    assert plaintext == input_bytes
    

if __name__ == '__main__':
    main()