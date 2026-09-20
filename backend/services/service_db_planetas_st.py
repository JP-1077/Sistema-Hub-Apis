from backend.models.planetas_api_starwars import PlanetasApiStarWars

class PlanetasService:

    def coleta_dados_planetas(self):

        planetas = PlanetasApiStarWars.query.all()

        resultado_planetas = []

        for planeta in planetas:
            resultado_planetas.append({
                "id": planeta.id,
                "nome_planeta": planeta.nome_planeta,
                "periodo_rotacao": planeta.periodo_rotacao,
                "periodo_orbital": planeta.periodo_orbital,
                "diametro": planeta.diametro,
                "clima": planeta.clima,
                "gravidade": planeta.gravidade,
                "terreno": planeta.terreno,
                "agua_superficie": planeta.agua_superficie,
                "populacao": planeta.populacao,
                "Data criacao planeta": planeta.data_criacao_planeta,
                "Data atualizacao planeta": planeta.data_atualizacao_planeta,
                "Nome API": planeta.nome_api,

            })

        return resultado_planetas