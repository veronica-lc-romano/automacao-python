mensagem1 = {"role": "assistant", "content": "Bora aprender python?"}
mensagem2 = {"role": "user", "content": "Sim, bora aprender!"}
mensagem3 = {"role": "assistant", "content": "Então vamos começar a aula!"}

lista_mensagens = [mensagem1, mensagem2, mensagem3]

nova_mensagem = {"role": "user", "content": "Então vamos lá!"}
lista_mensagens.append(nova_mensagem)

print(lista_mensagens)