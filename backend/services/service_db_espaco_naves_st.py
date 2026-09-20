from backend.models.espaco_naves_api_starwars import EspacoNavesApiStarWars

class EspacoNavesService:

    def coleta_dados_naves(self):
        naves = EspacoNavesApiStarWars.query.all()

        resultado_naves = []

        for nave in naves:
            resultado_naves.append({
                "id": nave.id,
                "nome": nave.nome,
                "modelo": nave.modelo,
                "fabricante": nave.fabricante,
                "custo_creditos": nave.custo_creditos,
                "comprimento": nave.comprimento,
                "velocidade_maxima_atmosfera": nave.velocidade_maxima_atmosfera,
                "tripulacao": nave.tripulacao,
                "passageiros": nave.passageiros,
                "capacidade_carga": nave.capacidade_carga,
                "consumiveis": nave.consumiveis,
                "classificacao_hiperpropulsor": nave.classificacao_hiperpropulsor,
                "mglt": nave.mglt,
                "classe_nave": nave.classe_nave,
                "nome_api": nave.nome_api,
            })

        return resultado_naves