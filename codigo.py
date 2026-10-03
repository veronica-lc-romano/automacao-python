import pyautogui
import time
import pandas

# Passo 1: Entrar no sistema da empresa
pyautogui.PAUSE=1

link="https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.press("win")

pyautogui.write("chrome")

pyautogui.press("enter")

pyautogui.write(link)

pyautogui.press("enter")


# Passo 2: Fazer Login
## pausa para o site carregar
time.sleep(3)

## clicar no campo de email
pyautogui.click(x=402, y=373)

## digitar o email
pyautogui.write("pythonimpressionador@gmail.com")

## ir para o campo senha
pyautogui.press("tab")

## digitar a senha
pyautogui.write("pythonimpressionadorsenha")

## ir para o botão login
pyautogui.press("tab")

## apertar o botão login
pyautogui.press("enter")



# Passo 3: Abrir a base de dados (importr o arquivo)    Philco
## aguardar o site carregar
time.sleep(3)

tabela = pandas.read_csv("./Aula1/produtos.csv") 

print(tabela)

# Passo 4: Cadastrar 1 produto
for linha in tabela.index:
    ## clicar no campo 'produto'
    pyautogui.click(x=480, y=254)
    codigo = str(tabela.loc[linha, "codigo"])
    ## informar produto
    pyautogui.write(codigo)

    ## ir para o próximo campo
    pyautogui.press("tab")

    marca = str(tabela.loc[linha, "marca"])
    ## informar marca
    pyautogui.write(marca)

    ## ir para o próximo campo
    pyautogui.press("tab")

    tipo = str(tabela.loc[linha, "tipo"]  )
    ## informar tipo
    pyautogui.write(tipo)

    ## ir para o próximo campo
    pyautogui.press("tab")

    categoria = str(tabela.loc[linha, "categoria"])
    ## informar categoria
    pyautogui.write (categoria)

    ## ir para o próximo campo
    pyautogui.press("tab")

    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    ## informar preco
    pyautogui.write(preco_unitario)

    ## ir para o próximo campo
    pyautogui.press("tab")

    custo = str(tabela.loc[linha, "custo"])
    ## informar custo
    pyautogui.write(custo)

    ## ir para o próximo campo
    pyautogui.press("tab")

    obs = str(tabela.loc[linha, "obs"])
    ## informar observação
    if obs != "nan":
        pyautogui.write(obs)

    ## ir para o botão
    pyautogui.press("tab")

    ## salvar o produto
    pyautogui.press("enter")
   
    # Passo 5: Repetir o paso 4 até o fim da lista
    ## aguardar o site carregar
    time.sleep(3)

    ## voltar ao início da tela
    pyautogui.scroll(5000)

