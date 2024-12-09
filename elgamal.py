import random

     
def titkositas(p,g,x,h,szavazatok):
    titkositott_szavazatok = []
    for szavazat in szavazatok:
        k = random.randint(1,p-2)
        c1 = pow(g, k, p)
        c2 = (szavazat * pow(h, k, p)) % p
        titkositott_szavazatok.append((c1, c2))

    print("Titkositott szavazatok:", titkositott_szavazatok)
    return titkositott_szavazatok

def visszafejtes(titkositott_szavazatok, x, p):
    visszafejtett_szavazatok = []
    for szavazat in titkositott_szavazatok:
        c1, c2 = szavazat
        s = pow(c1, x, p)
        s_1 = pow(s, -1, p)
        szavazat = (c2 * s_1) % p
        visszafejtett_szavazatok.append(szavazat)
    print("Igen(1) szavazatok szama: ", sum(szavazat == 1 for szavazat in visszafejtett_szavazatok))
    print("Nem(2) szavazatok szama: ", sum(szavazat == 2 for szavazat in visszafejtett_szavazatok))
    return visszafejtett_szavazatok


if __name__ == "__main__":
    p = 104729  
    g = 2  
    x = 56789 
    h = pow(g, x, p) 

    szavazatok = [1, 2, 1, 1, 2, 2, 1]
    print("Szavazatok: ",szavazatok)

    titkositott_szavazatok = titkositas(p,g,x,h,szavazatok)
    visszafejtett_szavazatok = visszafejtes(titkositott_szavazatok, x, p)
