def calculate_risk_score(country, product, exchange_risk=None, logistics_risk=None, regulatory_risk=None):
    """
    Calcula un puntaje de riesgo basado en varios factores.
    
    Args:
        country (str): País para el análisis
        product (str): Producto para el análisis
        exchange_risk (float, optional): Riesgo cambiario (0-1)
        logistics_risk (float, optional): Riesgo logístico (0-1)
        regulatory_risk (float, optional): Riesgo regulatorio (0-1)
    
    Returns:
        float: Puntaje de riesgo total (0-100)
    """
    # Por ahora usamos valores predeterminados simples
    # En una implementación real, estos valores vendrían de un análisis más profundo
    base_risk = 50  # Riesgo base medio
    
    # Ajustes por país (simplificado)
    country_risk = {
        'EEUU': -10,
        'China': 5,
        'Brasil': 0,
        'Argentina': 10,
        'Chile': -5,
        'México': 0
    }
    
    # Ajustes por producto (simplificado)
    product_risk = {
        'Soja': 5,
        'Maíz': 0,
        'Trigo': -5,
        'Arroz': 0,
        'Carne': 10
    }
    
    # Calcular ajustes
    country_adjustment = country_risk.get(country, 0)
    product_adjustment = product_risk.get(product, 0)
    
    # Usar valores proporcionados o predeterminados
    exchange_risk = exchange_risk if exchange_risk is not None else 0.5
    logistics_risk = logistics_risk if logistics_risk is not None else 0.5
    regulatory_risk = regulatory_risk if regulatory_risk is not None else 0.5
    
    # Calcular riesgo total
    risk_score = (
        base_risk +
        country_adjustment +
        product_adjustment +
        (exchange_risk * 20) +
        (logistics_risk * 15) +
        (regulatory_risk * 15)
    )
    
    # Asegurar que el riesgo esté entre 0 y 100
    return max(0, min(100, risk_score))
