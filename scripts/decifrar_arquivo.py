import subprocess
import sys
from pathlib import Path
 
RAIZ_PROJETO = Path(__file__).resolve().parent.parent
CHAVE_PRIVADA = RAIZ_PROJETO / "chave_privada.pem"
ARQUIVO_CIFRADO = RAIZ_PROJETO / "arquivo.txt.enc"
ARQUIVO_SAIDA = RAIZ_PROJETO / "arquivo.txt"
 
 
def decifrar(chave_privada: Path, arquivo_cifrado: Path, arquivo_saida: Path) -> str:
    """
    Executa 'openssl pkeyutl -decrypt' para decifrar arquivo_cifrado
    usando chave_privada, gravando o resultado em arquivo_saida.
    Retorna o conteudo decifrado como string.
    """
    comando = [
        "openssl", "pkeyutl",
        "-decrypt",
        "-inkey", str(chave_privada),
        "-in", str(arquivo_cifrado),
        "-out", str(arquivo_saida),
    ]
 
    resultado = subprocess.run(comando, capture_output=True, text=True)
 
    if resultado.returncode != 0:
        # stderr traz a mensagem de erro do OpenSSL (ex: chave incorreta)
        raise RuntimeError(f"Falha ao decifrar: {resultado.stderr.strip()}")
 
    return arquivo_saida.read_text(encoding="utf-8")
 
 
if __name__ == "__main__":
    for caminho in (CHAVE_PRIVADA, ARQUIVO_CIFRADO):
        if not caminho.exists():
            sys.exit(f"Arquivo nao encontrado: {caminho}")
 
    conteudo = decifrar(CHAVE_PRIVADA, ARQUIVO_CIFRADO, ARQUIVO_SAIDA)
 
    print("=" * 50)
    print("Pergunta 1 - Conteudo de arquivo.txt")
    print("=" * 50)
    print(conteudo)