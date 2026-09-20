from flask import Blueprint, render_template
from backend.services.service_db_personagens_st import PersonagemServiceStarWars

personagens_st_front_bp = Blueprint("personagens_front_starwars", __name__)

@personagens_st_front_bp.route("/starwars/personagens")
def tela_episodios():

    service = PersonagemServiceStarWars()

    personagens_st = service.coleta_dados_personagens_st()

    return render_template("personagens_starwars.html", personagens_st=personagens_st)