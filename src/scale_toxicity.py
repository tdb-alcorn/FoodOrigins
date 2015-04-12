def check_toxicity(x):
    if x <= 5:
        return "Very Toxic"
    elif x <= 5 and x >= 50:
        return "Toxic"
    elif x <= 50 and x >= 300:
        return "Moderately Toxic"
    elif x <= 300 and x >= 2000:
        return "Not Toxic"
    elif x == "Varies":
        return "Unknown"
    else:
        return "Unknown"


def get_ld50(x):
    chemicals = {
        'Bipiridils': 157,
        'Anticoagulants': 280,
        'Botanic prod&biologSdTrF': "Varies",
        'Carbamates-insect-SdTr': 500,
        'Chlorinated Hydrocarbons': 18,
        'Urea derivates': 11000,
        'Uracil': 6000,
        'Mineral Oils': "Varies",
        'Triazines': 672,
        'Organo-Phosphates': 1300,
        'Inorganics': "Varies",
        'Botanic.Produc&Biologic.': "Varies",
        'Carbamates Herbicides': 30000,
        'Amides': 380,
        'Triazoles diazoles-SdTrF': 1453,
        'Disinfectants': 192,
        'Phenoxy Hormone Products': 930,
        'Benzimidazoles-SeedTrF': 385,
        'Carbamates Insecticides': 500,
        'Pyrethroids': 2000,
        'Dithiocarbamates-SeedTrF': 400,
        'Dinitroanilines': 10000,
        'Triazoles, Diazoles': 1453,
        'Diazines, Morpholines': 3900,
        'Organo-phospates-SdTr In': 1300,
        'Narcotics': 127,
        'Plant Growth Regulators': "Varies",
        'Benzimidazoles': 385,
        'Pyrethroids-SeedTr Ins': 2000,
        'Dithiocarbamates': 400,
        'Sulfonyl Ureas': 2000
    }
    if x in chemicals:
        return chemicals.get(x)
    else:
        return "NONE"


def get_tox(chemical):
    lDValue = get_ld50(chemical)
    toxicity = check_toxicity(lDValue)
    return toxicity
