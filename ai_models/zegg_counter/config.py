# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 12:23:49 2026

@author: hugoz
"""

import cv2

from utils.paths import app_root


# Taille de l'image cible en cas de rognage d'image
TARGET_H = 2048
TARGET_W = 3072


# En cas de redimensionnement de l'image on comble en multipliant la dernière ligne / colonne de pixels
BORDER_MODE = cv2.BORDER_CONSTANT


# Heatmap
SIGMA = 15
SIGMA_VAR = 2.5


# Training
BATCH_SIZE = 1
EARLY_STOPPING_PATIENCE = 15
N_EPOCHS = 100
LEARNING_RATE = 8e-5
NUM_WORKERS = 0
WEIGHT_DECAY = 5e-4
BCE_WEIGHT = 0.5
DICE_WEIGHT = 0.5


# Validation
VAL_RATIO = 0.15
RANDOM_SEED = 11


# Test
TEST_SIZE = 50


# Ratio de changement d'augmentation
AUG2_PATIENCE = 6


# Processing de la carte de probabilité prédite par le modèle
PEAK_THRESHOLD = 0.55
PEAK_MIN_DISTANCE = 12


# =====================================================
# Chemins vers les différents répertoires et fichiers
# =====================================================

RACINE = app_root()

DATASET_PATH = RACINE / "dataset"

IMAGE_PATH = DATASET_PATH / "images"
LABEL_PATH = DATASET_PATH / "labels"

TEST_IMAGE_PATH = DATASET_PATH / "test" / "images"
TEST_LABEL_PATH = DATASET_PATH / "test" / "labels"

SPLIT_PATH = DATASET_PATH / "split"
TRAIN_SPLIT = DATASET_PATH / "train.txt"
VAL_SPLIT = DATASET_PATH / "val.txt"


# Modèles
MODEL_PATH = RACINE / "ai_models" / "zegg_counter" / "models"

METADATA_PATH = RACINE / "metadata.json"
TRAINING_HISTORY_PATH = RACINE / "training_history.json"

MODEL_PREFIX = "v"


# Normalisation pour stabiliser l'apprentissage du modèle
GRADIENT_CLIPPING = 1