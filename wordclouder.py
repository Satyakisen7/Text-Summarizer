# Python program to generate WordCloud
# https://www.geeksforgeeks.org/generating-word-cloud-python/

# importing all necessery modules 
from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 
import pandas as pd 

def WC(text):
	# Reads 'Youtube04-Eminem.csv' file 

	wordcloud = WordCloud(width = 900, height = 500, background_color ='#DCE1DE', min_font_size = 10).generate(text) 

	# plot the WordCloud image                   
	plt.figure(figsize = (9, 5), facecolor = None) 
	plt.imshow(wordcloud) 
	plt.axis("off") 
	plt.tight_layout(pad = 0) 

	plt.savefig("static/images/save")

#st = ''
#with open('Donald-Tweets!.txt', 'r') as text:
#	for line in text:
#		st += line + '. '

#WC(st)