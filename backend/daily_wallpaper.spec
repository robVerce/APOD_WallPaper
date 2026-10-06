# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['daily_wallpaper.py'],
    excludes=['IPython', 'webview', 'tkinter'],
)
pyz = PYZ(a.pure)
exe = EXE(
    pyz, a.scripts, a.binaries, a.datas,
    name='daily_wallpaper',
    console=True,
)
