'''

░█████╗░░█████╗░░█████╗░░█████╗░░█████╗░
██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗
╚═╝███╔╝╚═╝███╔╝╚═╝███╔╝╚═╝███╔╝╚═╝███╔╝
░░░╚══╝░░░░╚══╝░░░░╚══╝░░░░╚══╝░░░░╚══╝░
░░░██╗░░░░░██╗░░░░░██╗░░░░░██╗░░░░░██╗░░
░░░╚═╝░░░░░╚═╝░░░░░╚═╝░░░░░╚═╝░░░░░╚═╝░░

WELCOME TO THE ACTUAL CHALLENGE DETECTIVE! I SEE YOU'VE CRACKED THE FIRST CIPHER! I COULD'VE SOLVED THAT CIPHER TWICE AS FAST.

'''

from sympy.ntheory.factor_ import totient

flag='[REDACTED]'

############################ MY VERY ADVANCED FUNCTION! ########################################
def Riddler_XOR(a, b, c):
	return (ord(a)^ord(b)*ord(b)^ord(c))

cipher_1=[]
for i in range(len(flag)-2):
	cipher_1.append(Riddler_XOR(flag[i],flag[i+1],flag[i+2]))


cipher_1.append(Riddler_XOR(flag[len(flag)-2],flag[len(flag)-1],flag[0]))

cipher_1.append(Riddler_XOR(flag[len(flag)-1], flag[0], flag[1]))

list_n=[2140324650240744961264423072839333563008614715144755017797754920881418023447140136643345519095804679610992851872470914587687396261921557363047454770520805119056493106687691590019759405693457452230589325976697471681738069364894699871578494975937497937,
	124620366781718784065835044608106590434820374651678805754818788883289666801188210855036039570272508747509864768438458621054865537970253930571891217684318286362846948405301614416430468066875699415246993185704183030512549594371372159029236099, 
	115792089237316195423570985008687907853269984665640564039457584007913129639937, 
	69203410113561398433978337198079999737
	]

list_e=[[REDACTED], 3, [REDACTED], [REDACTED]]
list_phi=[]

###################### BET YOUR BATCOMPUTER CAN'T RUN THIS! ###############################################
for i in n:
	list_phi.append(totient(n))

list_d=[1, [REDACTED], 77266263685307006230322907286315353524856777913832852852497884154975370477569, 56758248688344445618535855545843339303]

############## I HOPE YOU UNDERSTOOD THIS DOES NOT WORK DETECTIVE #####################################
'''
for i in range(4):
	list_d_riddle.append(pow(e[i],-1,phi[i]))
'''
#######################################################################################################

output=[]
for i in range(len(cipher_1)):
	output.append(pow(cipher_1[i],list_e[i%4],list_n[i%4]))
print(output)

########################################### NOW FIND THE FLAG DETECTIVE! #####################################################