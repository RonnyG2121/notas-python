""" Este ejercicio trata de encontrar si una palabra es un isograma.
Un isograma es una palabra que no tienes letras repetitivas.
 """


def palabra_isograma(palabra):
    for letra in palabra:
        if letra in palabra:
            return False
    return True

frase = input("Ingrese una palabra")
# print(palabra_isograma(frase))


def is_isograma(word):
    obj_words = {}
    for e in word:
        print(obj_words)
        if e in obj_words:
            obj_words[e] += 1
        else:
            obj_words[e] = 1
    return all(e % 2 == 0 or e == 1 for e in obj_words.values())

print(is_isograma(frase))