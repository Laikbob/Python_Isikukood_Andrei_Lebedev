ikoodid=[]
arvud=[]

while True:
    isikukood=input("Введите личный код: ")
    #Проверка личного кода
    if len(isikukood) !=11:
        print("Неверный код isiskukood. Введите правильный:")
        arvud.append(isikukood)
        continue
    
    esimene=isikukood[0]
    if esimene not in['1','2','3','4','5','6']:
        print("Первый символ болжен быть 1,2,3,4,5 или 6!")
        arvud.append(isikukood)
        continue
    #Пол
    if esimene in ['1','3','5']:
        sex="Мужчина"
    else:
        sex="Женщина"
    
    #Год рождения
    год = isikukood[1:3]
    месяц = isikukood[3:5]
    день = isikukood[5:7]
    if esimene in ['1', '2']:
        полный_год = "19" + год
    else:
        полный_год = "20" + год
    дата_рождения = день + "." + месяц + "." + полный_год

    #Больница
    номер_рождения = int(isikukood[7:10]) 
    if 0 <= номер_рождения <= 10:
        место_рождения = "Kuressaare Haigla"
    elif 11 <= номер_рождения <= 19:
        место_рождения = "Tartu Ülikooli Naistekliinik, Tartumaa, Tartu"
    elif 21 <= номер_рождения <= 220:
        место_рождения = "Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla"
    elif 221 <= номер_рождения <= 270:
        место_рождения = "Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)"
    elif 271 <= номер_рождения <= 370:
        место_рождения = "Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla"
    elif 371 <= номер_рождения <= 420:
        место_рождения = "Narva Haigla"
    elif 421 <= номер_рождения <= 470:
        место_рождения = "Pärnu Haigla"
    elif 471 <= номер_рождения <= 490:
        место_рождения = "Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigла"
    elif 491 <= номер_рождения <= 520:
        место_рождения = "Järvamaa Haigla (Paide)"
    elif 521 <= номер_рождения <= 570:
        место_рождения = "Rakvere, Tapa haigла"
    elif 571 <= номер_рождения <= 600:
        место_рождения = "Valga Haigla"
    elif 601 <= номер_рождения <= 650:
        место_рождения = "Viljandi Haigla"
    elif 651 <= номер_рождения <= 700:
        место_рождения = "Lõuna-Eesti Haigla (Võru), Põlva Haigla"
    else:
        место_рождения = "Неизвестное место рождения"

    print(f"Это {sex}, его/ее день рождения {дата_рождения} и место рождения {место_рождения}")
    ikoodid.append(isikukood)

    print("\nСписок правильных кодов:")
    for код in ikoodid:
        print(код)

    print("\nСписок неправильных кодов:")
    for код in sorted(arvud):  
        print(код)
