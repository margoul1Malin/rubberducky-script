# RubberDucky avec MicroPython sur Raspberry Pi Pico

## Description

Ce projet permet d’utiliser un Raspberry Pi Pico comme un périphérique HID (clavier automatisé), similaire à une Rubber Ducky. L’objectif est de proposer un outil pédagogique pour comprendre le fonctionnement des Bad USB, automatiser certaines tâches et renforcer sa connaissance de la cybersécurité.

Ce dépôt contient tous les fichiers nécessaires au fonctionnement : scripts, structure de projet et exemples de payloads. Aucun code n’est présenté ici, tout est déjà disponible dans le répertoire.

## Avertissement

Ce projet est destiné à un usage éducatif uniquement. N’utilisez jamais un dispositif de ce type sur une machine sans autorisation explicite. L’auteur décline toute responsabilité en cas d’usage inapproprié.

## Prérequis

* Thonny (éditeur/IDE pour flasher et gérer les fichiers MicroPython)
* Raspberry Pi Pico (version 1 ou 2)
* Câble micro USB compatible avec le transfert de données
* MicroPython installé sur le Pico
* micropython-lib installée sur votre environnement si nécessaire

## Installation

1. Connecter le Raspberry Pi Pico à votre ordinateur.
2. Ouvrir Thonny et sélectionner le bon interpréteur MicroPython.
3. Copier les fichiers du dépôt sur la mémoire du Pico.
4. Redémarrer le Pico pour exécuter le script principal.

## Utilisation

Une fois le Pico branché, il se comportera comme un clavier USB et exécutera les actions prévues par le script contenu dans le dépôt. Pour modifier ou créer vos propres séquences, éditez simplement les fichiers correspondants via Thonny.

## Structure du dépôt

* `main.py` : script principal lancé automatiquement par le Pico
* `myLibs/` : répertoire contenant les différents scripts d’automatisation
* `lib/` : bibliothèques nécessaires au fonctionnement du projet
* `config.txt` : Environnement de Variables
## Support

En cas de problème ou de suggestion d’amélioration, ouvrez une issue sur le dépôt GitHub ou proposez une pull request.

## Licence

Ce projet est distribué sous licence MIT. Consultez le fichier LICENSE pour plus de détails.
