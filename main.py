def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


def ler_numeros_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as file:
        conteudo = file.read()
    
    numeros = [int(num) for num in conteudo.split() if num.isdigit()]
    return numeros


nome_arquivo = input("Digite o nome do arquivo com extensão (ex: numeros.txt): ")
numeros = ler_numeros_arquivo(nome_arquivo)

print("Números antes da ordenação:", numeros)
merge_sort(numeros)
print("Números após a ordenação:", numeros)
