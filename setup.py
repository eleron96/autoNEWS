
from setuptools import setup

APP_NAME = "AutoNews"
APP = ['autonews/main.py']
DATA_FILES = [('autonews', ['autonews/autonews.db'])]
OPTIONS = {
    'packages': ['openai', 'aiohttp', 'wheel', 'selenium',
                 'colorama', 'requests', 'pipreqs'],
    'iconfile': 'autonews.icns',
    'argv_emulation': True,
    'plist': {
        'CFBundleName': APP_NAME,
        'CFBundleDisplayName': APP_NAME,
        'CFBundleGetInfoString': "Summarize news articles",
    }
}

setup(
    app=APP,
    name=APP_NAME,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
