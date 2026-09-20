from backend.models.veiculos_api_starwars import VeiculosApiStarWars


class VeiculosService:

    def coleta_dados_veiculos(self):

        veiculos = VeiculosApiStarWars.query.all()

        resultado_veiculos = []

        for veiculo in veiculos:
            resultado_veiculos.append({
                "id": veiculo.id,
                "nome_veiculo":veiculo.nome_veiculo,
                "modelo": veiculo.modelo,
                "fabricante": veiculo.fabricante,
                "custo_creditos": veiculo.custo_creditos ,
                "comprimento": veiculo.comprimento,
                "velocidade_maxima_atmosfera": veiculo.velocidade_maxima_atmosfera,
                "tripulacao": veiculo.tripulacao,
                "passageiros": veiculo.passageiros,
                "capacidade_carga": veiculo.capacidade_carga,
                "consumiveis": veiculo.consumiveis,
                "classe_veiculo": veiculo.classe_veiculo,
                "nome_api": veiculo.nome_api,
            })

        return resultado_veiculos