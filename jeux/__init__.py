# -*- coding: utf-8 -*-
from pathlib import Path
RepertoireJeux = Path(__file__).parent
RepertoireXe = RepertoireJeux / "xe"
GroupProjet = RepertoireXe / "TstBuild.groupproj"
LibProjet = RepertoireXe / "TstLib/TstLib.cbproj"
PackageExecProjet = RepertoireXe / " TstPackageExec/TstPackageExec.cbproj"
PackageIdeProjet = RepertoireXe / "TstPackageIde/TstPackageIde.cbproj"
ExecProjet = RepertoireXe / "TstExe/TsstExe.cbproj"