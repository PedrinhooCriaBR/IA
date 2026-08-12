import chaat as ia
from tkinter import *

main_window = Tk()

main_window.title("Krona IA")
main_window.geometry("1200x800")

main_window.grid_rowconfigure(0, weight=1)
main_window.grid_columnconfigure(0,weight=1)


frame = Frame(main_window)
frame.grid(row=1, column=0, sticky="ew", padx=10, pady=10)

frame.grid_columnconfigure(1, weight=1)

text_box = Label(frame, text="Insira sua mensagem aqui: ")
text_box.grid(row=0, column=0, padx=(0,5))

resposta = Entry(frame)
resposta.grid(row=0, column=1, sticky="ew", padx=5)

frame2 = Frame(main_window)
frame2.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
frame2.grid_rowconfigure(0, weight=1)
frame2.grid_columnconfigure(0, weight=1)

v = StringVar()
Label(frame2, textvariable=v, anchor="nw", justify="left", wraplength=460).grid(row=0, column=0, sticky="nsew")

nome_maquina = "Pedro"
v.set("Qual é o seu nome?")


entrada_sugestao = False
entrada_nome_usuario = True


nome_usuario = ""

def roda_ChatBot():
    global entrada_sugestao
    global entrada_nome_usuario
    global historico_conversa
    global nome_usuario

    if entrada_nome_usuario:
        nome_usuario = resposta.get()
        saudacoes = ia.saudacoes_GUI(nome_maquina)
        historico_conversa = f"{nome_maquina}: {saudacoes}\n"
        v.set(historico_conversa)
        entrada_nome_usuario = False

    else:
        texto = resposta.get()
        historico_conversa += f"\n{nome_usuario}: {texto}"
        v.set(historico_conversa)

        if entrada_sugestao:
            ia.salva_sugestao(texto)
            entrada_sugestao = False
            historico_conversa += "\nAHHHHHHH AGORA EU ENTENDI, AGORA EU SAQUEI. pode continuar."
            v.set(historico_conversa)
        else:
            res = ia.buscaResposta_GUI(f"Cliente: {texto}\n")
            if res == "Sua pergunta nao existe aqui.":
                historico_conversa += "\n Sua pergunta nao existe aqui. O que esperava?\n"
                v.set(historico_conversa)
                entrada_sugestao = True
            else:
                historico_conversa += f"\n{ia.exibeResposta_GUI(texto, res, nome_maquina)}"
                v.set(historico_conversa)

Button(frame, text="Clique", command=roda_ChatBot).grid(row=0, column=2, padx=(5,0))







main_window.mainloop()