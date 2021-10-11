from flask import Flask, send_file
from database_handler import data
app = Flask(__name__)


@app.route('/')
def get_data():  # put application's code here
    city_names = [(record.city_name) for record in data]
    print(city_names)
    return "jkhqklgh  "


@app.route('/main.png')
def main_plot():
    """The view for rendering the scatter chart"""
    img = get_main_image()
    return send_file(img, mimetype='image/png', cache_timeout=0)



if __name__ == '__main__':
    app.run()
