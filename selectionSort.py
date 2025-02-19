
listan= [2,4,6,7,8,3,5]
def selecSort(listan):
    n = len(listan)
    for i in range(n):
        min_index = i 
        for j in range (i+1, n):
            if listan[j]< listan[min_index]:
                min_index = j 
        listan[i], listan[min_index] = listan[min_index],listan[i]
    return listan

lista_ordenada = selecSort(listan)
print(lista_ordenada)