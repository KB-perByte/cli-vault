from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [
        line.strip() for line in fh if line.strip() and not line.startswith("#")
    ]

setup(
    name="cli-vault",
    version="1.0.0",
    author="Sagar Paul",
    author_email="paul.sagar@yahoo.com",
    description="A secure command-line password manager with encryption and backup capabilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com//KB-perByte/cli-vault",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Security",
        "Topic :: Utilities",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "cli-vault=cli_vault.__main__:main",
        ],
    },
    keywords="password manager security encryption cli",
    project_urls={
        "Bug Reports": "https://github.com/KB-perByte/cli-vault/issues",
        "Source": "https://github.com/KB-perByte/cli-vault",
    },
)
