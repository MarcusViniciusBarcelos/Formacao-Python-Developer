def calcular_garrafas_total(N, K):
    garrafas_cheias = N // K
    garrafas_resto = N % K
    garrafas_total = N + garrafas_cheias
    while garrafas_cheias >= K:
        garrafas_extra = garrafas_cheias // K
        garrafas_total += garrafas_extra
        garrafas_cheias = garrafas_cheias % K + garrafas_extra

    return garrafas_total


T = int(input(""))
for i in range(T):
    N, K = map(int, input().split())
    resultado = calcular_garrafas_total(N, K)
    print(resultado)