# -*- coding: utf-8 -*-
#todo Argparse

import getopt


from .TypeProjet import *


class OptionBuild(object):

    def __init__(self,options1=None, options2=[]):
        self._Racine = None
        self._Targets = []
        self._Plateformes = []
        self._Configs = []
        self._TypeProjets = []
        self._Properties = []
        self._projets = []
        self.ParserOptions(options1)
        self.ParserOptions(options2)
        self.def_options()



    def help(self):
        print("""
commande en ligne
    rxbuild [options] [groupe projets RX ] [projets RXC]
    
Options targets
    --clean -l suppression des fichiers de construction
    --build -b construction des projets
    --make -m make des projets
    --install  -i installe les packages de l'IDE
    --uninstall  -u desinstalle les packages de l'IDE
    --valide    -v Lance les programmes de tests comme google test
    Par defaut build et install

Options de selection des fichiers projets Rad studio
    Plateformes
        --win32  compilation limitee pour la plateforme win32
        --win64  compilation limitee pour la plateforme win64
        Pas d'indiquation, compilation de toutes les plateformes
    Configurations
        --debug  -d   compilation limitee à la configuration debug
        --release -r  compilation limitee à la configuration release
        Pas d'indiquation, compilation de toutes les configurations
    Type de projets/ packages
        --excecution -e compilation des librairies et des packages executions
        --conception -c compilation et installation des packages de conception pour ide
        --test       -t compilation  des programmes de tests
        --appli      -a ccompilation des executables 
        Pas d'indiquation, compilation de tous les projets
        


    Nota: Pas de build des packages de conception en x64 

""")

    def __lectureOption(self, listopt: list):
        try:
            opts,projs = getopt.getopt(listopt, "hlbiudrectamv",
                                                ["help", "clean", "build", "install", "uninstall", "debug", "release",
                                                 "excecution", "conception", "test", "appli", "make", "valide", "win32",
                                                 "win64", "nopch"])
            for proj in  projs:
                self._projets.append(proj)

            for opt, bid in opts:
                if opt in ("--help", "-h"):
                    self.help()
                    exit(0)
                # Plateforme
                elif opt in "--win32":
                    self._Plateformes.append(Plateforme.WIN32)
                elif opt in "--win64":
                    self._Plateformes.append(Plateforme.WIN64)
                # configuration
                elif opt in ("--debug", "-d"):
                    self._Configs.append(Config.DEBUG)
                elif opt in ("--release", "-r"):
                    self._Configs.append(Config.RELEASE)
                # type projet
                elif opt in ("--excecution", "-e"):
                    self._TypeProjets.append(TypeProjet.PackageExe)
                    self._TypeProjets.append(TypeProjet.Librairie)
                elif opt in ("--conception", "-c"):
                    self._TypeProjets.append(TypeProjet.PackageIde)
                elif opt in ("--test", "-t"):
                    self._TypeProjets.append(TypeProjet.Test)
                elif opt in ("--appli", "-a"):
                    self._TypeProjets.append(TypeProjet.Application)
                    self._TypeProjets.append(TypeProjet.Test)
                # build
                elif opt in ("--clean", "-l"):
                    self._Targets.append(Target.CLEAN)
                elif opt in ("--make", "-m"):
                    self._Targets.append(Target.MAKE)
                elif opt in ("--build", "-b"):
                    self._Targets.append(Target.BUILD)
                elif opt in ("--install", "-i"):
                    self._Targets.append(Target.INSTALL)
                elif opt in ("--uninstall", "-u"):
                    self._Targets.append(Target.UNINSTALL)
                elif opt in ("--valide", "-v"):
                    self._Targets.append(Target.TEST)
                # properties
                elif opt in "--nopch":
                    self._Properties.append("nopch")



        except getopt.GetoptError as err:
            # print help information and exit:
            print(err)  # will print something like "option -a not recognized"
            self.help()
            raise Exception("Option de compilation invalide")

    def def_options(self):
        if len(self._Plateformes) == 0:
            self._Plateformes = ToutesPlateformes
        if len(self._Configs) == 0:
            self._Configs = ToutesConfigs
        if len(self._TypeProjets) == 0:
            self._TypeProjets = TousTypeProjets
        if len(self._Targets) == 0:
            self._Targets = TousTargets
        if Target.INSTALL in self._Targets or Target.UNINSTALL in self._Targets:
            if TypeProjet.PackageIde not in self._TypeProjets:
                self._TypeProjets.append(TypeProjet.PackageIde)
        # if "nopch" not in self._Properties :
        #    self._Properties.append("nopch")

    def ParserOptions(self, options):
        if options:
            options_li=options
            if type(options) == str :
                options_li = options.split()

            if type(options_li) == list and  len(options_li)>0:
                 self.__lectureOption(options_li)


    @property
    def TypeProjets(self):
        return self._TypeProjets

    @property
    def Plateformes(self):
        return tuple(self._Plateformes)

    @property
    def Configs(self):
        return tuple(self._Configs)

    @property
    def Targets(self):
        return tuple(self._Targets)

    @property
    def Properties(self):
        return tuple(self._Properties)

    @property
    def Projets(self):
        return tuple(self._projets)

    @property
    def PreProjets(self):
        return lambda projet: projet.lower() in option.TypeProjets

    @property
    def PreTargets(self):
        return lambda target: target.lower() in option.Targets

    @property
    def PreProperties(self):
        return lambda property: property.lower() in option.Properties

    @property
    def Racine(self):
        return self._Racine

    @Racine.setter
    def Racine(self, value):
        self._Racine = Path(value)
        if self._Racine:
            if (not (self._Racine.is_dir())):
                raise Exception(f" Le repertoire racine {self._Racine} n'est pas defini.")

    def AddProjetsListe(self, groupe):
        for rep in groupe:
            self._projets.append(rep)

    def AddProjets(self, groupe):
        for rep, nom in groupe:
            nom = Path(rep) / nom
            self._projets.append(str(nom))
