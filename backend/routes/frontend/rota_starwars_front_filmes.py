from flask import Blueprint, render_template
from backend.services.service_db_filmes_st import FilmesService

filmes_st_front_bp = Blueprint("filmes_front_starwars", __name__)

@filmes_st_front_bp.route("/starwars/filmes")

def front_filmes():

    service = FilmesService()

    filmes_st = service.coleta_dados_filmes()

    return render_template("filmes_starwars.html", filmes_st=filmes_st)