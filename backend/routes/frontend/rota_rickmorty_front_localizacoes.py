from flask import Blueprint, render_template

from backend.services.service_db_localizacoes import LocalizoesServices


localizacoes_front_bp = Blueprint("localizacoes_front", __name__)

@localizacoes_front_bp.route("/rickmorty/localizacoes")

def tela_localizacoes():
    service = LocalizoesServices()
    localizacoes = service.coleta_dados_localizoes()

    return render_template("localizacao_rickmorty.html", localizacoes=localizacoes)
