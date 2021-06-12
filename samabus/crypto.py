#cryptage MHD1
from random import randint
alpha,c_alpha="abcdefghijklmnopqrstuvwxyz.-@","X*-)/[+<\(]}=,';!_&$Z{.@|eµI>"
nb,erron="0123456789",[]
for i in range(4):
    erron.append(randint(0,10))

def crypt(msg):
    saut=randint(0,15)
    msg,mem=[l for l in msg],saut
    for loop in range(len(msg)):
        if msg[loop] in alpha:
            msg[loop]=c_alpha[(alpha.find(msg[loop])+saut)%29]
        elif msg[loop] in nb:
            msg[loop]=":"+c_alpha[(nb.find(msg[loop])+saut)%10]
        else:
            return -1
        if loop in erron:
            msg[loop]=nb[randint(0,9)]+msg[loop]
        saut+=saut
    msg[0]=c_alpha[mem]+msg[0]
    return ''.join(msg)

def decrypt(msg):
    msg,cont=[l for l in msg],False
    cle=c_alpha.find(msg.pop(0))
    for item in range(len(msg)):
        if msg[item] in nb:
            msg[item]=''
    msg="".join(msg)
    msg=[l for l in msg]
    n,item=len(msg),0
    while item<n:
        if msg[item] in c_alpha:
            msg[item]=alpha[(c_alpha.find(msg[item])-cle)%29]
        elif msg[item]==":":
            msg[item]=msg.pop(item+1)
            msg[item]=nb[(c_alpha.find(msg[item])-cle)%10]
            n-=1
        cle,item=2*cle,item+1
    return "".join(msg)
#print(crypt(input(),saut))
"""msg=input('Entrez le message ')
print("le message decrypté est {}".format(decrypt(msg)))"""
