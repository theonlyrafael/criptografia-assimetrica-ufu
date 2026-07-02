import subprocess
from pathlib import Path
 
RAIZ_PROJETO = Path(__file__).resolve().parent.parent
CHAVE_PUBLICA = RAIZ_PROJETO / "chave_publica.pem"
ASSINATURA = RAIZ_PROJETO / "assinatura.sha256"
CANDIDATOS = sorted(RAIZ_PROJETO.glob("assinado*.txt"))
 
 
def verificar(chave_publica: Path, assinatura: Path, candidato: Path) -> bool:
    
    # executa 'openssl pkeyutl -verify' para checar se 'assinatura' corresponde a assinatura de 'candidato' feita com a chave privada correspondente a'chave_publica' 
    # retorna True se a verificacao for bem-sucedida
    
    comando = [
        "openssl", "pkeyutl",
        "-verify",
        "-pubin",
        "-inkey", str(chave_publica),
        "-sigfile", str(assinatura),
        "-in", str(candidato),
    ]
    resultado = subprocess.run(comando, capture_output=True, text=True)
    return "Signature Verified Successfully" in resultado.stdout
 
 
if __name__ == "__main__":
    if not CANDIDATOS:
        raise SystemExit("Nenhum arquivo assinadoN.txt encontrado.")
 
    encontrado = None
    for candidato in CANDIDATOS:
        valido = verificar(CHAVE_PUBLICA, ASSINATURA, candidato)
        status = "valida" if valido else "invalida"
        print(f"{candidato.name}: {status}")
        if valido:
            encontrado = candidato
 
    print("=" * 50)
    if encontrado:
        print("Pergunta 2 - Arquivo assinado:", encontrado.name)
        print("Conteudo:", encontrado.read_text(encoding="utf-8"))
    else:
        print("Nenhum arquivo correspondeu a assinatura.")