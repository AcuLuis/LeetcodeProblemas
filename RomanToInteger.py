
def romanToInt(s):
    numero_final = 0
    anterior = 0
    for x in s[::-1]:
        actual = 0
        match(x):
            case "I": actual = 1 
            case "V": actual = 5
            case "X": actual = 10
            case "L": actual = 50
            case "C": actual = 100
            case "D": actual = 500
            case "M": actual = 1000
        if actual >= anterior:
            numero_final+=actual
        else:
            numero_final-=actual
        anterior=actual
    return numero_final