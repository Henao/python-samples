"""
"abacabad" c
"abacabaabacaba" _
"abcdefghijklmnopqrstuvwxyziflskecznslkjfabe" d
"bcccccccccccccyb" y
"""

def first_not_repeating_char(char_sequence):
    seen_letters = {}

# Hago iteración en char_sequence que se convierte en una tupla por la función enumerate
# Luego verifico si cada letra esta o no en el diccionario seen_letters
# Si la letra no esta, la agrego
    for idx, letter in enumerate(char_sequence):
        if letter not in seen_letters:
            #sintaxis de diccionario y llave donde la letra es la llave y como valor una tupla
            seen_letters[letter] = (idx, 1)
        else:
            seen_letters[letter] = (seen_letters[letter][0], seen_letters[letter][1] + 1)

            # seen_letters se vería así  para este valor -> "abacabac"
            # {
            #   'a' : (0, 4),
            #   'b' : (1, 2),
            #   'c' : (3, 1),        
            # }
    final_letters = []
    for key, value in seen_letters.items():
        if value[1] == 1:
            final_letters.append((key, value[0]))
        #"abacabac"
        # lista de tuplas
        # [('a', 0),('d' ,7 )]

    not_repeated_letters = sorted(final_letters, key=lambda value: value[1])    
# otra forma
# def sort_order(value):
#     return value[1]
    if not_repeated_letters:
        return not_repeated_letters[0][0]
    else:
        return '_'


if __name__ == '__main__':
    char_sequence = str(input('Escribe una secuencia de caracteres: '))

    result = first_not_repeating_char(char_sequence)

    if result == '_':
        print('Todos los caracteres se repiten.')
    else:
        print('El primer caracter no repetido es: {}'.format(result))

