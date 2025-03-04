from add import *

print("Praktiline ülesanne Isikukood kasutajate funktsioonide abil\n")

ikoodid=[]
arvud=[]
stop=" "

while stop != "STOP":
    ik=input("Enter ikood: ")
    while len(ik)!=11 or not ik.isdigit():
        arvud.append(ik)
        ik=input("Your ikood has wrong number of symbols or contains letters! Enter ikood again (11 symbols and only numbers): ")
    while ik[0] not in ["1","2","3","4","5","6"]:
        arvud.append(ik)
        ik=input("The ikood must start with 1,2,3,4,5 or 6! Enter ik again: ")
    while True:
        if 0<=int(ik[1:3])<=99 and 1<=int(ik[3:5])<=12 and 1<=int(ik[5:7])<=31:
            break
        else :
            arvud.append(ik)
            ik = input("the 2-7 symbols cannot be date of birth. Enter ikood again: ")
    #Контрольное число
    # Вес первой степени: 1 2 3 4 5 6 7 8 9 1
    # Вес второй степени: 3 4 5 6 7 8 9 1 2 3


    kn=kontrollnumber(ik)

     
    if int(ik[10]) == kn:
        print("ikood is right!(kontrollnumber matches)\n\n")
        ikoodid.append(ik)

        v=result(ik)
        v1=haigla(ik)
        print("\n\n")

    else:
        print("ikood is wrong... (kontrollnumber doesnt match)")
        arvud.append(ik)
 
    print("All entered ikoods:\n",ikoodid)
    print("All wrong attemts:\n",arvud)
    stop=input("\n\nPress enter to continue--> ").upper()