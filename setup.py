from setuptools import setup, find_packages
import os, sys

def parse_requirements(filename='requirements.txt'):
    with open(filename) as file:
        return file.read().splitlines()

try:
    print("...Checking requirements.txt...")
    if os.path.exists('requirements.txt'):
        install_requires = parse_requirements('requirements.txt')
except FileNotFoundError:
    sys.exit('...Requirements.txt file not found!')
else:
    print('...Requirements.txt found, installing packages...')
    setup(
        name='avantzero',
        version='0.1.0',
        author='Jordy Veenstra / A Pixelated Point of View',
        author_email='jordy.gaptx@gmail.com',
        description='Random data-generating algorithm prototype for experimental Quake III Arena Machinima post-production',
        long_description=open('README.md').read(),
        long_description_content_type='text/markdown',
        url='https://github.com/jiyorude/avantzero',
        project_urls={
            "GitHub": "https://www.github.com/jiyorude/avantzero",
            "Documentation": "https://avantzero-docs.vercel.app/",
            "PyPi": "#"
        },
        package_dir={'': 'src'},
        packages=find_packages(where='src'),
        install_requires=install_requires,
        classifiers=[
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
        ],
        python_requires='>=3.11',
        entry_points={
            'console_scripts': [
                'run_avantzero = avantzero.avantzero:main',
            ],
        },
    )
    print("...Dependencies succesfully installed!")
