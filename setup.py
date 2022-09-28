from setuptools import setup

requirements = ["requests", "urllib3", "enum34",]

setup(
    name="cod_api",
    packages=['cod_api'],
    install_requires=requirements,
    setup_requires=["wheel"],
)
