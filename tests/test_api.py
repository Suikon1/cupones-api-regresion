import pytest
import json
from app.api import app

@pytest.fixture
def client():
    """Fixture para cliente de pruebas de Flask"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

class TestAPIEndpoints:
    """Pruebas para los endpoints de la API"""
    
    def test_health_check(self, client):
        """Prueba que el endpoint de salud funcione"""
        response = client.get('/health')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['status'] == 'OK'
    
    def test_calcular_precio_con_cupon_valido(self, client):
        """Prueba cálculo de precio con cupón válido"""
        payload = {
            "precio": 100,
            "cupon": "OFERTA10",
            "impuesto": 0.19
        }
        response = client.post('/precio', 
                             data=json.dumps(payload),
                             content_type='application/json')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['precio_final'] == 107.1
        assert data['cupon_aplicado'] == "OFERTA10"
    
    def test_calcular_precio_sin_cupon(self, client):
        """Prueba cálculo de precio sin cupón"""
        payload = {
            "precio": 100
        }
        response = client.post('/precio', 
                             data=json.dumps(payload),
                             content_type='application/json')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['precio_final'] == 119.0
    
    def test_calcular_precio_sin_datos(self, client):
        """Prueba error cuando no se envían datos"""
        response = client.post('/precio')
        assert response.status_code == 400
    
    def test_calcular_precio_sin_precio(self, client):
        """Prueba error cuando falta el campo precio"""
        payload = {"cupon": "OFERTA10"}
        response = client.post('/precio', 
                             data=json.dumps(payload),
                             content_type='application/json')
        assert response.status_code == 400