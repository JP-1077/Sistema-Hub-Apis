from backend.models.episodios_rickmorty import Filme

class EpisodiosServices:
    def coleta_dados_episodios(self):
        episodios = Filme.query.all()
        resultado_episodios = []

        for episodio in episodios:

            quantidade_personagens = len(episodio.url_personagens_episodio.split(","))

            resultado_episodios.append({
                "id": episodio.id,
                "nome_episodio": episodio.nome_episodio,
                "data_lancamento": episodio.data_lancamento.strftime("%d/%m/%Y"),
                "nomenclatura_episodio": episodio.nomenclatura_episodio,
                "quantidade_personagens": quantidade_personagens,
                "api": episodio.nome_api
            })
        return resultado_episodios