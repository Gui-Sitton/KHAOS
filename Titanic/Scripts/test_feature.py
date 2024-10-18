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

    df['embarked_s'] = df['embarked_s'].astype(int)
    df['embarked_q'] = df['embarked_q'].astype(int)
    df['embarked_c'] = df['embarked_c'].astype(int)
    #df = df.drop(['embarked_unk'], axis=1)

    # Criar uma nova coluna 'Cabin_Group' que extrai a primeira letra da cabine
    def get_cabin_group(cabin):
        if cabin == 'Unk':
            return 'Unk'
        return cabin[0]

    df['cabin_group'] = df['cabin'].apply(get_cabin_group)


    df['title'] = df['name'].str.extract(r',\s*([^\.]+)\.', expand=False)
    df['last_name'] = df['name'].str.extract(r'([^,]+),', expand=False)
    df['name'] = df['name'].str.extract(r',\s*[^\s]+\s*(.*)', expand=False)

    df['family_size'] = df['sibsp'] + df['parch'] + 1

    df['fare_group'] = pd.cut(df['fare'], 
                          bins=[0, 7.9104, 14.4542, 31.0000, df['fare'].max()], 
                          labels=['Low Fare', 'Medium-Low Fare', 'Medium-High Fare', 'High Fare'])
    

    df['is_alone'] = (df['family_size'] == 1).astype(int)

    df['ticket_length'] = df['ticket'].apply(len)

    df['ticket_qtd'] = df.groupby('ticket')['ticket'].transform('count')

    df['sex_pclass_interaction'] = df['is_male'].apply(lambda x: 'male' if x == 1 else 'female') + '_' + df['pclass'].astype(str)
    df.columns = df.columns.str.lower()
    return df
