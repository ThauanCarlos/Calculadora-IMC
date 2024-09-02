# Calcula IMC

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def interpretar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 24.9:
        return "Peso normal"
    elif imc < 29.9:
        return "Sobrepeso"
    elif imc < 34.9:
        return "Obesidade Grau I"
    elif imc < 39.9:
        return "Obesidade Grau II"
    else:
        return "Obesidade Grau III"

# Solicitar entrada do usuário
peso = float(input("Digite o seu peso (em kg): "))
altura = float(input("Digite a sua altura (em metros): "))

# Calcular IMC
imc = calcular_imc(peso, altura)

# Interpretar e exibir o resultado
interpretacao = interpretar_imc(imc)
print(f"Seu IMC é {imc:.2f}, o que é considerado: {interpretacao}")
