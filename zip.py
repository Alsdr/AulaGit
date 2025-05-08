"""
gabarito = [
    'a', 'b', 'c', 'd', 'e',
    'a', 'b', 'c', 'd', 'e',
    'a', 'b', 'c', 'd', 'e',
    'a', 'b', 'c', 'd', 'e'
]

total = len(gabarito)
"""
minha_resposta = ['a', 'b', 'e', 'b', 'd', 'a', 'e', 'c', 'b', 'd', 'a', 'e', 'c', 'b', 'd', 'a', 'e', 'c', 'b', 'd']

"""
acertos = sum(1 for c, t in zip(gabarito, respostas)if c.lower() == t.lower())
print(f"{acertos}/20")
"""

#if valor1 == valor2
 #   print(f"{valor}/{total}")

def resposta_correta(minha_resposta):
    gabarito = ['a', 'b', 'e', 'b', 'd', 'a', 'e', 'c', 'b', 'd', 'a', 'e', 'c', 'b', 'd', 'a', 'e', 'c', 'b', 'd']
    total = len(gabarito)
    valor = sum(1 for val1, val2 in zip(gabarito, minha_resposta) if val1 == val2)
    porcentagem = (valor / total) * 100
    return f"{valor}/{total} = {porcentagem}%"

print(resposta_correta(minha_resposta))

