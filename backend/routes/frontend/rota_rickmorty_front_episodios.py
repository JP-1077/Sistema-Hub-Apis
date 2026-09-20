from flask import Blueprint, render_template
from backend.services.service_db_episodios import EpisodiosServices


episodios_rickmorty_front_bp = Blueprint("episodios_front", __name__)

@episodios_rickmorty_front_bp.route("/rickmorty/episodios")

def front_episodios_rickmorty():
    service = EpisodiosServices()
    episodios = service.coleta_dados_episodios()
    return render_template("episodios_rickmorty.html", episodios=episodios)