import re
from pathlib import Path
from subprocess import *

from .WinConsole import get_code_page


def get_cmd(path: Path):
    cmd = Path(path)
    return Popen(["cmd.exe"], cwd=str(cmd), stderr=PIPE, stdin=PIPE, stdout=PIPE, encoding=get_code_page(),
                 errors="surrogateescape")


def get_prompt():
    drive = Path().resolve().drive
    return re.compile(fr"^{drive}\\.*>", re.MULTILINE | re.IGNORECASE)


class InteractiveCmd:

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.process:
            self.process.__exit__(exc_type, exc_value, traceback)

    def __init__(self, path: Path = ""):
        self._cmd = path
        self.process = get_cmd(self._cmd)
        self.prompt = get_prompt()
        self.output = ""
        self.attente_prompt()

    def expect_re(self, reg: re.Pattern):
        while not reg.search(self.output):
            c = self.process.stdout.read(1)
            if c == "":
                break
            self.output += c
            print(c, end="")

        # Now we're at a prompt; clear the output buffer and return its contents
        tmp = self.output
        self.output = ""

        return tmp

    def expect(self, att: str):
        return self.expect_re(re.compile(att, re.MULTILINE | re.IGNORECASE))

    def attente_prompt(self):
        return self.expect_re(self.prompt)

    def send_line(self, line):
        self.process.stdin.write(line + "\n")
        self.process.stdin.flush()

    def cde(self, command):
        self.send_line(command)
        return self.attente_prompt()

    def exit(self):
        self.cde("exit")

    def attente_fin(self):
        a, b = self.process.communicate(timeout=120)  # timeout 2mn
        print(a, b)

    def lance(self, prg, attente="", attente_fin=False):
        self.send_line(prg)
        if attente:
            self.expect(attente)
        if attente_fin:
            self.attente_fin()

    def is_alive(self):
        return self.process.poll() is None

    def sortie(self):
        self.send_line('exit')
        self.attente_fin()

    def set_path(self, path: Path):
        self._cmd = Path(path)
        self.send_line(path.drive)
        self.cde('cd ' + str(path))

    def kill(self):
        if self.is_alive():
            self.process.kill()
            self.attente_fin()

