import setuptools

with open("README.md", "r",encoding="utf-8") as f:
    long_description =f.read()

_version_ ="0.0.0"
REPO_NAME = "cnclassifier"
AUTHOR_USER_NAME = "NeerajSharma31"
SRC_REPO = "cnclassifier"
AUTHOR_EMAIL ="rneerajsharma31@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=_version_,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/{AUTHER_USER_NAME}/{REPO_NAME}/issues",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
