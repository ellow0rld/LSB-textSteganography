#Hide
secret_mssg = list(input("Enter secret message: "))
password = input("Create key: ")

##cover text to stego object
def cover_steg():        
    cover = input("Enter cover text: ")
    stegokey = input("Create stego key: ")
    print()
    global d_sc
    d_sc = {stegokey:cover}
    global d_cc
    d_cc = {cover:ciphertxt}
    print("Stego Object:",cover)
    
##secret to cipher text
def sec_steg():
    ascii_secret=[]
    binary=[]
    global ciphertxt
    ciphertxt=""
    cipher=[]
    for i in secret_mssg:
        ascii_secret.append(ord(str(i)))
    for i in ascii_secret:
        binary.append(list(bin(i).replace("0b","")))
    for i in range (0,len(binary)):
        if (binary[i][-1] =='0'):
            binary[i][-1] ='1'
        else:
            binary[i][-1] ='0'
    for i in range (0,len(binary)):
        b=""
        for j in binary[i]:
            b=b+j
        cipher.append(chr(int(b,2)))
    for i in cipher:
        if i == "`":
            ciphertxt = ciphertxt+ 'z'
        elif i == "{":
            ciphertxt = ciphertxt + 'a'
        elif i == '@':
            ciphertxt = ciphertxt + 'Z'
        elif i == '[':
            ciphertxt = ciphertxt + 'A'
        else:
            ciphertxt = ciphertxt + i
    cover_steg()

sec_steg()
y = input("Do you want to reveal the message?(y/n)")
x = 0
if (y=='y'):
    x = 2

#Reveal
##stego object to cipher text
def steg_ci():   
    count = 0
    print()
    while (count<5):
        cover_r = input("Enter Stego Object: ")
        skey = input("Enter stego key: ")
        if (skey in d_sc.keys() and cover_r in d_cc.keys()):
            stego = d_cc[cover_r]
            print("Cipher text:",d_cc[cover_r])
            print()
            return stego
        else:
            print("Incorrect stego object or key")
            count = count+1
            continue
    else:
        print("Exceeded limit")
        exit()
        
##cipher text to secret
def cipher_sec(stego):
        ascii_stego = []
        binary_s = []
        Sec = []
        sec = ""
        for i in stego:
            ascii_stego.append(ord(str(i)))
        for i in ascii_stego:
            binary_s.append(list(bin(i).replace("0b","")))
        for i in range (0,len(binary_s)):
            if (binary_s[i][-1] =='0'):
                binary_s[i][-1] ='1'
            else:
                binary_s[i][-1] ='0'
        for i in range (0,len(binary_s)):
            b=""
            for j in binary_s[i]:
                b=b+j
            Sec.append(chr(int(b,2)))
        for i in Sec:
            if i == "`":
                sec = sec+ 'z'
            elif i == "{":
                sec = sec + 'a'
            elif i == '@':
                sec = sec + 'Z'
            elif i == '[':
                sec = sec + 'A'
            else:
                sec = sec + i
        print("Secret message:",sec)
    
            
if (x==2):
    stego = steg_ci()
    k = input("Enter Key: ")
    if k == password:
        cipher_sec(stego)
    else:
        print("Incorrect key")
        exit()

