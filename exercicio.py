import csv
import random


lista_palavras_limpas = [
    "abacate", "abafado", "abajur", "abalar", "abanar", "abater", "abeto", "abismo", "abono", "aborrecido",
    "abrasivo", "abrigar", "abril", "abrir", "absoluto", "absorver", "abstrato", "absurdo", "abundante", "abusar",
    "acabar", "academia", "acai", "acalmar", "acampar", "acanhado", "acao", "acariciar", "acaso", "aceitar",
    "acender", "acesso", "fiel", "firme", "floresta", "fogo", "folha", "fonte", "forte", "fracao",
    "frase", "frente", "fresco", "frio", "fruta", "fuga", "fumaca", "fundo", "furacao", "futebol",
    "gabarito", "gado", "gaiola", "galaxia", "galeao", "galho", "galinha", "galo", "ganhar", "garagem", 
    "garfo", "gargalo", "garrafa", "garra", "gato", "gatilho", "gaviao", "geladeira", "gelatina", "gelo", 
    "gema", "gemeo", "gemer", "generoso", "gengiva", "genio", "gente", "geral", "gerente", "gesso", 
    "gesto", "gigante", "ginasio", "gincana", "girafa", "girar", "giro", "giz", "globo", "goleiro", 
    "goma", "gondola", "gordura", "gorjeta", "gorro", "gostar", "gosto", "gota", "governo", "gradual", 
    "graca", "grade", "grafite", "grao", "grama", "grampo", "grande", "granito", "gravata", "grito"
]

# Validação do tamanho da lista
#print(f"Total de elementos: {len(lista_palavras_limpas)}")


with open('chamada.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    
    # Optional: Skip the header row
    header = next(reader) 
    
    for row in reader:
        #print(row)  # row is a list, e.g., ['John', '30', 'New York']
        nome = row[0]+row[1]
        nome = nome.replace(" ","")
        print("mkdir ",nome)
        print("cd ",nome)
        print("openssl genpkey -algorithm RSA -out chave_privada.pem -pkeyopt rsa_keygen_bits:2048")
        print("openssl pkey -in chave_privada.pem -pubout -out chave_publica.pem")

        segredo=""
        for _ in range(5):
            segredo =segredo +  random.choice(lista_palavras_limpas)
             
        print("echo ",segredo," > arquivo.txt")
        print("openssl pkeyutl -encrypt -pubin -inkey chave_publica.pem -in arquivo.txt -out arquivo.txt.enc")
        print("rm arquivo.txt")

        for a in range(5):
            segredo=""
            for _ in range(5):
                segredo =segredo +  random.choice(lista_palavras_limpas)
            print(f"echo {segredo} > assinado{a}.txt")

        a= random.choice([0,1,2,3,4])
        print(f"openssl pkeyutl -sign -inkey chave_privada.pem -in assinado{a}.txt -out assinatura.sha256")
        print("cd ..")
        
