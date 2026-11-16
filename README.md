# Sistema de Assistencia Tecnica de Celular (projeto em grupo)

Programa em Python que apoia uma assistencia tecnica de celulares na abertura de ordens de servico, no calculo de orcamentos e no fechamento do dia. Trabalho academico desenvolvido em grupo na Unisa (Analise e Desenvolvimento de Sistemas).

## Funcionalidades

- Abertura de ordens de servico.
- Aplicacao do preco do conserto.
- Acrescimo por urgencia.
- Regras de parcelamento.
- Relatorio de fechamento do dia.

## Minha participacao

Este e um projeto em grupo, e eu nao fiz tudo sozinho.

- Configuracoes iniciais (marcadas no codigo como "CONFIGURACOES INICIAIS / GUSTAVO"): dicionario com os valores dos servicos, lista de respostas validas, e as listas e contadores que guardam o que o usuario digita (ordens de servico, parcelamento, quantidade de trocas de tela, bateria, conector, software e ordens urgentes) ate ele encerrar o dia.
- Loop principal do programa (marcado no codigo como "LOOP PRINCIPAL / GUSTAVO"): menu com as opcoes "Abrir OS" e "Encerrar o dia", que se repete ate o usuario encerrar, com validacao da opcao digitada.
- Ideias e sugestoes em outras partes do programa.

As demais partes foram desenvolvidas por outros integrantes do grupo: Jonathan, Samuel.

## Avaliacao

O programa foi avaliado com base em normas de qualidade de software:

- Testes funcionais com 48 combinacoes de orcamento, todas corretas.
- 200 medicoes de tempo, com cerca de 14 microssegundos por ordem.
- Crescimento linear do tempo total ate 10 mil ordens.

## O que ficou de fora e limitacoes

- O programa encerra com erro quando o usuario digita letras em campos numericos. A melhoria recomendada e validar as entradas.
- [ADICIONAR O QUE MAIS FICOU DE FORA, se houver]

## Como executar

1. Tenha o Python 3 instalado.
2. No terminal, dentro da pasta do projeto, execute: `python assistencia.py`

## Tecnologias

- Python

## Contato

- LinkedIn: linkedin.com/in/gustavodelimamaximo
- E-mail: maximogustavo47@gmail.com
