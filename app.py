
from flask import Flask, render_template, request
from scanner import analyze_url

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/scan", methods=["POST"])
def scan():

    url = request.form.get("url", "").strip()

    if not url:
        return render_template(
            "index.html",
            error="Please enter a URL."
        )

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    result = analyze_url(url)

    return render_template(
        "index.html",
        scanned_url=url,
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)
