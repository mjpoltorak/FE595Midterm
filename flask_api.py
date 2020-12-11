import flask
import nltk
from textblob import TextBlob
from textblob import Word
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk import tokenize
import os

app = flask.Flask(__name__)


def sentiment(string):
    try:
        results = [] #list to add vader, TextBlob NLP
        analyzer = SentimentIntensityAnalyzer() #calling vader sentiment
        scores = analyzer.polarity_scores(string) #returning the negative, neutral, positive, and neutral scores
        results.append([scores]) 
        return results
    except:
        return 'Error occurred calculating sentiment'


def subjectivity(string):
    try:
        blob = TextBlob(string)
        sub = blob.sentiment.subjectivity
        return sub
    except:
        return 'Error occurred calculating subjectivity'


def commonwords(string):
    try:
        token_list = []
        for w in TextBlob(string).words:
            token_list.append(w)
        tokendf = pd.DataFrame(token_list, columns=['Tokens'])
        mostWords = tokendf['Tokens'].value_counts()[:5]
        return mostWords.to_dict()
    except:
        return 'Error occurred calculating common words'


def nounsverbs(string):
    try:
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
        dictionary = {"Nouns":nouns, "Verbs": verbs}
        return dictionary
    except:
        return 'Error occurred calculating nouns and verbs'


def pluralize(string):
    try:
        pluralize = ''
        for x in TextBlob(string).words:
            pluralize = pluralize + x.pluralize() + ' '
        return pluralize
    except:
        return 'Error occurred pluralizing'


def singularize(string):
    try:
        singularize = ''
        for x in TextBlob(string).words:
            singularize = singularize + x.singularize() + ' '
        return singularize
    except:
        return 'Error occurred calculating singularizing'

   
def sentences(string):
    try: 
        analyzer = SentimentIntensityAnalyzer() # calling vader sentiment
        results = [] #empty list to add scores
        for sentence in tokenize.sent_tokenize(string): # for loop through all the sentences
            compound = analyzer.polarity_scores(sentence)['compound']
            pos = analyzer.polarity_scores(sentence)['pos']
            neg = analyzer.polarity_scores(sentence)['neg']
            neu = analyzer.polarity_scores(sentence)['neu']
            results.append([sentence.replace('\n', ' '), compound, pos, neg, neu]) # appending the sentences and the scores to the results list
        df = pd.DataFrame(results, columns=['Sentence', 'Compound','Positive','Negative','Neutral']).sort_values('Compound', ascending=False).set_index(
            'Sentence')
        return df.to_dict() #need dictionary for flask
    except:
        return 'Error occurred finding sentences'


def definition(string):
    try:
        blob = TextBlob(string)
        words = blob.words
        ret_val = []
        for word in words:
            ret_val.append({word: Word.define(word)})
        return ret_val
    except:
        return 'Error occurred finding definitions'


def translate(string):
    try:
        new_string = string.replace('\n', ' ')
        blob = TextBlob(new_string)
        detection = blob.detect_language()
        if detection == 'en':
            spanish = ('Spanish: ' + str(blob.translate(to = 'es')))
            german = ('German: ' + str(blob.translate(to = 'de')))
            french = ('French: ' + str(blob.translate(to = 'fr')))
            chinese = ('Chinese: ' + str(blob.translate(to = 'zh')))
            arabic = ('Arabic: ' + str(blob.translate(to = 'ar')))
            Dictionary = {1: spanish, 2: german, 3: french, 4: chinese, 5: arabic}
            return {'detected_language': 'English', 'translations': Dictionary}
        else:
            lang_det = blob.detect_language()
            eng = str(blob.translate(to = 'en'))
            return {'detected_language': lang_det, 'translations': {"English": eng}}
    except:
        return 'Error occurred translating'


@app.route('/help', methods=['GET'])
def help():
    return flask.render_template("help.html")


@app.route('/process_string', methods=['POST'])
def process_string():
    post_json = flask.request.json
    string = post_json.get('string', None)
    if string:
        methods = post_json.get('methods', None)
        if methods:
            res_dict = {}
            if 'sentiment' in methods:
                res_dict['sentiment'] = sentiment(string)
            if 'subjectivity' in methods:
                res_dict['subjectivity'] = subjectivity(string)
            if 'commonwords' in methods:
                res_dict['commonwords'] = commonwords(string)
            if 'nounsverbs' in methods:
                res_dict['nounsverbs'] = nounsverbs(string)
            if 'pluralize' in methods:
                res_dict['pluralize'] = pluralize(string)
            if 'singularize' in methods:
                res_dict['singularize'] = singularize(string)
            if 'sentences' in methods:
                res_dict['sentences'] = sentences(string)
            if 'definition' in methods:
                res_dict['definition'] = definition(string)
            if 'translate' in methods:
                res_dict['translate'] = translate(string)
            return {"success": True, 'response': res_dict}
        else:
            return {'success': False, 'error': 'No string passed in json payload'}, 400
    else:
        return {'success': False, 'error': 'No string passed in json payload'}, 400


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
