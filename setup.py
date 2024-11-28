import setuptools

setuptools.setup(     
     name="pycaruna",     
     version="0.1",
     python_requires=">=3.11",
     py_modules=["pycaruna"],
     install_requires=[
        "beautifulsoup4>=4.12.3",
        "bs4>=0.0.2",
        "certifi>=2024.8.30",
        "charset-normalizer>=3.4.0",
        "idna>=3.10",
        "requests>=2.32.3",
        "setuptools>=69.0.2",
        "soupsieve>=2.6",
        "urllib3>=2.2.3",
        "wheel>=0.42.0"
     ]
)