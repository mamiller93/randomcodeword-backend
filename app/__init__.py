import os

from flask import request, Flask, make_response, jsonify
from flask_cors import CORS, cross_origin
from random_word import RandomWords


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError as e:
        pass

    # a simple page that says hello
    @app.route('/get')
    @cross_origin()
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

    return app
