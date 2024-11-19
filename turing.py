def resumo():
    mensagem = "Alan Mathison Turing  foi um matemático britânico, pioneiro da computação e considerado o pai da ciência computacional e da inteligência artificial."
    return mensagem


def doutorado():
    mensagem = "Entre 1936 e 1938, estudou matemática e criptografia em Princeton, local em que obteve seu PhD"
    return mensagem


def contribuicoes():
    mensagem = "A sua maior contribuição, foi a Maquina de Turing, tendo outros projetos como: Sistema Bombe, Conceito de Jogo aa imitaçao, Bases de computação moderna, e etc."
    return mensagem


def artigos():
    mensagem = "Alan Turing escreveu vários artigos, entre os quais: \nUm artigo publicado na revista IEEE Annals of the History of Computing que revisa fontes históricas e apresenta evidências de que Turing variou o design de seus testes de inteligência. \n Um artigo acadêmico de 1936 em que Turing desenvolve uma máquina automática que podia ler e escrever diferentes números e símbolos. \nUm artigo em que Turing apresenta um modelo teórico de computador e propõe o jogo da imitação, que hoje é conhecido como Teste de Turing. "
    return mensagem


def citacoes():
    mensagem = ""
    return mensagem


def sair():
    mensagem = "\nObrigado pela leitura!"
    return mensagem


def erro():
    mensagem = "\nOpção inválida!"
    return mensagem


print("\nBoa noite! Você está aprendendo sobre Allan Turing.\n")

continuar = True
while continuar == True:

    opcao = int(
        input(
"""
\nDigite o número correspondente ao menu que você deseja acessar:
1 - Resumo
2 - Doutorado
3 - Contribuições
4 - Principais Artigos
5 - Citações
6 - Sair\n
"""
        )
    )

    if opcao == 1:
        print("1 - Resumo")
        mensagem = resumo()

    elif opcao == 2:
        print("2 - Doutorado")
        mensagem = doutorado()

    elif opcao == 3:
        print("3 - Contribuições")
        mensagem = contribuicoes()

    elif opcao == 4:
        print("4 - Principais Artigos")
        mensagem = artigos()

    elif opcao == 5:
        print("5 - Citações")
        mensagem = citacoes()

    elif opcao == 6:
        mensagem = sair()
        continuar = False

    else:
        mensagem = erro()

    print(mensagem)
