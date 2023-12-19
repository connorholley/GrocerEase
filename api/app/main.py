#!/usr/bin/env python3

from pathlib import Path

from flask import Flask

from app.config import ServiceConfig
from app.data_service import DataService

app = Flask(__name__)


@app.route("/")
def check_health():
    return {"status": "healthy"}


@app.route("/ingredients")
def get_ingredients():

    # TODO: setup DataBase(DBEngine(ServiceConfig))) in a before_serving function

    raise NotImplementedError()
    


if __name__ == "__main__":
    app.run()
