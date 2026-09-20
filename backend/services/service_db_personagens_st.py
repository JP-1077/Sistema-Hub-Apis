from backend.models.personagens_api_starwars import PersonagemApiStarWars
from backend.models.planetas_api_starwars import PlanetasApiStarWars
class PersonagemServiceStarWars:

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
        
    def coleta_dados_personagens_st(self):

        personagens_st = PersonagemApiStarWars.query.all()
        planetas = PlanetasApiStarWars.query.all()

        mapa_planetas = {
            planeta.id: planeta.nome_planeta
            for planeta in planetas
        }

        resultado_personagens = []

        for personagem in personagens_st:
            
            planeta_id = self.extrair_id_url(personagem.id_planeta_origem)

            nome_planeta = mapa_planetas.get(planeta_id, "Desconhecido")

            resultado_personagens.append({
                "id": personagem.id,
                "nome_personagem": personagem.nome_personagem,
                "altura": personagem.altura,
                "peso": personagem.peso,
                "cor_cabelo": personagem.cor_cabelo,
                "cor_pele": personagem.cor_pele,
                "cor_olhos": personagem.cor_olhos,
                "ano_nascimento": personagem.ano_nascimento,
                "genero": personagem.genero,
                "nome_planeta": nome_planeta,
                "nome_api": personagem.nome_api
            })

        return resultado_personagens
