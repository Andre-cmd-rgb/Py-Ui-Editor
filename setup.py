from setuptools import setup

# reading long description from file
with open('README.md') as file:
	long_description = file.read()


# specify requirements of your package here
REQUIREMENTS = ['']

# some more details
CLASSIFIERS = [
	'Development Status :: Beta',
	'Intended Audience :: Everyone',
	'Topic :: Gui',
	'License :: OSI Approved :: MIT License',
	'Programming Language :: Python 3.10',
	]

# calling the setup function
setup(name='UiLibrary',
	version='1.0.0',
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
