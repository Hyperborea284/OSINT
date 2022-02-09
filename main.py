import os
from datetime import datetime

from yout import youtube_down
from transc import get_large_audio_transcription
from summ import summarize


# Inicio do dicionario dc_01
os.system('clear')
link_input = input("Link do Youtube: ")
dc_01 = {'date': datetime.now(), 'link_yt': link_input}

alfa = youtube_down(dc_01)
charlie = get_large_audio_transcription(dc_01)
delta = summarize()


def analict():
    """
    Analisa (parse) a transcrição e retorna:
    a) similaridades
    b) concordâncias
    c) dispersion plot
    d) diversidade lexical e comprimento do texto

        sorted(set(text3)
        len(set(text3))
        len(text3) / len(set(text3))

    e) termos que mais ocupam espaço no texto
        text3.count("smote")
        100 * text4.count('a') / len(text4)

    f) distribuicao de frequencia
    g) bigrams 'extracting from a text a list of word pairs'
    h) collocations 'collocation is a sequence of words that occur together unusually often'
    i) Polaridade (introversão e extroversão)
    j) Pronoun Resolution '"who did what to whom" — i.e., to detect the subjects and objects of verbs.'
    k) tagger em linggua portuguesa usando dicionário/mac_morpho/Floresta
    l) chunking 
    m) Ambiguidades
    """
    pass


def trained():
    """
    Gera um classificador que analisa e compara
    um texto novo e retorna os elementos compartilhados
    e elementos novos
    """
    pass


def visual():
    """
    Gera nuvens de tags para:
    a) o texto inteiro
    b) melhor score de cada sentimento
    c) resumo
    d) elements percebidos na função analict
    """
    pass


def generator():
    """
    Gera texto com base nas características analisadas
    """
    pass


def bot():
    """
    Usa um agendador para ativar o selenium
    webdriver que busca vídeos para serem analisados;
    """
    pass


def django():
    """
    a) Base para uma aplicação django local;
    Aplicação local recede os inputs do usuário e
    outras configurações;
    b) Assiste pessoal controlado por voz;
    c) Retorna abas no navegador para apresentar os arquivos 
    gerados;
    d) Paywall
    
    """
    pass


def vault():
    """
    cofre de informações
    """
    pass


def dist():
    """
    Calcula a distância euclidiana entre
    os dados novos e os dados antigos;
    Gera recomendações
    """
    pass


def parallel():
    """
    Gera uma instrução em C para
    o procecssamento paralelo na GPU
    """
    pass


def latex():
    """
    Usa da linguagem laTeX para
    gerar um pdf resumindo as informações
    """


def maltego():
    """
    Exporta os dados no formato de uma planilha
    csv que pode ser lida pelo Maltego
    """


def frequ():
    """
    Análise de frequencias usando fourier
    """


def datas():
    """
    Busca strings de datas usando Regex
    """
