from flask import Flask, render_template, request, redirect
from wordclouder import WC
from sumysummarizer import lexranker, luhner, lsaer

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
#app.config["CACHE_TYPE"] = "null"

@app.route("/")
def hello():
    return render_template("home.html")

@app.route('/landingpage')
def landingpage():
	choice = request.args.get('outtype')
	text = request.args.get('text')
	count = request.args.get('count')
	if not text or not text.strip():
		return render_template("noinput.html")
	if choice == 'wc':
		return wordcloud(text)
	elif choice == 'lexrank':
		return lexrank(text, count)
	elif choice == 'luhn':
		return luhn(text, count)
	elif choice == 'lsa':
		return lsa(text, count)

def wordcloud(text):
	WC(str(text))
	return render_template("wordcloud.html")

def lexrank(text, count):
	return render_template("text.html", text = lexranker(text, count))

def luhn(text, count):
	return render_template("text.html", text = luhner(text, count))

def lsa(text, count):
	return render_template("text.html", text = lsaer(text, count))