 # Sistema de Cadrastro e Verificação de Empre3stimos - terminal

# 1. ** Cadastrar e Armazenar Usuarios:**
# Permite que o usuario insira seu nome, idade,renda mensal, histórico de créditos e armazenar em um diiconario.

def cadastrar_usuario(usuarios):
    nome = input("digite o nome do usuario")
    idade = int(input("digite a idade do usuario"))
    renda_mensal = float(input ("digite a rendea do usuwrio"))
    historico__creditos = input("digite se o usuario tem créditos")

    usuarios[nome] = {
        "idade":idade,
        "renda-mensal":renda_mensal,
        "historico_renda":historico__creditos,

    }

    print(f"\n Usuário{nome}Cadastrado com sucesso!")



    

# 2. ** |Verificação de Elegibilidade:**
#  Usa operadores relacionais e lógicos para verificar se o usuário é elegivel para um empréstimo.
# Condições para ser elegivel idade maior de 18, renda maior que 1000 e histórico de credito exitente.

def elegibilidade(usuarios):

    nome = input("Digite o nome para a consulta de elegibilidade")

    if nome in usuarios:
        usuario_info = usuarios[nome]
        if usuario_info["idade"] >= 18 and usuario_info["renda_mensal"] >=1000 and usuario_info["histórico_creditos"] == "sim":
           print(f"\n {nome}é elegivel para um empréstimo")

        else:
            print(f"\n{nome}não é elegível par4a um empréstimo.")
            
    else:
        print("\n Ususário não Cadastrado")



# 3. **Exibição do usuários:**
#  Retorna todas as informações cadastradas de um unico usuário.

def exibir_usuario (usuarios):
    nome = input("Digite o nome do usário:")

    if nome in usuarios:
        usuario_info = usuarios[nome]
        print(f"Idade: {usuario_info["idade"]}")
        print(f"Renda mensal: {usuario_info["historico_credito"]}")
        print(f"Histórico de Credito: {usuario_info["historico_credito"]}")
    else:
        print("/n Usuario não Cadastrado.")



# 4. ** Exibe o número total de usuaros e os nomes dos usuários.
def exibir_usuarios(usuarios):
    print(f"\nNúmero total de usuários cadastrados:{len[usuarios]}")
    for nome in usuarios.keys():
        print(f" - {nome}")


def main():
    usuarios = {}

    while True:
        print("\n Sistma de Cadastro e Verificação de Empréstimo")
        print("\n 1. Cadastrar Usu´qario")
        print("\n 2. Verificqar Elegibilidade")
        print("\n 3. Exibir dados do Usuário")
        print("\n 4. Exibir Total de Usuários e seus nomes")
        print("\n 5. Sair do Sistema")

        opcao = int(input("Escolha a sua opção"))

        if opcao == 1:
            cadastrar_usuario(usuarios)
        elif opcao == 2:
            elegibilidade(usuarios)
        elif opcao == 3:
            exibir_usuario(usuarios)
        elif opcao == 4:
            exibir_usuarios(usuarios)
        elif opcao == 5:
            print("Saindo do Sistema\n")
            break
        else: 
            print("Opção inválida, tente novamente")
main()
