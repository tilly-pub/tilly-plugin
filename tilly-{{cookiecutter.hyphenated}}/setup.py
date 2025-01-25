import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt', 'r') as f:
    requirements = [line.strip().split('#')[0] for line in f.read().split('\n') if line.strip().split('#')[0]]

setuptools.setup(
    name="tilly-{{ cookiecutter.hyphenated }}",
    version="0.0.1",
    author="{{ cookiecutter.author_name }}",
    author_email="{{ cookiecutter.author_email }}",
    description="{{ cookiecutter.description }}",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/{{ cookiecutter.github_username }}/tilly-{{ cookiecutter.hyphenated }}",
    packages=setuptools.find_packages(),
    py_modules=["tilly_{{cookiecutter.underscored}}"],
    install_requires=requirements,
    entry_points={
        "tilly": ["{{cookiecutter.underscored}} = tilly_{{cookiecutter.underscored}}.main"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)
