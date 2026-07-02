"""
Segurança da Informação - Exercício de Criptografia Assimétrica (RSA)
Objetivo: decifrar o arquivo 'arquivo.txt.enc' utilizando a chave privada RSA
gerada para este aluno, respondendo à Pergunta 1 do trabalho.

Como funciona:
  - O professor gerou um par de chaves RSA (2048 bits) para cada aluno.
  - Um segredo em texto puro foi cifrado com a CHAVE PUBLICA (chave_publica.pem),
    gerando 'arquivo.txt.enc'.
  - Em RSA, o que e cifrado com a chave publica so pode ser decifrado com a
    chave privada correspondente (propriedade de confidencialidade).
  - Este script usa o binario OpenSSL (via subprocess) para realizar a operacao
    inversa: 'pkeyutl -decrypt', a mesma ferramenta usada por exercicio.py
    para cifrar, agora usada para decifrar.
"""

import subprocess
import sys
from pathlib import Path

PASTA = Path(__file__).parent
CHAVE_PRIVADA = PASTA / "chave_privada.pem"
ARQUIVO_CIFRADO = PASTA / "arquivo.txt.enc"
ARQUIVO_SAIDA = PASTA / "arquivo.txt"


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