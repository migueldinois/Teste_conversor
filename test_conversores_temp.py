import pytest
from conversores_temp import converter_temperatura

#  HAPPY PATCH
@pytest.mark.parametrize("valor, de_escala, para_escala, esperado", [
    (0, "CELSIUS", "FAHRENHEIT", 32.0),
    (100, "CELSIUS", "KELVIN", 373.15),
    (32, "FAHRENHEIT", "CELSIUS", 0.0),
    (212, "FAHRENHEIT", "KELVIN", 373.15),
    (300, "KELVIN", "CELSIUS", 26.85),
    (300, "KELVIN", "FAHRENHEIT", 80.33),
    (25, "celsius", "CELSIUS", 25.0),  
])



def test_conversores_happy_path(valor, de_escala, para_escala, esperado):
    resultado = converter_temperatura(valor, de_escala, para_escala)
    # esse pytest.approx é pra deixar passar pequenas variacoes decimais
    # abs=1e-2 é um parametro para deixar uma margem de erro de 0.01 para tolerar pequenas variações no calculo de float
    assert resultado == pytest.approx(esperado, abs=1e-2)


#  TESTES DE ERRO
@pytest.mark.parametrize("valor, de_escala, para_escala, erro, mensagem", [
    (25, "MIGUEL", "CELSIUS", ValueError, "Escala de temperatura inválida"), 
    (-1, "KELVIN", "CELSIUS",ValueError, "Temperatura em KELVIN não pode ser negativa")


])


def teste_temperatura_erros(valor, de_escala, para_escala, erro, mensagem):
        with pytest.raises(erro, match=mensagem):
            assert converter_temperatura(valor, de_escala, para_escala)


