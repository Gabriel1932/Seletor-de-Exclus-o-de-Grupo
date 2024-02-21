import random

def remover_nomes(lista_nomes, quantidade):
    # Verifica se a quantidade fornecida é válida
    if quantidade >= len(lista_nomes):
        print("A quantidade fornecida é maior ou igual ao tamanho da lista. Nenhum nome será removido.")
        return lista_nomes

    # Remove aleatoriamente a quantidade especificada de nomes
    nomes_removidos = random.sample(lista_nomes, quantidade)
    for nome in nomes_removidos:
        lista_nomes.remove(nome)

    # Imprime os nomes removidos
    print(f"Nomes removidos: {nomes_removidos}")

    return lista_nomes

# Exemplo de uso
lista_nomes = ["Gabriel", "Deyvid", "Carlos", "Jorge", "Igor", "Natan", "Jacson", "Arthur"]
quantidade_a_remover = int(input("Quantos nomes você quer remover? "))

lista_nomes_atualizada = remover_nomes(lista_nomes, quantidade_a_remover)

print("Lista atualizada:", lista_nomes_atualizada)
