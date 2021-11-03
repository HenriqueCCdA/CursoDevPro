import operator

alunos = [('Renzo', 0), ('Luciano', 10), ('Ada', 9)]

print([(nome, nota) for nome, nota in alunos if nota > 5])

def possui_nota_mario_que_5(aluno):
    _, nota = aluno
    return nota > 5

print(list(filter(possui_nota_mario_que_5, alunos)))


def extrair_nome(aluno):
    nome, _ = aluno
    return nome

print([nome for nome, nota in alunos if nota > 5])
print(list(map(extrair_nome, filter(possui_nota_mario_que_5, alunos))))
print(list(map(operator.itemgetter(0), filter(possui_nota_mario_que_5, alunos))))

