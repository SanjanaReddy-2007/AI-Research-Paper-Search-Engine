from flask import Flask, render_template, request
from search.search_engine import SearchEngine

app = Flask(__name__)

engine = SearchEngine()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/search")
def search():
    query = request.args.get("query")

    if not query:
        return render_template("results.html", papers=[])

    papers = engine.search(query)

    return render_template("results.html", papers=papers)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)