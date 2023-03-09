# Definir uma função que inverte um string
def inverter_string(s):

    resultado = ""
    

    for i in range(len(s)-1, -1, -1):
        resultado += s[i]  
    return resultado

string_original = "Exemplo de string para inverter"
string_invertida = inverter_string(string_original)
print(string_invertida) 