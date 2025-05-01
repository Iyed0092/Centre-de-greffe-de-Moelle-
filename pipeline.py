import numpy as np
import pandas as pd

chambre_to_cluster = {
    'cabine1': 4, 'cabine10': 4, 'cabine11': 1, 'cabine12': 1, 'cabine2': 2, 'cabine3': 3,
    'cabine4': 0, 'cabine5': 0, 'cabine6': 4, 'cabine7': 1, 'cabine8': 1, 'cabine9': 1,
    'chambre1': 4, 'chambre10': 0, 'chambre11': 1, 'chambre12': 1, 'chambre2': 1, 'chambre3': 1,
    'chambre4': 3, 'chambre5': 1, 'chambre8': 1, 'chambre9': 1, 'chambreabidjan': 4, 'chambrebagdad': 1,
    'chambrecotono': 0, 'chambredakar': 4, 'chambrekhorthoume': 1, 'chambrekods': 4, 'chambrekonakri': 1,
    'chambrelondon': 1, 'chambrelyma': 1, 'chambremoscou': 1, 'chambreniami': 1, 'chambreparis': 1,
    'chambrepikine': 1, 'chambretrabelsi': 1, 'chambretunis': 1
}

cleaning_point_to_cluster = {
    'chaise': 3, 'chaise percée': 2, 'dessus éclairage': 3, 'interphone': 4,
    'lavabo': 1, 'lit': 0, 'matelas': 4, 'mur': 4, 'oreiller': 3, 'poignée de porte': 3,
    'potence': 4, 'table de lit': 3, 'table de nuit': 3, 'élément': 4
}

germs_names =['bacillus', 'bacterie_non_pathogene', 'bacterie_pathogene', 
              'bactérie_gram_negative', 'champignons', 'pseudomonas']

disinfs_names = ['ddn surf',
       'javel', 'nosocomia surf spae', 'nosocomial spray', 'phgo spry',
       'stera surf']

def get_season(month):
    if month in [3, 4, 5]:
        return 1
    elif month in [6, 7, 8]:
        return 2
    elif month in [9, 10, 11]:
        return 3
    else:
        return 0

import numpy as np

class CleaningPipeline:
    def __init__(self,
                 germ_classifier,            # model1
                 germ_number_regressor,      # multi_target_regressor1
                 disinf_classifier,          # model2
                 disinf_volume_regressor):    # multi_target_regressor2
        self.model1 = germ_classifier
        self.reg1   = germ_number_regressor
        self.model2 = disinf_classifier
        self.reg2   = disinf_volume_regressor
        self.germ_names  = germs_names
        self.disinf_names = disinfs_names

    def pipeline1(self, X):
        # Predict multi-label germ presence
        germs_one_hot = self.model1.predict(X)
        # Concatenate features + germ one-hot
        step1_out = np.concatenate((X, germs_one_hot), axis=1)
        # Predict germ counts
        germ_counts = self.reg1.predict(step1_out)
        step_out= np.concatenate((step1_out, germ_counts), axis=1)
        # build germ_dict
        germ_dict = {}
        for i, name in enumerate(self.germ_names):
            if germs_one_hot[0, i] == 1:
                germ_dict[name] = germ_counts[0, i]

        return step_out, germ_dict

    def pipeline2(self, X):
        # Predict disinfectant one-hot
        disinf_one_hot = self.model2.predict(X)
        # Concatenate features + disinfectant one-hot
        step2_out = np.concatenate((X, disinf_one_hot), axis=1)
        # Predict disinfectant volumes
        disinf_vols = self.reg2.predict(step2_out)

        # build disinf_dict
        disinf_dict = {}
        for i, name in enumerate(self.disinf_names):
            if disinf_one_hot[0, i] == 1:
                disinf_dict[name] = disinf_vols[0, i]

        return disinf_dict

    def __call__(self, X):
        """Run the full 4-step pipeline for a single sample X (1×n_features)."""
        X = self.inputFormatter(X)
        step1_out, germ_dict = self.pipeline1(X)
        disinf_dict = self.pipeline2(step1_out)
        return germ_dict, disinf_dict

    @staticmethod
    def inputFormatter(X):
        date_str, surface, service, chambre, cleaning_point = X
        date = pd.to_datetime(date_str)
        season = get_season(date.month)
        surface_encoded = 1 if surface == 'surface' else 0
        service_encoded = 1 if service == 'pédiatrie' else 0
        ch_cluster = chambre_to_cluster.get(chambre, 0)
        cp_cluster = cleaning_point_to_cluster.get(cleaning_point, 0)
        return [[season, surface_encoded, service_encoded, ch_cluster, cp_cluster]]

