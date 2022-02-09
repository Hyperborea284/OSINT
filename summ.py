import nltk


def summarize():
    """
    Abre a transcrição e retorna uma lista 
    contendo cada linha do dicionário 
    """

    with open('transcricao.txt', 'r', encoding='utf8') as f:

        summary = ''

        transc = []
        transc_lines = f.readlines()
        for line in transc_lines:
            alfa = line.split()
            transc.append(alfa)

        stopwords = nltk.corpus.stopwords.words('portuguese')

        # Cria um dicionário contendo a frequencia 
        # de cada palavra

        freq_table = {}
        for words in transc:
            for word in words:
                word = word.lower()
                if word in stopwords:
                    continue
                if word in freq_table:
                    freq_table[word] += 1
                else:
                    freq_table[word] = 1

        # Cria um dicionário contendo a frequencia
        # de cada frase

        sentence_value = {}

        for line in transc_lines:
            sentences = nltk.sent_tokenize(line)

            for sentence in sentences:
                for word, freq in freq_table.items():
                    if word in sentence.lower():
                        if sentence in sentence_value:
                            sentence_value[sentence] += freq
                        else:
                            sentence_value[sentence] = freq

            sum_values = 0
            for sentence in sentence_value:
                sum_values += sentence_value[sentence]

            # Calcula a média do valor de cada
            # sentença presente no texto original

            average = int(sum_values / len(sentence_value))

            # Armazena as sentenças no sumário

            for sentence in sentences:
                if (sentence in sentence_value) and (sentence_value[sentence] > (1.2 * average)):
                    summary += " " + sentence

        resume = open('resume.txt', 'w')
        resume.write(f'{summary}')
        resume.close()

    return summary
