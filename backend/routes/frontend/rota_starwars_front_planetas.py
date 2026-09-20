from flask import Blueprint, render_template
from backend.services.service_db_planetas_st import PlanetasService

planetas_st_front_bp = Blueprint("planetas_front_starwars", __name__)

@planetas_st_front_bp.route("/starwars/planetas")

def front_planetas():

    service = PlanetasService()

    planetas_st = service.coleta_dados_planetas()

    return render_template("planetas_starwars.html", planetas_st=planetas_st)

