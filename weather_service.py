from flask import Flask, request, jsonify
import requests
import geocoder

app = Flask(__name__)

@app.route('/weather', methods=['GET'])
def get_weather_data():

    # A API key deve ser enviada como parâmetro na query string (ou você pode definir um default)
    API_KEY = request.args.get("apikey")
    if not API_KEY:
        return jsonify({"error": "API key is required"}), 400

    # Obtém coordenadas com base na localização do usuário
    location = geocoder.ip('me')
    lat, lon = location.latlng
        
    # Monta a URL com os parâmetros necessários (usando vers"ao 2.5)
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"
    try:
        response = requests.get(url, verify=False)
        if response.status_code == 200:
            data = response.json()
            return jsonify(data)
        else:
            return jsonify({"error": "OpenWeatherMap API error", "status": response.status_code, "detail": response.text}), 500
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Error fetching weather data: {e}"}), 500

if __name__ == '__main__':
    # Escuta em todas as interfaces na porta 5001
    app.run(host="0.0.0.0", port=5001, debug=True)