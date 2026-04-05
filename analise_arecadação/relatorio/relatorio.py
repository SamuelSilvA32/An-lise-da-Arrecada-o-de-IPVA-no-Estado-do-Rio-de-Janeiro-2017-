from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

styles = getSampleStyleSheet()
story = []

# -------------------------
# TÍTULO
# -------------------------

story.append(Paragraph("Análise da Arrecadação de IPVA no Estado do Rio de Janeiro — 2017", styles['Title']))
story.append(Spacer(1,30))

# -------------------------
# INTRODUÇÃO
# -------------------------

story.append(Paragraph("1. Introdução", styles['Heading2']))
story.append(Spacer(1,10))

intro = """
Este relatório apresenta uma análise exploratória da arrecadação de IPVA no estado do
Rio de Janeiro referente ao ano de 2017.

O objetivo é identificar padrões de arrecadação ao longo dos meses e compreender
como essa arrecadação se distribui entre municípios e regiões administrativas
ao longo do período analisado.
"""

story.append(Paragraph(intro, styles['Normal']))
story.append(Spacer(1,25))

# -------------------------
# ARRECADAÇÃO MENSAL
# -------------------------

story.append(Paragraph("2. Concentração da arrecadação ao longo do ano", styles['Heading2']))
story.append(Spacer(1,10))

texto1 = """
A arrecadação de IPVA apresenta forte concentração no início do ano, com destaque
para o mês de janeiro, que registra o maior volume arrecadado. Esse comportamento
está relacionado ao calendário de pagamento do imposto, quando muitos contribuintes
optam pelo pagamento em cota única ou realizam as primeiras parcelas.
"""

story.append(Paragraph(texto1, styles['Normal']))
story.append(Spacer(1,20))

story.append(Image("graficos/grafico01.png", width=450, height=250))
story.append(Spacer(1,30))

# -------------------------
# MUNICÍPIOS E REGIÕES
# -------------------------

story.append(Paragraph("3. Municípios e regiões com maior arrecadação", styles['Heading2']))
story.append(Spacer(1,10))

texto2 = """
A análise da arrecadação anual revela forte concentração em poucos municípios.
O município do Rio de Janeiro apresenta participação expressiva, representando
aproximadamente 34,32% da arrecadação total observada.

Além da capital, outros municípios da região metropolitana também aparecem entre
os maiores arrecadadores, como Niterói, São Gonçalo, Duque de Caxias e Nova Iguaçu.

Quando observamos a distribuição por regiões administrativas, nota-se a predominância
da Região Metropolitana, refletindo fatores como densidade populacional, atividade
econômica e tamanho da frota de veículos.
"""

story.append(Paragraph(texto2, styles['Normal']))
story.append(Spacer(1,20))

story.append(Image("graficos/grafico02.png", width=450, height=260))
story.append(Spacer(1,30))

# -------------------------
# HEATMAP
# -------------------------

story.append(Paragraph("4. Distribuição mensal entre os principais municípios", styles['Heading2']))
story.append(Spacer(1,10))

texto3 = """
A visualização em formato de heatmap permite observar como a arrecadação mensal
se distribui entre os principais municípios. O padrão observado indica que,
independentemente da cidade, a arrecadação tende a atingir valores mais elevados
nos primeiros meses do ano, diminuindo progressivamente ao longo do restante do período.
"""

story.append(Paragraph(texto3, styles['Normal']))
story.append(Spacer(1,20))

story.append(Image("graficos/grafico03.png", width=450, height=260))
story.append(Spacer(1,30))

# -------------------------
# CONCLUSÃO
# -------------------------

story.append(Paragraph("5. Conclusão", styles['Heading2']))
story.append(Spacer(1,10))

conclusao = """
A análise exploratória da arrecadação de IPVA no estado do Rio de Janeiro revelou
dois padrões principais. O primeiro é a forte sazonalidade da arrecadação,
concentrada principalmente nos primeiros meses do ano.

O segundo padrão é a concentração geográfica da arrecadação, com predominância
da capital e de municípios da região metropolitana. Esses resultados refletem
características estruturais do estado, como densidade populacional, tamanho da
frota de veículos e dinâmica econômica regional.
"""

story.append(Paragraph(conclusao, styles['Normal']))
story.append(Spacer(1,40))

# -------------------------
# SOBRE OS DADOS
# -------------------------

story.append(Paragraph("Sobre os dados", styles['Heading3']))
story.append(Spacer(1,10))

dados = """
Os dados utilizados nesta análise foram obtidos a partir do portal de dados abertos
do governo brasileiro (dados.gov.br).

O conjunto de dados utilizado refere-se à arrecadação de IPVA no estado do
Rio de Janeiro ao longo do ano de 2017, contendo registros mensais organizados
por município e região administrativa.
"""

story.append(Paragraph(dados, styles['Normal']))
story.append(Spacer(1,20))

# -------------------------
# AUTOR
# -------------------------

story.append(Paragraph("Autor", styles['Heading3']))
story.append(Spacer(1,10))

autor = """
Samuel de Andrade da Silva

Projeto de análise de dados desenvolvido utilizando Python e bibliotecas
de análise e visualização de dados para exploração de dados públicos.
"""

story.append(Paragraph(autor, styles['Normal']))

# -------------------------
# GERAR PDF
# -------------------------

doc = SimpleDocTemplate("Relatorio_IPVA_RJ.pdf", pagesize=A4)
doc.build(story)