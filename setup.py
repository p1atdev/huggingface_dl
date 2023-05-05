from setuptools import setup, find_packages

setup(
    name="huggingface_dl",
    version="0.0.2",
    author="p1atdev",
    description="A downloader of files on huggingface",
    package_dir={"": "src"},
    packages=find_packages("src"),
    license="Apache-2.0 License",
    install_requires=["huggingface_hub"],
    entry_points={
        "console_scripts": [
            "hfdl=huggingface_dl.cli:main",
        ]
    },
    python_requires=">=3.7.0",
)
