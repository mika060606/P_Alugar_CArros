def filtrar_carros(carros, termo_pesquisa='', ordenar=''):
    termo = (termo_pesquisa or '').strip().lower()

    if termo:
        carros = [
            carro
            for carro in carros
            if termo in (getattr(carro, 'modelo', '') or '').lower()
            or termo in (getattr(carro, 'localizacao', '') or '').lower()
            or termo in (getattr(carro, 'descricao', '') or '').lower()
        ]

    if ordenar == 'preco':
        return sorted(carros, key=lambda carro: carro.valor)

    if ordenar == 'nome':
        return sorted(carros, key=lambda carro: (getattr(carro, 'modelo', '') or '').lower())

    return carros
