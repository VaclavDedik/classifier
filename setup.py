from setuptools import setup, find_packages


setup(
    name="classifier",
    version="0.1",
    description="Text classification library.",
    url="https://github.com/VaclavDedik/classifier",
    keywords="classifier machine_learning text",
    license="MIT",

    author="Vaclav Dedik",
    author_email="vaclav.dedik@gmail.com",

    packages=find_packages(),
    install_requires=[
        'numpy>=1.7.1', # at least 1.8.0rc1 recommended
        'nltk>=3.0.4',
        'scipy>=0.12.1',  # at least 0.14.1 recommended
        'scikit-learn>=0.16.1'
    ],
)
