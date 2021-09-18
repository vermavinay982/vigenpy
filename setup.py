from setuptools import _install_setup_requires, setup, find_packages

with open('readme.md','r') as f:
	long_desc = f.read()

with open('documents/short_desc.txt','r') as f:
	short_desc = f.read()

with open('requirements.txt','r') as f:
	requirements = f.read()

requirements = requirements.split('\n')

setup(
	name='vigenpy',
	version='0.3.5',
	description=short_desc,
	license='MIT',
	long_description=long_desc,
	long_description_content_type='text/markdown',
	author='Vinay Kumar Verma',
	maintainer='Vinay Kumar Verma',
	maintainer_email='vermavinay982@gmail.com',
	author_email='vermavinay982@gmail.com',
	platforms=['Windows','Linux','Mac OS-X','Unix'],
	url='https://github.com/vermavinay982/vigenpy',
	python_requires='>=3.7',
	packages= [
		'vigenpy',
		'vigenpy/video',
	],
	keywords = ['vigenpy','video gen','video','generator','computer vision', 'image processing'],   # Keywords that define your package best
	install_requires=requirements,
	classifiers=[
    'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      # Specify which python versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],

)