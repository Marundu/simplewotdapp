from flask import Flask, render_template, request
from api_key import WORDNIK_API_KEY
import json
import requests

app=Flask(__name__)

WOTD_URL='http://api.wordnik.com/v4/words.json/wordOfTheDay?api_key='

@app.route('/')
def home():
	wotd=requests.get(WOTD_URL+WORDNIK_API_KEY)
	parsed=wotd.json()
	word=parsed['word']
	note=parsed['note']
	partofspeech=parsed['definitions'][0]['partOfSpeech']
	definition=parsed['definitions'][0]['text']
	example1=parsed['examples'][0]['text']
	example2=parsed['examples'][1]['text']
	
	return render_template('home.html',
			word=word, note=note,
			partofspeech=partofspeech,
			definition=definition,
			example1=example1,
			example2=example2)

if __name__=='__main__':
	app.run(port=7095, debug=True)