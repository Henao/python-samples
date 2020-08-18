

def binary_search(numbers, number_to_find, low, high):
    
    if low > high:
        return False

    mid = (low + high) / 2

    if numbers[mid] == number_to_find:
        return True

    elif numbers[mid] > number_to_find:
        return binary_search(numbers, number_to_find, low, mid - 1)
    else:
        return binary_search(numbers, number_to_find, mid + 1, high)



if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 25, 27, 28, 34, 36, 49, 51] 

    number_to_find = int(input('Ingresa un número: '))

    binary_search(numbers, number_to_find, 0, len(numbers)- 1) 
    # Se le resta 1 a len(numbers), más que nada porque si no se le restase # se pasaría por parametro la longitud de la lista,
    #  y no el último indice (que es siempre uno menos que la longitud de la lista ya que el primer # indice empieza en 0 y no en 1)
    result = binary_search(numbers, number_to_find, 0, len(numbers)- 1) 

    if result is True:
        print('El número sí está en la lista.')
    else:
        print('El número no está en la lista')