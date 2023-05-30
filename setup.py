from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

required = [
    "transformers>=4.25",
]

# pylint: disable=use-dict-literal
setup_args = dict(
    name="tokens-per-word",
    version="0.0.1",
    packages=find_packages(),
    author="Søren Winkel Holm",
    author_email="swholm@protonmail.com",
    url="https://github.com/sorenmulli/tokens-per-word",
    download_url="https://pypi.org/project/tokens-per-word",
    install_requires=required,
    description="How many tokens per word using given tokenizer and given dataset?",
    long_description_content_type="text/markdown",
    long_description=readme,
    license="MIT",
    entry_points={
        "console_scripts": [
            "tokens-per-word = tokens_per_word.__main__:run_from_cli",
        ]
    },
)

if __name__ == "__main__":
    setup(**setup_args)
