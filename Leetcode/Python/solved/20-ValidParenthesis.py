#20. Paréntesis válidos
'''
Dada una cadena sque contiene sólo los caracteres '(', ')', '{', '}'y , determine si la cadena '['de ']'entrada es válida.

Una cadena de entrada es válida si:

Los corchetes abiertos deben cerrarse con el mismo tipo de corchetes.
Los corchetes abiertos deben cerrarse en el orden correcto.
Cada corchete cerrado tiene un corchete abierto correspondiente del mismo tipo.

Ejemplo 1:

Entrada: s = "()"
    Salida: verdadero
Ejemplo 2:

Entrada: s = "()[]{}"
    Salida: verdadero
Ejemplo 3:

Entrada: s = "(]"
    Salida: falso

Restricciones:

1 <= s.length <= 104
sconsta únicamente de paréntesis '()[]{}'
'''
class Solution:
    def isValid(self, s: str) -> bool:
        open = ["(","{","["]
        close = [")","}","]"]
        if len(s)%2 > 0:
            return False
        def parentheses(s,visited="",current=s[0]):
            if len(s) == 0:
                if len(visited) > 0:
                    return False
                return True
            else:
                if len(visited) == 0 or s[0] in open:
                    current = s[0]
                    visited += current
                    return parentheses(s[1:], visited,current)
                elif (s[0] in close):
                    if current in open and s[0] in close:
                        if (open.index(current) == close.index(s[0])):
                            visited += s[0]
                            if len(visited) >=3:
                                visited = visited[:-2]
                                current = visited[-1] if visited[-1] in open else ""
                            elif len(visited) == 2:
                                visited = ""
                        else: 
                            return False
                    else:
                        return False
                    return parentheses(s[1:],visited,current)
                else:
                    return False

        return parentheses(s)
x = Solution()
x.isValid("(){}[[[({})]]]")