# minorproject-textanalysis
Tools to clean datasets and other text visualization code snippets.

I'm  using python 3.6 (64 bit, of course)
Other dependencies (use pip install x, where x are as follows) -

Ones in use at the moment: sumy, pandas, wordcloud, matplotlib(, TBA)

Other recommended ones that might be used in near future: numpy(, TBA)

csv2str is a program that will convert your csv datasets into a single plain txt document which can be later imported into python as a string. Usage: replace 'elonmusk_tweets' with your filename, without the .csv extension and 'Text' with your desired column header from your csv.

sumy-summarizer has been referenced from https://jcharistech.wordpress.com/2019/01/05/how-to-summarize-text-or-document-with-sumy/. i encourage you to try out all of the summarization methods listed and demoed on the article. (i have only tried out lexrank so far with moderately fair results). note: the second parameter of summarizer (i.e 20 as in the code) is the desired number of clusters / summaries you want, please change according to need.
note: you might need to run the following python snippet separately before running the summarizer1 py file

UPDATED PRECISE INSTRUCTIONS TO RUN PROJECT -
1. pip install packages: pandas, sumy, wordcloud, flask
2. open a python terminal and enter the following
`import nltk` and `nltk.download('punkt')`
3. flask run
