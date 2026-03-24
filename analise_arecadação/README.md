# Análise da Arrecadação de IPVA no Estado do Rio de Janeiro (2017)

## 📊 Sobre o Projeto

Este projeto apresenta uma análise exploratória da arrecadação de **IPVA no estado do Rio de Janeiro no ano de 2017**, utilizando dados públicos disponibilizados pelo portal de dados abertos do governo brasileiro.

O objetivo da análise é compreender **como a arrecadação do imposto se distribui ao longo do ano e entre diferentes municípios e regiões do estado**.

O projeto percorre todas as etapas de um fluxo de trabalho típico de análise de dados:

* coleta de dados públicos
* tratamento e limpeza dos dados
* análise exploratória
* visualização de dados
* geração de relatório automatizado

---

## 📁 Estrutura do Projeto

```
analise_arrecadacao_ipva_rj/

dados/
    ipva_2017_raw.csv

notebooks/
    01_tratamento_dados.ipynb
    02_analise_exploratoria_ipva_rj.ipynb

graficos/
    arrecadacao_mensal.png
    municipios_regioes.png
    heatmap.png

relatorio/
    Relatorio_IPVA_RJ_2017.pdf

README.md
```

---

## 🔎 Perguntas de Análise

A análise foi conduzida para responder algumas perguntas principais:

* Como a arrecadação de IPVA se comporta ao longo dos meses do ano?
* Quais municípios concentram a maior arrecadação?
* Como a arrecadação se distribui entre as regiões do estado?
* Existe um padrão mensal semelhante entre os principais municípios?

---

## 📈 Principais Resultados

A análise identificou alguns padrões relevantes na arrecadação de IPVA no estado do Rio de Janeiro em 2017.

**1️⃣ Forte sazonalidade da arrecadação**

A arrecadação apresenta forte concentração no início do ano, especialmente no mês de janeiro, quando muitos contribuintes realizam o pagamento em cota única ou quitam as primeiras parcelas do imposto.

**2️⃣ Alta concentração geográfica**

O município do **Rio de Janeiro** representa aproximadamente **34,32% da arrecadação total observada**, evidenciando a concentração da arrecadação na capital e em municípios da região metropolitana.

**3️⃣ Padrão mensal consistente entre municípios**

Mesmo entre diferentes municípios, o comportamento mensal da arrecadação segue um padrão semelhante, com maior volume nos primeiros meses e redução gradual ao longo do ano.

---

## 📊 Exemplos de Visualizações

### Arrecadação total de IPVA por mês

![Arrecadação mensal](graficos/arrecadacao_mensal.png)

### Municípios e regiões com maior arrecadação

![Municípios e regiões](graficos/municipios_regioes.png)

### Distribuição mensal da arrecadação entre municípios

![Heatmap](graficos/heatmap.png)

---

## 🛠️ Tecnologias Utilizadas

* Python
* Pandas
* Matplotlib
* Seaborn
* Jupyter Notebook
* ReportLab (geração de relatório em PDF)

---

## 📄 Relatório

O projeto inclui um relatório analítico com os principais resultados da análise.

📎 **[Acessar relatório completo](relatorio/Relatorio_IPVA_RJ_2017.pdf)**

---

## 📊 Fonte dos Dados

Dados públicos disponibilizados pelo portal de dados abertos do governo brasileiro.

https://dados.gov.br/dados/conjuntos-dados/arrecadacao-receitas

---

## 👤 Autor

**Samuel de Andrade da Silva**

Projeto desenvolvido como exercício de análise exploratória de dados públicos utilizando Python.
