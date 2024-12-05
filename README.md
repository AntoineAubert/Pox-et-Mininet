# Pox-et-Mininet
Projet Privacité et Sécurité des Données avec Pox et Mininet

# Description du projet

Ce projet vise à appliquer les concepts étudiés en Privacité et Sécurité des Données à travers la simulation et la gestion d'un réseau virtualisé en utilisant les outils Mininet et POX. Il comporte deux principaux objectifs :

Créer un environnement virtualisé pour simuler un réseau sécurisé.
Développer et déployer des mécanismes de détection et de blocage de deux attaques spécifiques :
ARP Spoofing
Déni de Service (DoS)
Environnement virtualisé
L'environnement est conçu à l'aide de Docker Compose et comporte deux conteneurs principaux :

Docker Container Mininet :
Simule la topologie réseau.
Implémente deux sous-réseaux interconnectés par un routeur.
Un sous-réseau contient un serveur web cible et des générateurs de trafic, l'autre contient des clients HTTP et les attaquants.
Docker Container POX :
Contrôle les switchs OpenFlow pour gérer et analyser le trafic réseau.
Implémente des algorithmes de détection (Machine Learning possible : KNN, SVM, etc.) et applique des mesures de blocage en cas d'attaque.

# Automatisation
Tous les composants du projet doivent être entièrement automatisés à l'aide de scripts Python ou Shell.