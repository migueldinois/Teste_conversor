def converter_temperatura(valor: float, de_escala: str, para_escala: str) -> float:
    """
    Converte valores de temperatura entre as escalas CELSIUS, FAHRENHEIT e KELVIN.
    
    :param valor: Valor da temperatura (int ou float).
    :param de_escala: Escala de origem ("CELSIUS", "FAHRENHEIT", "KELVIN").
    :param para_escala: Escala de destino ("CELSIUS", "FAHRENHEIT", "KELVIN").
    :return: Valor da temperatura convertida como float.
    """
    # Escalas válidas suportadas
    escalas_validas = {"CELSIUS", "FAHRENHEIT", "KELVIN"}
    
    # Padronização para maiúsculas
    de_escala = de_escala.upper()
    para_escala = para_escala.upper()
    
    # 1. Validação de Escalas
    if de_escala not in escalas_validas or para_escala not in escalas_validas:
        raise ValueError("Escala de temperatura inválida")
    
    # 2. Validação de Valor
    if de_escala == "KELVIN" and valor < 0:
        raise ValueError("Temperatura em KELVIN não pode ser negativa")
    
    # 4. Caso as escalas sejam iguais
    if de_escala == para_escala:
        return float(valor)
    
    # 3. Lógica de Conversão
    # Primeiro converte qualquer escala de origem para CELSIUS
    if de_escala == "FAHRENHEIT":
        celsius = (valor - 32) * 5 / 9
    elif de_escala == "KELVIN":
        celsius = valor - 273.15
    else:  # de_escala == "CELSIUS"
        celsius = valor

    # Agora converte de CELSIUS para a escala de destino
    if para_escala == "FAHRENHEIT":
        return celsius * 9 / 5 + 32
    elif para_escala == "KELVIN":
        return celsius + 273.15
    else:  # para_escala == "CELSIUS"
        return celsius