# -*- mode: python ; coding: utf-8 -*-

# Pyinstaller pyinstall.spec

block_cipher = None


a = Analysis(
    ['web_qt_gui.py',
    'C:\\Users\\16946\\Desktop\\web_UI\\Auto_wed_current\\Auto_UI\\GUI_Untitled\\untitled.py',
    'C:\\Users\\16946\\Desktop\\web_UI\\Auto_wed_current\\Auto_UI\\__init__.py',
    'C:\\Users\\16946\\Desktop\\web_UI\\Auto_wed_current\\Auto_UI\\GUI_Perform\\web_perform_func.py'], # 要动用的模块
    pathex=['C:\\Users\\16946\\Desktop\\web_UI\\Auto_wed_current\\Auto_UI\\'],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='web_UI', # 修改.exe文件名
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True, # 设置管理员模式
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='web_UI', # 模块名
)
