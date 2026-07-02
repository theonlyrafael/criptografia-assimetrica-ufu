"""
Seguranca da Informacao - Exercicio de Criptografia Assimetrica (RSA)
Objetivo: descobrir qual dos arquivos 'assinadoN.txt' foi realmente assinado
pela chave privada, comparando cada um com 'assinatura.sha256' atraves da
chave publica. Responde a Pergunta 2 do trabalho.

Como funciona:
  - O professor assinou APENAS UM dos 5 arquivos assinadoN.txt com a
    chave privada (openssl pkeyutl -sign), gerando 'assinatura.sha256'.
  - Uma assinatura digital so e validada com sucesso (openssl pkeyutl -verify)
    quando comparada com o mesmo conteudo que foi originalmente assinado.
  - Por isso, basta testar a assinatura contra cada um dos 5 arquivos:
    apenas um deles resultara em "Signature Verified Successfully".
  - Observacao: 'pkeyutl -sign', sem a opcao '-pkeyopt digest:sha256',
    assina diretamente os bytes do arquivo (padding PKCS#1 v1.5), sem
    calcular antes um hash SHA-256 -- por isso funciona mesmo o arquivo
    nao tendo sido reduzido a um digest antes da assinatura.
"""

import subprocess
from pathlib import Path

PASTA = Path(__file__).parent
CHAVE_PUBLICA = PASTA / "chave_publica.pem"
ASSINATURA = PASTA / "assinatura.sha256"
CANDIDATOS = sorted(PASTA.glob("assinado*.txt"))


def verificar(chave_publica: Path, assinatura: Path, candidato: Path) -> bool:
    """
    Executa 'openssl pkeyutl -verify' para checar se 'assinatura' corresponde
    a assinatura de 'candidato' feita com a chave privada correspondente a
    'chave_publica'. Retorna True se a verificacao for bem-sucedida.
    """
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