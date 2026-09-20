from flask import Blueprint, render_template
from backend.services.service_db_veiculos_st import VeiculosService

veiculos_st_front_bp = Blueprint("veiculos_front_starwars", __name__)

@veiculos_st_front_bp.route("/starwars/veiculos")
def front_veiculos():

    service = VeiculosService()

    veiculos_st = service.coleta_dados_veiculos()

    return render_template("veiculos_starwars.html", veiculos_st=veiculos_st)