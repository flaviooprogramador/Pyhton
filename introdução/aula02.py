#x = input(str('qual seu nome?'))
#print(x)

nome = input("Por favor digite seu nome:")
anoNascimento = input("Por favor digite seu ano de anscimento:")
idade = 2020 - int(anoNascimento)
print("Olá {} sua idade é {} anos".format(nome,idade))