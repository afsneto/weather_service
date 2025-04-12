# weather_service/Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Instale as dependências necessárias para o serviço de clima
RUN pip install --upgrade pip && \
    pip install flask requests geocoder

# Copie o arquivo do serviço para o container
COPY weather_service.py .

# Exponha a porta definida no microserviço
EXPOSE 5001

# Inicie o serviço
CMD ["python", "weather_service.py"]
