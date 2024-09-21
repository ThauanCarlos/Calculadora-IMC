# Calcula IMC

def calcular_imc(peso, altura):
    """
    Calcula o Índice de Massa Corporal (IMC) com base no peso e altura fornecidos.
    :param peso: Peso da pessoa em kg.
    :param altura: Altura da pessoa em metros.
    :return: Valor do IMC.
    """
    return peso / (altura ** 2)

def interpretar_imc(imc):
    """
    Interpreta o valor do IMC e retorna a classificação.
    :param imc: Valor calculado do IMC.
    :return: Classificação de acordo com o valor do IMC.
    """
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

def obter_dados_usuario():
    """
    Solicita o peso e altura do usuário e valida se os dados são numéricos.
    :return: Peso e altura válidos do usuário.
    """
    while True:
        try:
            peso = float(input("Digite o seu peso (em kg): "))
            altura = float(input("Digite a sua altura (em metros): "))
            if peso <= 0 or altura <= 0:
                print("Peso e altura devem ser números positivos. Por favor, insira valores maiores que 0.")
            else:
                return peso, altura
        except ValueError:
            print("Entrada inválida. Por favor, insira números válidos para peso e altura.")
        except KeyboardInterrupt:
            print("\nOperação interrompida. Saindo do programa.")
            break

# Função principal
def main():
    # Solicitar entrada do usuário
    peso, altura = obter_dados_usuario()
    if peso and altura:
        # Calcular IMC
        imc = calcular_imc(peso, altura)
    
        # Interpretar e exibir o resultado
        interpretacao = interpretar_imc(imc)
        print(f"Seu IMC é {imc:.2f}, o que é considerado: {interpretacao}")

if __name__ == "__main__":
    main()
