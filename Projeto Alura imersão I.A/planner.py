from prompt_templates import prompt_plano_estudos, prompt_duvida

def gerar_plano_estudos(porcentagem: int, model):
    prompt = prompt_plano_estudos.format(porcentagem=porcentagem)
    response = model.generate_content(prompt)
    return response.text

def responder_duvida(pergunta: str, model):
    prompt = prompt_duvida.format(pergunta=pergunta)
    response = model.generate_content(prompt)
    return response.text
