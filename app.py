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
engine = create_engine(f'postgresql://postgres:{password}@localhost:5432/credit_cards')
connection = engine.connect()
connection

app = Flask(__name__)

@app.route("/")
def index():

    # import SQL table as pandas
    cards_df = pd.read_sql('select * from credit_card', connection)
    
    # convert pandas column to a list
    cards_list = cards_df['card'].to_list()

    return render_template("index.html", cards = cards_list)

if __name__ == "__main__":
    app.run(debug = True)