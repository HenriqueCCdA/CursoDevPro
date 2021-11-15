# TDD da Tombola

Uma tômbola pode ser criada da seguinte maneira:

```python
    >>> from tombola import tombola
    >>> t = tombola.Tombola()

```

Após a criação os itens da tômbola são representados por um lista vazia:

```python
    >>> t.itens
    []

```

Um lista recém criada não possui elementos. Portanto o método "carregada" retorna falso:

```python
    >>> t.carregada()
    False

```

É possível carregar itens através do método "carregar":

```python
    >>> t.carregar([1, 2])
    >>> t.itens
    [1, 2]

```

Após ser carregada o método "carregada" retorna true:

```python
    >>> t.carregada()
    True

```

Uma tômbola pode misturar os seus itens:

```python
    >>> def embaralhador_mock(lista):
    ...     lista[0], lista[-1] = lista[-1], lista[0]
    >>> tombola.shuffle = embaralhador_mock
    >>> t.itens
    [1, 2]
    >>> t.misturar()
    >>> t.itens
    [2, 1]

```

Uma tômbola serve para sortear elementos:

```python
    >>> t.sortear()
    1
    >>> t.carregada()
    True
    >>> t.sortear()
    2
    >>> t.carregada()
    False
    
```