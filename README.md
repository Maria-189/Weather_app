# Weather App

Aplicação de meteorologia em Python que obtém e armazena distritos de Portugal a partir da API pública [PTData](https://api.ptdata.org).

Projeto escolar em desenvolvimento.

## Autores

- Maria João
- Luis Ramos
- Rodrigo Lima

## Requisitos

- Python 3.8+
- `pip install requests`

## Como executar

```bash
python gestor_cidades.py
```

## Funcionalidades

- Consulta distritos de Portugal via API REST
- Guarda os dados em ficheiro JSON local
- Gestão de erros de rede e ficheiro

## API

- Base URL: `https://api.ptdata.org`
- Endpoint: `GET /v1/geo/districts`

## Trabalho futuro

- Previsões meteorológicas por distrito
- Interface gráfica
- Alertas meteorológicos
- Histórico de consultas

## Licença

Projeto académico — uso educacional.
