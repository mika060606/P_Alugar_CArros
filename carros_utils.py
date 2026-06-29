def _coerce_int(value):
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def filtrar_carros(carros, termo_pesquisa='', ordenar='', filtros=None):
    termo = (termo_pesquisa or '').strip().lower()
    filtros = filtros or {}
    carros_filtrados = list(carros)

    if termo:
        carros_filtrados = [
            carro
            for carro in carros_filtrados
            if termo in (getattr(carro, 'modelo', '') or '').lower()
            or termo in (getattr(carro, 'localizacao', '') or '').lower()
            or termo in (getattr(carro, 'descricao', '') or '').lower()
        ]

    min_preco = filtros.get('min_preco')
    if min_preco not in (None, ''):
        min_preco = float(min_preco)
        carros_filtrados = [carro for carro in carros_filtrados if getattr(carro, 'valor', 0) >= min_preco]

    max_preco = filtros.get('max_preco')
    if max_preco not in (None, ''):
        max_preco = float(max_preco)
        carros_filtrados = [carro for carro in carros_filtrados if getattr(carro, 'valor', 0) <= max_preco]

    ano = _coerce_int(filtros.get('ano'))
    if ano is not None:
        carros_filtrados = [
            carro for carro in carros_filtrados
            if _coerce_int(getattr(carro, 'ano', None)) == ano
        ]

    modelo = (filtros.get('modelo') or '').strip().lower()
    if modelo:
        carros_filtrados = [
            carro for carro in carros_filtrados
            if modelo in (getattr(carro, 'modelo', '') or '').lower()
        ]

    localidade = (filtros.get('localidade') or '').strip().lower()
    if localidade:
        carros_filtrados = [
            carro for carro in carros_filtrados
            if localidade in (getattr(carro, 'localizacao', '') or '').lower()
        ]

    classificacao = (filtros.get('classificacao') or '').strip().lower()
    if classificacao:
        carros_filtrados = [
            carro for carro in carros_filtrados
            if classificacao in (getattr(carro, 'classificacao', '') or '').lower()
        ]

    if ordenar == 'preco':
        return sorted(carros_filtrados, key=lambda carro: carro.valor)

    if ordenar == 'nome':
        return sorted(carros_filtrados, key=lambda carro: (getattr(carro, 'modelo', '') or '').lower())

    return carros_filtrados
