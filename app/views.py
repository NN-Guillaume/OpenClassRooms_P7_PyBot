from app import app
from flask import Flask, render_template, url_for, request, jsonify
from app.geo import Geo
from app.wiki import Wiki
from app.parser import Parser
from app.bot import botAnswer

import requests


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
    
###################################################################################
# KEEP THIS PART ! ! ! KEEP THIS PART ! ! ! KEEP THIS PART ! ! ! KEEP THIS PART ! ! !
###################################################################################
    
    return jsonify(
        {
            "lat": coordonnees[0],
            "lng": coordonnees[1],
            "summary": summary,
            "answer": bot,
        }
    )
    
###################################################################################
# KEEP THIS PART ! ! ! KEEP THIS PART ! ! ! KEEP THIS PART ! ! ! KEEP THIS PART ! ! !
###################################################################################
