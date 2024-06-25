# Projet4_Tournoi_Jeux_Echecs


# Projet 4 :  <Projet4_Tournoi_Jeux_Echecs>


## Mise en place du projet: <img src="ressources/Diagram-MVC.pdf" widht="250" height="250">

## Pipeline ETL du code d’application python exécutable à la demande 
      

### Mise en place d’un environnement virtuel 

       < Placez-vous sur la racine du projet  en exécutant le code: cd  Projet4_Tournoi_Jeux_Echecs    >

#### Création de l'environnement virtuel du code 

          - - Exécuter en étant à la racine du projet le code suivant :         ls

          - - Taper et exécuter sur la commande : ls 

        <Vous allez-voir que vous avez créer un document env qui est votre environnement virtuel>

#### Activation de l'environnement virtuel 

         < Pour activer votre environnement virtuel > 

         - - Taper et exécuter sur la commande :                 source env/bin/activate  

         <Vous allez-voir que votre terminal a ajouté  (env) en début de la ligne de commande, ceci est le comportement de l’activation de votre environnement virtuel

### Exécution du code

       - - Taper et exécuter sur la commande le code suivant :                 pip freeze

       <Si vous n’observez pas de paquets installés, ceci est le comportement par défaut de votre environnement virtuel où il faudra installer tous les packages nécessaires à l'exécution du code>

       - - Taper et exécuter sur la commande le code suivant :                   pip install -r requierments.txt


        <Votre terminal va installer tous les paquets de librairies dans votre environnement virtuel >

       - - Taper et exécuter sur la commande le code suivant :                   python3 main.py

        <....>
          
## Flake8 generate html report

install flake8 with following command

==> pip install flake8-html

then do

flake8 --format=html --htmldir=flake-report


## License

[MIT](https://choosealicense.com/licenses/mit/)

