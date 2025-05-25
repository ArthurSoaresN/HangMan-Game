# Jogo da Forca em Python

Um pequeno e divertido jogo da forca desenvolvido em Python, com o objetivo principal de praticar a sintaxe da linguagem e entender os conceitos fundamentais de programação.

📘 [Read in English](README.md)
---

## 🎯 Objetivo do Projeto

Este projeto foi criado como um exercício prático para aprender e solidificar conhecimentos em:

* **Sintaxe Básica do Python**: Como variáveis, tipos de dados (strings, listas), operadores, etc.
* **Estruturas de Controle de Fluxo**: Uso de `if`, `elif`, `else`, `while` e `for` loops.
* **Funções**: Definição e chamada de funções (`def`).
* **Manipulação de Strings e Listas**: Operações como `.join()`, `len()`, acesso por índice `[]`, e mutabilidade de listas vs. imutabilidade de strings.
* **Entrada e Saída (I/O)**: Utilização de `print()` para exibir informações e `input()` para obter dados do usuário.
* **Módulos Nativos**: Como `os` (para limpar a tela) e `random` (para escolher palavras aleatoriamente).
* **F-strings**: Uma forma moderna e eficiente de formatar strings.
* **Tratamento de Erros Básicos**: Como `try-except` para entradas de usuário (se você implementou validação de `int(input())`).
* **Lógica de Jogo**: Implementação de regras básicas de um jogo de terminal.

---

## ✨ Funcionalidades

* Jogo da forca clássico com palavras em português (ou inglês, dependendo da sua escolha).
* Contagem regressiva de chances.
* Desenho do boneco da forca que evolui a cada erro.
* Limpeza de tela para uma melhor experiência visual.
* Validação de entrada do usuário (garante que apenas uma letra seja digitada).
* Opção de jogar novamente ao final da partida.
* Menu inicial simples para iniciar ou sair do jogo.

---

## 🚀 Como Rodar o Jogo

Para jogar, siga estes passos:

1.  **Clone o repositório** (ou baixe o arquivo `main.py` diretamente).
2.  **Navegue até a pasta do projeto** no seu terminal ou prompt de comando.
3.  **Execute o script Python**:
    ```bash
    python main.py
    ```
4.  Siga as instruções na tela para começar a jogar!

---

## 💡 Lições Aprendidas e Desafios Superados

* **Imutabilidade de Strings vs. Mutabilidade de Listas**: Entender por que `palavra_secreta` não pode ser modificada diretamente e a necessidade de usar uma lista (`palavra_oculta`) para revelar as letras.
* **Gerenciamento de Loops (`while` e `for`)**: A importância de `break` para sair de loops e a correta condição do `while` para encerrar o jogo por vitória ou derrota.
* **Ordem de Execução e `limpar_tela()`**: A necessidade de chamar `limpar_tela()` no início de cada rodada e de re-imprimir todo o estado do jogo.
* **Comparações em Python**: Usando `==` para igualdade e `in`/`not in` para verificar a presença de elementos, de forma mais Pythônica que em outras linguagens.
* **Erros de Codificação (Encoding)**: Entender e solucionar o `UnicodeEncodeError` ao usar caracteres especiais (se você os tentou).

---

## 👨‍💻 Contribuição

Este é um projeto de aprendizado, mas sinta-se à vontade para inspecionar o código, sugerir melhorias ou utilizá-lo como base para seus próprios estudos.

---

## 📄 Licença

Este projeto está sob a licença [MIT](https://opensource.org/licenses/MIT) (ou outra licença de sua escolha, se preferir).