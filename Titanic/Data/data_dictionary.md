## Descrição do Conjunto de Dados

### Visão Geral

Os dados foram divididos em dois grupos:

- **Conjunto de treinamento (`train.csv`)**: 
  - Deve ser usado para construir seus modelos de aprendizado de máquina. 
  - Para o conjunto de treinamento, fornecemos o resultado (também conhecido como "verdade de base") para cada passageiro. 
  - Seu modelo será baseado em "features" (características) como gênero e classe dos passageiros. Você também pode usar engenharia de features para criar novas características.

- **Conjunto de teste (`test.csv`)**: 
  - Deve ser usado para avaliar o desempenho do seu modelo em dados não vistos. 
  - Para o conjunto de teste, não fornecemos a verdade de base para cada passageiro. É sua responsabilidade prever esses resultados.
  - Para cada passageiro no conjunto de teste, use o modelo que você treinou para prever se eles sobreviveram ao naufrágio do Titanic.

Além disso, incluímos o arquivo `gender_submission.csv`, que contém um conjunto de previsões que assume que todos os passageiros do sexo feminino sobrevivem, como um exemplo do que um arquivo de submissão deve parecer.

### Dicionário de Dados

| Variável   | Definição                      | Chave                                   |
|------------|--------------------------------|-----------------------------------------|
| survival   | Sobrevivência                  | 0 = Não, 1 = Sim                        |
| pclass     | Classe do bilhete              | 1 = 1ª, 2 = 2ª, 3 = 3ª                 |
| sex        | Sexo                           |                                         |
| age        | Idade em anos                 |                                         |
| sibsp      | Número de irmãos/cônjuges a bordo |                                     |
| parch      | Número de pais/filhos a bordo  |                                         |
| ticket     | Número do bilhete              |                                         |
| fare       | Tarifa do passageiro           |                                         |
| cabin      | Número da cabine               |                                         |
| embarked   | Porto de embarque              | C = Cherbourg, Q = Queenstown, S = Southampton |

### Notas sobre as Variáveis

- **pclass**: Um proxy para o status socioeconômico (SES)
  - 1ª = Superior
  - 2ª = Médio
  - 3ª = Inferior

- **age**: A idade é fracionária se for menor que 1. Se a idade for estimada, está na forma xx.5.

- **sibsp**: O conjunto de dados define relações familiares desta forma:
  - Irmão = irmão, irmã, meio-irmão, meia-irmã
  - Cônjuge = marido, esposa (amantes e noivos foram ignorados)

- **parch**: O conjunto de dados define relações familiares desta forma:
  - Pai = mãe, pai
  - Filho = filha, filho, enteada, enteado
  - Algumas crianças viajaram apenas com uma babá, portanto parch=0 para elas.

---

## Dataset Description

### Overview

The data has been split into two groups:

- **Training set (`train.csv`)**: 
  - This should be used to build your machine learning models. 
  - For the training set, we provide the outcome (also known as the "ground truth") for each passenger. 
  - Your model will be based on features like passengers' gender and class. You can also use feature engineering to create new features.

- **Test set (`test.csv`)**: 
  - This should be used to evaluate how well your model performs on unseen data. 
  - For the test set, we do not provide the ground truth for each passenger. It is your job to predict these outcomes.
  - For each passenger in the test set, use the model you trained to predict whether or not they survived the sinking of the Titanic.

We also include `gender_submission.csv`, a set of predictions that assume all and only female passengers survive, as an example of what a submission file should look like.

### Data Dictionary

| Variable   | Definition                      | Key                                   |
|------------|---------------------------------|---------------------------------------|
| survival   | Survival                        | 0 = No, 1 = Yes                      |
| pclass     | Ticket class                    | 1 = 1st, 2 = 2nd, 3 = 3rd           |
| sex        | Sex                             |                                       |
| age        | Age in years                   |                                       |
| sibsp      | # of siblings / spouses aboard  |                                       |
| parch      | # of parents / children aboard   |                                       |
| ticket     | Ticket number                   |                                       |
| fare       | Passenger fare                  |                                       |
| cabin      | Cabin number                    |                                       |
| embarked   | Port of Embarkation             | C = Cherbourg, Q = Queenstown, S = Southampton |

### Variable Notes

- **pclass**: A proxy for socio-economic status (SES)
  - 1st = Upper
  - 2nd = Middle
  - 3rd = Lower

- **age**: Age is fractional if less than 1. If the age is estimated, it is in the form of xx.5.

- **sibsp**: The dataset defines family relations in this way:
  - Sibling = brother, sister, stepbrother, stepsister
  - Spouse = husband, wife (mistresses and fiancés were ignored)

- **parch**: The dataset defines family relations in this way:
  - Parent = mother, father
  - Child = daughter, son, stepdaughter, stepson
  - Some children traveled only with a nanny, therefore parch=0 for them.

