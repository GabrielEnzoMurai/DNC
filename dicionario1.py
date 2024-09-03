dicio = {
    'nome': 'Gabriel',
    'idade': 21,
    'cidade': 'SCS'
}
dicio['nome'] = 'Enzo'
dicio['peso'] = 65
print(dicio['nome'])
print(dicio['idade'])
print(dicio['cidade'])
print(dicio['peso'])
print(dicio)
print(dicio.values())
print(dicio.keys())
print(dicio.items())
del dicio['peso']
print(dicio)