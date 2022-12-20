from flask import Flask, send_from_directory
from blueprint_main.main import showImage
from blueprint_main.loader import add_post
import logging
logging.basicConfig(filename='log.log', level=logging.INFO)
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024

app.register_blueprint(showImage)
app.register_blueprint(add_post)

@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path=path)


app.run()
