cipher="11101010100010001010101000101000111010001110101000000010001010101110001000101110100011101011101110000000111010111010001110111011100011101010001000000010100010101000000010111000111010000000100011101000101000111011101000111011100010111"
#morse code idea from Unicode output
#observe that we have odd number of 1s between consecutive 0s and vice versa, with lengths 7 and 3

MORSE_CODE_DICT = { '.-':'A', '-...':'B',
                    '-.-.':'C', '-..':'D', '.':'E',
                    '..-.':'F', '--.':'G', '....':'H',
                    '..':'I', '.---':'J', '-.-':'K',
                    '.-..':'L', '--':'M', '-.':'N',
                    '---':'O', '.--.':'P', '--.-':'Q',
                    '.-.':'R', '...':'S', '-':'T',
                    '..-':'U', '...-':'V', '.--':'W',
                    '-..-':'X', '-.--':'Y', '--..':'Z',
                    '.----':'1', '..---':'2', '...--':'3',
                    '....-':'4', '.....':'5', '-....':'6',
                    '--...':'7', '---..':'8', '----.':'9',
                    '-----':'0'}
morse=""

i=0
while (i<len(cipher)):
    ch=cipher[i]
    if (ch=='1'): #check length of 1s
        count=1
        j=i+1
        while (j<len(cipher) and cipher[j]=='1'):
            count+=1
            j+=1
        if (count==3): #add a dash
            morse=morse+"-"
        elif (count==1):
            morse=morse+"."
        i=j #move onto the next element
    else: #check length of 0s
        morse=morse+" "
        i+=1
        
#use the dictionary to convert the morse code back to letters, after removing spaces and adding _ between words
plain=""
rep1=morse.replace('       ','x') #length 7 space
words=rep1.split('x')
sentence=""
for w in words:
    rep2=w.replace('   ','a') #length 3 space
    word=""
    characters=rep2.split('a') #individual characters
    for ch in characters:
        ch=ch.replace(' ','') #removing spaces
        letter=MORSE_CODE_DICT[ch]
        word=word+letter
    sentence=sentence+word+"_"
sentence=sentence[:-1]
print("Flag:",sentence.lower())
    
        


    
    