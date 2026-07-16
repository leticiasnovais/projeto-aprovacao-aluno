# Testes gerados com o GitHub Copilot.
# Prompt utilizado: "Crie testes utilizando pytest para a função verificar_aprovacao."

import pytest
from app import verificar_aprovacao


def test_aprovado_com_media_igual_a_sete():
    assert verificar_aprovacao(7, 7) == 'Aprovado'


def test_aprovado_com_media_maior_que_sete():
    assert verificar_aprovacao(8.5, 7.5) == 'Aprovado'


def test_reprovado_com_media_menor_que_sete():
    assert verificar_aprovacao(5, 6) == 'Reprovado'


def test_erro_quando_nota_negativa():
    with pytest.raises(ValueError):
        verificar_aprovacao(-1, 8)


def test_erro_quando_nota_maior_que_dez():
    with pytest.raises(ValueError):
        verificar_aprovacao(10, 10.1)


def test_erro_quando_nota_nao_numerica():
    with pytest.raises(TypeError):
        verificar_aprovacao('8', 9)
