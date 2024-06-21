# Projet4_Tournoi_Jeux_Echecs


# Projet 4 :  <Projet4_Tournoi_Jeux_Echecs>

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
          

## Acknowledgements

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)


## Authors

- [@octokatherine](https://www.github.com/octokatherine)


## API Reference

#### Get all items

```http
  GET /api/items
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get item

```http
  GET /api/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### add(num1, num2)

Takes two numbers and returns the sum.


## Badges

Add badges from somewhere like: [shields.io](https://shields.io/)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

## Color Reference

| Color             | Hex                                                                |
| ----------------- | ------------------------------------------------------------------ |
| Example Color | ![#0a192f](https://via.placeholder.com/10/0a192f?text=+) #0a192f |
| Example Color | ![#f8f8f8](https://via.placeholder.com/10/f8f8f8?text=+) #f8f8f8 |
| Example Color | ![#00b48a](https://via.placeholder.com/10/00b48a?text=+) #00b48a |
| Example Color | ![#00d1a0](https://via.placeholder.com/10/00b48a?text=+) #00d1a0 |


## Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.


## Demo

Insert gif or link to demo


## Lessons Learned

What did you learn while building this project? What challenges did you face and how did you overcome them?


## Flake8 generate html report

install flake8 with following command

==> pip install flake8-html

then do

flake8 --format=html --htmldir=flake-report


## License

[MIT](https://choosealicense.com/licenses/mit/)

