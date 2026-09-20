from flask import Flask
from flask_migrate import Migrate

from backend.config import Config
from backend.database.db import db

from backend.models import *

from backend.routes.api.rota_rickmorty_localizacao import localizacao_bp
from backend.routes.api.rota_rickmorty_personagem import personagens_bp
from backend.routes.api.rota_rickmorty_episodios import episodios_bp

from backend.routes.api.rota_star_wars_personagens import personagens_bp
from backend.routes.api.rota_starwars_filmes import filmes_bp
from backend.routes.api.rota_starwars_planetas import planetas_bp
from backend.routes.api.rota_starwars_veiculos import veiculos_bp
from backend.routes.api.rota_starwars_especies import especies_bp
from backend.routes.api.rota_starwars_espaco_naves import espaco_naves_bp

from backend.routes.api.rota_sistema_home import home_bp
from backend.routes.frontend.rota_rickmorty_front_episodios import episodios_rickmorty_front_bp
from backend.routes.frontend.rota_rickmorty_front_localizacoes import localizacoes_front_bp
from backend.routes.frontend.rota_starwars_front_personagens import personagens_st_front_bp
from backend.routes.frontend.rota_starwars_front_filmes  import filmes_st_front_bp
from backend.routes.frontend.rota_starwars_front_planetas import planetas_st_front_bp
from backend.routes.frontend.rota_starwars_front_veiculos import veiculos_st_front_bp
from backend.routes.frontend.rota_starwars_front_especies import especies_st_front_bp
from backend.routes.frontend.rota_starwars_front_espaco_naves import espaco_naves_st_front_bp


try:
    from backend.routes.api.rota_rickmorty import rickmorty_bp
except ModuleNotFoundError:
    rickmorty_bp = None

migrate = Migrate()

def create_app():

    app = Flask(__name__, template_folder="../frontend/templates")

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(localizacao_bp)
    app.register_blueprint(personagens_bp)
    app.register_blueprint(episodios_bp)
    app.register_blueprint(filmes_bp)
    app.register_blueprint(planetas_bp)
    app.register_blueprint(veiculos_bp)
    app.register_blueprint(especies_bp)
    app.register_blueprint(espaco_naves_bp)

    app.register_blueprint(home_bp)
    app.register_blueprint(episodios_rickmorty_front_bp)
    app.register_blueprint(localizacoes_front_bp)
    app.register_blueprint(personagens_st_front_bp)
    app.register_blueprint(filmes_st_front_bp)
    app.register_blueprint(planetas_st_front_bp)
    app.register_blueprint(veiculos_st_front_bp)
    app.register_blueprint(especies_st_front_bp)
    app.register_blueprint(espaco_naves_st_front_bp)

    return app