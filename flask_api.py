import flask
import nltk
from textblob import TextBlob
from textblob import Word
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk import tokenize

app = flask.Flask(__name__)


@app.route('/sentiment', methods=['POST'])
def sentiment():
    post_json = flask.request.json
    string = post_json.get('string')
    if string:
        # calling vader sentiment
        analyzer = SentimentIntensityAnalyzer()
        # returning the negative, neutral, positive, and neutral scores
        polarity = analyzer.polarity_scores(string)
        return {'success': True, 'response': polarity}
    else:
        return {'success': False, 'error': 'No string passed in json payload'}, 400


@app.route('/subjectivity', methods=['POST'])
def subjectivity():
    post_json = flask.request.json
    string = post_json.get('string')
    if string:
        blob = TextBlob(string)
        sub = blob.sentiment.subjectivity
        return {'success': True, 'response': sub}
    else:
        return {'success': False, 'error': 'No string passed in json payload'}, 400


@app.route('/commonwords', methods=['POST'])
def commonwords():
    post_json = flask.request.json
    string = post_json.get('string')
    if string:
        token_list = []
        for w in TextBlob(string).words:
            token_list.append(w)
        tokendf = pd.DataFrame(token_list, columns=['Tokens'])
        mostWords = tokendf['Tokens'].value_counts()[:5]
        return {'success': True, 'response': mostWords.to_dict()}
    else:
        return {'success': False, 'error': 'No string passed in json payload'}, 400


@app.route('/nounsverbs', methods=['POST'])
def nouns():
    post_json = flask.request.json
    string = post_json.get('string')
    if string:
        words = nltk.word_tokenize(string)
        tags = nltk.pos_tag(words)
	verbs = []
        nouns = []
	verb_tag = ['RB','RBR','RBS','VB','VBD','VBG','VBN','VBP','VBZ','WRB']
	noun_tag = ['NN','NNS','NNP','NNPS','PRP','PRP$','WP','WP$']
        for x in tags:
            if x[1] in verb_tag:
                verbs.append(x[0])
	    if x[1] in noun_tag:
		nouns.append(x[0])
	dictionary = {"Nouns":nouns, "Verbs":verbs}
        return {'success': True, 'response': dictionary}
    else:
        return {'success': False, 'error': 'No string passed in json payload'}, 400


@app.route('/pluralize', methods=['POST'])
def pluralize():
    post_json = flask.request.json
    string = post_json.get('string')
    if string:
        pluralize = ''
        for x in TextBlob(string).words:
            pluralize = pluralize + x.pluralize() + ' '
        return {'success': True, 'response': pluralize}
    else:
        return {'success': False, 'error': 'No string passed in json payload'}, 400


@app.route('/singularize', methods=['POST'])
def singularize():
    post_json = flask.request.json
    string = post_json.get('string')
    if string:
        singularize = ''
        for x in TextBlob(string).words:
            singularize = singularize + x.singularize() + ' '
        return {'success': True, 'response': singularize}
    else:
        return {'success': False, 'error': 'No string passed in json payload'}, 400


@app.route('/sentences', methods=['POST'])
def sentences():
    post_json = flask.request.json
    string = post_json.get('string')
    if string:
        # calling vader sentiment
        analyzer = SentimentIntensityAnalyzer()
        # results variable to append the sentences and scores of each sentence
        results = []
        # for loop through all the sentences
        for sentence in tokenize.sent_tokenize(string):
            # the compound score of each sentence
            score = analyzer.polarity_scores(sentence)['compound']
            # appending the sentences and the scores to the results list
            results.append([sentence.replace('\n', ' '), score])
        df = pd.DataFrame(results, columns=['Sentence', 'Score']).sort_values('Score', ascending=False).set_index(
            'Sentence')
        return {'success': True, 'response': df.to_dict()}
    else:
        return {'success': False, 'error': 'No string passed in json payload'}, 400


@app.route('/definition', methods=['POST'])
def definition():
    post_json = flask.request.json
    string = post_json.get('string')
    if string:
        blob = TextBlob(string)
        words = blob.words
        ret_val = []
        for word in words:
            ret_val.append({word: Word.define(word)})
        return {'success': True, 'response': ret_val}
    else:
        return {'success': False, 'error': 'No string passed in json payload'}, 400


@app.route('/translate', methods=['POST'])
def translate():
    post_json = flask.request.json
    string = post_json.get('string')
    new_string = string.replace('\n',' ')
        blob = TextBlob(new_string)
        detection = blob.detect_language()
        if detection == 'en':
            spanish = ('Spanish: ' + str(blob.translate(to = 'es')))
            german = ('German: ' + str(blob.translate(to = 'de')))
            french = ('French: ' + str(blob.translate(to = 'fr')))
            chinese = ('Chinese: ' + str(blob.translate(to = 'zh')))
            arabic = ('Arabic: ' + str(blob.translate(to = 'ar')))
            Dictionary = {1: spanish, 2: german, 3: french, 4: chinese, 5: arabic}
            return {'success': True, 'String is already in English': new_string},'Dictionary below: ', Dictionary
        else:
            list = ['es','fr','de','zh','ar']
            for lan in list:
                detection = blob.detect_language()
                if list.count(detection) == 1:
                    lang_det = blob.detect_language()
                    eng = str(blob.translate(to = 'en'))
                    return {'success': True,'String is in a listed language': new_string, 'Detected Language': lang_det,'English Translation': eng}
                else: 
                    lang_det = blob.detect_language()
                    eng = str(blob.translate(to = 'en'))
                    return {'success': True,'String is in a non-listed language': new_string, 'Detected Language': lang_det,'English Translation': eng}
    else:
        return {'success': False, 'error': 'No string passed in json payload'}, 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
