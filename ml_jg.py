import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.tree import  DecisionTreeClassifier
import pickle
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from yellowbrick.classifier import ConfusionMatrix

# # carrega o csv

# base_credit = pd.read_csv('credit_data.csv')


# # resume informações estatísticas do csv

# alfa = base_credit.describe()


# # filtra valores em 'income' maiores ou igual que 69436.579552

# beta = base_credit[base_credit["income"] >= 69436.579552 ]


# # filtra valores em 'loan' menor ou igual a 1.377630

# charlie = base_credit[base_credit["loan"] <= 1.377630 ]


# # filtra os dados em 'default'

# delta = np.unique(base_credit['default'], return_counts = True)


# # Gera o gráfico dos dados em 'default'

# sns.countplot(x = base_credit['default'])
# plt.show()




# ######### Visualizações experimentais

# base_credit = pd.read_csv('credit_data.csv', index_col=0, parse_dates=True)
# base_credit.plot()
# plt.show()

# base_credit = pd.read_csv('credit_data.csv', index_col=0, parse_dates=True)
# base_credit['income'].plot()
# plt.show()

# base_credit = pd.read_csv('credit_data.csv', index_col=0, parse_dates=True)
# base_credit['age'].plot()
# plt.show()

# base_credit = pd.read_csv('credit_data.csv', index_col=0, parse_dates=True)
# base_credit['loan'].plot()
# plt.show()

# base_credit = pd.read_csv('credit_data.csv', index_col=0, parse_dates=True)
# base_credit['default'].plot()
# plt.show()

# ## plot.scatter

# base_credit.plot.scatter(x="income", y="age", alpha=0.5)
# plt.show()

# base_credit.plot.scatter(x="age", y="income", alpha=0.5)
# plt.show()

# base_credit.plot.box()
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt

# # Fixing random state for reproducibility
# np.random.seed(19680801)

# dt = 0.01
# t = np.arange(0, 30, dt)
# nse1 = np.random.randn(len(t))                 # white noise 1
# nse2 = np.random.randn(len(t))                 # white noise 2

# # Two signals with a coherent part at 10Hz and a random part
# s1 = np.sin(2 * np.pi * 44 * t) + nse1
# s2 = np.sin(2 * np.pi * 10 * t) + nse2

# fig, axs = plt.subplots(2, 1)
# axs[0].plot(t, s1, t, s2)
# axs[0].set_xlim(0, 2)
# axs[0].set_xlabel('time')
# axs[0].set_ylabel('s1 and s2')
# axs[0].grid(True)

# cxy, f = axs[1].cohere(s1, s2, 256, 1. / dt)
# axs[1].set_ylabel('coherence')

# fig.tight_layout()
# plt.show()



# sns.set_theme(style="ticks", palette="pastel")
# sns.boxplot(x=base_credit['clientid'], y=base_credit['mean'],
#             hue="smoker", palette=["m", "g"],
#             data=base_credit)
# sns.despine(offset=10, trim=True)
# plt.show()



# sns.set_theme(style="darkgrid")
# df = pd.read_csv('credit_data.csv')
# sns.displot(
#     df, x="clientid", col="age", row="default",
#     binwidth=3, height=3, facet_kws=dict(margin_titles=True),
# )
# plt.show()


# # importing pandas library
# import pandas as pd
# import matplotlib.pyplot as plt

  
# base_credit = pd.read_csv('credit_data.csv')

# # plotting a bar graph
# base_credit.plot(x="default", y="age", kind="bar")

# plt.show()


# ##########################################################3


# # Gera o histograma dos dados em 'age'

# plt.hist(x = base_credit['age'])
# plt.show()


# # Gera o histograma dos dados em 'income'

# plt.hist(x = base_credit['income'])
# plt.show()


# # Gera o histograma dos dados em 'loan'

# plt.hist(x = base_credit['loan'])
# plt.show()


# # gera um gráfico dinâmico dos dados em 'age' 'income' e 'loan'; colorido 'default'

# echo = px.scatter_matrix(base_credit, dimensions = ['age', 'income', 'loan'], color = "default")
# echo.show()


# # remove os valores negativos em 'age'

# fox = base_credit.loc[base_credit['age'] < 0]

# # remove os valores negativos em 'age' - Alternativo

# fox = base_credit[base_credit['age'] < 0 ]


# # Cria a variável 'base_credit2' sem a coluna 'age'

# base_credit2 = base_credit.drop('age', axis = 1)


# # Cria a variável 'base_credit3' sem valores negativos em 'age'

# gama = base_credit3 = base_credit.drop(base_credit[base_credit ['age'] < 0].index)


# # Preencher os valores inconsistentes manualmente - Melhor alternativa; distorce menos

# # Preenche os dados faltantes com a média dos valores em 'age'

# # Retorna as médias de todas as colunas

# hotel = base_credit.mean()
# hotel

# # Retorna a média em 'age'

# hotel = base_credit['age'].mean()
# hotel


# # filtra os valores em 'age' > 0 e retona a média

# base_credit['age'][base_credit['age'] > 0].mean()


# # busca em 'age' os elementos < 0

# base_credit.loc[base_credit['age'] < 0]


# # substitui em 'age' os elementos < 0 pela média

# base_credit.loc[base_credit['age'] < 0, 'age'] = base_credit['age'][base_credit['age'] > 0].mean()


# # gera um gráfico dinâmico dos dados em 'age' 'income' e 'loan'; colorido 'default'; sem os elementos age' < 0 

# echo = px.scatter_matrix(base_credit, dimensions = ['age', 'income', 'loan'], color = "default")
# echo.show()



# # Pre-processamento dos dados


# # tratamento dos valores faltantes

# # apresenta o somatório da quantidade de elementos nulos

# base_credit.isnull().sum()


# # retorna o índice dos elementos faltantes

# base_credit.loc[pd.isnull(base_credit['age'])]


# # Preenche os valores nulos em 'age' usando a média dos valores na mesma coluna

# base_credit['age'].fillna(base_credit['age'].mean(), inplace = True)


# # busca os elementos previamente identificados como NaN

# base_credit.loc[ (base_credit['clientid'] == 29) | (base_credit['clientid'] == 31) | (base_credit['clientid'] == 32)]

# # alternativa

# base_credit.loc[base_credit['clientid'].isin([29, 31, 32])]


# # Divisão dos dados entre atributos preditores e classe
# # Parte dos dados presentes em 'income', 'age' e 'loan' para prever a chance de 'default'

# X_credit = base_credit.iloc[:, 1:4].values
# y_credit = base_credit.iloc[:, 4].values


# # retorna o menor e o maior valor presente na respectiva coluna
# # importante perceber a diferênça entre as escalas
# # é necessário padronizar estes valores para que estes fiquem dentro da mesma escala


# X_credit[:,0].min()
# X_credit[:,0].max()

# X_credit[:,1].min()
# X_credit[:,1].max()

# X_credit[:,2].min()
# X_credit[:,2].max()


# X_credit[:,0].min(), X_credit[:,1].min(), X_credit[:,2].min()
# X_credit[:,0].max(), X_credit[:,1].max(), X_credit[:,2].max()

# # Padronização x = ((x - média(x) / desvio-padrão(x)) ; mais indicado quando existem outliers
# #
# # Normalização x = ((x - mínimo(x) / (máximo(x) - mínimo(x)))


# from sklearn.preprocessing import StandardScaler

# scaler_credit = StandardScaler()
# X_credit2 = scaler_credit.fit_transform(X_credit)

# X_credit2[:,0].min(), X_credit2[:,1].min(), X_credit2[:,2].min()
# X_credit2[:,0].max(), X_credit2[:,1].max(), X_credit2[:,2].max()



# # Pré-processamento da base de dados do {database_name}

# base_{database_name} = pd.read_csv('{database_name}.csv')


# # Análise primária do dataframe

# base_{database_name}.describe()


# # Busca por elementos nulos no dataframe

# base_{database_name}.isnull().sum()


# index = ['age', 
#          'workclass',
#          'education',
#          'education-num',
#          'marital-status',
#          'occupation',
#          'relationship',
#          'race',
#          'sex',
#          'capital-gain',
#          'capital-loos',
#          'hour-per-week',
#          'native-country',
#          'income']


# # Conta os elementos únicos numa dada coluna

# for i in index:
#     np.unique(base_{database_name}[i], return_counts = True)


# # Gera uma visualização em colunas dos dados na coluna selecionada

# for i in index:
#     sns.countplot(x = base_{database_name}[i])
#     plt.show()



# # Gera uma visualização em histogramas dos dados na coluna selecionada

# for i in index:
#     plt.hist(x = base_{database_name}[i])
#     plt.show()


# # Gera uma visualização dinâmica em treemap dos dados na coluna selecionada

# for i in index:
#     grafico = px.treemap(base_{database_name}, path = [i])
#     grafico.show()


# # Gera uma visualização dinâmica em treemap dos dados de duas colunas selecionadas

# for i in index:
#     unique = 'sex'

#     if i != unique:
#         grafico = px.treemap(base_{database_name}, path = [i, unique])
#         grafico.show()
#     else:
#         pass


# # Gera uma visualização de categorias paralelas dos dados de duas colunas selecionadas


# for i in index:
#     unique = 'sex'

#     if i != unique:
#         grafico = px.parallel_categories(base_{database_name}, dimensions = [i, unique])
#         grafico.show()
#     else:
#         pass


# def paral_cat(categ):
#     for i in index:
    
#         if i != categ:
#             grafico = px.parallel_categories(base_{database_name}, dimensions = [i, categ])
#             grafico.show()
#         else:
#             pass

# #paral_cat('race')
# #paral_cat('occupation')
# #paral_cat('income')


# # Divide os dados entre previsores e classe


# # retorna os nomes das colunas

# base_{database_name}.columns


# # retorna os conteúdos das colunas
# # Previsores

# X_{database_name} = base_{database_name}.iloc[:, 0:14].values

# # Classe; Coluna-alvo

# y_{database_name} = base_{database_name}.iloc[:, 14].values


# # Tratamento dos dados categóricos
# # label-encoder;  tranforma todos os dados categóricos em elementos numéricos

# from sklearn.preprocessing import LabelEncoder

# label_encoder_teste = LabelEncoder()
# teste = label_encoder_teste.fit_transform(X_{database_name}[:,1])


# label_encoder_workclass = LabelEncoder()
# label_encoder_education = LabelEncoder()
# label_encoder_marital = LabelEncoder()
# label_encoder_occupation = LabelEncoder()
# label_encoder_relationship = LabelEncoder()
# label_encoder_race = LabelEncoder()
# label_encoder_sex = LabelEncoder()
# label_encoder_country = LabelEncoder()

# X_{database_name}[:,1] = label_encoder_workclass.fit_transform(X_{database_name}[:,1])
# X_{database_name}[:,3] = label_encoder_education.fit_transform(X_{database_name}[:,3])
# X_{database_name}[:,5] = label_encoder_marital.fit_transform(X_{database_name}[:,5])
# X_{database_name}[:,6] = label_encoder_occupation.fit_transform(X_{database_name}[:,6])
# X_{database_name}[:,7] = label_encoder_relationship.fit_transform(X_{database_name}[:,7])
# X_{database_name}[:,8] = label_encoder_race.fit_transform(X_{database_name}[:,8])
# X_{database_name}[:,9] = label_encoder_sex.fit_transform(X_{database_name}[:,9])
# X_{database_name}[:,13] = label_encoder_country.fit_transform(X_{database_name}[:,13])


# # Outro procedimento pro tratamento de dados categóricos - OneHotEncoder
# # troca o número de elementos únicos em cada coluna por uma quantidade iqual
# # de novas colunas preenchidas com elementos booleanos; evita a hierarquização 
# # dentro da categoria

# # retorna a quantidade de elementos únicos em uma dada coluna

# len(np.unique(base_{database_name}['workclass']))

# from sklearn.preprocessing import OneHotEncoder
# from sklearn.compose import ColumnTransformer

# onehotencoder_{database_name} = ColumnTransformer(transformers = [
#     ('OneHot', OneHotEncoder(), [1,3,5,6,7,8,9,13])], remainder = 'passthrough')

# X_{database_name} = onehotencoder_{database_name}.fit_transform(X_{database_name}).toarray()


# # Faz o escalonamento das variáves, coloca os elementos do np.array
# # dentro da mesma dimensão escalar - Padronização

# from sklearn.preprocessing import StandardScaler

# scaler_{database_name} = StandardScaler()
# X_{database_name} = scaler_{database_name}.fit_transform(X_{database_name})


# # Faz a divisão da dase de dados entre base de teste e base de treinamento


# from sklearn.model_selection import train_test_split

# X_credit_treinamento, X_credit_teste, y_credit_treinamento, y_credit_teste = train_test_split(X_credit, y_credit, test_size = 0.25, random_state = 0)

# X_credit_treinamento.shape
# X_credit_teste.shape
# y_credit_treinamento.shape
# y_credit_teste.shape


# # Divide a base de dados {database_name}

# X_{database_name}_treinamento, X_{database_name}_teste, y_{database_name}_treinamento, y_{database_name}_teste = train_test_split(X_{database_name}, y_{database_name}, test_size = 0.15, random_state = 0)

# X_{database_name}_treinamento.shape
# X_{database_name}_teste.shape
# y_{database_name}_treinamento.shape
# y_{database_name}_teste.shape


# # Salva as bases de dados após o pré-processamento

# import pickle

# with open('credit.pkl', mode = 'wb')as f:
#     pickle.dump([X_credit_treinamento, X_credit_teste, y_credit_treinamento, y_credit_teste], f)


# with open('{database_name}.pkl', mode = 'wb')as f:
#     pickle.dump([X_{database_name}_treinamento, X_{database_name}_teste, y_{database_name}_treinamento, y_{database_name}_teste], f)




# # Aplica o algoritmo Naive Bayes
# # 
# # Abordagem probabiblística com base no teorema de Bayes

# base_risco_credito = pd.read_csv('risco_credito.csv')

# # Separa-se o banco de dados em X = atributos previsores e y = classe prevista

# X_risco_credito = base_risco_credito.iloc[:, 0:4].values

# y_risco_credito = base_risco_credito.iloc[:, 4].values


# # Usa do label encoder pra transformar as 
# # variáveis categóricas em variáveis numéricas

# label_encoder_historia = LabelEncoder()
# label_encoder_divida = LabelEncoder()
# label_encoder_garantia = LabelEncoder()
# label_encoder_renda = LabelEncoder()


# # Aplica o processamento do label encoder

# X_risco_credito[:,0] = label_encoder_historia.fit_transform(X_risco_credito[:,0])
# X_risco_credito[:,1] = label_encoder_divida.fit_transform(X_risco_credito[:,1])
# X_risco_credito[:,2] = label_encoder_garantia.fit_transform(X_risco_credito[:,2])
# X_risco_credito[:,3] = label_encoder_renda.fit_transform(X_risco_credito[:,3])


# # Para esta análise não aplica-se o OneHotEncoder; opcional por se tratar de um teste
# #
# # Salva a base de dados com o pickle

# with open('risco_credito.pkl', 'wb') as f:
#     pickle.dump([X_risco_credito, y_risco_credito], f)


# # Aplica-se o algoritmo naive bayes; gera a tabela de probabilidades
# # treinamento do algoritmo

# naive_risco_credito = GaussianNB()
# naive_risco_credito.fit(X_risco_credito, y_risco_credito)


# # gera uma previsão com base em uma entrada nova; codificado na base de dados

# # história boa (0), dívida alta (0), garantias nenhuma (1), renda > 35 (2)
# # história ruim (2), dívida alta (0), garantias adequada (0), renda < 15 (0)

# previsao = naive_risco_credito.predict([[0,0,1,2], [2,0,0,0]])
# previsao = naive_risco_credito.predict([[2,1,1,0], [2,0,0,2]])


# # Apresenta as classes dentro do previsor

# naive_risco_credito.classes_


# # Apresenta a contagem dos registros nas classes dentro do previsor

# naive_risco_credito.class_count_


# # Apresenta as probabilidaes apriori dos registros nas classes dentro do previsor

# naive_risco_credito.class_prior_



# # Aplica o algoritmo Naive Bayes na base de dados de crédito completa
# # 
# # Abordagem probabiblística com base no teorema de Bayes

# with open('credit.pkl', 'rb') as f:
#     X_credit_treinamento, y_credit_treinamento, X_credit_teste, y_credit_teste = pickle.load(f)


# # alternativa; picle quebou o formato do array y_credit_teste

# X_credit_treinamento, X_credit_teste, y_credit_treinamento, y_credit_teste = train_test_split(X_credit, y_credit, test_size = 0.25, random_state = 0)

# # apresenta o formato dos dados nas variáveis

# X_credit_treinamento.shape, y_credit_treinamento.shape
# X_credit_teste.shape, y_credit_teste.shape


# # cria a tabela de probabilidades

# naive_credit_data = GaussianNB()
# naive_credit_data.fit(X_credit_treinamento, y_credit_treinamento)


# # previsões

# previsoes = naive_credit_data.predict(X_credit_teste)
# previsoes


# # Compara as respostas do algoritmo com os dados presentes na base de dados,
# # y_credit_teste e retorna a taxa de acertos do algoritmo; compara as respostas 
# # reais com as previsões 

# accuracy_score(y_credit_teste, previsoes)


# # retorna uma matrix de confusão, visualização e outras estatísticas

# confusion_matrix(y_credit_teste, previsoes)

# cm = ConfusionMatrix(naive_credit_data)
# cm.fit(X_credit_treinamento, y_credit_treinamento)
# cm.score(X_credit_teste, y_credit_teste)
# cm.show()

# print(classification_report(y_credit_teste, previsoes))




# # Aplica o algoritmo Naive Bayes na base de dados do {database_name}
# # 
# # Abordagem probabiblística com base no teorema de Bayes;
# # retorna uma tava de acerto menor que 50% nesse caso
# # resultados melhores se a base for processada sem o escalonamento

# with open('{database_name}.pkl', 'rb') as f:
#     X_{database_name}_treinamento, y_{database_name}_treinamento, X_{database_name}_teste, y_{database_name}_teste = pickle.load(f)

# # alternativa; picle quebou o formato do array y_{database_name}_teste

# X_{database_name}_treinamento, X_{database_name}_teste, y_{database_name}_treinamento, y_{database_name}_teste = train_test_split(X_{database_name}, y_{database_name}, test_size = 0.15, random_state = 0)


# # cria a tabela de probabilidades

# naive_{database_name}_data = GaussianNB()
# naive_{database_name}_data.fit(X_{database_name}_treinamento, y_{database_name}_treinamento)


# # previsões

# previsoes = naive_{database_name}_data.predict(X_{database_name}_teste)
# previsoes

# accuracy_score(y_{database_name}_teste, previsoes)


# confusion_matrix(y_{database_name}_teste, previsoes)

# cm = ConfusionMatrix(naive_{database_name}_data)
# cm.fit(X_{database_name}_treinamento, y_{database_name}_treinamento)
# cm.score(X_{database_name}_teste, y_{database_name}_teste)
# cm.show()

# print(classification_report(y_{database_name}_teste, previsoes))




# # Aprendizagem por árvores de decisão

# from sklearn.tree import  DecisionTreeClassifier



# with open('risco_credito.pkl', 'rb') as f:
#     X_risco_credito, y_risco_credito = pickle.load(f)


# arvore_risco_credito = DecisionTreeClassifier(criterion='entropy')
# arvore_risco_credito.fit(X_risco_credito, y_risco_credito)

# arvore_risco_credito.feature_importances_

# from sklearn import tree

# previsores = ['história', 'dívida', 'garantias', 'renda']
# figura, eixos =plt.subplots(nrows=1, ncols=1, figsize=(10,10))
# tree.plot_tree(arvore_risco_credito, feature_names=previsores, class_names = arvore_risco_credito.classes_, filled=True);


# plt.show()
# plt.savefig('arvore_decisao.png')
# previsores = arvore_risco_credito.predict([[0,0,1,2], [2,0,0,0]])





# # base credit.pkl

# with open('credit.pkl', 'rb')as f:
#     X_credit_treinamento, X_credit_teste, y_credit_treinamento, y_credit_teste = pickle.load(f)

# X_credit_treinamento.shape
# X_credit_teste.shape
# y_credit_treinamento.shape
# y_credit_teste.shape


# arvore_credit = DecisionTreeClassifier(criterion='entropy', random_state=0)
# arvore_credit.fit(X_credit_treinamento, y_credit_treinamento)

# previsoes = arvore_credit.predict(X_credit_teste)

# accuracy = accuracy_score(y_credit_teste, previsoes)

# confusion_matrix(y_credit_teste, previsoes)

# cm = ConfusionMatrix(arvore_credit)
# cm.fit(X_credit_treinamento, y_credit_treinamento)
# cm.score(X_credit_teste, y_credit_teste)
# cm.show()

# print(classification_report(y_credit_teste, previsoes))

# previsores = ['income', 'age', 'loan']
# figura, eixos =plt.subplots(nrows=1, ncols=1, figsize=(20,20))
# tree.plot_tree(arvore_credit, feature_names=previsores, class_names =['0', '1'], filled=True);

# plt.show()
# plt.savefig('arvore_decisao2.png')





# # Mesmo procedimento - base do {database_name}

# # base credit.pkl

# with open('{database_name}.pkl', 'rb')as f:
#     X_{database_name}_treinamento, y_{database_name}_treinamento, X_{database_name}_teste, y_{database_name}_teste = pickle.load(f)

# X_{database_name}_treinamento.shape;
# X_{database_name}_teste.shape;
# y_{database_name}_treinamento.shape;
# y_{database_name}_teste.shape;


# arvore_{database_name} = DecisionTreeClassifier(criterion='entropy', random_state=0)
# arvore_{database_name}.fit(X_{database_name}_treinamento, y_{database_name}_treinamento)

# previsoes = arvore_{database_name}.predict(X_{database_name}_teste)

# accuracy = accuracy_score(y_{database_name}_teste, previsoes)

# confusion_matrix(y_{database_name}_teste, previsoes)

# cm = ConfusionMatrix(arvore_{database_name})
# cm.fit(X_{database_name}_treinamento, y_{database_name}_treinamento)
# cm.score(X_{database_name}_teste, y_{database_name}_teste)
# cm.show()

# print(classification_report(y_{database_name}_teste, previsoes))

# previsores = ['income', 'age', 'loan']
# figura, eixos =plt.subplots(nrows=1, ncols=1, figsize=(20,20))
# tree.plot_tree(arvore_{database_name}, feature_names=previsores, class_names =['0', '1'], filled=True);

# plt.show()
# plt.savefig('arvore_decisao3.png')





# def dec_tree(database_name, lista_previsores):
#     name = str(database_name)[0:-4]
    
#     alfa = f'X_{name}_treinamento'
#     beta = f'X_{name}_teste'
#     charlie = f'y_{name}_treinamento'
#     delta = f'y_{name}_teste'
#     arvor = f'arvore_{name}'
#     fig = f'arvore_decisao_{name}.png'
    
#     with open(f'{name}.pkl', 'rb')as g:
#         alfa, charlie, beta, delta = pickle.load(g)
        
#         arvor = DecisionTreeClassifier(criterion='entropy', random_state=0)
#         arvor.fit(alfa, charlie)
        
#         previsoes = arvor.predict(beta)
#         accuracy = accuracy_score(delta, previsoes)
#         confusion_matrix(delta, previsoes)
        
#         cm = ConfusionMatrix(arvor)
#         cm.fit(alfa, charlie)
#         cm.score(beta, delta)
#         cm.show()
        
#         print(classification_report(delta, previsoes)
        
#         figura, eixos =plt.subplots(nrows=1, ncols=1, figsize=(20,20))
#         tree.plot_tree(arvor, feature_names=lista_previsores, class_names =['0', '1'], filled=True);
        
#         plt.show()
#         plt.savefig(fig)

# previsores = ['income', 'age', 'loan']
# dec_tree('credit.pkl', previsores)