# -*- mode: python ; coding: utf-8 -*-
# PyInstaller spec pentru release production (windowed, icon, UPX)
from PyInstaller.utils.hooks import collect_submodules

a = Analysis(
    ['CalculatorPierderi.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=collect_submodules('tkinter') + collect_submodules('requests'),
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['tkinter.test', 'tkinter.demos'],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='CalculatorPierderi',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='CalculatorPierderi.ico',
)
