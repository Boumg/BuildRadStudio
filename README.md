RXBuilder
Gestion des builds Rad Studio

Installation
pre-requis
    installer python3
    installer les packages (nose2 et pythonnet)
      - sous le repetoire , BuildRadStudio
      - pip install -r requirements.txt

    vérification du framework dot net
     Il est possible de changer les framework dotnet  du build;
     Sachant que le composant "rxbuild" utilise le batch %BDS%\bin\rsvars.bat pour determiner l'environement de build :
        => modifier les varibles du fichier batch : "FrameworkDir" et "FrameworkVersion" pour les faire pointer sur le bon repertoire.


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

 Utilisation

 tapez sous une console :
  rxbuild --help
  
  rxbuild