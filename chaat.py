def saudações(nome):
    import random
    frases = [f"Bom dia! Meu nome é {nome}! Como vai você?","Olá","Vai embora seu betinha sem aura", f"Boa Tarde! Meu nome é {nome}! Como vai você?", f"Boa noite! Meu nome é {nome}! Como vai você?"]
    print(frases[random.randint(0,4)])

def recebeTexto():
    texto = "Cliente: " + input("Cliente: ")
    palavrasProibidas = ["boboca","feio","Palmeiras tem mundial","carambolas",
    "burro",
    "idiota",
    "imbecil",
    "otário",
    "otario",
    "babaca",
    "trouxa",
    "corno",
    "fdp",
    "filho da puta",
    "filha da puta",
    "puta",
    "puto",
    "putinha",
    "vagabundo",
    "vagabunda",
    "arrombado",
    "arrombada",
    "desgraçado",
    "desgracado",
    "desgraçada",
    "desgracada",
    "lixo",
    "escroto",
    "escrota",
    "merda",
    "bosta",
    "caralho",
    "cacete",
    "porra",
    "foda",
    "foder",
    "fodase",
    "foda-se",
    "vsf",
    "vtnc",
    "vai tomar no cu",
    "vai se foder",
    "tomar no cu",
    "cu",
    "cuzão",
    "cuzao",
    "pau no cu",
    "pau",
    "rola",
    "piroca",
    "pinto",
    "bilau",
    "buceta",
    "xereca",
    "xota",
    "boquete",
    "punheta",
    "gozar",
    "gozo",
    "sexo",
    "pornô",
    "porno",
    "pornografia",
    "hentai",
    "nudes",
    "nude",
    "pack",
    "onlyfans",
    "racista",
    "racismo",
    "nazista",
    "nazismo",
    "hitler",
    "matar",
    "assassinar",
    "suicídio",
    "suicidio",
    "bomba",
    "explodir",
    "explosivo",
    "hackear",
    "hack",
    "cracker",
    "phishing",
    "golpe",
    "fraude",
    "scam",
    "cartão clonado",
    "cartao clonado",
    "clonar cartão",
    "clonar cartao",
    "cpf falso",
    "rg falso",
    "documento falso",
    "dinheiro falso",
    "maconha",
    "cocaína",
    "cocaina",
    "crack",
    "heroína",
    "heroina",
    "ecstasy",
    "lsd",
    "droga",
    "spam",
    "divulgação",
    "divulgacao",
    "propaganda ilegal"]

    for p in palavrasProibidas:
        if p in texto:
            print("NÃO ADIANTA TENTAR ME XINGAR SEU BOBOCA, BETINHA, SEM AURA, 67. NEM VEM FALAR COISAS ERRADAS.")
            return recebeTexto()
        return texto


def buscaResposta(nome, texto):
    with open("base.txt", "a+", encoding="utf-8") as conhecimento:
        conhecimento.seek(0)
        while True:
            viu = conhecimento.readline()
            if viu != "":
                if  texto.replace("Cliente: ","") == "tchau":



                    import random
                    frases=[f"{nome}: Volte sempre",
                    "Vai embora, seu betinha sem aura.",
                    "Some daqui, boboca.",
                    "Tchau, feioso. Volta quando evoluir.",
                    "Até nunca... brincadeira, volta aí.",
                    "Vai dormir, esquisito.",
                    "Sai daqui, NPC.",
                    "Tchau, seu cabaço.",
                    "Vai lá, seu sem XP.",
                    "Flw, sem aura.",
                    "Vaza, criatura.",
                    "Até mais, lerdão.",
                    "Vai com Deus, seu cabeça de vento.",
                    "Some, pangaré.",
                    "Vai lá, seu cone.",
                    "Tchau, Zé Ruela.",
                    "Vai treinar, seu noob.",
                    "Sai daqui, seu amassado.",
                    "Tchau, espanta-pombo.",
                    "Vai embora, seu Wi-Fi de 1 barrinha.",
                    "Até mais, seu Ctrl+C Ctrl+V.",
                    "Flw, calabreso.",
                    "Vai, seu boneco de posto.",
                    "Some, seu NPC de tutorial.",
                    "Tchau, seu lagado.",
                    "Vai farmar XP primeiro.",
                    "Volta quando desbloquear o cérebro.",
                    "Tchau, seu CLT premium.",
                    "Vai lá, liso.",
                    "Até mais, rei da gambiarra.",
                    "Some, seu HTML sem CSS.",
                    "Vai estudar, cabeção.",
                    "Tchau, seu bug ambulante.",
                    "Vai carregar o celular, miserinha.",
                    "Flw, seu beta de fábrica.",
                    "Volta quando tiver aura.",
                    "Tchau, jogador de Free Fire no ultra low.",
                    "Vai lá, seu filtro de barro.",
                    "Até mais, seu mouse sem clique.",
                    "Some, sua batata.",
                    "Tchau, seu teclado sem Enter.",
                    "Vai embora antes que eu cobre aluguel.",
                    "Flw, seu cidadão duvidoso.",
                    "Vai tocar uma grama, meu patrão.",
                    "Tchau, seu JPEG borrado.",
                    "Vai resetar esse cérebro aí.",
                    "Até mais, seu meme vencido.",
                    "Some, seu pão sem miolo.",
                    "Tchau, seu pinguim de chinelo.",
                    "Vai com calma, seu bobão.",
                    "Volta depois de uma atualização."]
                    print(frases[random.randint(0,len(frases)-1)])
                    return "Vai embora!!!!!!!!!"


                elif viu.strip() == texto.strip():
                    proximalinha = conhecimento.readline()
                    if "ChatBot: " in proximalinha:
                        return proximalinha


            else:
                print("Sua pergunta nao existe aqui.")
                conhecimento.write(f"\n{texto}")
                resposta_user = input("O que esperava?\n")
                conhecimento.write(f"\nChatBot: {resposta_user}")
                return "AHHHHHHH AGORA EU ENTENDI, AGORA EU SAQUEI"



def exibeResposta(resposta, nome):
    print(resposta.replace("ChatBot",nome))
    if resposta == "Vai embora!!!!!!!!!":
        return "Vai embora!!!!!!!!!"
    return "continua"

def exibeResposta_GUI(texto, resposta, nome):
    return resposta.replace("ChatBot", nome)

def saudacoes_GUI(nome):
    import random
    frases = [f"Bom dia! Meu nome é {nome}! Como vai você?","Olá","Vai embora seu betinha sem aura", f"Boa Tarde! Meu nome é {nome}! Como vai você?", f"Boa noite! Meu nome é {nome}! Como vai você?"]
    return frases[random.randint(0,4)]

def salva_sugestao(sugestao):
    with open("base.txt", "a", encoding="uft-8") as conhecimento:
        conhecimento.write(f"ChatBot: {sugestao}\n")


def buscaResposta_GUI(texto):
    with open("base.txt", "a+", encoding="utf-8") as conhecimento:
        conhecimento.seek(0)
        while True:
            viu = conhecimento.readline()
            if viu != "":
                if  jaccard(texto, viu) >0.3:
                    proximalinha = conhecimento.readline()
                    if "ChatBot: " in proximalinha:
                        return proximalinha
            else:
                conhecimento.write(texto)
                return"Sua pergunta nao existe aqui."


def jaccard(textoUsuario, textoBase):
    textoUsuario = limpa_frase(textoUsuario)
    textoBase = limpa_frase(textoBase)
    if len(textoBase) < 1:
        return 0
    else:
        palavras_em_comum = 0
        for palavra in textoUsuario.split():
            if palavra in textoBase.split():
                palavras_em_comum += 1

        return palavras_em_comum/(len(textoBase.split()))


def limpa_frase(frase):
    tirar = ["?","!","...",".",",","Cliente", "\n"]
    for t in tirar:
        frase = frase.replace(t,"")
    frase = frase.upper()
    return frase