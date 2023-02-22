import os

command = "cls" if os.name == "nt" else "clear"
os.system(command)

lang = "en"

def remove_(x, liste):
    if x in liste:
        while x in liste:
            liste.remove(x)

def numberToLetter(x):
    birler = ["","bir", "iki","üç","dört", "beş","altı","yedi","sekiz","dokuz"] 
    onlar = ["", "on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]
    yüz = "yüz"
    bin = "bin"
    milyon = "milyon"

    if lang == "en":
        birler = ["","one", "two","three","four", "five","six","seven","eight","nine"] 
        onlar = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
        yüz = "hundred"
        bin = "thousand"
        milyon = "million"
    cikti = []
    try:
        x = int(x)
        uzunluk = len(str(x))
        if str(x)[0] == 0:
            for i in range(uzunluk):
                if x[i] == 0:
                    remove_(0, x)

        if str(x) == "0":
            cikti.append("zero" if lang == "en" else "sıfır") 
        elif uzunluk == 7:
            cikti.append(birler[int(str(x)[0])] + milyon)
            cikti.append("" if str(x)[1]=="0" else yüz if str(x)[1]=="1" else birler[int(str(x)[1])] + " " + yüz)
            cikti.append(onlar[int(str(x)[2])])
            cikti.append("" if str(x)[1]=="0" else bin if str(x)[3]=="1" or str(x)[3]=="0" else birler[int(str(x)[3])] + " " + bin)
            cikti.append(yüz if str(x)[4]=="1" else "" if str(x)[4]=="0" else birler[int(str(x)[4])] + " " + yüz)
            cikti.append(onlar[int(str(x)[5])])
            cikti.append(birler[int(str(x)[6])])
        elif uzunluk == 6:
            cikti.append(yüz if str(x)[0]=="1" else birler[int(str(x)[0])] + yüz)
            cikti.append(onlar[int(str(x)[1])])
            cikti.append(bin if str(x)[2]=="1" else bin if str(x)[2]=="0" else birler[int(str(x)[2])] + " " + bin)
            cikti.append(yüz if str(x)[3]=="1" else "" if str(x)[3]=="0" else birler[int(str(x)[3])] + " " + yüz)
            cikti.append(onlar[int(str(x)[4])])
            cikti.append(birler[int(str(x)[5])])
        elif uzunluk == 5:
            cikti.append(onlar[int(str(x)[0])])
            cikti.append(bin if str(x)[1]=="1" else bin if str(x)[2]=="0" else birler[int(str(x)[1])] + " " + bin)
            cikti.append(yüz if str(x)[2]=="1" else "" if str(x)[2]=="0" else birler[int(str(x)[2])] + " " + yüz)
            cikti.append(onlar[int(str(x)[3])])
            cikti.append(birler[int(str(x)[4])])
        elif uzunluk == 4:
            cikti.append(bin if str(x)[0]=="1" else birler[int(str(x)[0])] + " " + bin)
            cikti.append(yüz if str(x)[1]=="1" else "" if str(x)[1]=="0" else  birler[int(str(x)[1])] + " " + yüz)
            cikti.append(onlar[int(str(x)[2])])
            cikti.append(birler[int(str(x)[3])])
        elif uzunluk == 3:
            cikti.append(yüz if str(x)[0]=="1" else birler[int(str(x)[0])] + " " + yüz)
            cikti.append(onlar[int(str(x)[1])]) 
            cikti.append(birler[int(str(x)[2])])
        elif uzunluk == 2:
            if lang == "en" and x<20:
                if x == 10:
                    cikti.append("ten")
                elif x == 11:
                    cikti.append("eleven")
                elif x == 12:
                    cikti.append("twelve")
                elif x == 13:
                    cikti.append("thirteen")
                elif x == 15:
                    cikti.append("fifteen")
                elif x == 18:
                    cikti.append("eighteen")
                else:
                    cikti.append(birler[int(str(x)[1])] + "teen")
            else:
                cikti.append(onlar[int(str(x)[0])]) 
                cikti.append(birler[int(str(x)[1])]) 
        elif uzunluk == 1:
            cikti.append(birler[int(str(x)[0])])
        else:
            cikti.append("out of range") 
        remove_("", cikti)
    except:
        cikti.append("can only concatenate str")
    return " ".join(cikti)

with open("en.txt", "w") as file:
    file.write("")
with open("tr.txt", "w") as file:
    file.write("")
with open("en.txt", "a") as file:
    for i in range(10001):
        file.write(str(i) + " : " + str(numberToLetter(i)) + "\n")
lang = "tr"
with open("tr.txt", "a") as file:
    for i in range(10001):
        file.write(str(i) + " : " + str(numberToLetter(i)) + "\n")
