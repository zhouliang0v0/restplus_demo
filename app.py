from flask import Flask
from main import blueprint

app = Flask(__name__)
app.register_blueprint(blueprint, url_prefix='')

if __name__ == '__main__':
    app.run()
