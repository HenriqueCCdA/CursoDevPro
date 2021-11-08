'''
>>> app = Flask()
>>> set(app.rotas)
set()
>>> @app.rota('/')
... def raiz():
...     return 'raiz'
...
>>> set(app.rotas)
{'/'}
>>> raiz()
'raiz'
>>> app.executar('/')
'raiz'
>>> @app.rota('/home')
... def nome(usuario):
...     return f'Nome: {usuario}'
...
>>> list(app.rotas)
['/', '/home']
>>> nome('Python')
'Nome: Python'
>>> app.executar('/home', 'Pro')
'Nome: Pro'
>>> app.executar('/nao_existe')
404
'''

class Flask():
    def __init__(self):
        self.rotas = dict()

    def rota(self, path):
        def decorator(f):
            self.rotas[path] = f
            return f
        return decorator

    def executar(self, path, *args, **kwargs):
        if path not in self.rotas:
            return 404
        f = self.rotas[path]
        return f(*args, **kwargs)
    