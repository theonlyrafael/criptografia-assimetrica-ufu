# Trabalho de Segurança da Informação — Criptografia Assimétrica (RSA)

> Projeto desenvolvido e finalizado em Julho de 2026 para a matéria de Segurança da Informação.

Este repositório contém a resolução do trabalho prático da disciplina de
Segurança da Informação, do oitavo período do curso de Sistemas de Informação na Universidade Federal
de Uberlândia (UFU). O exercício foi proposto pelo professor através do
script `exercicio.py`, presente na raiz deste repositório, e trabalha com
dois conceitos centrais de criptografia assimétrica: confidencialidade via
cifragem RSA e autenticidade via assinatura digital.

## Como o exercício foi montado

Cada aluno da turma recebeu um conjunto de arquivos gerados individualmente
pelo `exercicio.py`. Para mim, o processo funcionou assim: primeiro o script
gerou um par de chaves RSA de 2048 bits (`chave_privada.pem` e
`chave_publica.pem`); em seguida, cifrou um segredo em texto puro com a minha
chave pública, produzindo o arquivo `arquivo.txt.enc`; por fim, criou cinco
arquivos candidatos (`assinado0.txt` até `assinado4.txt`), cada um com uma
sequência aleatória de palavras, e assinou apenas um deles — escolhido
aleatoriamente — com a minha chave privada, gerando `assinatura.sha256`.

## Os conceitos envolvidos

Como o objetivo do trabalho não é só chegar num resultado, mas entender o
porquê de cada etapa, deixo aqui registrado o raciocínio que segui.

### Confidencialidade: cifrar com a chave pública, decifrar com a privada

Em RSA, tudo que é cifrado com uma chave pública só pode ser decifrado com a
chave privada correspondente. É essa propriedade que garante
confidencialidade: mesmo que qualquer pessoa tenha acesso à minha chave
pública (e, portanto, consiga cifrar mensagens para mim), só eu, com a chave
privada, consigo reverter esse processo. No meu caso, decifrar
`arquivo.txt.enc` não representa nenhum tipo de "quebra" de criptografia — a
chave privada me foi entregue justamente para que eu pudesse fazer essa
operação de forma legítima, e não para eu tentar reverter matematicamente
algo que, sem a chave, seria inviável.

### Autenticidade: assinar com a chave privada, verificar com a pública

Já a assinatura digital funciona ao contrário: quem assina usa a chave
privada, e quem verifica usa a chave pública. A ideia é que só o dono da
chave privada consegue gerar uma assinatura válida para um determinado
conteúdo, e qualquer pessoa com a chave pública correspondente consegue
conferir se aquela assinatura realmente corresponde àquele conteúdo
específico. Foi exatamente esse princípio que usei para descobrir qual dos
cinco arquivos `assinadoN.txt` era o verdadeiro: bastou testar a assinatura
contra cada um deles até encontrar o único que validava.

## As perguntas que preciso responder

O professor pediu duas coisas neste trabalho:

1. Qual o conteúdo de `arquivo.txt`?
2. Qual o conteúdo do arquivo assinado?

## Como organizei a resolução

Para responder as duas perguntas, escrevi dois scripts em Python, que ficam
dentro da pasta `scripts/`: um para decifrar `arquivo.txt.enc` usando a
chave privada, e outro para testar a assinatura contra os cinco candidatos e
identificar qual deles é válido. Os dois usam o próprio OpenSSL por trás dos
panos (via `subprocess`), então não dependem de nenhuma biblioteca externa
de Python — só o binário do OpenSSL instalado na máquina.

As respostas das duas perguntas estão documentadas no README dentro da pasta
`scripts/`, junto dos scripts que as geraram.

A chave privada (`chave_privada.pem`) não é versionada neste repositório,
mas está listada no `.gitignore` porque, ao contrário do resultado da
decifração, ela é uma informação reutilizável: se vazasse, poderia ser usada
para decifrar outros conteúdos ou forjar assinaturas em meu nome.

## Conclusão

Ao concluir este trabalho, entendi na prática a diferença entre cifrar e assinar com RSA, 
já que a chave pública e a chave privada assumem papéis opostos em cada operação. 
Desse modo, percebi que decifrar um arquivo com a chave certa não é quebrar a criptografia, 
mas sim aplicar corretamente o processo para o qual ela foi projetada. 