import pandas as pd
import zipfile

# 1. Extraction and loading
with zipfile.ZipFile("data.zip") as z:
    with z.open("DS_SIDE_CREA_EI_2024_data.csv") as f1, z.open("DS_SIDE_CREA_EI_2024_metadata.csv") as f2:
        data = pd.read_csv(f1, sep=";", encoding="utf-8")
        meta = pd.read_csv(f2, sep=";", encoding="utf-8")

print("✅ Data loaded successfully")


# 2. Creating dimension tables
def create_dim(var_code, filename):
    dim = meta[meta['COD_VAR'] == var_code][['COD_MOD', 'LIB_MOD']].copy()
    dim.columns = [var_code, f'Libelle_{var_code}']
    dim.to_csv(f'Star_schema_tables/Dim_{filename}.csv', index=False, sep=';')
    return dim

dim_activite = create_dim('ACTIVITY', 'Activity')
dim_age = create_dim('AGE', 'Age')
dim_sexe = create_dim('SEX', 'Sex')
dim_legal = create_dim('LEGAL_FORM', 'Legal_form')

## DIM_GEO

# Get labels
labels = meta[meta['COD_VAR'] == 'GEO'][['COD_MOD', 'LIB_MOD']].drop_duplicates(subset=['COD_MOD'])
labels.columns = ['GEO', 'Label']

# Get department data
df_auto = data[data['GEO_OBJECT'].isin(['DEP', 'FRANCE'])][['GEO', 'GEO_OBJECT']].drop_duplicates()
df_auto = pd.merge(df_auto, labels, on='GEO', how='left')

# Make region mappings
regions_mapping = {
    '11': 'Île-de-France', '24': 'Centre-Val de Loire', '27': 'Bourgogne-Franche-Comté',
    '28': 'Normandie', '32': 'Hauts-de-France', '44': 'Grand Est', '52': 'Pays de la Loire',
    '53': 'Bretagne', '75': 'Nouvelle-Aquitaine', '76': 'Occitanie', 
    '84': 'Auvergne-Rhône-Alpes', '93': "Provence-Alpes-Côte d'Azur", '94': 'Corse', '01': 'Guadeloupe',
    '02': 'Martinique',
    '03': 'Guyane',
    '04': 'La Réunion',
    '06': 'Mayotte'
}

df_regions = data[data['GEO_OBJECT'] == 'REG'][['GEO', 'GEO_OBJECT']].drop_duplicates()
df_regions['Label'] = df_regions['GEO'].map(regions_mapping)

# Concatenate 
dim_geo = pd.concat([df_auto, df_regions])

dim_geo['ID'] = dim_geo['GEO_OBJECT'] + "_" + dim_geo['GEO'].astype(str)
dim_geo = dim_geo[['ID', 'GEO_OBJECT', 'GEO', 'Label']]

dim_geo.to_csv('Star_schema_tables/Dim_Geo.csv', index=False, sep=';', encoding='utf-8')