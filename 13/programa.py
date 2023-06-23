varUm = input("Insira um número:")
while not varUm.isdigit():
    varUm = input("Insira um número:")
varUm = int(varUm)

varDois = input("Insira outro número:")
while not varDois.isdigit():
    varDois = input("Insira outro número:")
varDois = int(varDois)

constantePi = 3.14
vezesPi = varUm * constantePi
vezesPi2 = varDois * constantePi

if varUm == varDois:
    print("São números iguais!")

if varUm > varDois:
    print(varUm, "é maior que", varDois, "!")
    
if varUm < varDois:
    print(varDois, "é maior que", varUm, "!")

print(varUm, "* PI =", vezesPi)
print(varDois, "* PI =", vezesPi2)
calculosFeitos = ["Número * PI", "Qual número é maior"]
print(calculosFeitos)