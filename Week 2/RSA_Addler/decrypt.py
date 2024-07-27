import binascii as bin
import base64

string="JJFEKVCFKZFVES2KJJLE2UZSJ5EUUS2VGJKVEU2KLJDUKVKUINDESNKMIVDVMQ2LJJNEIVKLKZFVKSKOJRKVKTSLJVFVMS2WJVITETSKIZHEKS2WJNGEWRK2IZBVGU2KI5FEWVSDKZJUWSZVIZLEGV2TI5EUMSSVKVHESPI="

d1=base64.b32decode(string)
#d2=bin.hexlify(d1)
#print(d2)
print(d1,len(d1))
d2=base64.b32decode(d1)
print(d2)
d3=base64.b32decode(d2)
print(d3)
d4=base64.b32decode(d3)
print(d4)
d5=base64.b32decode(d4)
print(d5,len(d5))

#apply Vigenere with key length 3
#key=KEY (using hint)
#decryption through online tool
print("plain text: intelligent")



