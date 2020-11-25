"""
https://www.codingame.com/ide/puzzle/defibrillators

Input
3,879483
43,608177
3
1;Maison de la Prevention Sante;6 rue Maguelone 340000 Montpellier;;3,87952263361082;43,6071285339217
2;Hotel de Ville;1 place Georges Freche 34267 Montpellier;;3,89652239197876;43,5987299452849
3;Zoo de Lunaret;50 avenue Agropolis 34090 Mtp;;3,87388031141133;43,6395872778854

Output
Maison de la Prevention Sante

In2:
3.874054
43.606779
4
107;Caisse Primaire d'Assurance Maladie;29 cours Gambetta 34000 MONTPELLIER;04 99 52 54 49;3,87110915929521;43,6065196099402
108;Caisse Primaire d'Assurance Maladie;90 allee Almicare Calvetti 34000 Montpellier;04 99 52 54 49;3,82126953167633;43,6322018829039
109;Caisse d'assurance retraite et de la Sante au travail;29 cours Gambetta 34000 MONTPELLIER;04 67 12 94 72;3,87064343057042;43,6068847626242
110;Caisse d'assurance retraite et de la Sante au travail;Century 2 , 101 place pierre Duhem le millenaire 34000 MONTPELLIER;04 67 12 94 72;3,91465549573187;43,6068978500869

Out2:
?

"""
import math


def alg(cur_lon, cur_lat, defibs):
    """
    >>> alg()

    >>> alg()
    """

    dist = []
    for s in defibs:
        ss = s.split(";")
        lon = float(ss[-2].replace(",", "."))
        lat = float(ss[-1].replace(",", "."))

        # x = (cur_lon - lon) * math.cos(cur_lon + lon)
        # y = cur_lat - lat
        # d = math.sqrt(x**2 + y**2) * 6371
        dlon = cur_lon - lon
        dlat = cur_lat - lat
        a = (math.sin(dlat / 2)) ** 2 + math.cos(cur_lat) * math.cos(lat) * (math.sin(dlon / 2)) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        d = c * 6371

        dist.append((d, ss[1]))
    res = min(dist)
    return res[1]



if __name__ == "__main__":
    lon = float(input().replace(",", "."))
    lat = float(input().replace(",", "."))
    n = int(input())
    # log(n)
    defibs = [input() for i in range(n)]
    print(alg(lon, lat, defibs))

