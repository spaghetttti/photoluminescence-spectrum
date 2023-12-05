# photoluminescence-spectrum
https://github.com/spaghetttti/photoluminescence-spectrum
### Version Française :

#### Vue d'ensemble du Projet : Analyse de Spectre de Photoluminescence

Le projet vise à analyser les données de spectre de photoluminescence obtenues à partir d'un fichier contenant des mesures de longueur d'onde et d'intensité. Il comprend des scripts Python et Bash pour traiter, indexer et visualiser graphiquement les données d'intensité dans des plages de longueurs d'onde spécifiées.

#### Fichiers et Fonctions :

1. **`intensite.py`** :
    - **Fonctionnalités** :
        - Lit et indexe les données d'intensité à partir du fichier de spectre.
        - Organise les données d'intensité en fenêtres de longueurs d'onde.
        - Calcule des statistiques (telles que le nombre de points de données, l'intensité minimale, maximale et moyenne) dans chaque fenêtre de longueur d'onde.
    - **Fonctions** :
        - `read_spectrum_file(file_path)`: Lit et extrait les longueurs d'onde et les intensités du fichier de spectre.
        - `organize_data(wavelengths, intensities, window_size=10)`: Segment les données d'intensité en fenêtres de longueur d'onde spécifiées.
        - `calculate_statistics(intensity_data)`: Calcule les métriques statistiques pour les données d'intensité dans chaque fenêtre de longueur d'onde.

2. **`recherche_plot.py`** :
    - **Fonctionnalités** :
        - Visualise graphiquement les données d'intensité dans une plage de longueurs d'onde spécifique définie par l'utilisateur.
    - **Fonctions** :
        - `read_intensity_data(file_path)`: Lit et extrait les intensités dans des marqueurs spécifiques du fichier de spectre.
        - `plot_intensity(wavelengths, intensities, start, end)`: Trace les valeurs d'intensité dans une plage de longueurs d'onde donnée.

3. **`main.sh`** (Script Bash) :
    - Orchestrer l'exécution des scripts Python (`intensite.py` et `recherche_plot.py`).
    - Gère l'interaction avec l'utilisateur, exécute le traitement des données et la visualisation en fonction de l'entrée de l'utilisateur.

#### Flux de Travail :

- **Lecture de Données et Indexation** :
    - `intensite.py` lit le fichier de spectre et extrait les données de longueur d'onde et d'intensité.
    - Indexe les données d'intensité en fenêtres de longueur d'onde et calcule des statistiques (optionnel).

- **Visualisation** :
    - `recherche_plot.py` permet aux utilisateurs de spécifier un intervalle de longueur d'onde pour visualiser les données d'intensité de manière graphique.

#### Utilisation :
- Exécuter `main.sh` avec le chemin du fichier de spectre en tant qu'argument.
- Le script exécute `intensite.py` pour indexer les données d'intensité et propose des options pour visualiser l'intensité dans des plages de longueurs d'onde spécifiées.

#### Objectif :
Le projet offre une approche structurée pour extraire, traiter et visualiser les données de spectre de photoluminescence. Il permet de segmenter les données d'intensité en fenêtres de longueur d'onde, de calculer des statistiques et de représenter graphiquement les variations d'intensité dans des intervalles de longueur d'onde spécifiques.

#### Conclusion :
En fournissant des outils d'analyse et de visualisation, le projet aide à comprendre les caractéristiques et les distributions des données d'intensité dans des plages de longueurs d'onde distinctes, facilitant ainsi des insights scientifiques et des analyses approfondies dans les études de spectre de photoluminescence.


### English Version:

#### Project Overview: Photoluminescence Spectrum Analysis

The project aims to analyze photoluminescence spectrum data obtained from a file containing wavelength and intensity measurements. It encompasses Python and Bash scripts to process, index, and graphically visualize intensity data within specified wavelength ranges.

#### Files and Functions:

1. **`intensite.py`**:
    - **Functionalities**:
        - Reads and indexes intensity data from the spectrum file.
        - Organizes intensity data into wavelength windows.
        - Calculates statistics (such as number of data points, minimum, maximum, and average intensity) within each wavelength window.
    - **Functions**:
        - `read_spectrum_file(file_path)`: Reads and extracts wavelengths and intensities from the spectrum file.
        - `organize_data(wavelengths, intensities, window_size=10)`: Segments intensity data into specified wavelength windows.
        - `calculate_statistics(intensity_data)`: Computes statistical metrics for intensity data within each wavelength window.

2. **`recherche_plot.py`**:
    - **Functionalities**:
        - Graphically visualizes intensity data within a user-specified wavelength range.
    - **Functions**:
        - `read_intensity_data(file_path)`: Reads and extracts intensities at specific markers from the spectrum file.
        - `plot_intensity(wavelengths, intensities, start, end)`: Plots intensity values within a given wavelength range.

3. **`main.sh`** (Bash Script):
    - Orchestrates the execution of Python scripts (`intensite.py` and `recherche_plot.py`).
    - Manages user interaction, executes data processing, and visualization based on user input.

#### Workflow:

- **Data Reading and Indexing**:
    - `intensite.py` reads the spectrum file and extracts wavelength and intensity data.
    - Indexes intensity data into wavelength windows and optionally calculates statistics.

- **Visualization**:
    - `recherche_plot.py` enables users to specify a wavelength interval for graphical representation of intensity data.

#### Usage:
- Run `main.sh` with the spectrum file path as an argument.
- Executes `intensite.py` to index intensity data and offers options to visualize intensity within specified wavelength ranges.

#### Objective:
The project offers a structured approach to extract, process, and visualize photoluminescence spectrum data. It segments intensity data into wavelength windows, computes statistics, and graphically represents intensity variations within specific wavelength intervals.

#### Conclusion:
By providing analysis and visualization tools, the project aids in understanding intensity data characteristics and distributions within distinct wavelength ranges, facilitating scientific insights and in-depth analyses in photoluminescence spectrum studies.
