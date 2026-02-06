# GemVDA - Google Gemini AI pour NVDA

## Apercu

GemVDA integre les capacites de Google Gemini AI directement dans NVDA, offrant aux utilisateurs aveugles et malvoyants une assistance IA puissante. L'extension prend en charge plusieurs modeles Gemini, notamment Gemini 3, Gemini 2.5 Pro et les variantes Flash pour le chat, la description d'images, l'analyse video et plus encore.

## Fonctionnalites

* **Chat IA**: Discuter avec Gemini AI directement depuis NVDA
* **Description d'ecran**: Capturer et decrire l'ecran entier
* **Description d'objet**: Decrire l'objet du navigateur actuel
* **Analyse video**: Enregistrer une video de l'ecran et la faire analyser par Gemini
* **Joindre des images**: Joindre des fichiers images pour description par l'IA
* **Historique de conversation**: Maintenir le contexte sur plusieurs messages
* **Plusieurs modeles**: Choisir parmi differents modeles Gemini selon vos besoins
* **Resumer la selection**: Selectionnez du texte et Gemini resumera les points cles
* **Parametres personnalisables**: Configurer la temperature, les tokens, le streaming et plus

## Exigences

* NVDA 2023.1 ou ulterieur
* Cle API Google Gemini (niveau gratuit disponible)
* Connexion Internet

## Configuration

### Obtenir une cle API

1. Visitez [Google AI Studio](https://aistudio.google.com/apikey)
2. Connectez-vous avec votre compte Google
3. Creez une nouvelle cle API
4. Copiez la cle pour l'utiliser dans l'extension

### Configurer la cle API

1. Appuyez sur NVDA+N pour ouvrir le menu NVDA
2. Allez dans Preferences > Parametres
3. Selectionnez la categorie "Gemini AI"
4. Cliquez sur "Configurer la cle API..."
5. Collez votre cle API et appuyez sur OK

## Raccourcis clavier

| Raccourci | Action |
|-----------|--------|
| NVDA+G | Ouvrir le dialogue Gemini AI |
| NVDA+Maj+E | Decrire l'ecran entier |
| NVDA+Maj+O | Decrire l'objet du navigateur |
| NVDA+V | Demarrer/arreter l'enregistrement video pour analyse |
| NVDA+Maj+U | Resumer le texte selectionne |

## Utiliser le dialogue Gemini

Lorsque vous ouvrez le dialogue Gemini avec NVDA+G:

1. **Modele**: Selectionnez le modele Gemini a utiliser
2. **Invite systeme**: Instructions optionnelles sur la facon dont Gemini doit repondre
3. **Historique**: Voir l'historique de conversation
4. **Message**: Tapez votre message ou question
5. **Envoyer**: Envoyer votre message a Gemini
6. **Joindre image**: Ajouter un fichier image pour analyse par Gemini
7. **Effacer**: Effacer l'historique de conversation
8. **Copier reponse**: Copier la derniere reponse dans le presse-papiers

### Conseils pour le dialogue

* Appuyez sur ctrl+entree dans le champ message pour envoyer rapidement
* Utilisez Tab pour naviguer entre les controles
* L'historique se met a jour automatiquement pendant que vous chattez
* Les images jointes sont envoyees avec votre prochain message

## Parametres

Accedez aux parametres via le menu NVDA > Preferences > Parametres > Gemini AI:

* **Modele par defaut**: Choisissez votre modele Gemini prefere
* **Temperature (0-200)**: Controle la creativite des reponses (0=concentre, 200=creatif)
* **Tokens de sortie max**: Longueur maximale des reponses
* **Reponses en streaming**: Afficher les reponses au fur et a mesure
* **Mode conversation**: Inclure l'historique du chat pour le contexte
* **Retenir l'invite systeme**: Sauvegarder votre invite personnalisee
* **Bloquer la touche Echap**: Empecher la fermeture accidentelle du dialogue
* **Filtrer le markdown**: Supprimer le formatage markdown des reponses

### Retour sonore

* **Jouer un son a l'envoi de la requete**: Confirmation audio lorsque le message est envoye
* **Jouer un son pendant l'attente**: Son de progression pendant le traitement IA
* **Jouer un son a la reception de la reponse**: Notification a l'arrivee de la reponse

## Modeles disponibles

* **Gemini 3 Pro (Preview)**: Modele le plus performant avec capacites de reflexion
* **Gemini 3 Flash (Preview)**: Modele rapide avec capacites de reflexion
* **Gemini 2.5 Pro**: Modele puissant pret pour la production
* **Gemini 2.5 Flash**: Rapide et efficace pour la plupart des taches
* **Gemini 2.5 Flash-Lite**: Leger et reponses les plus rapides
* **Gemini 2.5 Flash Image**: Optimise pour les taches liees aux images

## Fonctionnalites image et video

### Description d'ecran (NVDA+Maj+E)

Capture votre ecran entier et l'envoie a Gemini pour une description detaillee. Utile pour:

* Comprendre des interfaces inconnues
* Obtenir un apercu du contenu visuel
* Identifier des elements que NVDA ne peut pas decrire

### Description d'objet (NVDA+Maj+O)

Capture uniquement l'objet du navigateur actuel. Utile pour:

* Decrire des elements d'interface specifiques
* Comprendre des images ou icones
* Obtenir des details sur les controles focuses

### Analyse video (NVDA+V)

1. Appuyez sur NVDA+V pour demarrer l'enregistrement
2. Effectuez les actions que vous voulez analyser
3. Appuyez a nouveau sur NVDA+V pour arreter
4. Attendez que Gemini analyse la video

Utile pour:

* Comprendre les flux de travail visuels
* Obtenir des descriptions etape par etape
* Analyser du contenu dynamique

### Resumer la selection (NVDA+Maj+U)

Selectionnez du texte dans n'importe quelle application et Gemini resumera les points cles. Fonctionne en mode navigation (navigateurs web, lecteurs PDF) et dans les champs de texte normaux. L'invite de resume peut etre personnalisee dans les parametres de l'extension.

## Depannage

### "Bibliotheque Google GenAI non installee"

Executez l'installateur de dependances:
1. Naviguez vers %APPDATA%\nvda\addons\GemVDA
2. Executez install_deps.bat ou install_deps.py
3. Redemarrez NVDA

### "Aucune cle API configuree"

Configurez votre cle API dans Parametres > Gemini AI > Configurer la cle API

### Les reponses sont trop courtes ou tronquees

Augmentez le parametre "Tokens de sortie max"

### Les reponses sont trop aleatoires

Reduisez le parametre de Temperature (essayez 50-100)

## Note de confidentialite

* Vos messages et images sont envoyes a l'API Gemini de Google
* Les cles API sont stockees localement dans votre configuration NVDA
* Aucune donnee n'est partagee avec le developpeur de l'extension
* Consultez la politique de confidentialite IA de Google pour plus de details

## Support

* Signaler des problemes: [GitHub Issues](https://github.com/ogomez92/GemVDA/issues)
* Code source: [GitHub Repository](https://github.com/ogomez92/GemVDA)

## Licence

Cette extension est publiee sous la Licence Publique Generale GNU v2.

## Auteur

Oriol Gomez Sentis
