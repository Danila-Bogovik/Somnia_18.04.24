from flask import Flask, render_template
from flask_bootstrap import Bootstrap

from app.config import CONFIG

app = Flask(__name__)
Bootstrap(app)
 
@app.route('/', methods=['GET', 'POST'])
def index_page():
    return render_template('index.html', site_name=CONFIG['site_name'])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=False)