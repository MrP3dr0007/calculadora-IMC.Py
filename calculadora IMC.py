# Inicio do código da calculadora de IMC
historico = []


def calcular_imc():
    try:
        nome = input("Digite seu nome: ")
        idade = int(input("Digite sua idade: "))
        peso = float(input("Digite seu peso (kg): ").replace(",", "."))
        altura = float(input("Digite sua altura (m): ").replace(",", "."))
    except ValueError:
        print("❌ Erro: digite valores válidos!")
        return

    imc = peso / (altura ** 2)

    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25:
        classificacao = "Peso normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obesidade"

    print("\n--- Resultado ---")
    print(f"Nome: {nome}")
    print(f"IMC: {imc:.2f}")
    print(f"Classificação: {classificacao}")

    # Salvar no histórico
    historico.append({
        "nome": nome,
        "imc": round(imc, 2),
        "classificacao": classificacao
    })


def ver_historico():
    if not historico:
        print("📭 Nenhum dado no histórico.")
        return

    print("\n=== Histórico ===")
    for pessoa in historico:
        print(
            f"{pessoa['nome']} | IMC: {pessoa['imc']} | {pessoa['classificacao']}")


def main():
    while True:
        print("\n=== MENU ===")
        print("1 - Calcular IMC")
        print("2 - Ver histórico")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            calcular_imc()
        elif opcao == "2":
            ver_historico()
        elif opcao == "3":
            print("Saindo do sistema...")
            break
        else:
            print("❌ Opção inválida!")


if __name__ == "__main__":
    main()

# Fim do código da calculadora de IMC
