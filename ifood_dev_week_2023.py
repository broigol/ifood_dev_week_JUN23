
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
#import openai

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#url = 'https://raw.githubusercontent.com/broigol/dev_week_ifood/master/nps_sample.csv'
#df = pd.read_csv(url, delimiter=';')
#print(df)

dados = pd.read_csv('nps_sample.csv', delimiter=';')
print(dados.head())

class Feedback:
  def __init__(self, nota, comentario):
    self.nota = nota
    self.comentario = comentario

class AnaliserFeedback:

  def __init__(self, feedbacks):
    self.feedbacks = feedbacks

  def nps(self):
    detratores = sum(1 for feedback in self.feedbacks if feedback.nota <= 6)
    promotores = sum(1 for feedback in self.feedbacks if feedback.nota >= 9)
    nps = (((promotores - detratores) / len(self.feedbacks)) * 100)
    return nps

# Converte o Data Frame 'dados' em uma lista, para ser percorrida. Obs.: Listas são 'percorríveis'.
feedbacks = dados.values.tolist()

# A lista de feedbacks é percorrida e cada resigtro é instanciado como um objeto
feedback = [ Feedback(feed[0], feed[1]) for feed in feedbacks]

analise = AnaliserFeedback(feedback)
nps = analise.nps()
print(f'O NPS resultante é de {nps} %')
'''
# Constantes para plotagem dos dados
nps_zonas = ['Crítico', 'Aperfeiçoamento', 'Qualidade', 'Excelência']
nps_valores = [-100, 0, 50, 75, 100]
nps_cores = ['#FF595E', '#FFCA3A', '#8AC926', '#1982C4']

def create_plot(nps):
  # figsize=(largura, altura)
  fig, ax = plt.subplots(figsize=(10, 2))

  # Loop duplo onde percorros os elementos do array e um indice de suporte, pinta o backgroud de acordo com as categorias
  for i, zona in enumerate(nps_zonas):
    ax.barh([0], width=nps_valores[i+1]-nps_valores[i], left=nps_valores[i], color=nps_cores[i])

  # Inclui a marcação do NPS
  ax.barh([0], width=1, left=nps, color='black' )

  # Remove a legenda do eixo Y
  ax.set_yticks([])

  # Aplica margem ao gráfico
  ax.set_xlim(-100, 100)

  # Define q os valores do eixo x, que são baseados nos ranges de nps_valores
  ax.set_xticks(nps_valores)
  
#  Plota o label no nps:
#  - 'ha' e 'va' alinhamento do label,
#  - 'color' e 'bbox' desenha uma box para exibição do label
  
  plt.text(nps, 0, f'{nps: .2f}', ha='center', va='center', color='white', bbox=dict(facecolor='black'))

  patches = [mpatches.Patch(color=nps_cores[i], label=nps_zonas[i]) for i in range(len(nps_zonas))]
  plt.legend(handles=patches, bbox_to_anchor=(1, 1))
  plt.title("Análise de NPS")
  plt.show()

create_plot(nps)



insights = analise_sentimento(feedback)
print(insights)

analyzer = SentimentIntensityAnalyzer()
print(feedback[0].comentario)
print(analyzer.polarity_scores(feedback[0].comentario))
'''
'''
for sentence in feedback[0].comentario:
    vs = analyzer.polarity_scores(sentence)
    print("{:-<65} {}".format(sentence, str(vs)))
'''