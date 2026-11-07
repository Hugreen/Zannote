# Zannote

Zannote est un logiciel d'annotation d'images avec comptage assisté par IA (modèle « ZeggCounter »). Il permet d'annoter des images à la main, d'utiliser un modèle pour détecter automatiquement les objets à compter, et d'exporter les résultats en CSV et en tableau récapitulatif Excel.

Des guides détaillés (utilisateur et développeur) sont disponibles dans le dossier [`docs/`](docs/).

---

## Télécharger l'application

Les versions prêtes à l'emploi sont sur la page des Releases :

➡️ **https://github.com/Hugreen/Zannote/releases/latest**

- **Windows** : télécharger `Zannote_windows_1.0.0.zip`, le décompresser, puis lancer `Zannote.exe`.
  Windows peut afficher un avertissement SmartScreen (l'application n'est pas signée) : cliquer sur « Informations complémentaires », puis « Exécuter quand même ».
- **Linux (Ubuntu)** : ⚠️ Téléchargez toutes les parties .part00X dans le même dossier, recollez-les, puis vérifiez le SHA256 avant de décompresser.

Aucune installation de Python n'est nécessaire pour utiliser ces versions.

---

## Utiliser le code source

### Prérequis

* Python 3.11 ou supérieur
* Git
* Environ 20 Go d'espace disque libre recommandés
* Pour l'entraînement : GPU NVIDIA recommandé (CUDA). Un CPU suffit pour utiliser l'application, mais l'entraînement y est beaucoup plus lent.

### Récupérer le code

```bash
git clone https://github.com/Hugreen/Zannote.git
cd Zannote
```

### Créer l'environnement Python

Avec conda :

```bash
conda create -n zannote python=3.11
conda activate zannote
```

Ou avec venv :

```bash
python -m venv zannote_env
```

Sous Windows :

```bash
zannote_env\Scripts\activate
```

Sous Linux :

```bash
source zannote_env/bin/activate
```

### Installer PyTorch

GPU NVIDIA (recommandé) : consulter la commande officielle correspondant à la version CUDA installée sur https://pytorch.org/get-started/locally/

Exemple :

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128
```

CPU uniquement :

```bash
pip install torch torchvision torchaudio
```

Vérification :

```python
import torch

print(torch.__version__)
print(torch.cuda.is_available())
```

`True` s'affiche si un GPU CUDA est correctement détecté.

### Installer les dépendances du projet

```bash
pip install -r requirements.txt
```

Pour l'entraînement de modèles, ajouter :

```bash
pip install albumentations matplotlib tqdm
```

### Lancer l'application

Depuis la racine du dépôt :

```bash
python main.py
```

L'application a besoin d'un modèle pour la détection automatique. Télécharger un modèle depuis la page des [Releases](https://github.com/Hugreen/Zannote/releases/latest) et placer son dossier de version (par exemple `V003_epoque_36/`, contenant `best_model.pt`) dans :

```text
ai_models/zegg_counter/models/
```

Le modèle apparaît ensuite dans le menu « Utiliser un modèle ».

---

## Entraîner un nouveau modèle

L'entraînement se lance en ligne de commande. La page « Entraîner un modèle » de l'application n'est pas encore disponible.

### Où placer les données

Créer le dossier `dataset/` **à la racine du dépôt** (à côté de `main.py`) :

```text
Zannote/
├── main.py
└── dataset/
    ├── images/
    │   ├── image_001.jpg
    │   ├── image_002.jpg
    │   └── ...
    ├── labels/
    │   ├── image_001.csv
    │   ├── image_002.csv
    │   └── ...
    └── test/
        ├── images/
        └── labels/
```

- Chaque image doit avoir un CSV du même nom (sans l'extension) dans `labels/`.
- Formats d'image acceptés : `.jpg`, `.jpeg`, `.png`, `.bmp`, `.tif`, `.tiff`.
- Le dossier `test/images/` doit exister, même vide. Les images qu'il contient sont exclues de l'entraînement et de la validation.
- Les fichiers `train.txt`, `val.txt` et le dossier `split/` sont générés automatiquement.

Chaque CSV contient les coordonnées de chaque élément annoté :

```csv
x,y
125,412
318,940
742,1051
```

### Lancer l'entraînement

Depuis la racine du dépôt :

```bash
python -m ai_models.zegg_counter.train
```

Si des modèles existent déjà, le script propose de reprendre depuis le dernier checkpoint, depuis le meilleur, ou de repartir de zéro.

Les modèles entraînés sont sauvegardés automatiquement dans :

```text
ai_models/zegg_counter/models/
├── V001/
├── V002/
└── ...
```

Chaque dossier de version contient notamment `best_model.pt`, `metrics.json`, `metadata.json`, `config.py`, `train_split.txt` et `val_split.txt`. Les modèles ainsi produits sont directement utilisables dans l'application.

---

## Construire l'exécutable

Les fichiers `Zannote_windows.spec` et `Zannote_linux.spec` décrivent la compilation avec PyInstaller :

```bash
pyinstaller Zannote_windows.spec   # sous Windows
pyinstaller Zannote_linux.spec     # sous Linux
```

L'exécutable est généré dans `dist/`.
