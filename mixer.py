import itertools
import nltk
from base import *


def mixer(sent, dc_01):
    """
    Recebe uma string a arranja todas as 
    possíveis combinações que montam
    a função caller(sen1, sen2, frase)

    Parâmetros: list_desgosto, list_medo, list_surpresa, 
    list_tristeza, list_raiva, list_alegria
    """

    list_desgosto = desgosto()
    list_medo = medo()
    list_surpresa = surpresa()
    list_tristeza = tristeza()
    list_raiva = raiva()
    list_alegria = alegria()

    def caller(sen1, sen2, frase):
        """
        Recebe um chamado no formato seguinte e retorna a análise de 
        sentimento da frase:
    
        caller(list_alegria, list_tristeza, 'sai daqui que dia ruim')
        ['alegria: 0.171988', 'tristeza: 0.828012']
        """

        stopwordsnltk = nltk.corpus.stopwords.words('portuguese')

        basetreinamento = sen1 + sen2

        def aplicastemmer(texto):
            stemmer = nltk.stem.RSLPStemmer()
            frasessteemining = []
            for (palavras, emocao) in texto:
                comsteeming = [str(stemmer.stem(p)) for p in palavras.split() if p not in stopwordsnltk]
                frasessteemining.append((comsteeming, emocao))
            return frasessteemining

        frasessteemining = aplicastemmer(basetreinamento)

        def buscapalavras(frases):
            todaspalavras = []
            for (palavras, emocao) in frases:
                todaspalavras.extend(palavras)
            return todaspalavras

        palavras = buscapalavras(frasessteemining)

        def buscafrequencia(palavras):
            palavras = nltk.FreqDist(palavras)
            return palavras

        frequencia = buscafrequencia(palavras)

        def buscapalavrasunicas(frequencia):
            freq = frequencia.keys()
            return freq

        palavrasunicas = buscapalavrasunicas(frequencia)

        def extratorpalavras(documento):
            doc = set(documento)
            caracteristicas = {}
            for palavras in palavrasunicas:
                caracteristicas['%s' % palavras] = (palavras in doc)
            return caracteristicas

        basecompleta = nltk.classify.apply_features(extratorpalavras, frasessteemining)
        classificador = nltk.NaiveBayesClassifier.train(basecompleta)

        teste = frase

        testesteeming = []
        stemmer = nltk.stem.RSLPStemmer()

        for palavras in teste.split():
            comstem = [p for p in palavras.split()]
            testesteeming.append(str(stemmer.stem(comstem[0])))

        novo = extratorpalavras(testesteeming)

        result = []
        distribuicao = classificador.prob_classify(novo)

        for classe in distribuicao.samples():
            result.append(str("%s: %f" % (classe, distribuicao.prob(classe))))

        return result

    unique_combinations = []

    list_1 = ['list_desgosto', 'list_medo', 'list_surpresa',
              'list_tristeza', 'list_raiva', 'list_alegria']

    list_2 = ['list_desgosto', 'list_medo', 'list_surpresa',
              'list_tristeza', 'list_raiva', 'list_alegria']

    for r in itertools.product(list_1, list_2):
        if r[0] != r[1]:
            e1 = f"caller{r[0], r[1]}"
            e2 = e1.replace("'", "")
            e3 = f"{e2}"

            unique_combinations.append(e3)

    sent_combinations = []

    for i in unique_combinations:
        d1 = f'{i, sent}'
        d2 = d1.replace(")',", ",")
        d3 = d2.replace('"(', '')
        d4 = d3.replace("('", '')
        sent_combinations.append(d4)

    final = []
    for l in sent_combinations:
        alfa = eval(l)
        final.append(alfa)

    dc_01['resultado'] = final
    return final
