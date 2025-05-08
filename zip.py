gabarito = [
    'a', 'b', 'c', 'd', 'e',
    'a', 'b', 'c', 'd', 'e',
    'a', 'b', 'c', 'd', 'e',
    'a', 'b', 'c', 'd', 'e'
]

total = len(gabarito)
respostas = ['a', 'b', 'e', 'b', 'd', 'a', 'e', 'c', 'b', 'd', 'a', 'e', 'c', 'b', 'd', 'a', 'e', 'c', 'b', 'd']

acertos = sum(1 for c, t in zip(gabarito, respostas)if c.lower() == t.lower())

print(f"{acertos}/20")