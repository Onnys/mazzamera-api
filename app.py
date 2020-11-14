from flask import  Flask, request, send_from_directory, safe_join, abort , jsonify
import os

APP_ROOT = (os.path.dirname(os.path.abspath(__file__))+'/static')


def create_app(test_config=None):
    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'Hello world'

    @app.route('/add-mazzameras', methods=['POST'])
    def upload_file():
        image = request.files['image']
        url = os.path.join(APP_ROOT,image.filename)
        image.save(url)
        return jsonify({
            'success': True,
            'file_name':image.filename,
        })

    @app.route('/get-mazzamera', methods=['GET'])
    def get_image():
        try:
            return send_from_directory(directory='static',filename='production.png')

        except FileNotFoundError:
            abort(404)

    return app

app = create_app()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
