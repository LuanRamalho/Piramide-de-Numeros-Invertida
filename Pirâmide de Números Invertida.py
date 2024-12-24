# Solicitar o número de linhas ao usuário
print("Quantas linhas você deseja?")
no_of_rows = int(input())

row_count = no_of_rows
print("Aqui está sua pirâmide:")

for i in range(no_of_rows):
    # Imprimir espaços
    for j in range(i * 2):
        print(" ", end="")
    
    # Imprimir números crescentes
    for j in range(1, row_count + 1):
        print(j, end=" ")
    
    # Imprimir números decrescentes
    for j in range(row_count - 1, 0, -1):
        print(j, end=" ")
    
    print()  # Quebra de linha após cada linha
    row_count -= 1
input()