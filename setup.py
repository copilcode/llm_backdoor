from setuptools import setup, find_packages

with open("requirements.txt") as f:
    required = f.read().splitlines()


setup(
    name="llm_backdoor",
    version="0.0.1",
    description="",
    url="https://github.com/copilcode/llm_backdoor",
    author="Augustin Poelmans",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    install_requires=required,
)