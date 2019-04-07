from winreg import HKEY_CURRENT_USER, KEY_READ, HKEY_LOCAL_MACHINE

from .RegParcours import Registre

_REG_CODE_PAGE_SYSTEM = 'SYSTEM\\CurrentControlSet\\Control\\Nls\\CodePage\\'
_REG_CODE_PAGE_CONSOLE = 'Console\\%SystemRoot%_system32_cmd.exe\\'


def get_def_cp_cmd():
    """

    """
    console = Registre(_REG_CODE_PAGE_CONSOLE, HKEY_CURRENT_USER, access=KEY_READ)
    if console.si_existe_valeur("CodePage"):
        return console.get_valeur("CodePage")
    system = Registre(_REG_CODE_PAGE_SYSTEM, HKEY_LOCAL_MACHINE, access=KEY_READ)
    if system.si_existe_valeur("OEMCP"):
        return system.get_valeur("OEMCP")
    """Multilingual (Latin I)"""
    return 850


def get_code_page():
    """lecture code page console windows"""
    code_page = get_def_cp_cmd()
    return f"cp{code_page}"
