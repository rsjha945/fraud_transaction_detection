from flask import Flask
import sys
from fraud.logger import logging
from fraud.exception import FraudException


app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    try:
        raise Exception("We are testing custom exception")
    except Exception as e:
        fraud = FraudException(e,sys)
        logging.info(fraud.error_message)
        logging.info("We are testing logging module")
    return "CI CD pipeline has been established."


if __name__=="__main__":
    app.run(debug=True)