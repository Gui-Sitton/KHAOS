import pandas as pd
import numpy as np

def engineer_features (df):
# Função para classificar a faixa etária
    def classify_age_group(age):
        if pd.isna(age):
            return np.nan
        elif age < 4:
            return 'Baby'
        elif 5 <= age <= 10:
            return 'Child'
        elif 11 <= age <= 14:
            return 'Pre-Teen'
        elif 15 <= age <= 17:
            return 'Teenager'
        elif 18 <= age <= 24:
            return 'Young Adult'
        elif 25 <= age <= 50:
            return 'Adult'
        elif 51 <= age <= 60:
            return 'Senior'
        else:
            return 'Elderly'

    # Aplicando a função para criar a nova coluna
    df['age_group'] = df['age'].apply(classify_age_group)


    #Nova coluna de Sexo
    df['is_male'] = df['sex_male'].astype(int)
    df = df.drop(['sex_male'], axis=1)


    # Criar uma nova coluna 'Cabin_Group' que extrai a primeira letra da cabine
    def get_cabin_group(cabin):
        if cabin == 'Unk':
            return 'Unk'
        return cabin[0]

    df['cabin_group'] = df['cabin'].apply(get_cabin_group)

    return df
