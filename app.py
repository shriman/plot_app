from flask import Flask
from database_handler import data
app = Flask(__name__)


@app.route('/')
def get_data():  # put application's code here
    city_names = [(record.city_name) for record in data]
    print(city_names)
    return "jkhqklgh  "





if __name__ == '__main__':
    app.run()
