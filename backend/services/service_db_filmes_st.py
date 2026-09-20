from backend.models.filmes_api_starwars import Filmesstarwars


class FilmesService:

    def coleta_dados_filmes(self):

        filmes = Filmesstarwars.query.all()

        resultado_filmes = []

        for filme in filmes:
            resultado_filmes.append({
                "id": filme.id,
                "titulo_filme": filme.titulo_filme,
                "episodio": filme.episodio,
                "texto_abertura": filme.texto_abertura,
                "diretor": filme.diretor,
                "produtor": filme.produtor,
                "data_lancamento": filme.data_lancamento,
                "nome_api": filme.nome_api,
            })

        return resultado_filmes