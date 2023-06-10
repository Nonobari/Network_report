Rapport
\
Introduction à la cybersécurité
==============

Auteurs: BACKERT Noé, BANCHET Antoine, BARA Yassmina

# Table des matières
1. [Introduction](#introduction)
2. [Footprint](#footprint)
3. [Scanning Networks](#scanning-networks)


# Introduction

Ce rapport est écrit dans un but d'introduction à la sécurité dans le cadre des cours d'ingénieur à l'école des Mines de Saint-Etienne.
On s'intéressera alors au Phishing, au scan de réseaux et des ports ouverts sur différentes machines, ainsi qu'aux scans de leurs vulnérabilitées.
On s'occupera dans un second temps de proposer des solutions à ces vulnérabilitées. 
Pour les parties 2,3 et 4, nous allons utiliser le réseau privé suivant fabriqué à l'aide d'un réseau privé fait par l'ordinateur fixe de Noé:
<p align = "center"> 
<img src = "assets/network.png" width = 300>
</p>

# Footprint
## 1. Phishing : Information about the target, how they were obtained etc.
## 2. Phishing by e-mail: Example of an email to be sent to the target
## 3. Countermeasures against phishing


# Scanning networks
## 1. Network scan

On commence par chercher notre addresse IP à l'aide de la commande : 

    ifconfig

![pictureNmapPing](assets/ifconfig.png)

Pour effectuer un scan basique d'un réseau, on peut utiliser la commande suivante : 

    fping -s -g 192.168.137.0 192.168.137.254

Celle-ci nous permet d'envoyer une requête et d'attendre un retour sur l'ensemble des adresses IP du sous-réseau indiqué.

![pictureNmapPing](assets/fping1.png)
![pictureNmapPing](assets/fping2.png)

Ainsi, nous savons que 3 appareils sont connectés au réseau.

On peut donc augmenter la taille des paquets jusqu'à obtenir une erreur de timeout en utilisant la commande suivante :

    ping -s <packet_size> 192.168.137.68

![pictureNmapPing](assets/ping10.png)
![pictureNmapPing](assets/ping1000000.png)

En tâtonnant, on observe qu'il y a une erreur en envoyant un paquet au dessus de 65507 bytes. Le buffer ne doit pas accepter autant. 


Autrement, on peut vérifier cela à l'aide du script python suivant :

    import os
    import sys

    if len(sys.argv)<=1:
        print("Error : Arg missing, ip required")
    else: 
        ip = sys.argv[1]
        for size in range(0,80000,8):
            os.system(f"ping -s {size} -c 1 {ip}")

Celui-ci teste un ping vers l'adresse ip mis en argument lors du lancement du script en augmantant à chaque fois d'un octet, jusqu'à qu'une erreur intervienne.

On obtient alors bien une erreur vers la taille trouvée en tâtonnant :

>![pictureNmapPing](assets/pingError.png)

Autrement, on peut tout simplement effectuer un nmap sur l'ensemble du sous-réseau :

![pictureNmapPing](assets/nmapPing.png)


La commande suivante nous permet d'envoyer une requête de ping à toutes les addresses IP du réseau (en utilisant le masque de sous-réseau 255.255.255.0)

    nmap 192.168.137.0/24 -sP

Cela nous permet ainsi de voir quels addresses IP sont utilisées, cependant, on ne peut pas deviner l'identité de cette machine en utilisant seulement cette commande.

---
## 2. Port scan

![pictureNmap](assets/portScan.png)

Cette commande nous permet de trouver tous les ports ouverts et également de trouver des informations supplémentaires sur la machine, comme son addresse MAC.

    sudo nmap 192.168.137.68

Cette commande requiert l'accès root.


## 3. Vulnerabily scan

    traceroute raphaelviera.fr

traceroute - affiche le chemin d'un paquet vers le domaine entré

![traceroute](assets/traceroute.png)
## 4. Patching the Vulnerabily