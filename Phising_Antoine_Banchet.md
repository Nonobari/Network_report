# Report on social engineering: Phising made by Antoine Banchet

## Introduction

Cette section est individuelle et a pour but de présenter le phishing et ses différentes formes.

La cible durant cette section est Noé Backert, dont j'ai obtenu son autorisation préalable.
## I. Phishing

Le phishing est une forme de cyberattaque qui peut être utilisée pour voler des données sensibles, notamment des informations de connexion et des détails de carte de crédit. Il se produit lorsqu'un attaquant, se faisant passer pour une entité de confiance, vous incite à cliquer sur un lien ou à ouvrir une pièce jointe dans un courrier électronique ou un message. Cela peut également se produire via un appel téléphonique ou un message texte. Les attaques de phishing peuvent être utilisées pour voler des informations personnelles, telles que des noms d'utilisateur, des mots de passe et des détails de carte de crédit, ou pour distribuer des logiciels malveillants.

## II. Méthodologie

Généralement, le phishing se déroule en plusieurs étapes :

1. L'attaquant doit d'abord choisir sa cible et obtenir des informations sur elle. Cela peut se faire, par exemple, en utilisant les réseaux sociaux ou en utilisant des techniques de social engineering pour obtenir des informations sur la cible (OSINT).

2. L'attaquant doit ensuite choisir la forme de phishing qu'il va utiliser. Il peut s'agir d'un e-mail, d'un message texte, d'un appel téléphonique, d'un message sur les réseaux sociaux, etc.

3. L'attaquant doit ensuite créer le message de phishing. Celui-ci doit être crédible et inciter la cible à effectuer une action, comme cliquer sur un lien ou ouvrir une pièce jointe.

4. L'attaquant doit ensuite envoyer le message de phishing à la cible. Une fois que la cible a effectué l'action demandée, l'attaquant peut alors obtenir les informations qu'il souhaite. La plupart du temps, le lien de phishing renvoie vers une fausse page de connexion qui enregistre les identifiants de la cible, installe un logiciel malveillant sur la machine ou enregistre les informations de carte bancaire.


### III. Cas pratique

Le cas pratique le plus courant consiste à créer un mail de phishing. Pour cela, on peut utiliser des outils tels que [GoPhish](https://getgophish.com/), qui permettent de créer des mails de phishing et de suivre les personnes qui ont cliqué sur le lien ou ouvert la pièce jointe. Cet outil est principalement utilisé pour mener des campagnes de phishing. On peut également utiliser Social Engineering Toolkit (SET) pour cibler une personne spécifique. Cet outil permet de créer directement un mail de phishing et de l'envoyer à la cible. Il est également possible de cloner directement un site.

Cependant, j'ai décidé d'utiliser une technique appelée "Rogue Wi-Fi Access Point Attack" en utilisant le framework "Wifipumpkin3". Ce framework permet de créer un point d'accès Wi-Fi et de cloner un site. Ainsi, lorsque la cible se connecte au point d'accès, elle est redirigée vers le site cloné. On peut alors récupérer les identifiants de la cible. Vous pouvez trouver le framework "Wifipumpkin3" sur GitHub à l'adresse suivante : [https://github.com/P0cL4bs/wifipumpkin3](https://github.com/P0cL4bs/wifipumpkin3).

### IV. Explication de la méthode utilisée

Sur le réseau de notre résidence étudiante, après s'être connecté au réseau Wi-Fi, nous devons nous identifier avec nos identifiants étudiants pour pouvoir accéder à Internet. Ainsi, j'ai décidé de créer un point d'accès Wi-Fi avec le même nom que le réseau Wi-Fi de la résidence étudiante et de cloner la page de connexion. Ainsi, lorsque la cible se connecte au point d'accès, elle est redirigée vers la page de connexion clonée.

Pour cela, j'ai utilisé le framework "Wifipumpkin3". Ce framework permet de créer un point d'accès Wi-Fi et de cloner un site.

Voici la page de connexion du réseau Wi-Fi de la résidence étudiante :
<img src = "assets/fw_connexion.png" width = 500>

1. Le framework wifipumpkit3 ressemble à cela:
<img src = "assets/Wifipumpkit3.png" width = 500>

1. Il faut dans un premier temps configurer le point d'accès wifi (ap):
<img src = "assets/wp3_ap.png" width = 500>
On voit que le ap est configuré avec le nom du réseau Wi-Fi de la résidence étudiante, et que le mode de sécurité est WPA2. J'aurais aussi pu mettre le même mot de passe mais je dois hacker uniquement noé et pas toute la résidence 😅.

1. Ensuite, il faut configurer le module de clonage de site (web-cloner). J'ai pour cela utilisé goclone : https://github.com/imthaghost/goclone
2. On active ensuite le portail de connexion sur wifipumpkin3, activant la page de connexion de la résidence étudiante. Ici emse_v2.
<img src = "assets/wp3_proxy.png" width = 500>J'ai pour cela suivis le tutoriel suivant: https://wifipumpkin3.github.io/docs/getting-started#development

1. Enfin, on lance le point d'accès Wi-Fi, et on attend que la cible se connecte.
<img src = "assets/wp3_run.png" width = 500>
On voit l'adresse MAC de la cible connexté au point d'accès Wi-Fi, ici Noé. Un serveur DHCP et DNS est aussi lancé, permettant de rediriger la cible vers la page de connexion clonée. On voit que c'est l'ordinateur de Noé DESKTOP-1BGVP3K.
1. Lorsque la cible se connecte, elle est redirigée vers la page de connexion clonée. On peut alors récupérer les identifiants de la cible. Ici noe.backert et le mot de passe: test.
<img src = "assets/wp3_done.png" width = 500>

Remarque :
On pourrait déconnecter de manière répétée les utilisateurs du réseau Wi-Fi en envoyant en boucle des paquets de déauthentification, ce qui rendrait la connexion au vrai Wi-Fi impossible. Cela forcerait ainsi les utilisateurs à se connecter au faux Wi-Fi. Wifipumpkin3 permet de réaliser cette action.
<img src = "assets/wp3_Deauth.png" width = 500>
On peut utiliser aireplay-ng pour le faire aussi:
https://www.inkyvoxel.com/wi-fi-deauthentication-attacks-using-aireplay-ng/

### V. Du point de vue de la victime

1. Noé se connecte au réseau Wi-Fi de la résidence étudiante. 
2. Il voit que le réseau est bien celui de la résidence étudiante, et qu'il est sécurisé. Il se connecte donc au réseau Wi-Fi.
<img src = "assets/fake_wifi.png" width = 400 height = 600>
3. Il est redirigé vers la page de connexion de la résidence étudiante. Il rentre alors ses identifiants.
<img src = "assets/fake_portal.png" width = 500>
4. il navigue ensuite sur Internet normalement sans rien remarquer. J'ai en plus accès à tout ce qu'il consulte et qui est visible en clair.
   
### VI. Conclusion
Pour conclure, l'attaque n'est pas encore parfaite car on voit que l'Url de la fausse page de connexion affiche 10.0.0.1 qui est l'adresse du routeur et non pas l'adresse de la page de connexion de la résidence étudiante. Il faudrait donc trouver un moyen de changer l'Url de la page de connexion. En configurant le DNS du point d'accès on pourrait peut être y arriver.

Cette attaque est très simple à mettre en place et peut être très efficace. Il est donc important de faire attention aux réseaux Wi-Fi auxquels on se connecte (ex: réseaux publics) et de vérifier que l'adresse de la page de connexion est bien celle du site officiel.
