# MLEmbarque_transpiler

- Veillez à ce que tous les modules nécessaires soient installés.
Pour ce faire lancez la commande
$
pip install -r requirements.tx
$

- Créez ensuite le joblib contenant le modèle de regression linéaire avec la commande 

$
python3 linear_regression.py
$

Pour créer le script main.c, lancez

$
python3 transpile_simple_model.py
$

Le nombre s'affichant est la prédiction de notre regression logistique.

Lancez ensuite 

$
gcc main.c
$

puis 
$
./a.out
$

Vous verrez la prediction du script main.c s'afficher.
