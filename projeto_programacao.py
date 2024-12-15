import csv


tweets_dict = {}

path = 'C:\\Users\\educo\\Downloads\\Tweets.csv\\'

file_name = 'Tweets.csv'

#Tira os dados do ficheiro csv e põem num dicionário

with open(path + file_name, encoding='utf-8') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        tweet_id = row[0]
        airline_sentiment = row[1]
        airline_sentiment_confidence = row[2]
        negative_reason = row[3]
        negative_reason_confidence = row[4]
        airline = row[5]
        airline_sentiment_gold = row[6]
        name = row[7]
        negative_reason_gold = row[8]
        retweet_count = row[9]
        text = row[10]
        text_coord = row[11]
        tweet_created = row[12]
        tweet_location = row[13]
        tweets_dict[tweet_id] = {
            'airline_sentiment': airline_sentiment,
            'airline_sentiment_confidence': airline_sentiment_confidence,
            'negative_reason': negative_reason,
            'negative_reason_confidence': negative_reason_confidence,
            'airline': airline, 'airline_sentiment_gold': airline_sentiment_gold,
            'name': name, 'negative_reason_gold': negative_reason_gold,
            'retweet_count': retweet_count,
            'text': text,
            'text_coord': text_coord,
            'tweet_created': tweet_created,
            'tweet_location': tweet_location
        }

#print(tweets_dict)

#Contar o número de tweets por sentimento

def numero_de_tweets_por_sentimento(tweets_dict):

    tweets_negativos = 0
    tweets_neutros = 0
    tweets_positivos = 0

    for tweet_id in tweets_dict:
        if tweets_dict[tweet_id]['airline_sentiment'] == 'negative':
            tweets_negativos += 1
        elif tweets_dict[tweet_id]['airline_sentiment'] == 'neutral':
            tweets_neutros += 1
        else:
            tweets_positivos += 1

    print(f'Número de tweets negativos: {tweets_negativos}')
    print(f'Número de tweets neutros: {tweets_neutros}')
    print(f'Número de tweets positivos: {tweets_positivos}')


#numero_de_tweets_por_sentimento(tweets_dict)

#Calcular a percentagem de cada tipo de sentimento para todas as companhias aéreas

def sentimento_por_companhia_percentagem(tweets_dict):

    total_por_companhia = {}
    sentimentos_por_companhia = {}

    for tweet_id in tweets_dict:
        companhia = tweets_dict[tweet_id]['airline']
        sentimento = tweets_dict[tweet_id]['airline_sentiment']

        if companhia == 'airline':
            continue


        if companhia not in total_por_companhia:
            total_por_companhia[companhia] = 0
            sentimentos_por_companhia[companhia] = {'negative': 0, 'neutral': 0, 'positive': 0}

        else:
            total_por_companhia[companhia] += 1


        if sentimento in sentimentos_por_companhia[companhia]:
            sentimentos_por_companhia[companhia][sentimento] += 1


    for companhia in total_por_companhia:
        total = total_por_companhia[companhia]
        sentimento_negativo = sentimentos_por_companhia[companhia]['negative']
        sentimento_neutro = sentimentos_por_companhia[companhia]['neutral']
        sentimento_positivo = sentimentos_por_companhia[companhia]['positive']

        print(f'Sentimentos negativos da companhia {companhia} é {(sentimento_negativo / total) * 100:.2f}%')
        print(f'Sentimentos positivos da companhia {companhia} é {(sentimento_positivo / total) * 100:.2f}%')
        print(f'Sentimentos neutros da companhia {companhia} é {(sentimento_neutro / total) * 100:.2f}%')




    print(f'Total por companhia {total_por_companhia}')
    print(f'Sentimentos por companhia {sentimentos_por_companhia}')


#sentimento_por_companhia_percentagem(tweets_dict)

#Identificar a companhia aérea com o maior número de tweets positivos

def companhia_com_maior_numero_positivo(tweets_dict):

    sentimentos_por_companhia = {}
    companhia_positiva = {}

    for tweet_id in tweets_dict:
        tweet = tweets_dict[tweet_id]
        # Verifica se as chaves 'airline' e 'airline_sentiment' existem
        if 'airline' in tweet and 'airline_sentiment' in tweet:
            companhia = tweet['airline']
            sentimento = tweet['airline_sentiment']

            if companhia == 'airline':
                continue

            if companhia not in sentimentos_por_companhia:
                sentimentos_por_companhia[companhia] = {'negative': 0, 'neutral': 0, 'positive': 0}

            # Incrementa o sentimento correspondente
            if sentimento in sentimentos_por_companhia[companhia]:
                sentimentos_por_companhia[companhia][sentimento] += 1

    for key in sentimentos_por_companhia:
        comp = key
        numero = sentimentos_por_companhia[key]['positive']

        if comp not in companhia_positiva:
            companhia_positiva[comp] = numero

        maior_valor = max(companhia_positiva.values())
        chave = [chave for chave, valor in companhia_positiva.items() if valor == maior_valor][0]


    #print(sentimentos_por_companhia)
    #print(companhia_positiva)
    print(chave)



#companhia_com_maior_numero_positivo(tweets_dict)

#Analisar o número médio de retweets por tipo de sentimento

#Listar todas as companhias aéreas mencionadas no dataset

def listar_companhias(tweets_dict):

    companhias = []

    for tweet_id in tweets_dict:
        companhia = tweets_dict[tweet_id]['airline']

        if companhia == 'airline':
            continue

        if companhia not in companhias:
            companhias.append(companhia)

        else:
            pass

    print(companhias)

#listar_companhias(tweets_dict)

#Identificar a companhia com mais tweets negativos

def compnhia_com_mais_tweets_negativos(tweets_dict):

    sentimentos_por_companhia = {}
    companhia_negativa = {}

    for tweet_id in tweets_dict:
        tweet = tweets_dict[tweet_id]
        # Verifica se as chaves 'airline' e 'airline_sentiment' existem
        if 'airline' in tweet and 'airline_sentiment' in tweet:
            companhia = tweet['airline']
            sentimento = tweet['airline_sentiment']

            if companhia == 'airline':
                continue

            if companhia not in sentimentos_por_companhia:
                sentimentos_por_companhia[companhia] = {'negative': 0, 'neutral': 0, 'positive': 0}

            # Incrementa o sentimento correspondente
            if sentimento in sentimentos_por_companhia[companhia]:
                sentimentos_por_companhia[companhia][sentimento] += 1

    for key in sentimentos_por_companhia:
        comp = key
        numero = sentimentos_por_companhia[key]['negative']

        if comp not in companhia_negativa:
            companhia_negativa[comp] = numero

        maior_valor = max(companhia_negativa.values())
        chave = [chave for chave, valor in companhia_negativa.items() if valor == maior_valor][0]


    #print(sentimentos_por_companhia)
    #print(companhia_positiva)
    print(chave)

#compnhia_com_mais_tweets_negativos(tweets_dict)

#Calcular o número total de tweets por companhia

def total_tweets_por_companhia(tweets_dict):

    total_companhia = {}

    for tweet_id in tweets_dict:

        companhia = tweets_dict[tweet_id]['airline']

        if companhia == 'airline':
            continue

        if companhia not in total_companhia:
            total_companhia[companhia] = 0

        else:
            total_companhia[companhia] += 1

    print(total_companhia)

#total_tweets_por_companhia(tweets_dict)

#Filtrar os tweets de uma companhia específica e mostrar seus detalhes

def tweets_especificos_por_companhia(tweets_dict):

    comp = input('Digite a companhia que deseja ter informações:')

    dict_da_companhia = {}

    for tweet_id in tweets_dict:

        companhia = tweets_dict[tweet_id]['airline']

        if comp == companhia:
            if companhia not in dict_da_companhia:
                dict_da_companhia[companhia] = []

            dict_da_companhia[companhia].append(tweets_dict[tweet_id])

    print(dict_da_companhia)

#tweets_especificos_por_companhia(tweets_dict)

#Identificar o dia com maior número de tweets

#'tweet_created': '2015-02-24 00:48:26 -0800'

def dia_com_mais_tweets(tweets_dict):

    dias = {}

    for tweet_id in tweets_dict:
        dia = tweets_dict[tweet_id]['tweet_created'].split()[0]

        if dia == 'tweet_created':
            continue

        if dia not in dias:
            dias[dia] = 0

        else:
            dias[dia] += 1

    maior_valor = max(dias.values())
    chave = [chave for chave, valor in dias.items() if valor == maior_valor][0]

    print(f'O dia com mais tweets foi {chave}')

#dia_com_mais_tweets(tweets_dict)

#Contar quantos tweets foram feitos num determinado mês ou ano

def contar_numero_tweets(tweets_dict):

    dado1 = input('Digite se deseja contar os tweets de uma ano ou um mês:')

    if dado1 == 'mês':

        dado2 = input('Digite o mês que deseja saber quantos tweets existiram:')

        contagem_mes = 0

        for tweet_id in tweets_dict:

            dia = tweets_dict[tweet_id]['tweet_created'].split()[0].split('-')[1]

            if dia == dado2:
                contagem_mes += 1

        print(f'No ano {dado2} houveram {contagem_mes} tweets.')

    else:

        dado3 = input('Digite o ano que deseja saber quantos tweets existiram:')

        contagem_ano = 0

        for tweet_id in tweets_dict:

            ano = tweets_dict[tweet_id]['tweet_created'].split()[0].split('-')[0]

            if ano == dado3:
                contagem_ano += 1

    print(f'No ano {dado3} houveram {contagem_ano} tweets.')


contar_numero_tweets(tweets_dict)