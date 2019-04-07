import pathlib
import sys
import unittest
from pathlib import Path
from rxbuilder.CmdRad import Cde,CmdRad
if __name__ == '__main__':
    path = pathlib.Path(__file__).resolve().parent.parent
    sys.path.insert(0, str(path))

from rxbuilder.VerifAvantCompilation import siProcessEnCours, attenteArretBds, checkVarEnv,rxbuild_minimum_requis

class TestcheckVarEnvn(unittest.TestCase):
    def test_PasDeCle(self):
        #Pas de cle
        self.assertRaises(Exception, checkVarEnv, "kkkkkkkk")
        #impossible de forcer
        self.assertRaises(Exception, checkVarEnv, "kkkkkkkk",force=True)
        #Pas de forcage => erreur
        self.assertRaises(Exception, checkVarEnv, "kkkkkkkk", "c:\\users", force=False)
        #creation de la variable
        self.assertTrue(checkVarEnv("BIDON", "%ProgramData%"))
        self.verif_valeur("BIDON", "%ProgramData%")

    def verif_valeur(self,cle, ref):
        v = Path(CmdRad()[cle])
        v_ref = Path(CmdRad().ResolutionEnv(ref))
        self.assertEqual(v, v_ref)

    def test_CleExiste(self):
        CmdRad()["BIDON2"]="c:\\users"
        self.assertTrue(checkVarEnv("BIDON2"))
        self.assertTrue(checkVarEnv("BIDON2",force= False))

        CmdRad()["BIDON3"]="ce nest pas un repertoire"
        self.assertRaises(Exception, checkVarEnv, "BIDON3")
        self.assertRaises(Exception, checkVarEnv, "BIDON3","C:\\users" ,force=False)
        #on force , implicite

        #self.assertTrue(checkVarEnv("BIDON3","%HOMEDRIVE%\\users" ))
        #self.verif_valeur("BIDON3", "%HOMEDRIVE%\\users")



    def test_existeVariableEnv(self):
        # version avec verification du resultat
        self.assertTrue(checkVarEnv("BIDON4", "%ProgramData%"))
        self.assertTrue(checkVarEnv("USERPROFILE"))
        #la valeur du path n'est pas un repertoire
        self.assertRaises(Exception, checkVarEnv, "PATH")


class TestVerifAvantCompilation(unittest.TestCase):

    def test_ProcessAbsent(self):
        self.assertFalse(siProcessEnCours('kkkkkkkk'))

    def test_ProcessEnCours(self):
        self.assertTrue(siProcessEnCours('svchost'))
    @unittest.skip("partie à la main, skipping")
    def test_AttenteBDE(self):
        attenteArretBds()

    def test_rxbuild_minimum_requis(self):
        rxbuild_minimum_requis("0.0.1")
        with self.assertRaises(Exception):
            rxbuild_minimum_requis("99.0.1")



if __name__ == '__main__':
    unittest.main()
