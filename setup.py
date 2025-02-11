from setuptools import setup, find_packages


def get_description():
    return "A library to collect information from push tasks"


def get_long_description():
    with open("README.md") as f:
        text = f.read()

    # Long description is everything after README's initial heading
    idx = text.find("\n\n")
    return text[idx:]


def get_requirements():
    with open("requirements.txt") as f:
        return f.read().splitlines()


setup(
    name="pushcollector",
    version="1.3.0",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    url="https://github.com/release-engineering/pushcollector",
    license="GNU General Public License",
    description=get_description(),
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=get_requirements(),
    python_requires=">=2.6",
    project_urls={
        "Documentation": "https://release-engineering.github.io/pushcollector/",
        "Changelog": "https://github.com/release-engineering/pushcollector/blob/master/CHANGELOG.md",
    },
)
