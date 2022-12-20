from flask import Blueprint, render_template, request
from functions import findingPosts
import logging
showImage = Blueprint('main_blueprint', __name__, template_folder='templates')


@showImage.route('/')
def showImageFoo():
    return render_template('index.html')


@showImage.route('/search/')
def FindingPosts():
    logging.info('Выполнен поиск')
    word = request.args.get('s')
    ll = findingPosts(word)
    return render_template('post_list.html', name=word, posts=ll)