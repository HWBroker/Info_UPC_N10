"""
Aquesta funció només retorna un enter positiu.
Si el usuari posa un decimal, un negatiu o alguna lletra, 
el programa li demanarà que ho torni a intentar.

Utilitzar aquesta funció en més de `int(input())` evita que el programa
doni un error de parse o que tinguis errors més tard.
"""
 
def llegir_enter_positiu():
    while True:
        try:
            i = int(input())
            if i > 0:
                return i
            else:
                print('No es un enter positiu. Torna-ho a intentar')
        except ValueError:
            print('No es un enter positiu. Torna-ho a intentar')
            continue
