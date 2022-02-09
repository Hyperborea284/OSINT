import csv
import os
import re
import numpy as np
import matplotlib.pyplot as plt

"""
Trocar a manipulação de listas 
por um pandas dataframe
"""

def loader():
    datum = []
    path = "./scores"
    dirct = os.listdir(path)
    
    for file in dirct:
        filename = f'./scores/{file}'
        fileread = open(filename, 'r')
        read = csv.reader(fileread, delimiter = ',')
    
        for col in read:
            print(col)
            datum.append(col['resultado'])
    
    data_01 = []
    
    for data in datum:
        data_01.append(data.split(' '))

    data_clean = []

    for i in data_01:
        delta_0 = re.sub(r"[^a-zA-Z\s0-9\d.]", '', str(i))
        data_clean.append(delta_0.split(' '))


    return data_clean


def isolator(sent):

    alfa = loader()
    holder = []

    for i in range(0, len(alfa)):
        for _ in range(0, len(alfa[i])):
            if str(sent) in alfa[i][_]:
                try:
                    holder.append([alfa[i][_],
                                   alfa[i][int(_)+1],
                                   alfa[i][int(_)+2],
                                   alfa[i][int(_)+3]])
                except IndexError:
                    pass
        
    return holder


def cleaner(conj):
    h = isolator(str(conj))
    
    final = []
    
    for i in range(0, len(h)):

        delta_1 = h[i][1]
        delta_3 = h[i][3]

        delta_0 = h[i][0]
        delta_2 = h[i][2]

        final.append(f'{delta_0} {delta_2} {delta_1} {delta_3} {abs(float(delta_1) - float(delta_3))}')

    return final


def graphics(result):

    sents = ['raiva', 'alegria', 'medo', 'tristeza', 'surpresa', 'desgosto']

    for sent in sents:

        context = []
        result = cleaner(sent)

        for i in result:
            context.append(i.split(' '))


        def plotter(context):

            ([float_number, sents_string])

            dt = 0.001
            t = np.arange(0, 1, dt)
            numbers = np.array(float_number, dtype=np.float)

            # Compute the Fast Fourier Transform FFT
            n = len(t)                              
            fhat = np.fft.fft(numbers,n)                    #   Compute the FFT
            PSD = fhat * np.conj(fhat) / n                  #   Power spectrum (power per freq)
            freq = (1/(dt*n)) * np.arange(n)                #   Create x-axis of frequencies in Hz
            L = np.arange(1, np.floor(n/2), dtype='int')    #   Only plot the first half of freqs
            
            fig,axs = plt.subplots(3,1)
            
            plt.sca(axs[0])
            plt.plot(t,float_number, color='c', linewidth=1.5, label=f'{sents_string}')
            plt.xlim(t[0], t[-1])
            plt.legend()
            
            plt.sca(axs[1])
            plt.plot(freq[L], PSD[L], color='c', linewidth=2, label=f'{sents_string}')
            plt.xlim(freq[L[0]], freq[L[-1]])
            plt.legend()
            
            
            # Use the PSD to filter out the noise
            indices = PSD > 0.5
            PSDclean = PSD * indices
            fhat = indices * fhat
            ffilt = np.fft.ifft(fhat)
            
            plt.sca(axs[2])
            plt.plot(freq[L], PSD[L], color='c', linewidth=2, label=f'{sents_string}')
            plt.xlim(freq[L[0]], freq[L[-1]])
            plt.legend()
            
            plt.show()

    plotter(float_number, sents_string)

graphics(result)