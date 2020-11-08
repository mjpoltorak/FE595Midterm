import flask
from textblob import TextBlob
from textblob import Word

app = flask.Flask(__name__)


@app.route('/sentiment', methods=['POST'])
def sentiment():
    post_json = flask.request.json
    string = post_json.get('string')
    if string:
        return {'success': True, 'response': string}
    else:
        return {'success': False, 'error': 'No string passed in json payload'}, 400


@app.route('/subjectivity', methods=['POST'])
def subjectivity():
    post_json = flask.request.json
    string = post_json.get('string')
    if string:
        return {'success': True, 'response': string}
    else:
        return {'success': False, 'error': 'No string passed in json payload'}, 400


@app.route('/commonwords', methods=['POST'])
def commonwords():
    post_json = flask.request.json
    string = post_json.get('string')
    if string:
        return {'success': True, 'response': string}
    else:
        return {'success': False, 'error': 'No string passed in json payload'}, 400


@app.route('/nouns', methods=['POST'])
def nouns():
    post_json = flask.request.json
    string = post_json.get('string')
    if string:
        return {'success': True, 'response': string}
    else:
        return {'success': False, 'error': 'No string passed in json payload'}, 400


@app.route('/verbs', methods=['POST'])
def verbs():
    post_json = flask.request.json
    string = post_json.get('string')
    if string:
        return {'success': True, 'response': string}
    else:
        return {'success': False, 'error': 'No string passed in json payload'}, 400


@app.route('/pluralize', methods=['POST'])
def pluralize():
    post_json = flask.request.json
    string = post_json.get('string')
    if string:
        return {'success': True, 'response': string}
    else:
        return {'success': False, 'error': 'No string passed in json payload'}, 400


@app.route('/singularize', methods=['POST'])
def singularize():
    post_json = flask.request.json
    string = post_json.get('string')
    if string:
        return {'success': True, 'response': string}
    else:
        return {'success': False, 'error': 'No string passed in json payload'}, 400


@app.route('/sentences', methods=['POST'])
def sentences():
    post_json = flask.request.json
    string = post_json.get('string')
    if string:
        return {'success': True, 'response': string}
    else:
        return {'success': False, 'error': 'No string passed in json payload'}, 400


@app.route('/definition', methods=['POST'])
def definition():
    post_json = flask.request.json
    string = post_json.get('string')
    blob = TextBlob(string)
    words = blob.words
    ret_val = []
    for word in words:
        ret_val.append({word: Word.define(word)})
    if string:
        return {'success': True, 'response': ret_val}
    else:
        return {'success': False, 'error': 'No string passed in json payload'}, 400


@app.route('/translate', methods=['POST'])
def translate():
    post_json = flask.request.json
    string = post_json.get('string')
    if string:
        return {'success': True, 'response': string}
    else:
        return {'success': False, 'error': 'No string passed in json payload'}, 400


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
