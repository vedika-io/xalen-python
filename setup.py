from setuptools import setup, find_packages

setup(
    name="xalen",
    version="0.1.0",
    description="XALEN SDK — AI Infrastructure for the Faith Economy",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="XALEN Technology Pvt Ltd",
    author_email="sdk@xalen.ai",
    url="https://github.com/xalen-ai/xalen-python",
    project_urls={
        "Documentation": "https://xalen.io/docs",
        "Source": "https://github.com/xalen-ai/xalen-python",
        "Issues": "https://github.com/xalen-ai/xalen-python/issues",
    },
    packages=find_packages(),
    install_requires=["openai>=1.0.0"],
    python_requires=">=3.8",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries",
    ],
    keywords="xalen ai api faith-tech astrology inference",
)
