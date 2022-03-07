from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Face Recogition using Twin Neural Network'
LONG_DESCRIPTION = 'A package that allows to reconize the face using Siamese Neural Network.'

# Setting up
setup(
    name="Siamese_Face_Recognition",
    version=VERSION,
    author="AlphonseInbarajXavier",
    author_email="xalphonse@gmail.com",
    url='https://github.com/ageitgey/face_recognition',
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['opencv-python', 'dlib', 'cmake'],
    keywords=['python', 'video', 'face recognition', 'face identificaton'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3.6",
        "Natural Language :: English",
    ]
)
