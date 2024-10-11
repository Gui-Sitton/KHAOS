# Titanic Survival Prediction

### The Challenge
O naufrágio do Titanic é um dos desastres marítimos mais infames da história. Em 15 de abril de 1912, durante sua viagem inaugural, o RMS Titanic, amplamente considerado "inafundável", afundou após colidir com um iceberg. Infelizmente, não havia botes salva-vidas suficientes para todos a bordo, resultando na morte de 1502 das 2224 pessoas presentes entre passageiros e tripulação.

Embora a sobrevivência envolvesse um certo grau de sorte, alguns grupos de pessoas pareciam ter maior probabilidade de sobrevivência do que outros.

Neste desafio, você deverá construir um modelo preditivo que responda à pergunta: **"Quais tipos de pessoas tinham mais chances de sobreviver?"**, utilizando dados dos passageiros (nome, idade, gênero, classe socioeconômica, etc.).

### Objetivo
O objetivo deste projeto é prever se um passageiro sobreviveu ao naufrágio do Titanic ou não, com base em variáveis como idade, gênero, e classe socioeconômica.

Para cada passageiro no conjunto de teste, você deve prever um valor `0` (não sobreviveu) ou `1` (sobreviveu) para a variável **Survived**.

### Métrica de Avaliação
A performance do modelo será avaliada com base na **acurácia** — a porcentagem de passageiros cuja sobrevivência foi corretamente prevista.

### Conteúdo do Projeto
Este projeto contém os seguintes componentes:

1. **Notebook de pré-processamento e feature engineering**: Limpeza dos dados, pré-processamento e novas colunas.
2. **Notebook de análise exploratória (EDA)**: Investigação dos dados dos passageiros e visualização de padrões.
3. **Notebook de treinamento do modelo**: Criação, ajuste e validação de diferentes modelos de Machine Learning para prever a sobrevivência.
4. **Scripts de pré-processamento**: Funções auxiliares para tratamento de dados, como limpeza e engenharia de variáveis.
