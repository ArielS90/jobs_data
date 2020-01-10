from flask import Flask, jsonify, render_template
import pandas as pd
from sqlalchemy import create_engine

rds_connection_string = "postgres:postgres@localhost:5432/Project 2"
engine = create_engine(f'postgresql://{rds_connection_string}')

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/Comparisons")
def Comparisons():
    return render_template('trumpClinton.html')

@app.route("/ethnicity")
def Ethnicity():
    return render_template('demographics.html')

@app.route("/line")
def test():
    data = pd.read_sql_query('select * from working_respondents', con=engine).head()
    data = data.to_json()
    # data = [{
    #     "x": [1, 2, 3, 4, 5],
    #     "y": [1, 2, 4, 8, 16]}]

    # return jsonify(data)
    return data


if __name__ == "__main__":
    app.run(debug=True)
