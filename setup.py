from setuptools import setup

# reading long description from file
with open('README.md') as file:
	long_description = file.read()


# specify requirements of your package here
REQUIREMENTS = ['']

# some more details
CLASSIFIERS = []

# calling the setup function
setup(name='UiLibrary',
	version='1.0.7',
	description='A gui development library',
	long_description=long_description,
	url='https://github.com/Andre-cmd-rgb/Py-Ui-Library',
	author='Andre-Cmd-Rgb',
	author_email='andreavigolini@outlook.com',
	license='MIT',
	packages=['UiLibrary'],
	classifiers=CLASSIFIERS,
	install_requires=REQUIREMENTS,
	keywords='Py Ui Library'
	)
