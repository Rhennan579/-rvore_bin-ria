import matplotlib.pyplot as plt

def menu():
    lista = [1,2,4,6,9,12,15,23,19,27,32,17,76,29,91,102,54,82]

    while True:
        print("\n====== MENU ======")
        print("1 - Inserir número")
        print("2 - Listar números")
        print("3 - Atualizar número")
        print("4 - Remover número")
        print("5 - Buscar número (binária)")
        print("6 - Plotar árvore balanceada")
        print("0 - Sair")

        opc = input("\nEscolha: ")

        if opc == "1":
            try:
                num = int(input("Digite o número para adicionar: "))
                lista.append(num)
                lista.sort()
                print("Número adicionado!")
            except:
                print("Valor inválido.")

        elif opc == "2":
            print("\nLista atual:", lista)

        elif opc == "3":
            try:
                velho = int(input("Número que deseja alterar: "))
                if velho not in lista:
                    print("Número não encontrado!")
                else:
                    novo = int(input("Novo valor: "))
                    lista[lista.index(velho)] = novo
                    lista.sort()
                    print("Número atualizado!")
            except:
                print("Valor inválido.")

        elif opc == "4":
            try:
                num = int(input("Número para remover: "))
                if num in lista:
                    lista.remove(num)
                    print("Número removido!")
                else:
                    print("Número não está na lista.")
            except:
                print("Valor inválido.")

        elif opc == "5":
            try:
                buscar = int(input("Digite o número para buscar: "))
                if not lista:
                    print("Lista vazia!")
                else:
                    try:
                        idx = arvore(lista, buscar)
                        print(f"Encontrado no índice {idx}")
                    except:
                        print("Número não encontrado (fora da lista).")
            except:
                print("Valor inválido.")

        elif opc == "6":
            if not lista:
                print("Lista vazia!")
            else:
                raiz = construir_balanceada(lista)
                plotar_arvore(raiz)

        elif opc == "0":
            break

        else:
            print("Opção inválida!")



def arvore(lista_numeros, entrada, log=0):
    if not lista_numeros:
        raise ValueError("Não encontrado")

    dividir = len(lista_numeros) // 2

    if lista_numeros[dividir] == entrada:
        return dividir + log

    if lista_numeros[dividir] > entrada:
        return arvore(lista_numeros[:dividir], entrada, log)
    else:
        return arvore(lista_numeros[dividir+1:], entrada, dividir + log + 1)



class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esq = None
        self.dir = None


def construir_balanceada(nums):
    if not nums:
        return None
    meio = len(nums) // 2
    raiz = Node(nums[meio])
    raiz.esq = construir_balanceada(nums[:meio])
    raiz.dir = construir_balanceada(nums[meio+1:])
    return raiz


def coletar_posicoes(node, x=0, y=0, nivel=1, pos=None):
    if pos is None:
        pos = {}

    if node:
        pos[node] = (x, y)
        deslocamento = 1 / (2 ** nivel)
        coletar_posicoes(node.esq, x - deslocamento, y - 1, nivel + 1, pos)
        coletar_posicoes(node.dir, x + deslocamento, y - 1, nivel + 1, pos)

    return pos


def plotar_arvore(raiz):
    pos = coletar_posicoes(raiz)
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.set_axis_off()

    for node, (x, y) in pos.items():
        if node.esq:
            x2, y2 = pos[node.esq]
            ax.plot([x, x2], [y, y2], color="gray")
        if node.dir:
            x2, y2 = pos[node.dir]
            ax.plot([x, x2], [y, y2], color="gray")

    for node, (x, y) in pos.items():
        ax.scatter(x, y, s=400, color="#835F9B")
        ax.text(x, y, str(node.valor), ha='center', va='center', color='black', fontsize=14)

    plt.title("Árvore Binária de Busca")
    plt.show()


menu()
