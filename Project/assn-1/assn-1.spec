# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_submodules

block_cipher = None

a = Analysis(
    ['assn-1.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('.env', '.'),
    ],
    hiddenimports=collect_submodules('dotenv'),
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='Hedgehog_hangman',
    debug=False,
    strip=False,
    upx=True,
    console=True,
)