# Report on social engineering: Phising made by Yasmina

## Introduction
Partie Social engineering 
Le social engineering, ou ingénierie sociale, est une technique utilisée pour manipuler psychologiquement les individus afin d'obtenir des informations confidentielles ou de les amener à effectuer des actions spécifiques. Cette méthode exploite les faiblesses humaines, telles que la confiance, la curiosité, la peur ou l'ignorance, pour tromper les personnes ciblées. 
Concernant ce TP, on utilisera la technique phishing, il s'agit d'envoyer des e-mails ou des messages prétendant provenir d'une source fiable, telle qu'une institution financière ou une entreprise connue, afin de tromper les destinataires et de les inciter à divulguer des informations sensibles, telles que des mots de passe ou des numéros de carte de crédit. Pour réaliser ce TP, on a utilisé le framework Zphisher et l’outil intitulé Maigret.
1.	ZPhisher : ZPhisher est un framework de phishing automatisé basé sur le langage de programmation Python. Il offre une gamme d'outils et de modèles préconfigurés pour mener des attaques de phishing. Il permet aux utilisateurs de créer des pages de phishing pour imiter différents sites web populaires, tels que les réseaux sociaux, les services de messagerie, les sites bancaires, etc. ZPhisher facilite la génération de liens malveillants et la capture des informations confidentielles des victimes.
2.	Maigret : Maigret est un outil open source basé sur Python qui permet de collecter des informations sur une personne à partir de diverses sources en ligne. Il recherche les profils de médias sociaux, les adresses e-mail, les noms d'utilisateur et d'autres informations liées à une personne spécifique. Bien que Maigret puisse être utilisé pour recueillir des informations, il est important de souligner que l'utilisation abusive de ces données peut porter atteinte à la vie privée des individus.
On a installé les deux outils, et on a et exécute les deux commandes suivantes:
$ cd zphisher
$ bash zphisher.sh
On obtient les figures suivantes : on demande de sélectionner le site auquel appliquer le phishing, on choisit par exemple Instagram, on sélectionne le numéro correspondant au site voulu, on choisit le type du login, ceci afin de générer le lien menant à la page où la cible entrera les informations de son compte Instagram. Les figures suivantes illustrent les différentes étapes pour générer le lien à envoyer à la cible.


![yasmin1](<assets/yasmina1.png>)
![yasmin2](<assets/yasmina2.png>)
![yasmin3](<assets/yasmina3.png>)



 
 

 
Voici un exemple de mail envoyé à la cible, il contient le lien généré:

    Nous avons constaté une opération suspecte concernant votre compte Instagram, afin de renforcer la sécurité de votre compte, vous devez vous connectez au lien ci-dessous affin d’améliorer les paramètres de sécurité: https://is_get/SudDFzj


