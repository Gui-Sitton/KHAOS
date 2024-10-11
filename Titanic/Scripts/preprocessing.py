import pandas as pd
import numpy as np

def preprocess_data(df):
    # Preencher valores ausentes na coluna Age com base nos grupos
    df['Age'] = df.groupby(['Pclass', 'Fare', 'Parch', 'SibSp', 'Embarked'])['Age'].transform(lambda x: x.fillna(x.mean()))
    df['Age'] = df.groupby(['Pclass', 'Parch', 'SibSp', 'Embarked'])['Age'].transform(lambda x: x.fillna(x.mean()))
    df['Age'] = df.groupby(['Pclass', 'Parch', 'Embarked'])['Age'].transform(lambda x: x.fillna(x.mean()))
    df['Age'] = df.groupby(['Pclass', 'Parch'])['Age'].transform(lambda x: x.fillna(x.mean()))


    # One-Hot Encoding para sexo 
    df = pd.get_dummies(df, columns=['Sex'], drop_first=True)
    
    # Preencher valores ausentes na coluna Cabin com 'UNK'
    df['Cabin'] = df['Cabin'].fillna('Unk')


    # Preencher valores ausentes na coluna Embarked com 'UNK' e ohe
    df['Embarked'] = df['Embarked'].fillna('Unk')
    df = pd.get_dummies(df, columns=['Embarked'], prefix='embarked', drop_first=False)
    #Colunas em lower case
    df.columns = df.columns.str.lower()

    return df
