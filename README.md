# Weather Service Microservice

Este microserviço foi desenvolvido para adquirir dados climáticos do OpenWeatherMap e fornecê-los por meio de uma API REST. Ele foi projetado para ser consumido pela aplicação principal (app.py), que utiliza esses dados para complementar as informações de saúde.

## Funcionalidade

- **Detecção de Localização:**  
  Utiliza a biblioteca `geocoder` para capturar a localização atual com base no endereço IP.

- **Consulta à API do OpenWeatherMap:**  
  Com os dados de latitude e longitude, o microserviço realiza uma consulta à API do OpenWeatherMap para obter informações climáticas, como temperatura, nome da cidade, país e descrição do tempo.

- **Exposição via API REST:**  
  Disponibiliza um endpoint `/weather` que recebe a chave de API do OpenWeatherMap via query string e retorna os dados meteorológicos em formato JSON.

## Endpoint

### GET /weather

**Parâmetros:**  
- `apikey` (obrigatório): Chave de API para acessar o serviço do OpenWeatherMap.

**Exemplo de Requisição:**

```bash
curl "http://localhost:5001/weather?apikey=SEU_API_KEY"
