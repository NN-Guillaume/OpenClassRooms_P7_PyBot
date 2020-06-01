from app import app
from flask import Flask, render_template, url_for, request, jsonify
from app.classes import *


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api", methods=["POST"])
def api():

    query = request.form["query"]

    message = Parser(query)
    message.ponctuation()
    message.list_it()
    cleanMessage = message.delete_common_words()

    rep = Geo()
    coordonnees = rep.get_coordonnees(query)
    print(rep.get_address(coordonnees))

    print(cleanMessage)

    wiki = Wiki()
    page_id = wiki.get_page_id(coordonnees[0], coordonnees[1])
    summary = wiki.get_summary(page_id)

    answer = botAnswer()
    bot = answer.goodAnswer()
    print(bot)

    return jsonify(
        {
            "lat": coordonnees[0],
            "lng": coordonnees[1],
            "summary": summary,
            "answer": bot,
        }
    )
