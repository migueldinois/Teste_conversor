# Conversor de Temperatura

Este projeto implementa uma função em Python para converter valores de temperatura entre as escalas Celsius, Fahrenheit e Kelvin.

## Descrição

A função `converter_temperatura(valor, de_escala, para_escala)` recebe:

- `valor`: número a ser convertido;
- `de_escala`: escala de origem;
- `para_escala`: escala de destino.

Ela realiza a conversão e valida entradas inválidas, como escalas desconhecidas ou temperatura em Kelvin negativa.

## Escalas suportadas

- Celsius (`CELSIUS`)
- Fahrenheit (`FAHRENHEIT`)
- Kelvin (`KELVIN`)

## Fórmulas usadas

A conversão é feita a partir da escala de origem para Celsius e, em seguida, para a escala de destino.

- Celsius -> Fahrenheit:
  `F = C * 9 / 5 + 32`
- Celsius -> Kelvin:
  `K = C + 273.15`
- Fahrenheit -> Celsius:
  `C = (F - 32) * 5 / 9`
- Kelvin -> Celsius:
  `C = K - 273.15`

## Como usar

```python
from conversores_temp import converter_temperatura

print(converter_temperatura(0, "CELSIUS", "FAHRENHEIT"))  # 32.0
print(converter_temperatura(100, "CELSIUS", "KELVIN"))    # 373.15
print(converter_temperatura(212, "FAHRENHEIT", "KELVIN")) # 373.15
```

## Validações

A função lança `ValueError` quando:

- a escala informada não é válida;
- a temperatura em Kelvin for menor que zero.

## Testes

O projeto inclui testes automatizados com `pytest` para verificar conversões válidas e erros esperados.

Para executar os testes:

```bash
pytest
```

## Estrutura do projeto

```text
.
├── conversores_temp.py
├── test_conversores_temp.py
├── README.md
└── __pycache__/
```

## Observações

O código foi implementado de forma simples e didática, priorizando clareza e validação de entradas para uso em exercícios de programação e aprendizado de Python.
