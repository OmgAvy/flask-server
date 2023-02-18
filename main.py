from flask import Flask, request
import flask

app=Flask(__name__)

@app.route("/")
def root():
    return "RESOURCES FROM / root :)"




if __name__ == "__main__":
    app.run()
