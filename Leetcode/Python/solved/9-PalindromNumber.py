#9)-Palindrom Number
'''
Dado un entero x, devuelve True si x es un palíndromo, y False de otro modo.


Ejemplo 1:

Entrada: x = 121
    Salida: True
    Explicación: 121 se lee como 121 de izquierda a derecha y de derecha a izquierda.
Ejemplo 2:

Entrada: x = -121
    Salida: False
    Explicación: De izquierda a derecha, se lee -121. De derecha a izquierda, se convierte en 121-. Por lo tanto, no es un palíndromo.
Ejemplo 3:

Entrada: x = 10
    Salida: False
    Explicación: Lee 01 de derecha a izquierda. Por lo tanto, no es un palíndromo.

Restricciones:

-231 <= x <= 231 - 1

'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
solve = Solution()
print(solve.isPalindrome(121))
