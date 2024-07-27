import numpy as np

list_n=[2140324650240744961264423072839333563008614715144755017797754920881418023447140136643345519095804679610992851872470914587687396261921557363047454770520805119056493106687691590019759405693457452230589325976697471681738069364894699871578494975937497937,
	124620366781718784065835044608106590434820374651678805754818788883289666801188210855036039570272508747509864768438458621054865537970253930571891217684318286362846948405301614416430468066875699415246993185704183030512549594371372159029236099, 
	115792089237316195423570985008687907853269984665640564039457584007913129639937, 
	69203410113561398433978337198079999737
	]

output=[12331, 329796147429, 74123515046928094799825188664648897435800820530055170843191646450844356103736, 43902742405476161131473929002315604273, 12944, 27735580683, 78973387595019170784612458521728960323264867786515401685321385965026793856403, 31919992337066015048720993940025631713, 2347, 734847565824, 101271357811948351746604313864755895370188204420625050803278149660722073946239, 56349663930743838272275153491291168002, 8982, 2328310511064, 106058552522508819565468995006183368211991722056203258411598135921256264292248, 51792942655418674841644497405567291075, 11875, 384399163511, 35616979992135835717966741760639566123331219536421186604525024997159995343459, 40823011766295422493409073278264153576, 9039, 1129412837944, 49932432102491735682672329915063718414997565757845935029236989016277672292325, 13039422778599220469692552984865152667, 9053, 2181825073000, 84112885952588821792250635403984208020788974809389408663739568743119424997740, 30474861076101697076037209063127855525, 10835, 2430426096125, 11951553580270835032619325940480717483281377890052128849411588756090281688706, 63745756952654317830500039851174786720]


#factoring done by using factordb
pq=[[33372027594978156556226010605355114227940760344767554666784520987023841729210037080257448673296881877565718986258036932062711,64135289477071580278790190170577389084825014742943447208116859632024532344630238623598752668347708737661925585694639798853367],[244624208838318150567813139024002896653802092578931401452041221336558477095178155258218897735030590669041302045908071447,509435952285839914555051023580843714132648382024111473186660296521821206469746700620316443478873837606252372049619334517],[1238926361552897,93461639715357977769163558199606896584051237541638188580280321
],[263,263130836933693530167218012159999999]]

totient_n=[]

for elem in pq:
    totient_n.append((elem[0]-1)*(elem[1]-1))

list_e=[-1,3,-1,-1]

list_d=[1, -1, 77266263685307006230322907286315353524856777913832852852497884154975370477569, 56758248688344445618535855545843339303]
#try to break for index 1
#e=3 (given)
list_d[1]=pow(list_e[1],-1,totient_n[1])
#print(list_d[1])

#try to break for index 2
#need to find e
#let a=e^2
a=pow(list_d[2],-1,totient_n[2])
list_e[2]=round(np.sqrt(a))
#print(list_e[2])

#try to break for index 3
#need to find e
#let b=e^3
b=pow(list_d[3],-1,totient_n[3])
list_e[3]=round(np.cbrt(b))
#print(list_e[3])

#get the text after XORing
#for e^0 terms, we will leave it as it 
#for others, we will use terms like e, ed, (e**2)d ... to decode

XOR=[]

for i in range(len(output)):
    m=output[i]
    p=i%4
    if p>0: 
        m=pow(output[i],(list_e[p]**(p-1))*list_d[p],list_n[p])
    XOR.append(m)

#we get the array of numbers after Riddler XORing
#since we know flag starts with YoS, let us try to start the string with that

a,b,c=ord('Y'),ord('o'),ord('S') 
assert a^b*b^c==output[0]
#this does match with the first element in the XORed array

flag="YoS"

#we can now recover the string by XOring with previous two elements and current element of output array
for i in range(len(output)-3):
    a=ord(flag[i+1])
    b=ord(flag[i+2])
    c=XOR[i+1]^b*b^a
    char=chr(c)
    flag=flag+char

print("Flag:",flag)
