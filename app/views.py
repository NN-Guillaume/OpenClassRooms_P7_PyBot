from app import app
from flask import Flask, render_template, url_for, request, jsonify
from app.classes import *


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api", methods=["POST"])
def api():

    query = request.form["query"]

    # ---------------------------------------------------------------------------------
    message = Parser(query)
    message.ponctuation()
    message.list_it()
    cleanMessage = message.delete_common_words()
    # ---------------------------------------------------------------------------------

    rep = Geo(query)
    # appel de la fonction
    rep.get_coordonnees()
    # recherche des coordonnées GPS
    coordonnees = rep.get_coordonnees()
    # affichage des coordonnées GPS
    print(coordonnees[0], coordonnees[1])
    # ---------------------------------------------------------------------------------
    print(cleanMessage)
    # ---------------------------------------------------------------------------------
    wiki = Wiki(coordonnees[0], coordonnees[1])
    summary = wiki.summary

    answer = botAnswer()
    bot = answer.goodAnswer()
    print(bot)

    # print(answer) # affiche bien le code HTTP :-)

    #-----------------------------------------------------------------------------------
    #///////////////////////////////////////////////////////////////////////////////////
    #-----------------------------------------------------------------------------------
    """
    answer = botAnswer()
    
    try:
            result = requests.head("http://127.0.0.1:3020/")
            print(result.status_code)
            #
            if result.status_code == 200:
                # renvoie réponse +
                return answer.goodAnswer()
            else :
                # renvoie réponse -
                return answer.badAnswer()

    except requests.ConnectionError:
        print("failed to connect")
    """
    #-----------------------------------------------------------------------------------
    #///////////////////////////////////////////////////////////////////////////////////
    # ----------------------------------------------------------------------------------

    return jsonify(
        {
            "lat": coordonnees[0],
            "lng": coordonnees[1],
            "summary": summary,
            "answer": bot,
            #"answer":botAnswer,
        }
    )
