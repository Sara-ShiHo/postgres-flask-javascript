# import dependencies
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import pandas as pd
import json

# import my password from config.py
from config import password

# create engine and connection to postgres
from sqlalchemy import create_engine

db_name = "credit_cards"
engine = create_engine(f'postgresql://postgres:{password}@localhost:5432/{db_name}')
connection = engine.connect()
connection

app = Flask(__name__)

@app.route("/")
def index():
    cards_json = get_data()
    return render_template("index.html", cards_to_js = cards_json)

@app.route("/api/v1.0/data")
def get_data():

    # import SQL table as pandas dataframe
    cards_df = pd.read_sql('select * from credit_card', connection)
    
    # convert pandas dataframe to json
    cards_json = json.dumps(cards_df.to_dict('records'))
    
    return cards_json

if __name__ == "__main__":
    app.run(debug = True)