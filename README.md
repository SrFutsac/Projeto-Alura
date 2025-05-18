
# Projeto
![ChatGPT Image 17 de mai  de 2025, 21_49_10](https://github.com/user-attachments/assets/bb2a5ea5-a0dd-4385-9d5a-a3b0edf0b029)
-Alura
🤖 ChatBot Planejador de Estudos em Python - Arrays
Este projeto é um chatbot interativo desenvolvido em Python que utiliza a API do Google Gemini (models/gemini-2.0-flash) para ajudar iniciantes a aprender sobre arrays (listas em Python).

🔍 Funcionalidades
Gerar Plano de Estudos Personalizado
Com base no nível de conhecimento informado pelo usuário (de 0 a 100%), o bot gera um plano prático com conceitos, exemplos e exercícios.

Resolução de Dúvidas Didáticas
O usuário pode fazer perguntas sobre arrays e receber respostas claras, além de sugestões de mini projetos para praticar.

🛠️ Tecnologias e Bibliotecas
Python 3

Google Generative AI (google-generativeai==0.4.1)

🚀 Como Executar
Instale as dependências:

bash
Copiar
Editar
pip install -r requirements.txt
Substitua GOOGLE_API_KEYf pela sua chave de API no arquivo main.py.

Execute o chatbot:

bash
Copiar
Editar
python main.py
📁 Estrutura do Projeto
main.py: Interface principal do chatbot.

planner.py: Funções para geração de plano e respostas.

prompt_templates.py: Templates de prompts usados para interagir com a IA.

requirements.txt: Dependências do projeto.
