# Gestion de stock avec statistiques et visualisation
**🎯Objectif**

Réaliser une application en Python qui permet de gérer un stock de produits de manière
simple, calculer des statistiques de base et visualiser les données avec des graphiques.
Le projet doit être développé en binôme, avec une organisation professionnelle :

- Utilisation de Git pour la contribution collaborative.

- Utilisation de Jira pour planifier les tâches.

- Respect d’une structure de fichiers claire et modulaire.

**📂Structure du projet**

        stock-manager/
      
       ── src/
      
            ├── main.py # Point d’entrée, menu principal
      
            ├── stock.py # Fonctions de gestion du stock (ajout,suppression, mise à jour…)
      
            ├── stats.py # Fonctions de calculs statistiques avec numpy
      
            ├── visualize.py # Fonctions de visualisation avec matplotlib
      
            │── menu.py # Menu interactif (console)
      
      │── README.md # Documentation du projet
      
      │── requirements.txt # Dépendances (numpy, matplotlib)
      
      │── .gitignore 

**🚀Installation et utilisation**

1. Cloner le projet:
   
      `git clone https://github.com/Khaoula1025/Gestion-de-stock-avec-statistiques-et-visualisation.git`
   
   
      `cd Gestion-de-stock-avec-statistiques-et-visualisation.git`
   
2. Créer un environnement virtuel:

   `python -m venv venv`

4. Activer l’environnement

    `.\venv\Scripts\activate`
   
5. Installer les dépendances:
   
     `pip install -r requirements.txt`
   
6. Lancer l’application:

     `python src/main.py`


**📊 Fonctionnalités**

 - Gestion du stock
1. Ajouter un produit (nom, quantité, prix).
2.  Supprimer un produit.
3.  Mettre à jour la quantité d’un produit existant.
4.  Afficher la liste des produits disponibles.

- Statistiques sur le stock
1. Valeur totale du stock (somme(prix * quantité)).
2. Prix moyen des produits.
3. Prix minimum et maximum.
4. Produit le plus cher et le moins cher.

- Visualisations avec matplotlib
1. Graphique en barres : quantité par produit.
2. Camembert (pie chart)

**👥 Auteurs**
- SAIDA AOURAS
- MARYEM ELBERGUI
- KHAOULA ESIOUDI

   
