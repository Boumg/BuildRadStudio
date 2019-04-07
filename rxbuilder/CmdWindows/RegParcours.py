import winreg


class Registre(object):

    def __init__(self, path_reg, hklm=winreg.HKEY_CURRENT_USER, access=winreg.KEY_ALL_ACCESS):
        self._hklm = None
        self._reg = hklm
        self._keyR = None
        self._path = path_reg
        self.value = None
        self._access = access


    @property
    def path(self):
        return self._path

    @path.setter
    def set_path(self, value):
        if self._path != value:
            self._keyR = None
            self._path = value

    @property
    def hklm(self):
        if self._hklm is None:
            self._hklm = winreg.ConnectRegistry(None, self._reg)
        return self._hklm

    @property
    def key_handle(self):
        if self._keyR is None:
            self._keyR = winreg.OpenKey(self.hklm, self.path, 0, self._access)
        return self._keyR

    NO_DEFAULT = type(str('NO_DEFAULT'), (object,), {})()

    def get_valeur(self, name, default=NO_DEFAULT):
        try:
            value = winreg.QueryValueEx(self.key_handle, name)[0]
        except WindowsError:
            if default is self.NO_DEFAULT:
                raise ValueError("No such registry key", name)
            value = default
        return value

    def set_valeur(self, name, val, default=NO_DEFAULT):
        try:
            winreg.SetValueEx(self.key_handle, name, 0, winreg.REG_SZ, val)
        except WindowsError:
            if default is self.NO_DEFAULT:
                raise ValueError("Writing registry key failed ! - ", name)

    def get_ruche(self, value):
        return winreg.OpenKey(self.key_handle, value, 0, winreg.KEY_READ)

    def get_registre(self, value):
        reg = self._path
        if reg[-1] != "\\":
            reg += "\\"
        return Registre(reg + value, self._reg)

    def si_existe_ruche(self, value=""):
        try:
            self.get_ruche(value)
        except WindowsError:
            return False
        return True

    def si_existe_valeur(self, name):
        try:
            self.value = winreg.QueryValueEx(self.key_handle, name)[0]
        except WindowsError:
            return False
        return True

    def effacer_valeur(self, name):
        try:
            winreg.DeleteValue(self.key_handle, name)
        except WindowsError:
            raise ValueError("Deleting registry key failed ! - ", name)

    def effacer_valeur_si_existe(self, name):
        if self.si_existe_valeur(name):
            self.effacer_valeur(name)

    def liste_sub_key(self, nb_subk):
        liste_subk = []
        indexSk = 0
        while indexSk < nb_subk:
            liste_subk.append(winreg.EnumKey(self.key_handle, indexSk))
            indexSk += 1
        return liste_subk

    def effacer_cle(self, nomCle):
        if self.si_existe_ruche(nomCle):
            subKey = self.get_registre(nomCle)
            nb_subk, nb_v, t = winreg.QueryInfoKey(subKey.key_handle)
            if (nb_subk > 0):
                for subkname in subKey.liste_sub_key(nb_subk):
                    subKey.effacer_cle(subkname)
            winreg.DeleteKey(self.key_handle, nomCle)

    def lister_valeurs(self, value_name):
        valeurs = self.get_valeur(value_name)
        liste = valeurs.split(';')
        return liste

    def ajouter_chemin(self, value_name, path):
        old_value = self.get_valeur(value_name)
        new_value = old_value + ";" + path
        self.set_valeur(value_name, new_value)
