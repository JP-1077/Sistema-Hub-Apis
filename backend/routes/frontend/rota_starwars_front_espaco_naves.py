from flask import Blueprint, render_template
from backend.services.service_db_espaco_naves_st import EspacoNavesService

espaco_naves_st_front_bp = Blueprint("espaco_naves_front_starwars", __name__)

@espaco_naves_st_front_bp.route("/starwars/espaconaves")
def front_espaconaves():

    service = EspacoNavesService()

    naves_st = service.coleta_dados_naves()

    return render_template("espaco_naves_starwars.html", naves_st=naves_st)