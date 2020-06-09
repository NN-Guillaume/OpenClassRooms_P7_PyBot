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
    print(query)
    message = Parser(query)
    message.ponctuation()
    message.list_it()
    print(message)
    cleanMessage = message.delete_common_words()
    print(cleanMessage)


    rep = Geo()
    coordonnees = rep.get_coordonnees(query)
    
    if coordonnees is not None:
        print(rep.get_address(coordonnees))
        wiki = Wiki()
        page_id = wiki.get_page_id(coordonnees[0], coordonnees[1])
        summary = wiki.get_summary(page_id)
        answer = botAnswer()
        bot = answer.goodAnswer()
        print(bot)
        return jsonify({"lat": coordonnees[0], "lng": coordonnees[1], "summary": summary, "answer":bot,})
    else:
        print("pas trouvé")
        answer = botAnswer()
        bot = answer.badAnswer()
        print(bot)
        return jsonify({"answer":bot,})
    
###################################################################################
    """
    if coordonnees is not None:
        print(rep.get_address(coordonnees))
        wiki = Wiki()
        page_id = wiki.get_page_id(coordonnees[0], coordonnees[1])
        summary = wiki.get_summary(page_id)
        answer = botAnswer()
        bot = answer.goodAnswer()
        print(bot)
        return jsonify({"lat": coordonnees[0], "lng": coordonnees[1], "summary": summary, "answer":bot,})
    elif coordonnees is None:
        print("pas trouvé")
        answer = botAnswer()
        bot = answer.badAnswer()
        print(bot)
        return jsonify({"answer":bot,})
    else:
        print("lieu existant mais données inaccessibles")
        answer = botAnswer()
        bot = answer.confusedAnswer()
        print(bot)
        return jsonify({"answer":bot,})
    """

###################################################################################
