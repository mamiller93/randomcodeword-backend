import os

from flask import request, Flask, make_response, jsonify
from random_word import RandomWords

# pylint: disable=C0103
app = Flask(__name__)


@app.route('/get')
def get():
    params = request.args
    r = RandomWords()
    words = None
    while words == None:
        words = r.get_random_words(hasDictionaryDef=True,
                                   minCorpusCount=2,
                                   includePartOfSpeech=params.get(
                                       "partOfSpeech") or "noun,verb",
                                   limit=params.get('limit') or 1)

    responseObject = {
        "words": words,
    }
    return make_response(jsonify(responseObject)), 201


if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')
