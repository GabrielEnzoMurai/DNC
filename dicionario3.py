pessoas = [
    {'nome': 'Gabriel', 'idade': 21, 'cidade': 'SCS'},
    {'nome': 'Helena', 'idade': 21, 'cidade': 'Osasco'},
    {'nome': 'Carlos', 'idade': 40, 'cidade': 'Belém'},
]

for p in pessoas:
    for i, v in p.items():
        print(f'{i}: {v} ')
    print()