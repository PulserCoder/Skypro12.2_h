from flask import Blueprint, render_template, request
from functions import write_to_json
import logging
add_post = Blueprint('add_post_blueprint', __name__, template_folder='templates')
@add_post.route('/post')
def add_page():
    return render_template('post_form.html')


@add_post.route('/post', methods=['POST'])
def add_action():
    file = request.files.get('picture')
    content = request.form.get('content')
    filename = file.filename
    if filename.split('.')[-1] == 'png' or filename.split('.')[-1] == 'jpeg':
        try:
            file.save(f"./uploads/images/{filename}")
            write_to_json(content, f'../uploads/images/{filename}')
            return render_template('post_uploaded.html', path=f'./uploads/images/{filename}', content=content)
        except:
            return 'Ошибка с файлом'
    logging.error('Неправильный формат файла')
    return 'Неправильный формат файла'