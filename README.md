RXBuilder
Gestion des builds Rad Studio

Installation
Installer le module "rxbuilder"
 - sous le repetoire , BuildRadStudio
 - python setup.py install

Pour lancer directement un script python :

Lancer la console dos (cmd) en mode admin, et tapez les commandes suivantes :
 - assoc .py=Python.File
 - ftype Python.File=C:\Python36\python.exe "%1" %*

 => il n'est plus nécessaire de faire 'python script.py' pour le lancer, mais simplement 'script' en ligne de commande

 Deinstallation
 pip rxbuilder uninstall


Lancer les tests sour la console
 - sous le repetoire , BuildRadStudio
 - tapez : make test
 - ou tapez : nose2