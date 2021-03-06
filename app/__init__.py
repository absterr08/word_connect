import os

from flask import Flask, jsonify, render_template
from .word_tree import WordTree
from . import synonym_list
from . import synonym_tree
from . import synonym_path
from . import root


app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'app.sqlite'),
)

# if test_config is None:
#     # load the instance config, if it exists, when not testing
#     app.config.from_pyfile('config.py', silent=True)
# else:
#     # load the test config if passed in
#     app.config.from_mapping(test_config)

# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

app.register_blueprint(root.bp)
app.register_blueprint(synonym_list.bp)
app.register_blueprint(synonym_tree.bp)
app.register_blueprint(synonym_path.bp)
