# Gerado com o GitHub Copilot.
# Prompt utilizado: "Crie uma função em Python chamada verificar_aprovacao que receba duas notas,  valide se estão entre 0 e 10, calcule a média e retorne 'Aprovado' para média maior ou igual a 7 e 'Reprovado' caso contrário."

"""Verificador de aprova��o de aluno.

Fun��es:
- verificar_aprovacao(nota1, nota2): retorna 'Aprovado' ou 'Reprovado'.

Regras:
- notas devem estar entre 0 e 10.
- m�dia >= 7 => Aprovado.
- m�dia < 7 => Reprovado.
"""

def verificar_aprovacao(nota1, nota2):
    """Verifica se o aluno est� aprovado com base em duas notas."""
    for nota in (nota1, nota2):
        if not isinstance(nota, (int, float)):
            raise TypeError('As notas devem ser n�meros.')
        if nota < 0 or nota > 10:
            raise ValueError('Notas devem estar entre 0 e 10.')

    media = (nota1 + nota2) / 2
    return 'Aprovado' if media >= 7 else 'Reprovado'
