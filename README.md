# Sea Level Predictor

Este é um projeto de análise de dados que utiliza dados do nível do mar para criar visualizações e previsões. O projeto faz parte do curso "Data Analysis with Python" do freeCodeCamp.

## Descrição

O projeto analisa dados de mudança do nível do mar desde 1880 e usa os dados para prever a mudança do nível do mar até o ano 2050.

## Funcionalidades

- Lê dados do arquivo CSV `epa-sea-level.csv`
- Cria um gráfico de dispersão dos dados
- Calcula e plota duas linhas de melhor ajuste:
  - Uma linha usando todos os dados (1880-2013)
  - Uma linha usando apenas dados de 2000 em diante
- Extrapola ambas as linhas até 2050
- Salva o gráfico como `sea_level_plot.png`

## Arquivos

- `sea_level_predictor.py`: Arquivo principal com a função `draw_plot()`
- `main.py`: Arquivo para execução e testes
- `test_module.py`: Testes unitários
- `README.md`: Este arquivo
- `epa-sea-level.csv`: Dados do nível do mar (você precisa baixar este arquivo)

## Como usar

1. Baixe o arquivo de dados `epa-sea-level.csv` da EPA (Environmental Protection Agency)
2. Execute `python main.py` para gerar o gráfico e executar os testes

## Dependências

```bash
pip install pandas matplotlib scipy numpy
```

## Estrutura do Projeto

```
sea-level-predictor/
├── sea_level_predictor.py
├── main.py
├── test_module.py
├── README.md
└── epa-sea-level.csv (você precisa baixar)
```

## Notas

- O gráfico mostra o aumento do nível do mar ao longo do tempo
- A primeira linha de tendência usa todos os dados disponíveis
- A segunda linha de tendência usa apenas dados a partir do ano 2000, mostrando uma tendência mais recente
- Ambas as linhas são extrapoladas até 2050 para mostrar previsões futuras