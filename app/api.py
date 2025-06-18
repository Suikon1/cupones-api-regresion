from flask import Flask, request, jsonify
from app.cupones import calcular_precio_final

app = Flask(__name__)

@app.route('/precio', methods=['POST'])
def calcular():
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "No se proporcionaron datos"}), 400
            
        precio = data.get("precio")
        cupon = data.get("cupon")
        impuesto = data.get("impuesto", 0.19)
        
        if precio is None:
            return jsonify({"error": "El campo 'precio' es requerido"}), 400
            
        final = calcular_precio_final(precio, cupon, impuesto)
        
        return jsonify({
            "precio_original": precio,
            "cupon_aplicado": cupon,
            "impuesto": impuesto,
            "precio_final": final
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "OK", "message": "API de cupones funcionando correctamente"})

if __name__ == '__main__':
    app.run(debug=True)