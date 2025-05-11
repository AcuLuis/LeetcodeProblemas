def isValid(s: str):
    pila = []
    signos = {")": "(", "}": "{", "]": "["}
    
    for c in s:
        if c in signos.values():
            pila.append(c)
        elif c in signos.keys():
            if not pila or signos[c] != pila.pop():
                return False
        else:
            return False 
    return not pila

print(isValid("[]"))
