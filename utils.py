import pandas as pd
import os, datetime

def get_time_vars():
	year = datetime.datetime.today().strftime('%Y')
	month = datetime.datetime.today().strftime('%m')
	day = datetime.datetime.today().strftime('%d')
	hour = datetime.datetime.today().strftime('%H')
	minute = datetime.datetime.today().strftime('%M')
	second = datetime.datetime.today().strftime('%S')
	return year,month,day,hour,minute,second

def get_directory(y,m):
	directory = 'data/{0}/{1}/'.format(y,m)
	if os.path.exists(directory):
		print("Appending --- " + str(directory))
	else:
		print("Creating --- " + str(directory))
		os.makedirs(directory)
	return directory

def save_fakenews(df):
	yr,mth,day,hr,min,sec = get_time_vars()
	directory = get_directory(yr,mth)
	filename = str(directory) + "fakenews_{}.csv".format(str(yr)+str(mth)+str(day)+str(hr))
	df.to_csv(filename)
	return "Saved! --- " + str(len(df)) + " bites of news. Time: " , int(str(yr)+str(mth)+str(day)+str(hr)+str(min)+str(sec))
