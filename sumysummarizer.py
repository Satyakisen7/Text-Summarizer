import sumy

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.summarizers.lsa import LsaSummarizer

def lexranker(text, count):
	parser = PlaintextParser.from_string(text, Tokenizer("english"))
	summarizer = LexRankSummarizer()
	summary = summarizer(parser.document, count)

	return summary

def luhner(text, count):
	parser = PlaintextParser.from_string(text, Tokenizer("english"))
	summarizer_luhn = LuhnSummarizer()
	summary_1 =summarizer_luhn(parser.document, count)

	return summary_1

def lsaer(text, count):
	parser = PlaintextParser.from_string(text, Tokenizer("english"))
	summarizer_lsa = LsaSummarizer()
	summary_2 =summarizer_lsa(parser.document, count)

	return summary_2