import os
from groq import groq

#Defin a chve da API diretamente no código ou garanta que ela esteja configurada corretamente ao ambiente
os.environ ["GROQ_API_KEY"] = "Digite aqui a sua chave de API"

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

# Inicialia a lista de mensagen para manter o contexto da conversa
messages = []

while True:
    usuario = input("Digite uma mensagem ou 'sair' para encerrar: ")

    if usuario.lower() == 'sair':
        print("Conversada encerrada.")
        break

    # Adiciona a mensagem do usuário a lista de mensagens
    messages.append(["role": "user", "content":usuario])

    chat_completion = client.chat.completions.create(
        messages=messages,
        model="llama-3.1-70b-versatile"
    )

    reposta = chat_completion.choices[0].message.content
    print("Resposta:", resposta)

    # Adiciona a aresposta do assistente a lista de mensagens para manter o contexto
    messages.append({"role": "assistant, "content: resposta})