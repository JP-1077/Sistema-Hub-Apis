from backend.models.especies_api_starwars import EspeciesApiStarWars
from backend.models.planetas_api_starwars import PlanetasApiStarWars
class EspeciesService:

    @staticmethod
    def extrair_id_url(url: str) -> int | None:
        """
        Extrai o ID existente no final de uma URL da SWAPI.
        """

        if not url:
            return None
        try:
            return int(url.rstrip("/").split("/")[-1])
        except (ValueError, AttributeError):
            return None


    def coleta_dados_especies(self):
        especies = EspeciesApiStarWars.query.all()
        planetas = PlanetasApiStarWars.query.all()

        mapa_planetas = {
            planeta.id: planeta.nome_planeta
            for planeta in planetas
        }

        resultado_especies = []

        for especie in especies:

            planeta_id = self.extrair_id_url(especie.id_planeta_origem)

            nome_planeta = mapa_planetas.get(planeta_id, "Desconhecido")

            resultado_especies.append({
                "id": especie.id,
                "nome": especie.nome,
                "classificacao": especie.classificacao,
                "designacao": especie.designacao,
                "altura_media": especie.altura_media,
                "cor_pele": especie.cor_pele,
                "cor_cabelo": especie.cor_cabelo,
                "cor_olhos": especie.cor_olhos,
                "expectativa_vida_media": especie.expectativa_vida_media,
                "idioma": especie.idioma,
                "nome_planeta": nome_planeta,
                "nome_api": especie.nome_api,
            })

        return resultado_especies