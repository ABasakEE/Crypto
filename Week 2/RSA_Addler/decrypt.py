import binascii as bin
import base64

string="JJFEKVCFKZFVES2KJJLE2UZSJ5EUUS2VGJKVEU2KLJDUKVKUINDESNKMIVDVMQ2LJJNEIVKLKZFVKSKOJRKVKTSLJVFVMS2WJVITETSKIZHEKS2WJNGEWRK2IZBVGU2KI5FEWVSDKZJUWSZVIZLEGV2TI5EUMSSVKVHESPI="

#seems like a substitution cipher
freq=dict()

'''for ch in string:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1

for key, value in sorted(freq.items(), key=lambda x: x[1],reverse=True): 
    print("{} : {}".format(key, value))'''


''''hexa1="249144295085299155112d8a2492c4d94652279114512d95189295114d8a2c90d429529420d0c448d28c2150d5310d8b24934421528b29915529228e25129529348b255155312d9625521311348a2191c4292d9624d1845912b6219055194d8a2391445954832992545926552192c4195d932391143124952951c448f2"
out=""
count=0

hexa2="4a4a46454b5643464b5a46564553324b4a4a4c4532555a534a35455555533256474a4b564555324b4c4a44554b564b55494e4445534e4b4d495644564d51324c4a4a4e4549564b4c4b5a46564b534b4f4a524b564b54534c4a5646564d5332574a5649544554534b495a48454b5332574a4e474557524b32495a42564755324b49354645575653444b5a4a5557535a56495a4c4547563254493545554d5353564b5648455350493d0a"

for ch in hexa2:
    if count==0:
        out=out+"0x"
    out=out+ch
    count+=1
    if count==2:
        out=out+' '
        count=0

print(out)'''

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
#key=KEY
print("plain text: intelligent")

#print(d6str)

#print(bin.unhexlify(d3))


