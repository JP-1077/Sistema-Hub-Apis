from flask import Blueprint, render_template
from datetime import datetime

home_bp = Blueprint("home", __name__)

@home_bp.route("/")
def home():

    dados_apis = {

        "rick_morty": {
            "personagens": 20,
            "episodios": 20,
            "localizacoes": 20
        },

        "star_wars": {
            "filmes": 6,
            "personagens": 328,
            "planetas": 60,
            "veiculos": 39,
            "naves": 36,
            "especies": 37
        }
    }

    return render_template("home.html", dados_apis=dados_apis, ano=datetime.now().year)

