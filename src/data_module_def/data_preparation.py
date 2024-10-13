import pandas as pd
from src.config_manager import DataPreparationConfig
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import os
from custom_logger import logger


class DataPreparation:
    def __init__(self, config: DataPreparationConfig):
        self.config = config

    def train_test_splitting(self):    
        data = pd.read_csv(self.config.data_path)
        target = self.config.target

        # ave_flot_air_flow : Débit d'air moyen dans le processus de flottation.
        # ave_flot_level : Niveau moyen dans les cellules de flottation.
        # iron_feed : Quantité de minerai de fer entrant dans le processus de flottation.
        # starch_flow : Débit d'amidon utilisé comme réactif dans le processus de flottation.
        # amina_flow : Débit d'amine utilisé comme collecteur dans le processus de flottation.
        # ore_pulp_flow : Débit de la pulpe de minerai.
        # ore_pulp_pH : Niveau de pH de la pulpe de minerai, qui peut affecter le processus de flottation.
        # ore_pulp_density : Densité de la pulpe de minerai, un autre paramètre critique dans le processus de flottation.
        # silica_concentrate : Concentration de silice dans le produit final, qui est la variable cible.

        X = data[['ave_flot_air_flow','ave_flot_level', 'iron_feed', 'starch_flow',
                  'amina_flow', 'ore_pulp_flow', 'ore_pulp_pH', 'ore_pulp_density']]
        # X = data.drop(columns=[target])
        y = data[target]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=self.config.test_size, random_state=42)

        X_train.to_csv(os.path.join(self.config.root_dir, "X_train.csv"), index=False)
        y_train.to_csv(os.path.join(self.config.root_dir, "y_train.csv"), index=False)
        X_test.to_csv(os.path.join(self.config.root_dir, "X_test.csv"), index=False)
        y_test.to_csv(os.path.join(self.config.root_dir, "y_test.csv"), index=False)

        logger.info("Splitted data into training and test sets")
        logger.info(f"X_train shape: {X_train.shape}, y_train shape: {y_train.shape}")
        logger.info(f"X_test shape: {X_test.shape}, y_test shape: {y_test.shape}")

        print(X_train.shape, y_train.shape)
        print(X_test.shape, y_test.shape)

    