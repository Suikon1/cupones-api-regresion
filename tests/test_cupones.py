import pytest
from app.cupones import aplicar_cupon, calcular_precio_final

class TestAplicarCupon:
    """Pruebas para la función aplicar_cupon"""
    
    def test_descuento_oferta10(self):
        """Prueba que OFERTA10 aplique 10% de descuento"""
        resultado = aplicar_cupon(100, "OFERTA10")
        assert resultado == 90.0
    
    def test_descuento_super20(self):
        """Prueba que SUPER20 aplique 20% de descuento"""
        resultado = aplicar_cupon(200, "SUPER20")
        assert resultado == 160.0
    
    def test_descuento_bienvenida(self):
        """Prueba que BIENVENIDA aplique 15% de descuento"""
        resultado = aplicar_cupon(100, "BIENVENIDA")
        assert resultado == 85.0
    
    def test_cupon_inexistente(self):
        """Prueba que un cupón inexistente no aplique descuento"""
        resultado = aplicar_cupon(100, "CUPON_FALSO")
        assert resultado == 100.0
    
    def test_cupon_vacio(self):
        """Prueba que un cupón vacío no aplique descuento"""
        resultado = aplicar_cupon(100, "")
        assert resultado == 100.0
    
    def test_cupon_none(self):
        """Prueba que None no aplique descuento"""
        resultado = aplicar_cupon(100, None)
        assert resultado == 100.0

class TestCalcularPrecioFinal:
    """Pruebas para la función calcular_precio_final"""
    
    def test_precio_final_con_impuesto_default(self):
        """Prueba cálculo con impuesto por defecto (19%)"""
        # 100 * 0.9 (OFERTA10) * 1.19 (impuesto) = 107.1
        resultado = calcular_precio_final(100, "OFERTA10")
        assert resultado == 107.1
    
    def test_precio_final_con_impuesto_custom(self):
        """Prueba cálculo con impuesto personalizado"""
        # 100 * 0.8 (SUPER20) * 1.10 (impuesto 10%) = 88.0
        resultado = calcular_precio_final(100, "SUPER20", 0.10)
        assert resultado == 88.0
    
    def test_precio_final_sin_cupon(self):
        """Prueba cálculo sin cupón válido"""
        # 100 * 1.19 = 119.0
        resultado = calcular_precio_final(100, "INEXISTENTE")
        assert resultado == 119.0
    
    def test_precio_final_sin_impuesto(self):
        """Prueba cálculo sin impuesto"""
        # 100 * 0.85 (BIENVENIDA) * 1.0 = 85.0
        resultado = calcular_precio_final(100, "BIENVENIDA", 0.0)
        assert resultado == 85.0