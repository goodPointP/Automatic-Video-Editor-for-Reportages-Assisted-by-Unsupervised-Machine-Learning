
#https://www.machinelearningplus.com/nlp/topic-modeling-visualization-how-to-present-results-lda-models/#5.-Build-the-Topic-Model


#import paketa
import sys
# !{sys.executable} -m spacy download en
import re, numpy as np
from pprint import pprint

# Gensim
import gensim, spacy, logging, warnings
import gensim.corpora as corpora
from gensim.utils import lemmatize, simple_preprocess
from gensim.models import CoherenceModel
import matplotlib.pyplot as plt
import csv
import numpy as np
#ignoriraj upozorenja o starijoj verziji modula gensim
warnings.filterwarnings('ignore')

def getTopics():
    import pandas as pd
    
    #citanje dokumenta, dohvacanje jednog stupca kao liste
    data = pd.read_csv('project.csv', encoding='utf8')
    
    df = pd.DataFrame(data)
    sveRecenice = df[df.columns[5]]
    
    sveRecenice = sveRecenice.to_frame()
    #print(type(sveRecenice))
    
    # NLTK Stop words
    from nltk.corpus import stopwords
    stop_words = stopwords.words('english')
    stop_words.extend(['from', 'subject', 're', 'edu', 'use', 'not', 'would', 'say', 'could', '_', 'be', 'know', 'good', 'go', 'get', 'do', 'done', 'try', 'many', 'some', 'nice', 'thank', 'think', 'see', 'rather', 'easy', 'easily', 'lot', 'lack', 'make', 'want', 'seem', 'run', 'need', 'even', 'right', 'line', 'even', 'also', 'may', 'take', 'come', 'thing'])

    #warnings.filterwarnings("ignore",category=DeprecationWarning)
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.ERROR)

    #tokenizacija - razdvajanje svih recenica u listu rijeci, micanje punktuacije
    data = sveRecenice.values.tolist()
    def sent_to_words(sentences):
        for sentence in sentences:
            yield(gensim.utils.simple_preprocess(str(sentence), deacc=True))  # deacc=True mice punktuaciju

    data_words = list(sent_to_words(data))

    print(data_words)

    #stvaranje preduvjeta za stvaranje bigrama i trigrama

    bigram = gensim.models.Phrases(data_words, min_count=2, threshold=100) # higher threshold fewer phrases.
    trigram = gensim.models.Phrases(bigram[data_words], threshold=100)

    bigram_mod = gensim.models.phrases.Phraser(bigram)
    trigram_mod = gensim.models.phrases.Phraser(trigram)

    #micanje stopwords i lematizacija
    def process_words(texts, stop_words=stop_words, allowed_postags=['NOUN']): #'VERB','ADJ', 'ADJ', ,'VERB', 'ADV' su izbaceni jer se teme intervjua najcesce svode upravo na jednu temu
        """Remove Stopwords, Form Bigrams, Trigrams and Lemmatization"""
        texts = [[word for word in simple_preprocess(str(doc)) if word not in stop_words] for doc in texts]
        texts = [bigram_mod[doc] for doc in texts]
        texts = [trigram_mod[bigram_mod[doc]] for doc in texts]
        
        texts_out = []
        nlp = spacy.load('en_core_web_md', disable=['parser', 'ner'])
        for sent in texts:
            doc = nlp(" ".join(sent)) 
            texts_out.append([token.lemma_ for token in doc if token.pos_ in allowed_postags])
        # remove stopwords once more after lemmatization
        texts_out = [[word for word in simple_preprocess(str(doc)) if word not in stop_words] for doc in texts_out]    
        return texts_out

    data_ready = process_words(data_words)  # processed Text Data!

    #stvaranje topic modela
    # Create a Dictionary
    id2word = corpora.Dictionary(data_ready)
    
    # Create a Corpus: Term Document Frequency
    corpus = [id2word.doc2bow(text) for text in data_ready]
    
    # Build LDA model
    lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                               id2word=id2word,
                                               num_topics=2, 
                                               random_state=100,
                                               update_every=1,
                                               chunksize=10,
                                               passes=1000,
                                               alpha='symmetric',
                                               iterations=100,
                                               per_word_topics=True)

    pprint(lda_model.print_topics())

    # dominantan topic
    def format_topics_sentences(ldamodel=None, corpus=corpus, texts=data):
        # Init output
        sent_topics_df = pd.DataFrame()

##        # Get main topic in each document
        for i, row_list in enumerate(ldamodel[corpus]):
            row = row_list[0] if ldamodel.per_word_topics else row_list            
            # print(row)
            row = sorted(row, key=lambda x: (x[1]), reverse=True)
            # Get the Dominant topic, Perc Contribution and Keywords for each document
            for j, (topic_num, prop_topic) in enumerate(row):
                if j == 0:  # => dominant topic
                    wp = ldamodel.show_topic(topic_num)
                    topic_keywords = ", ".join([word for word, prop in wp])
                    sent_topics_df = sent_topics_df.append(pd.Series([int(topic_num), round(prop_topic,4), topic_keywords]), ignore_index=True)
                else:
                    break
        sent_topics_df.columns = ['Dominant_Topic', 'Perc_Contribution', 'Topic_Keywords']

        # Add original text to the end of the output
        contents = pd.Series(texts)
        sent_topics_df = pd.concat([sent_topics_df, contents], axis=1)
        return(sent_topics_df)


    df_topic_sents_keywords = format_topics_sentences(ldamodel=lda_model, corpus=corpus, texts=data_ready)

    # Format
    df_dominant_topic = df_topic_sents_keywords.reset_index()
    df_dominant_topic.columns = ['Document_No', 'Dominant_Topic', 'Topic_Perc_Contrib', 'Keywords', 'Text']
    df_dominant_topic.columns = ['Document_No', 'Dominant_Topic', 'Topic_Perc_Contrib', 'Keywords', 'Text']
    df_dominant_topic.head(10)
   # print(type(df_dominant_topic))

    #print(df_dominant_topic)
    df = df_dominant_topic['Keywords']
    #print(df)
    #zapisivanje tema u .csv za svaki red
    temeBezHeadera = df.values.tolist()
    for i in range(len(temeBezHeadera)):
        print(i)
        temeBezHeadera[i] = re.split(',', temeBezHeadera[i])[0]
    #print(temeBezHeadera)
    #print(type(temeBezHeadera))
    #temeBezHeadera.pop(0)
    dokumentZaPisanje = pd.read_csv('project.csv')
    dokumentZaPisanje["Tema"]= temeBezHeadera
    
    
    dokumentZaPisanje.to_csv("project.csv",index=False)
##    with open('project.csv', 'a') as fileZaPisanje:
##        writer = csv.writer(fileZaPisanje)
##        writer.writerows(df.values.tolist())
    
##    
# getTopics()