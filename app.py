from flask import  Flask, request
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

def create_app(test_config=None):
    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'Hello world'

    @app.route('/mazzameras', methods=['POST'])
    def upload_file():
        image = request.files['image']
        filename = secure_filename(image.filename)
        url = os.path.join(APP_ROOT,filename)

        image.save(url)
        return url

    return app

app = create_app()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
