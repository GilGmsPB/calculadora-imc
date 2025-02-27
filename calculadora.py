#   Calculadora de IMC

#   Função para calcular o imc
def calculate_BMI (peso,altura):
    BMI = peso / (altura**2)
    return BMI

#   Função para Avaliar a Condição de Saúde
def evaluate_health(BMI):
    if BMI < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= BMI < 24.9:
        return "Peso saudável"
    elif 24.9 <= BMI < 29.9:
        return "Sobre Peso"
    else:
        return "Obesidade"



#   Mensagem Inicial
print ("=" * 40)
print ("💪 Bem-vindo à Calculadora de IMC! 💪\nDescubra seu índice de massa corporal de forma rápida e fácil.\nDigite seus dados e veja sua classificação!")
print ("=" * 40)

#   Solicitação de Dados do Usuário
while True:
    nome = input("\nPor favor, digite seu nome: ")
    
    try:
        idade = int(input("Agora digite sua idade: "))
        peso = float(input("Agora digite seu peso (em Kg): ").replace(",", "."))
        altura = float(input("Digite sua altura em metros (ex: 1.75): ").replace(",", "."))
    except ValueError:
        print("\n❌ Entrada inválida! Certifique-se de digitar números corretamente.")
        continue  # Reinicia o loop caso ocorra erro na conversão

    #   Cálculo BMI(BODY MASS INDEX)
    BMI = calculate_BMI(peso, altura)

    #   Avaliação da saúde
    health_condition = evaluate_health(BMI)

    #   Resultado
    print(f"\nNome: {nome}\nIdade: {idade} anos\nPeso: {peso} quilos\nAltura {altura} metros\nIMC: {BMI:.2f}\nCondição de Saúde: {health_condition}")

    while True:
        repeat = input("Deseja continuar? [S/N]: ").strip().upper()
        
        if repeat == "N":
            print("\nObrigado por usar a Calculadora de IMC! Até mais! 👋")
            exit()  # Finaliza o programa completamente
        
        if repeat == "S":
            break  # Sai do loop interno e volta ao início do programa
        
        print("❌ Opção inválida! Digite apenas 'S' ou 'N'.")