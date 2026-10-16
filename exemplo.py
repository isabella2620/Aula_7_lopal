produto = "Mouse Gamer WIFI"
valores = [20, 71, 100, 30]
if "mouse".lower() in produto .lower() :
    print("produto encontrado")
else:
    print("produto nao encontrado")

def dobrar(valor):
    resultado = valor * 2
    return resultado
print(dobrar (11))

valores_novos = []

for valor in valores:
    valores_novos.append(dobrar(valor))
print(valores_novos)