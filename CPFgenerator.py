import random
def gerarcpf():
    digitosAleatorios = random.randint(100000000,999999999)
    menos = 10
    decimoDigito =0
    decimoPrimerioDigito =0
    L=0
    M=0
    #GERAÇÃO DECIMO DIGITO
    digitos = [int(digito) for digito in str(digitosAleatorios)]
    for i in digitos:
        L += menos*i
        menos -= 1
    if L % 11 == 0 or L % 11 == 1:
        decimoDigito = 0
        digitos.append(decimoDigito)
    else:
        decimoDigito = 11 - (L % 11)
        digitos.append(decimoDigito)

    menos =10
    #GERAÇÃO DECIMO PRIMEIRO DIGITO
    for x in digitos[1:]:
        M += menos*x
        menos -= 1
    if M % 11 == 0 or M % 11 == 1:
        decimoPrimeiroDigito = 0
        digitos.append(decimoPrimeiroDigito)
    else:
        decimoPrimerioDigito = 11 - (M % 11)
        digitos.append(decimoPrimerioDigito)

    cpf = ''.join(map(str, digitos))
    print(f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}")

print("CPF gerado: ")
gerarcpf()