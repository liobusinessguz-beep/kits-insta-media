# kits-insta-media

Images des épingles Pinterest de la boutique **Les Kits Insta** (compte Pinterest @leskitsinsta).

- `pins/` : images publiées (JPEG 1000×1500). Leur adresse publique sert à créer les épingles :
  `https://raw.githubusercontent.com/liobusinessguz-beep/kits-insta-media/main/pins/NOM.jpg`
- `outils/pins.py` : générateur des visuels (thèmes `roi`, `bord`, `terra`, `sapin`), avec les polices dans `tempo_fonts.css` et les couvertures dans `cov2/`.

## Fabriquer une épingle

```bash
cd outils
python3 -c "import pins; print(pins.build('08-mon-epingle','roi','Cadeau 5 legendes','Surtitre','Titre ligne 1','titre en italique','Texte court.','Gratuit · PDF à télécharger'))"
python3 -c "from PIL import Image; Image.open('pins/08-mon-epingle.png').convert('RGB').save('../pins/08-mon-epingle.jpg', quality=85, optimize=True)"
```

Le rendu utilise `google-chrome --headless`. Couvertures possibles : `Cadeau 5 legendes`, `Cadeau janvier`, `Kit du Mois`, `Pack Insta Photographe`.

## Tableaux Pinterest

| Tableau | Identifiant |
|---|---|
| Instagram pour photographes | 259449697222497892 |
| Idées de posts Instagram pour indépendants | 259449697222497896 |
| Calendrier Instagram et contenu du mois | 259449697222497898 |

Publication par le connecteur Windsor.ai (`pinterest_organic`, compte `leskitsinsta`, action `create_pin`), toujours après l'accord de Gabrielle.
