from flask import Blueprint, render_template
from backend.services.service_db_especies_st import EspeciesService

especies_st_front_bp = Blueprint("especies_front_starwars", __name__)

@especies_st_front_bp.route("/starwars/especies")
def front_especies():

    service = EspeciesService()

    especies_st = service.coleta_dados_especies()

    return render_template("especies_starwars.html", especies_st=especies_st)