import chaat as ia

nome_maquina = "Pedro"
ia.saudações(nome_maquina)

while True:
    texto = ia.recebeTexto()
    resposta = ia.buscaResposta(nome_maquina, texto)
    if ia.exibeResposta(resposta, nome_maquina) == "Vai embora!!!!!!!!!":
        break