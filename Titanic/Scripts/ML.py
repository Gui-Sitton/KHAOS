
import pandas as pd
import numpy as np




def last_FE(df):
    # Mapeamento para a coluna 'age_group'
    age_group_mapping = {
        'Baby': 1, 'Child': 2, 'Pre-Teen': 3, 'Teenager': 4,
        'Young Adult': 5, 'Adult': 6, 'Senior': 7, 'Elderly': 8
    }
    df['age_group'] = df['age_group'].map(age_group_mapping)
    df['age_group'] = df['age_group'].fillna(0)

    # Mapeamento para a coluna 'cabin_group'
    cabin_group_mapping = {
        'Unk': 0, 'A': 1, 'B': 2, 'C': 3, 'D': 4,
        'E': 5, 'F': 6, 'G': 7, 'T': 8
    }
    df['cabin_group'] = df['cabin_group'].map(cabin_group_mapping)
    df['cabin_group'] = df['cabin_group'].fillna(0)


    # Mapeamento para a coluna 'fare_group'
    fare_group_mapping = {
        'Low Fare': 1, 'Medium-Low Fare': 2, 'Medium-High Fare': 3, 'High Fare': 4
    }
    df['fare_group'] = df['fare_group'].map(fare_group_mapping)
        # Converter para string primeiro
    df['fare_group'] = df['fare_group'].astype(str)
    df['fare_group'] = df['fare_group'].fillna('0')

    # Ou converter para numérico
    df['fare_group'] = df['fare_group'].astype(float)
    df['fare_group'] = df['fare_group'].fillna(0)

    # Mapeamento para a coluna 'sex_pclass_interaction'
    sex_pclass_mapping = {
        'male_3': 1, 'female_1': 2, 'female_3': 3, 'male_1': 4,
        'female_2': 5, 'male_2': 6
    }
    df['sex_pclass_interaction'] = df['sex_pclass_interaction'].map(sex_pclass_mapping)
    df['sex_pclass_interaction'] = df['sex_pclass_interaction'].fillna(0)

    # Mapear os títulos para agrupar valores similares
    title_correction_mapping = {
        'Mme': 'Mrs',    # Mme (Madame) -> Mrs
        'Mlle': 'Miss',  # Mlle (Mademoiselle) -> Miss
        'Ms': 'Miss'     # Ms pode ser agrupado com Miss com base no tamanho da família
    }

    # Aplicar o mapeamento na coluna 'title'
    df['title'] = df['title'].replace(title_correction_mapping)


    # Mapeamento para a coluna 'title'
    title_mapping = {
        'Mr': 1, 'Mrs': 2, 'Miss': 3, 'Master': 4, 'Don': 5,
        'Rev': 6, 'Dr': 7, 'Major': 8,
        'Lady': 9, 'Sir': 10, 'Col': 11, 'Capt': 12,
        'the Countess': 13, 'Jonkheer': 14
    }
    df['title'] = df['title'].map(title_mapping)
    df['title'] = df['title'].fillna(0)
    # Criando uma coluna 'cabin_number', extraindo o número da cabine
    df['cabin_number'] = df['cabin'].str.extract(r'(\d+)').astype(float)

    # Criando uma coluna 'cabin_group' para agrupar números de cabines
    bins = [0, 20, 40, 60, 80, 100, np.inf]
    labels = ['0-20', '21-40', '41-60', '61-80', '81-100', '100+']
    df['cabin_group'] = pd.cut(df['cabin_number'], bins=bins, labels=labels, right=False)

    # Lidando com valores ausentes
    df['cabin_group'] = df['cabin_group'].cat.add_categories('Unknown').fillna('Unknown')
    df['cabin_number'] = df['cabin_number'].fillna(-1)

    # Convertendo todas as colunas para string antes da concatenação
    df['cabin_number_str'] = df['cabin_number'].astype(str)
    df['is_male_str'] = df['is_male'].astype(str)
    df['pclass_str'] = df['pclass'].astype(str)

    # Criando colunas de interação
    df['cabin_number_sex'] = df['cabin_number_str'] + '_' + df['is_male_str']
    df['cabin_number_pclass'] = df['cabin_number_str'] + '_' + df['pclass_str']

    # Criando colunas de interação com cabin_group
    df['cabin_group_sex'] = df['cabin_group'].astype(str) + '_' + df['is_male_str']
    df['cabin_group_pclass'] = df['cabin_group'].astype(str) + '_' + df['pclass_str']

    # Removendo colunas intermediárias se necessário
    df = df.drop(['cabin_number_str', 'is_male_str', 'pclass_str'], axis=1)

    
    # Criar interações entre features
    df['age_pclass_interaction'] = df['age'] * df['pclass']
    df['sex_pclass_interaction2'] = df['is_male'] * df['pclass']

    # Extrair a letra da cabine (deck) se a coluna 'cabin' existir
    def extract_deck(cabin):
        if pd.isna(cabin):
            return 'U'  # 'U' para 'Unknown' se a cabine for NaN
        else:
            return cabin[0]  # Retorna a primeira letra da cabine

    # Criar a coluna 'deck'
    df['deck'] = df['cabin'].apply(extract_deck)

    # Mapear os decks para valores numéricos (ou manter como categórico)
    deck_mapping = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'T': 8, 'U': 0  # 'U' para Unknown
    }
    df['deck'] = df['deck'].map(deck_mapping)


    return df
