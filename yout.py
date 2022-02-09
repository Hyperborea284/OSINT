from urllib import request
from bs4 import BeautifulSoup
import re
import os

from fire import *
from norm import normalize


def youtube_down(dc_01):
    """
    Baixa o vídeo do YouTube no formato mp4
    Busca o título do vídeo e gera a variável
    titulo
    """

    link = dc_01.get('link_yt')
    html = request.urlopen(link).read().decode('utf8')
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find('title')
    titulo = re.sub(r"[^a-zA-Z\s0-9]", '', str(title))[:30]
    dc_01['titulo'] = titulo


    try:
        os.system(f'youtube-dl -c -o tester.mp4 -f 18 {link}')

    #else
        #os.system(f'youtube-dl -c -o tester.mp4 -f 22 {link}')

    finally:
        beta = normalize()

    # Ativa o webdriver pra fazer scraping da página
    #f7 = Firefox()
    #fcr7 = f7.driver_web(f7)
    #f7.youtube(fcr7, link)

    return dc_01