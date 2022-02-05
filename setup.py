from setuptools import setup

README = ""
with open("README.md") as f:
    README = f.read()

setup(
    name="MyReplitDB",
    author="sifte",
    url="https://github.com/sifte/myreplitdb",
    version="1.3",
    description="An easy to use wrapper for replit's database.",
    long_description=README,
    long_description_content_type="text/markdown",
    packages=["myreplitdb"],
    include_package_data=True,
    license="MIT",
    project_urls = {
        "Github": "https://github.com/sifte/myreplitdb",
        },
    keywords="myreplitdb replit db replitdb replit-db",
    install_requires=[
        "replit",
    ],
)
