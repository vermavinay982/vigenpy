from setuptools import _install_setup_requires, setup, find_packages

with open('readme.md','r') as f:
	long_desc = f.read()

with open('short_desc.txt','r') as f:
	short_desc = f.read()

with open('requirements.txt','r') as f:
	requirements = f.read()

requirements = requirements.split('\n')

setup(
	name='vigenpy',
	version='0.1.3',
	description=short_desc,
	license='Proprietary',
	long_description=long_desc,
	long_description_content_type='text/markdown',
	author='Vinay Verma',
	maintainer='Vinay Verma',
	maintainer_email='vermavinay982@gmail.com',
	author_email='vermavinay982@gmail.com',
	platforms=['Windows','Linux','Mac OS-X','Unix'],
	url='https://github.com/vermavinay982/vigenpy',
	python_requires='>=3.7',
	packages= [
		'vigenpy',
		'vigenpy/video',
	],
	install_requires=requirements,
)