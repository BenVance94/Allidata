import pandas as pd
import nltk
#nltk.download('punkt')
#nltk.download('vader_lexicon')
#nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize, RegexpTokenizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class vaderGator:

    def __init__(self, text):
        self.text = text

    def overallSentiment(self):
        sentence = str(self.text)
        tokenized_sentence = nltk.word_tokenize(sentence)

        sid = SentimentIntensityAnalyzer()
        pos_word_list=[]
        neu_word_list=[]
        neg_word_list=[]

        for word in tokenized_sentence:
            if (sid.polarity_scores(word)['compound']) >= 0.1:
                pos_word_list.append(word)
            elif (sid.polarity_scores(word)['compound']) <= -0.1:
                neg_word_list.append(word)
            else:
                neu_word_list.append(word)
        score = sid.polarity_scores(sentence)
        return pd.Series((score['compound'],score['pos'],score['neu'],score['neg'],pos_word_list,neu_word_list,neg_word_list))

    def partOfSpeech(self):
        pos_type_list=[]
        coordinating_conjunction=0
        cardinal_digit=0
        determiner=0
        existential=0
        foreign=0
        preposition=0
        adjective=0
        numbering=0
        modal=0
        noun=0
        possessive=0
        pronoun=0
        adverb=0
        giveup=0
        to_go=0
        interjection=0
        verb=0
        tokens=nltk.word_tokenize(str(self.text))
        for row0 in nltk.pos_tag(tokens):
            pos_type_list.append(row0[1])
        for row1 in pos_type_list:
            if 'CC' in row1:
                coordinating_conjunction = coordinating_conjunction + 1
            elif 'CD' in row1:
                cardinal_digit = cardinal_digit + 1
            elif 'DT' in row1:
                determiner = determiner + 1
            elif 'EX' in row1:
                existential = existential + 1
            elif 'FW' in row1:
                foreign = foreign + 1
            elif 'IN' in row1:
                preposition = preposition + 1
            elif 'JJ' in row1:
                adjective = adjective + 1
            elif 'LS' in row1:
                numbering = numbering + 1
            elif 'MD' in row1:
                modal = modal + 1
            elif 'NN' in row1:
                noun = noun + 1
            elif 'POS' in row1:
                possessive = possessive + 1
            elif 'PRP' in row1 or 'WP' in row1:
                pronoun = pronoun + 1
            elif 'RB' in row1:
                adverb = adverb + 1
            elif 'RP' in row1:
                giveup = giveup + 1
            elif 'TO' in row1:
                to_go = to_go + 1
            elif 'UH' in row1:
                interjection = interjection + 1
            elif 'VB' in row1:
                verb = verb + 1
        return pd.Series((coordinating_conjunction,cardinal_digit,determiner,existential,foreign,preposition,adjective,numbering,modal,noun,possessive,pronoun,adverb,giveup,to_go,interjection,verb))
