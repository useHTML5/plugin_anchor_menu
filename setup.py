from setuptools import setup, find_packages

setup(
    name="plugin_anchor_menu",
    version="0.5",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "django>=2.2",
    ],
)
