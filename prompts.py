from typing import List, Dict
import os
import tiktoken
import inspect
from dotenv import load_dotenv
from utils import memoize_to_db
from openai import APIConnectionError, APIError, RateLimitError, OpenAI

load_dotenv(".env")

class PromptGenerator:
    def __init__(self, nome_banco):
        self.client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
        self.nome_banco = nome_banco

    def todos(self, lista_textos: List[str], model: str) -> None:
        for name, method in inspect.getmembers(self, predicate=inspect.ismethod):
            if name != 'todos' and name != '__init__':
                method(lista_textos, model)

    def generate_messages(self, lista_textos: List[str], bib_file_content: str) -> List[Dict[str, str]]:
        messages = []
        for i, sub_resumo in enumerate(lista_textos):
            sub_resumo_message = {
                "role": "system",
                "content": f"Texto {i+1}: {sub_resumo}"
            }
            messages.append(sub_resumo_message)

        messages.append({
            "role": "system",
            "content": bib_file_content
        })
        return messages

    def generate_response(self, messages: List[Dict[str, str]], model: str) -> str:
        response = self.client.chat.completions.create(
            messages=messages,
            model=model,
            max_tokens=self.remaining_tokens() - 10
        )
        generated_text = response.model_dump()['choices'][0]['message']['content']
        return generated_text
    
    @memoize_to_db(table_name="relato_gpt4")
    def relato(self, lista_textos: List[str], model: str) -> str:
        print(f"Sintetizando {len(lista_textos)} análises em um relato.")
        
        messages = self.generate_messages(lista_textos, self.bib_file_content)

        messages.extend([
            {"role": "user", "content": f"""
                Realize a análise destes textos temáticos.
                Por favor, revise-os e sintetize-os em um único e mais detalhado relatório,
                Este relatório será o trecho de um documento latex.
            """.strip()},
            {"role": "user", "content": f"""
                Este relatório deve ser o mais detalhado possível, possuindo
                grande verbosidade, preferindo a saída mais próxima ao limite de tokens permitido pelo modelo.
                Retorne uma saída com a seguinte estrutura, devidamente decorada com as instruções
                de seção, subseção e, caso necessário, citações e items latex; considere que a existência de um seção sempre antecede a
                existência de uma subseção. Se esforce para manter a continuidade entre as seções, 
                evitando omissões na cobertura dos temas. 
            """.strip()},
            {"role": "user", "content": f"""
                O trecho deve conter única e exclusivamente a string título sem nenhuma decoração latex.
                Adiante somente devem aparecer as seções, subseções latex, listas itemizadas e citações que forem necessárias; 
                Nenhum outro elemento latex deve aparecer, independentemente de sua funcionalidade, 
                contexto, ou qualquer outra razão, seja rígido e estrito acerca desta condição.
            """.strip()},
            {"role": "user", "content": f"""
                Evite estritamente qualquer outra indicação do tipo ''' ''' ou '''latex''' , 
                ou qualquer outra inserção de sinais, 
                indicativos, caracteres especiais desnecessários, ou símbolos visto que estes irão quebrar o código latex gerado; utilize unicamente
                os elementos indicados, na medida em que forem necessários.
            """.strip()},
            {"role": "user", "content": f"""
                Obedeça à sequinte estrutura:
                título - contendo o tema geral dos conteúdos relatados que servirá de título, 
                em uma string sem nenhuma decoração ou instrução latex. 
            """.strip()},
            {"role": "user", "content": f"""
                \section Introdução - Contendo a apresentação do tema geral dos conteúdos.
                insira aqui o texto da seção contendo a apresentação do tema;
            """.strip()},
            {"role": "user", "content": f"""
                \section - sendo uma com o conteúdo de cada um dos temas aprofundados.
                insira aqui o texto respectiva da seção contendo o começo, meio, fim e quando necessário use \cite para citações latex.
                Se assegure de que os blocos \itemize possuam begin e end, evitando trechos abertos e não concluídos.
            """.strip()},
            {"role": "user", "content": f"""
                Se for necessário, para cobrir todos os temas, adicione tantas estruturas do 
                tipo \section, \subsection e \itemize \cite
                tantas quantas forem necessárias para manter a lógica.
            """.strip()},
        ])

        generated_text = self.generate_response(messages, model)
        return generated_text
    
    @memoize_to_db(table_name="questionario_gpt4")
    def questionario(self, lista_textos: List[str], model: str) -> str:
        print(f"Sintetizando {len(lista_textos)} análises em um questionário.")
        
        messages = self.generate_messages(lista_textos, self.bib_file_content)

        messages.extend([
            {"role": "user", "content": f"""
                Realize a análise destes textos temáticos.
                Por favor, revise-os e sintetize-os em um único e mais detalhado questionário.
                Este questionário será o trecho de um documento latex.
            """.strip()},
            {"role": "user", "content": f"""
                O trecho do documento deve conter única e exclusivamente questões profundas nível, 
                de nível superior e pós-graduado, no mesmo nível de questões de concursos para nível superior. 
                Gere o máximo possível de questões, no mínimo 10, todas de alto nível, 
                sobre os temas contidos nos textos, visando cobrir todos os 
                aspectos do conteúdo, sendo cada uma com 4 alternativas A B C D, onde três são respostas erradas e a
                resposta certa aparece numa posição aleatória.
            """.strip()},
            {"role": "user", "content": f"""
                O trecho deve conter única e exclusivamente, i.e,
                somente devem aparecer as seções, subseções latex e listas itemizadas que forem necessárias; 
                Nenhum outro elemento latex deve aparecer, independentemente de sua funcionalidade, 
                contexto, ou qualquer outra razão, seja rígido e estrito acerca desta condição.
            """.strip()},
            {"role": "user", "content": f"""
                Evite estritamente qualquer outra indicação do tipo ''' ''' ou '''latex''' , 
                ou qualquer outra inserção de sinais, 
                indicativos, caracteres especiais desnecessários, ou símbolos visto que estes irão quebrar o código latex gerado; utilize unicamente
                os elementos indicados, na medida em que forem necessários.
            """.strip()},
            {"role": "user", "content": f"""
                Este questionário deve ser o mais detalhado possível, possuindo
                grande verbosidade, preferindo a saída mais próxima ao limite de tokens permitido pelo modelo.
                Retorne uma saída com a seguinte estrutura, devidamente decorada com as instruções
                de seção, subseção e items latex; considere que a existência de um seção sempre antecede a
                existência de uma subseção. Se esforce para manter a continuidade entre as seções, 
                evitando omissões na cobertura dos temas. 
            """.strip()},
            {"role": "user", "content": f"""
                Se for necessário, para cobrir todos os temas, adicione tantas estruturas do 
                tipo \section, \subsection e \itemize
                tantas quantas forem necessárias para manter a lógica.
                Obedeça à sequinte estrutura:
            """.strip()},
            {"role": "user", "content": f"""
                Associe cada uma das questões com uma resposta; 
                use um bloco separado com as seguintes seções, para cada uma das questões:
                \section Questão - contendo o texto da questão;
                \itemize - begin ; Contendo as quatro alternativas; \itemize - end.
                \subsection - Contendo a resposta.
                Se assegure de que os blocos \itemize possuam begin e end, evitando trechos abertos e não concluídos.
            """.strip()},
        ])

        generated_text = self.generate_response(messages, model)
        return generated_text
    
    @memoize_to_db(table_name="entidades_gpt4")
    def entidades(self, lista_textos: List[str], model: str) -> str:
        print(f"Sintetizando {len(lista_textos)} análises em um apontamento das entidades.")
        
        messages = self.generate_messages(lista_textos, self.bib_file_content)

        messages.extend([
            {"role": "user", "content": f"""
                Realize a análise destes textos temáticos.
                Por favor, revise-as e sintetize-as em um único e mais detalhado texto apresentando todas 
                as entidades mencionadas, com atenção para as pessoas físicas, jurídicas, e outros sujeitos presentes nos textos.
                Este texto será o trecho de um documento latex.
            """.strip()},

            {"role": "user", "content": f"""
                O trecho deve conter única e exclusivamente, i.e,
                adiante somente devem aparecer as seções, subseções latex, listas itemizadas e citações que forem necessárias; 
                Nenhum outro elemento latex deve aparecer, independentemente de sua funcionalidade, 
                contexto, ou qualquer outra razão, seja rígido e estrito acerca desta condição.
            """.strip()},
            {"role": "user", "content": f"""
                Evite estritamente qualquer outra indicação do tipo ''' ''' ou '''latex''' , 
                ou qualquer outra inserção de sinais, 
                indicativos, caracteres especiais desnecessários, ou símbolos visto que estes irão quebrar o código latex gerado; utilize unicamente
                os elementos indicados, na medida em que forem necessários.
            """.strip()},
            {"role": "user", "content": f"""
                Este texto deve ser o mais detalhado possível, possuindo
                grande verbosidade, preferindo a saída mais próxima ao limite de tokens permitido pelo modelo.
                Retorne uma saída com a seguinte estrutura, devidamente decorada com as instruções
                de seção, subseção e, caso necessário,items latex; considere que a existência de um seção sempre antecede a
                existência de uma subseção. Se esforce para manter a continuidade entre as seções, 
                evitando omissões na cobertura dos sujeitos. 
            """.strip()},
            {"role": "user", "content": f"""
                Se for necessário, para cobrir todos os sujeitos, adicione tantas estruturas do 
                tipo \section, \subsection, \itemize e, quando necessário, use \cite para citações latex,
                tantas quantas forem necessárias para manter a lógica.
                Se assegure de que os blocos \itemize iniciados sejam gerados de maneira completa, não deixando trechos abertos e não concluídos.
            """.strip()},
        ])

        generated_text = self.generate_response(messages, model)
        return generated_text

    @memoize_to_db(table_name="contexto_gpt4")
    def contexto(self, lista_textos: List[str], model: str) -> str:
        print(f"Sintetizando {len(lista_textos)} análises em um apontamento do contexto analisado.")
        
        messages = self.generate_messages(lista_textos, self.bib_file_content)

        messages.extend([
            {"role": "user", "content": f"""
                Realize a análise destes textos temáticos.
                Por favor, revise-os e sintetize-os em um único e mais detalhado texto apresentando
                o contexto geral, os elementos contextuais e a casuística analisada nos textos.
                Este texto será o trecho de um documento latex.
            """.strip()},
            {"role": "user", "content": f"""
                O trecho deve conter única e exclusivamente, i.e,
                adiante somente devem aparecer as seções, subseções latex, listas itemizadas e citações que forem necessárias; 
                Nenhum outro elemento latex deve aparecer, independentemente de sua funcionalidade, 
                contexto, ou qualquer outra razão, seja rígido e estrito acerca desta condição.
            """.strip()},
            {"role": "user", "content": f"""
                Evite estritamente qualquer outra indicação do tipo ''' ''' ou '''latex''' , 
                ou qualquer outra inserção de sinais, 
                indicativos, caracteres especiais desnecessários, ou símbolos visto que estes irão quebrar o código latex gerado; utilize unicamente
                os elementos indicados, na medida em que forem necessários.
            """.strip()},
            {"role": "user", "content": f"""
                Este texto deve ser o mais detalhado possível, possuindo
                grande verbosidade, preferindo a saída mais próxima ao limite de tokens permitido pelo modelo.
                Retorne uma saída com a seguinte estrutura, devidamente decorada com as instruções
                de seção, subseção e, caso necessário,items latex; considere que a existência de um seção sempre antecede a
                existência de uma subseção. Se esforce para manter a continuidade entre as seções, 
                evitando omissões na cobertura dos sujeitos. 
            """.strip()},
            {"role": "user", "content": f"""
                Se for necessário, para cobrir todos os elementos contextuais, adicione tantas estruturas do 
                tipo \section, \subsection, \itemize e, quando necessário, use \cite para citações latex,
                tantas quantas forem necessárias para manter a lógica.
                Se assegure de que os blocos \itemize iniciados sejam gerados de maneira completa, não deixando trechos abertos e não concluídos.
            """.strip()},
        ])

        generated_text = self.generate_response(messages, model)
        return generated_text

    @memoize_to_db(table_name="linha_tempo_gpt4")
    def linha_tempo(self, lista_textos: List[str], model: str) -> str:
        print(f"Sintetizando {len(lista_textos)} análises em uma linha do tempo.")
        
        messages = self.generate_messages(lista_textos, self.bib_file_content)

        messages.extend([
            {"role": "user", "content": f"""
                Realize a análise destes textos temáticos.
                Por favor, revise-os e sintetize-os em um único e mais detalhado texto apresentando todas 
                as linhas do tempo deduzidas do conteúdo ou explícitamente mencionadas,
                com atenção para as sequências lógicas de eventos presentes nos textos.
                Este texto será o trecho de um documento latex.
            """.strip()},
            {"role": "user", "content": f"""
                O trecho deve conter única e exclusivamente, i.e,
                adiante somente devem aparecer as seções, subseções latex, listas itemizadas e citações que forem necessárias; 
                Nenhum outro elemento latex deve aparecer, independentemente de sua funcionalidade, 
                contexto, ou qualquer outra razão, seja rígido e estrito acerca desta condição.
            """.strip()},
            {"role": "user", "content": f"""
                Evite estritamente qualquer outra indicação do tipo ''' ''' ou '''latex''' , 
                ou qualquer outra inserção de sinais, 
                indicativos, caracteres especiais desnecessários, ou símbolos visto que estes irão quebrar o código latex gerado; utilize unicamente
                os elementos indicados, na medida em que forem necessários.
            """.strip()},
            {"role": "user", "content": f"""
                Este texto deve ser o mais detalhado possível, possuindo
                grande verbosidade, preferindo a saída mais próxima ao limite de tokens permitido pelo modelo.
                Retorne uma saída com a seguinte estrutura, devidamente decorada com as instruções
                de seção, subseção e, caso necessário, citações e items latex; considere que a existência de um seção sempre antecede a
                existência de uma subseção. Se esforce para manter a continuidade entre as seções, 
                evitando omissões na cobertura das sequências temporais dos eventos. 
            """.strip()},
            {"role": "user", "content": f"""
                Se for necessário, para cobrir todas as sequências temporais dos eventos, adicione tantas estruturas do 
                tipo \section, \subsection, \itemize e, quando necessário, use \cite para citações latex,
                tantas quantas forem necessárias para manter a lógica.
                Se assegure de que os blocos \itemize possuam begin e end, evitando trechos abertos e não concluídos.
            """.strip()},
        ])

        generated_text = self.generate_response(messages, model)
        return generated_text

    @memoize_to_db(table_name="contradicoes_gpt4")
    def contradicoes(self, lista_textos: List[str], model: str) -> str:
        print(f"Sintetizando {len(lista_textos)} análises em uma linha do tempo.")
        
        messages = self.generate_messages(lista_textos, self.bib_file_content)

        messages.extend([
            {"role": "user", "content": f"""
                Realize a análise destes textos temáticos.
                Por favor, revise-os e sintetize-os em um único e mais detalhado texto apresentando todas 
                as contradições, polarizações e tensões dialéticas presentes nos textos,
                com atenção para as extremidades das polarizações presentes nos textos.
                Este texto será o trecho de um documento latex.
            """.strip()},
            {"role": "user", "content": f"""
                O trecho deve conter única e exclusivamente, i.e,
                adiante somente devem aparecer as seções, subseções latex, listas itemizadas e citações que forem necessárias; 
                Nenhum outro elemento latex deve aparecer, independentemente de sua funcionalidade, 
                contexto, ou qualquer outra razão, seja rígido e estrito acerca desta condição.
            """.strip()},
            {"role": "user", "content": f"""
                Evite estritamente qualquer outra indicação do tipo ''' ''' ou '''latex''' , 
                ou qualquer outra inserção de sinais, 
                indicativos, caracteres especiais desnecessários, ou símbolos visto que estes irão quebrar o código latex gerado; utilize unicamente
                os elementos indicados, na medida em que forem necessários.
            """.strip()},
            {"role": "user", "content": f"""
                Este texto deve ser o mais detalhado possível, possuindo
                grande verbosidade, preferindo a saída mais próxima ao limite de tokens permitido pelo modelo.
                Retorne uma saída com a seguinte estrutura, devidamente decorada com as instruções
                de seção, subseção e, caso necessário, citações e items latex; considere que a existência de um seção sempre antecede a
                existência de uma subseção. Se esforce para manter a continuidade entre as seções, 
                evitando omissões na cobertura das sequências temporais dos eventos. 
            """.strip()},
            {"role": "user", "content": f"""
                Se for necessário, para cobrir todas as sequências temporais dos eventos, adicione tantas estruturas do 
                tipo \section, \subsection, \itemize e, quando necessário, use \cite para citações latex,
                tantas quantas forem necessárias para manter a lógica.
                Se assegure de que os blocos \itemize possuam begin e end, evitando trechos abertos e não concluídos.
            """.strip()},
        ])

        generated_text = self.generate_response(messages, model)
        return generated_text
    
    @memoize_to_db(table_name="conclusao_gpt4")
    def conclusao(self, lista_textos: List[str], model: str) -> str:
        print(f"Sintetizando {len(lista_textos)} análises em uma conclusão.")
        
        messages = self.generate_messages(lista_textos, self.bib_file_content)

        messages.extend([
            {"role": "user", "content": f"""
                Realize a análise destes textos temáticos.
                Por favor, revise-os e sintetize-os em um único e mais detalhado texto apresentando
                uma conclusão sintética dos conteúdos presentes nos textos,
                com atenção para as implicações dos temas presentes nos textos.
                Este texto será o trecho de um documento latex.
            """.strip()},
            {"role": "user", "content": f"""
                O trecho deve conter única e exclusivamente, i.e,
                somente devem aparecer a seção latex.
                Nenhum outro elemento latex deve aparecer, independentemente de sua funcionalidade, 
                contexto, ou qualquer outra razão, seja rígido e estrito acerca desta condição.
            """.strip()},
            {"role": "user", "content": f"""
                Evite estritamente qualquer outra indicação do tipo ''' ''' ou '''latex''' , 
                ou qualquer outra inserção de sinais, 
                indicativos, caracteres especiais desnecessários, ou símbolos visto que estes irão quebrar o código latex gerado; utilize unicamente
                os elementos indicados, na medida em que forem necessários.
            """.strip()},
            {"role": "user", "content": f"""
                Este texto deve ser o mais detalhado possível, possuindo
                grande verbosidade, preferindo a saída mais próxima ao limite de tokens permitido pelo modelo.
            """.strip()},
        ])

        generated_text = self.generate_response(messages, model)
        return generated_text