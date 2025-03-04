def kontrollnumber(ik) -> int:
    kaal1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    kaal2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
    
    summ = sum(int(ik[i]) * kaal1[i] for i in range(10))

    if summ % 11 == 10:
        summ2 = sum(int(ik[i]) * kaal2[i] for i in range(10))
        return 0 if summ2 % 11 == 10 else summ2 % 11
    else:
        return summ % 11



def result(ik) -> str:
    gender = "male" if ik[0] in ["1", "3", "5"] else "female"
    century = {"1": "18", "2": "18", "3": "19", "4": "19", "5": "20", "6": "20"}[ik[0]]
    return f"{ik} - {gender}, {ik[5:7]}.{ik[3:5]}.{century}{ik[1:3]}"


def haigla(ik) -> str:
    haiglad = {
        range(1, 11): "Kuressaare Haigla",
        range(11, 20): "Tartu Ülikooli Naistekliinik, Tartumaa, Tartu",
        range(21, 221): "Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla",
        range(221, 271): "Ida-Viru Keskhaigla, Kohtla-Järve, endine Jõhvi",
        range(271, 371): "Maarjamõisa Kliinikum, Tartu, Jõgeva Haigla",
        range(371, 421): "Narva Haigla",
        range(421, 471): "Pärnu Haigla",
        range(471, 491): "Pelgulinna Sünnitusmaja, Tallinn, Haapsalu haigla",
        range(491, 521): "Järvamaa Haigla, Paide",
        range(521, 571): "Rakvere, Tapa haigla",
        range(571, 601): "Valga Haigla",
        range(601, 651): "Viljandi Haigla",
        range(651, 701): "Lõuna-Eesti Haigla, Võru, Põlva Haigla",
    }

    n = int(ik[7:9])
    for r in haiglad:
        if n in r:
            return haiglad[r]
    
    return "Неизвестное место рождения"



