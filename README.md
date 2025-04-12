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
````
**Exemplo de Repsosta:**
```json
{
  "coord": {"lon": -43.18, "lat": -22.90},
  "weather": [
    {"id": 800, "main": "Clear", "description": "céu limpo", "icon": "01d"}
  ],
  "base": "stations",
  "main": {
    "temp": 28.5,
    "feels_like": 30.0,
    "temp_min": 28.0,
    "temp_max": 29.0,
    "pressure": 1013,
    "humidity": 60
  },
  "visibility": 10000,
  "wind": {"speed": 5.1, "deg": 200},
  "clouds": {"all": 0},
  "dt": 1622577600,
  "sys": {
    "type": 1,
    "id": 8305,
    "country": "BR",
    "sunrise": 1622553600,
    "sunset": 1622596800
  },
  "timezone": -10800,
  "id": 3448439,
  "name": "Rio de Janeiro",
  "cod": 200
}
```

## Requisitos
* Python 3.9 ou superior
* Bibliotecas Python:
  * Flask
  * requests
  * geocoder

## Instalação e Execução
### Executando Localmente
1. Clone o repositório
```bash
git clone <URL_DO_REPOSITORIO>
cd weather_service
```
2. Crie e ative um ambiente virtual (opcional):
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```
3. Instale as dependências
```bash
pip install flask requests geocoder
```
4. Execute o serviço
```bash
python weather_service.py
```
O serviço iniciará na porta 5001.
## Utilizando o Docker
Este microserviço foi containerizado para facilitar a implantação.
1. Construa a imagem Docker:
```bash
docker build -t weather_service .
```
2. Rode o container:
```bash
docker run -p 5001:5001 weather_service
```
## Utilizando o Docker Compose
Caso este microserviço seja parte de um sistema maior, você pode usar o Docker Compose para orquestrar os containers. Um exemplo de docker-compose.yml:
```yaml
version: "3.8"

services:
  weather:
    build:
      context: ./weather_service
      dockerfile: Dockerfile
    ports:
      - "5001:5001"
```
## Integração com a Aplicação Principal
A aplicação principal (app.py) pode realizar consultas ao microserviço utilizando o hostname weather (definido no docker-compose) e a porta 5001. Por exemplo, a função de consulta no app.py pode fazer uma requisição para:
```bash
http://weather:5001/weather?apikey=SEU_API_KEY
```
Isso permite que o microserviço seja um componente independente e escalável, retornando as informações climáticas necessárias para complementar os dados da API principal.

## Observações
* Chave de API: Certifique-se de fornecer uma chave de API válida do OpenWeatherMap.

* Verificação de SSL: A verificação SSL foi desabilitada (verify=False) para contornar problemas com certificados. Em produção, recomenda-se configurar corretamente os certificados ou utilizar uma abordagem segura.

* Localização: O microserviço utiliza o IP do container para determinar a localização, o que pode variar conforme a rede e o ambiente em que o container está executando.
