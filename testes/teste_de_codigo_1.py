a = input()
b = input()
c = input()

if a == 'vertebrado':
    if b == 'ave':
        if c == 'carnivoro':
            print("agia")
        elif c == 'onivoro':
            print("pomba")
        else:
            print("digite uma palavra valida")
    elif b == 'mamifero':
        if c == 'onivoro':
            print("homem")
        elif c == 'herbivoro':
            print("vaca")
        else:
            print("digite uma palavra valida")
    else:
        print("digite uma palavra valida")
elif a == 'invertebrado':
    if b == 'inseto':
        if c == 'hematofago':
            print("pulga")
        elif c == 'herbivoro':
            print("lagarta")
        else:
            print("digite uma palavra valida")
    elif b == 'analideo':
        if c == 'hematofago':
            print("sanguessuga")
        elif c == 'onivoro':
            print("minhoca")
        else:
            print("digite uma palavra valida")
    else:
        print("digite uma palavra valida")
else:
    print("digite uma palavra valida")
