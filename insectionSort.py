numbers = [3,2,8,6,4,5]

max_lenght = len(numbers)

def inserctionSort(numbers):
    for i in range(1,max_lenght):
        insert_index = numbers[i]
        j = i - 1
        while j >=0 and numbers[j]> insert_index:
            numbers[j+1]=numbers[j]
            j-=1
        numbers[j+1] = insert_index
    return numbers

lista_ordenada = inserctionSort(numbers)
print(lista_ordenada)