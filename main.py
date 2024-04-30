import time, os, platform
from unidecode import unidecode

def limpar_terminal():
    sistema_operacional = platform.system()

    if sistema_operacional == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def time_sleep_e_limpar(tempo):
    time.sleep(tempo)
    limpar_terminal()
    
def carregamento():
    print("Só um momento! |......      |")
    time_sleep_e_limpar(1)
    print("Só um momento! |........    |")
    time_sleep_e_limpar(2)
    print("Só um momento! |............|")
    time_sleep_e_limpar(1)

def remover_acentos(frase):
    return unidecode(frase)

limpar_terminal()    
caminho_do_arquivo = input("Digite o caminho do arquivo: ")
limpar_terminal()

with open(caminho_do_arquivo, 'r', encoding='iso-8859-1') as arquivo_entrada:
    linhas = arquivo_entrada.readlines()

linhas_formatadas = []

print("Só um momento! |....        |")
time_sleep_e_limpar(1)

for linha in linhas:
    if linha.startswith("#F"):
        codigo_video = linha[:5]
        indice_clube = linha.find("Club - ") + len("Club - ")
        indice_codigo_final = linha.find("__M")
        codigo_final = linha[indice_codigo_final:].lower().replace("__", "")
        depois_clube_processo_1 = linha[indice_clube:indice_codigo_final].replace(",", "").replace(":", "")
        depois_clube_processo_2 = depois_clube_processo_1.lower().replace(" ", "_").replace("'", "")
        depois_clube_pronto = remover_acentos(depois_clube_processo_2)

        string_formatada = f"{codigo_video}_{depois_clube_pronto}_{codigo_final}"
        linhas_formatadas.append(string_formatada)
    else:
        linhas_formatadas.append(linha)

carregamento()

novo_arquivo = input("Agora, digite o caminho do novo arquivo, assim como nome e formato desejado: ")
limpar_terminal()

with open(novo_arquivo, 'w') as arquivo_saida:
    for linha_formatada in linhas_formatadas:
        arquivo_saida.write(linha_formatada)

print("Procedimento realizado com sucesso!")
time_sleep_e_limpar(3)