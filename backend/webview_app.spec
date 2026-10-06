# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['webview_app.py'],
    datas=[('../frontend/src/build', 'frontend/src/build')],
    hiddenimports=['webview.platforms.winforms', 'webview.platforms.edgechromium'],
    excludes=['IPython'],
)
pyz = PYZ(a.pure)
exe = EXE(
    pyz, a.scripts, a.binaries, a.datas,
    name='APOD_WallPaper',
    console=False,
    icon='../frontend/src/public/favicon.ico',
)
