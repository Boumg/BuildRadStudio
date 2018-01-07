# -*- coding: utf-8 -*-

import sys
import getopt
    

class OptionBuild(object):
    def help(self):
        print("""
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
        
    Proprietes
        --nopch  compilation sans les PCH

    Nota: Pas de build des packages de conception en x64 

""")

    def __lectureOption(self,listopt):
            if self._silecture :
                return
            self._silecture = True 
      
            
            self._Targets = []
            self._Plateformes = []
            self._Configs = []
            self._TypeProjets = []
            self._Properties = []
 
            try:
                opts, args = getopt.getopt(listopt, "hlbiudrectamv", ["help","clean", "build", "install","uninstall", "debug", "release","excecution","conception", "test", "appli","make","valide","win32","win64","nopch"])
                for opt, bid in opts:
                     if  opt in ("--help" ,"-h"):
                        self.help()
                        exit(0)   
                     elif opt in "--win32" :
                        self._Plateformes.append("win32")
                     elif  opt in "--win64" :   
                        self._Plateformes.append("win64")
                     elif  opt in ("--debug" ,"-d"):
                        self._Configs.append("debug")
                     elif  opt in ("--release" ,"-r"):
                        self._Configs.append("release") 
                     elif  opt in ("--excecution" ,"-e"):
                        self._TypeProjets("excecution") 
                     elif  opt in ("--conception" ,"-c"):
                        self._TypeProjets("conception") 
                     elif  opt in ("--test" ,"-t"):
                        self._TypeProjets("test") 
                     elif  opt in ("--appli" ,"-a"):
                        self._TypeProjets("appli") 
                     elif  opt in ("--clean" ,"-l"):
                        self._Targets.append("clean")
                     elif  opt in ("--make" ,"-m"):
                       self._Targets.append("make")
                     elif  opt in ("--build" ,"-b"):
                       self._Targets.append("build")
                     elif  opt in ("--install" ,"-i"):
                       self._Targets.append("install")
                     elif  opt in ("--uninstall" ,"-u"):
                       self._Targets.append("uninstall")
                     elif  opt in ("--valide" ,"-v"):
                       self._Targets.append("valide")
                     elif opt in "--nopch" :
                        self._Properties.append("nopch")

                if len(self._Plateformes) == 0 :
                    self._Plateformes = ["win32","win64"]  
                if len(self._Configs) == 0 :
                    self._Configs = ["release","debug"]   
                if len(self._TypeProjets) == 0 :
                    self._TypeProjets = ["excecution","conception","test","appli"]   
                if len(self._Targets) == 0 :
                    self._Targets = ["clean","build","install"]
                if "install" in self._Targets or "uninstall" in self._Targets :
                    if "conception" not in self._TypeProjets :
                        self._TypeProjets.append("conception")
                #if "nopch" not in self._Properties :
                #    self._Properties.append("nopch")
                    
            except getopt.GetoptError as err:
                # print help information and exit:
                print(err) # will print something like "option -a not recognized"
                help()
                raise Exception("Option de compilation invalide")

    def LectureOptionsLigneCde(self):
        __lectureOption(sys.argv[1:])

    def LectureOptionsChaine(self, options :str):
        args = options.split()
        __lectureOption(args)


    def __init__(self):
        self._silecture = False
        self.LectureOptionsLigneCde()
   
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
        return  tuple(self._Targets)
    @property
    def Properties(self):
        return  tuple(self._Properties)


