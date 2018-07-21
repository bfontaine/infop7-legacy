---
layout: home
---

Ce site permet de télécharger les fichiers déposés sur infop7.org entre 2014 et
début 2018. Ils concernent les cours de Licence et de Master informatique à
Paris Diderot (Paris 7) et comptent aussi bien des TP que des TD, des
corrections, des notes de cours, des examens et partiels corrigés ou non.

Licence : [L1](/cours-licence-1), [L2](/cours-licence-2), [L3](/cours-licence-3)<br>
Master : [M1](/cours-master-1), [M2](/cours-master-2)

L’arborescence des zip est la suivante :
```
année/cours/année_universitaire/type/contenu/fichier
```

Par exemple, pour l’examen de session 1 de CI2 (concepts informatiques) en
2013-2014 :
```
l1/CI2/2013/exam/Examen_session_1/ci2-2014-examen-s1.pdf
```

Le type correspond à celui associé au contenu dans la base de donnée
d’origine&nbsp;: `cours`,  `tp`, `td`, `exam` (examen), `partiel`,
`examen_corr` (examen corrigé), etc.

La plupart des contenus ont un seul fichier, mais certains en ont plusieurs,
par exemple pour les TP avec des fichiers additionnels. Quand le contenu avait
du texte associé, il est dans un fichier `description.txt`.
