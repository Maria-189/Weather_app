# Weather App

Aplicação de meteorologia em Python para Portugal (distritos, municípios e arquipélagos), com interface gráfica em **PySide6**. Os dados geográficos e a previsão do tempo são obtidos a partir da API pública [PTData](https://api.ptdata.org), com cache local em ficheiros JSON.

Projeto escolar em desenvolvimento (ISTEC Porto).

## Autores

- Maria João
- Luis Ramos
- Rodrigo Lima

## Requisitos

- Python 3.8+
- `pip install requests PySide6`

## ⚠️ Antes de executar

Os ficheiros do projeto (`main`, `interface`, `modelos`, `confi`, `distritos`, `municipios`, `arquipelagos`, `gestor_ficheiro`) estão atualmente **sem extensão `.py`**. Como usam `import` entre si (ex.: `from gestor_ficheiro import GestorFicheiro`), o Python não os reconhece como módulos enquanto não tiverem a extensão correta. Antes de correr o projeto, renomeia todos os ficheiros em `trabalho/` para terminarem em `.py`:

```bash
cd trabalho
for f in main interface modelos confi distritos municipios arquipelagos gestor_ficheiro; do mv "$f" "$f.py"; done
```

## Como executar

1. **Atualizar os dados geográficos** (gera/atualiza os ficheiros JSON em cache):

   ```bash
   python main.py
   ```

   Isto cria `distrito_30Maio2026.json` e `municipios_30Maio2026.json` com a lista de distritos, municípios e arquipélagos.

2. **Abrir a interface gráfica**:

   ```bash
   python interface.py
   ```

   Escolhe um distrito, depois um município, e clica em **"Ver Estado do Tempo"** para ver a previsão.

## Funcionalidades

- Obtenção de distritos e municípios de Portugal Continental via API REST (`/v1/geo/districts`, `/v1/geo/municipalities`)
- Dados da Madeira e dos Açores incluídos manualmente (a API pública não os disponibiliza), com geração automática de códigos `DDMM`
- Cache dos dados geográficos em ficheiros JSON locais, com atualização incremental (só regrava o ficheiro se os dados mudarem)
- Interface gráfica (PySide6) com:
  - Seleção em cascata de distrito → município
  - Cartões de previsão para 3 dias (hoje, amanhã, depois de amanhã): temperatura, condição com emoji, máxima/mínima, vento e probabilidade de precipitação
  - Gráfico de tendência de temperaturas (máxima/mínima) ao longo dos 3 dias
- Gestão de erros de rede e de ficheiro (`GestorFicheiro`, `try/except` nas chamadas à API)

### Em desenvolvimento / limitações conhecidas

- A barra de pesquisa de municípios (`search_bar`) existe na interface mas ainda não filtra a lista — falta ligar o sinal `textChanged` a uma função de filtro
- A chamada à API de previsão do tempo é feita de forma síncrona, na *thread* principal da interface (pode bloquear a UI brevemente enquanto os dados chegam)
- Não existe ainda tratamento de "município não encontrado" se os ficheiros JSON não tiverem sido gerados primeiro com `main.py`

## Estrutura do projeto

```
trabalho/
├── confi            → Configuração (URL_BASE da API)
├── modelos          → Classes: RegiaoAdministrativa, Distrito, Municipio
├── distritos        → carregar_distritos() — obtém distritos via API
├── municipios       → carregar_municipios() — obtém municípios via API (paginado), agrupados e ordenados por distrito
├── arquipelagos     → carregar_arquipelagos() — dados fixos da Madeira e dos Açores
├── gestor_ficheiro  → GestorFicheiro — leitura/escrita/atualização de ficheiros JSON
├── interface        → WeatherCard e DistrictWeatherApp — interface gráfica (PySide6)
└── main             → Ponto de entrada: gera os ficheiros JSON de distritos e municípios
```

## API

- Base URL: `https://api.ptdata.org`
- Endpoints usados:
  - `GET /v1/geo/districts` — lista de distritos
  - `GET /v1/geo/municipalities` — lista de municípios (com paginação `offset`/`limit`)
  - `GET /v1/weather/forecast/daily/{distrito}/{municipio}` — previsão diária por município

## Diagrama de classes

O diagrama UML do projeto está disponível no repositório (`Captura de ecrã 2026-06-26 161424.png`), incluindo a hierarquia `RegiaoAdministrativa` → `Distrito`/`Municipio`, a classe `GestorFicheiro` e a composição entre `DistrictWeatherApp` e `WeatherCard`.

## Trabalho futuro

- Ligar a barra de pesquisa de municípios à lista exibida
- Mover a chamada à API de previsão para uma *thread* separada (ex. `QThread`), evitando bloquear a interface
- Adicionar `requirements.txt`
- Histórico de consultas e alertas meteorológicos

## Licença

Projeto académico — uso educacional.
