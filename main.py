from flask import Flask, render_template
from flask_bootstrap import Bootstrap

from core.config import CONFIG

app = Flask(__name__)
Bootstrap(app)
 
@app.route('/')
def index_page():
    return render_template('base.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=False)