# -*- coding: utf-8 -*-
import sys

KEYS = {
    'a': 'w',
    'b': 'E',
    'c': 'x',
    'd': '1',
    'e': 'a',
    'f': 't',
    'g': '0',
    'h': 'C',
    'i': 'b',
    'j': '!',
    'k': 'z',
    'l': '8',
    'm': 'M',
    'n': 'I',
    'o': 'd',
    'p': '.',
    'q': 'U',
    'r': 'Y',
    's': 'i',
    't': '3',
    'u': ',',
    'v': 'J',
    'w': 'N',
    'x': 'f',
    'y': 'm',
    'z': 'W',
    'A': 'G',
    'B': 'S',
    'C': 'j',
    'D': 'n',
    'E': 's',
    'F': 'Q',
    'G': 'o',
    'H': 'e',
    'I': 'u',
    'J': 'g',
    'K': '2',
    'L': '9',
    'M': 'A',
    'N': '5',
    'O': '4',
    'P': '?',
    'Q': 'c',
    'R': 'r',
    'S': 'O',
    'T': 'P',
    'U': 'h',
    'V': '6',
    'W': 'q',
    'X': 'H',
    'Y': 'R',
    'Z': 'l',
    '0': 'k',
    '1': '7',
    '2': 'X',
    '3': 'L',
    '4': 'p',
    '5': 'v',
    '6': 'T',
    '7': 'V',
    '8': 'y',
    '9': 'K',
    '.': 'Z',
    ',': 'D',
    '?': 'F',
    '!': 'B',
}

def cypher(message):
    words = message.split(' ')
    print(words)
    #split convierte una cadena de texto en una lista. Por defecto, los elementos de dicha lista serán las palabras de la cadena.
    cypher_message = []

    for word in words:
        print(word)
        cypher_word = ''
        for letter in word:
            print(letter)
            cypher_word += KEYS[letter]
            print(cypher_word)

        cypher_message.append(cypher_word)
        print(cypher_message)

    return 'cifrado: ' + ' '.join(cypher_message)
    #La función join convierte una lista en una cadena formada por los elementos de la lista separados por comas. 

def decypher(message):
    words = message.split(' ')
    print(words)
    decypher_message = []

    for word in words:
        print(word)
        decypher_word = ''
        for letter in word:
            print(letter)
            for key, value in KEYS.items():
                if value == letter:
                    decypher_word += key
                    print(decypher_word)

        decypher_message.append(decypher_word)
        print(decypher_message)

    return 'descifrado: ' + ' '.join(decypher_message)


def run():

    while True:

        command = str(input('''--- * --- * --- * --- * --- * --- * --- * ---

            Bienvenido a criptografía. ¿Qué deseas hacer?

            [c]ifrar mensaje
            [d]ecifrar mensaje
            [s]alir
        '''))

        if command == 'c':
            message = str(input('Escribe un mensaje: '))
            cypher_message = cypher(message)
            print(cypher_message)

        elif command == 'd':
            message = str(input('Escribe tu mensaje cifrado: '))
            decypher_message = decypher(message)
            print(decypher_message)

        elif command == 's':
            salir = str(input('estas seguro ? s / n:' ))
            if salir == 's':
                sys.exit()
            else:
                run()
            print('salir')
            break
        else:
            print('¡Comando no encontrado!')


if __name__ == '__main__':
    print('M E N S A J E S  C I F R A D O S')
    run()