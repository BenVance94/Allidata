print("Chomp!\nChomp!\nChomp!")
import pandas as pd
from vaderGator import vaderGator
from gatorSoup import gatorSoup
from utils import (get_time_vars,get_directory,save_fakenews)
from config import *

yr,mth,day,hr,min,sec = get_time_vars()
startTime = int(str(yr)+str(mth)+str(day)+str(hr)+str(min)+str(sec))

media_list = followingMedia['mediaSites']

df = pd.DataFrame(columns=["mediaText","mediaUrl","responseStatusCode"])
for row in media_list:
    df_temp = gatorSoup(row).chomp()
    df = pd.concat([df,df_temp],ignore_index=True, sort=True)

df[['score_compound','score_pos','score_neu','score_neg','pos_words','neu_words','neg_words']] = df['mediaText'].apply(lambda x: vaderGator(x).overallSentiment())
df[['coordinating_conjunction','cardinal_digit','determiner','existential','foreign','preposition','adjective','numbering','modal','noun','possessive','pronoun','adverb','giveup','to_go','interjection','verb']] = df['mediaText'].apply(lambda x: vaderGator(x).partOfSpeech())

msg,stopTime = save_fakenews(df)
print(msg + str(int(stopTime)-int(startTime)))
