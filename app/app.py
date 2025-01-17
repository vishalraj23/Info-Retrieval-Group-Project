from flask import Flask, render_template, request, send_file, send_from_directory
import os
from utils import filter, geospatial_graph
import os

BASE_DIR = os.getcwd()
application = Flask(__name__)

PORT = os.getenv('PORT', 8000)


@application.route("/")
def index():
    return render_template('pages/about.html')


@application.route("/search")
def search():
    return render_template('pages/search.html')


@application.route("/search_results")
def search_results():
    search_query = request.args.get("search")
    if search_query:
        text = "content:"+search_query
        tweets = filter(text)
        if len(tweets) == 0:
            return render_template('pages/search_results.html', search_query = search_query, error = "No tweets Found", tweets = None)
        return render_template('pages/search_results.html', search_query = search_query, error= None, tweets = tweets)
    return render_template('pages/search.html')


@application.route("/sentiment")
def sentiment():
    return render_template('pages/sentiment_analysis.html')


@application.route("/geospatial_search")
def geospatial_search():
    return render_template("pages/geospatial_search.html", plot = geospatial_graph())


@application.route("/plotly/<filename>")
def plotly(filename):
    return send_from_directory(f"{BASE_DIR}/js/", filename=filename)


if __name__ == "__main__":
    application.run(debug=True, port=PORT)
