import google.generativeai as genai
from planner import gerar_plano_estudos, responder_duvida

GOOGLE_API_KEY = "GOOGLE_API_KEYf"  # substitua pela sua chave real
genai.configure(api_key=GOOGLE_API_KEY)

# Inicializa o modelo
model = genai.GenerativeModel(model_name="models/gemini-2.0-flash")

def menu():
    print("\n--- ChatBot Estudo Python: Arrays ---")
    print("1. Gerar plano de estudos")
    print("2. Tirar dúvida sobre arrays")
    print("3. Sair")

    while True:
        menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            porcentagem = int(input("Quanto você já sabe sobre arrays (0-100)? "))
            plano = gerar_plano_estudos(porcentagem, model)
            print("\n📚 Seu Plano de Estudos:\n", plano)
        elif escolha == "2":
            pergunta = input("Qual a sua dúvida? ")
            resposta = responder_duvida(pergunta, model)
            print("\n💡 Resposta:\n", resposta)
        elif escolha == "3":
            print("Até mais!")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()