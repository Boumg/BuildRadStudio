RXBuilder
Gestion des builds Rad Studio

Installation
pre-requis

Installer le module "rxbuilder"
 - sous le repetoire , BuildRadStudio
 - python setup.py install

Pour lancer directement un script python :

Lancer la console dos (cmd) en mode admin, et tapez les commandes suivantes :
 - assoc .py=Python.File
 - ftype Python.File=C:\Python36\python.exe "%1" %*
 Nota: changer le repertoire de pyhton.exe en fct de votre installation
 Nota: pyhtonw.exe n'a pas de console
 => il n'est plus nécessaire de faire 'python script.py' pour le lancer, mais simplement 'script' en ligne de commande

 Deinstallation
 pip rxbuilder uninstall


Lancer les tests sour la console
 - sous le repetoire , BuildRadStudio
 - tapez : make test
 - ou tapez : nose2

 Attention:
 msbuild en ligne de commande ne marche pas avec l'option "BCC_EnableBatchCompilation",
 il faut verifier directement dans le fichier xml du projet. (bug Ide, il active l'option, mais l'enleve partiellement