### AvantZero
Random-data generating Algorithm for experimental,<br>
Quake III Machinima (post-)production 
<br/>


<br/>

**Version: 0.0.0 (WORK IN PROGRESS)**
<br/><br/>
Created by Jordy Veenstra (A Pixelated Point of View)<br/>
Final submission project for Harvard's CS50X (Introduction to Computer Science) course. <br><br>

*Video Demo:* TBA

<br/>



### Table of Contents

* [Background](#background)
* [Documentation](#documentation)
* [Installation](#installation)
* [License](#license)

<br/><br/>


### Background
**Origins** <br/>
AvantZero is a Python-based tool designed to automate and randomize the post-production process of experimental machinima films, with a particular focus on Quake III machinima. It evolved from the (now defunct) Dominion algorithm; an early Node.js/JavaScript-based prototype released on NPM in late 2022. The main issue with the Dominion framework was that it lacked any automation features and merely outputted large quantities of randomized and raw (post-)production data in `.txt` format, which still had to be interpreted and used manually. 

Dominion's inability to fully automate its randomized workflow sparked the development for a better, more capable and intelligent system named *Avant*. Where Dominion merely generated randomized production- and edit data, such as sequence length, shot choice, framerates, camera positions, depth of field parameters and the like, Avant is able to automatically generate all of the required production data, post-production data, download all of the required maps, automate the creation of required files for the Q3MME mod and generate a singular `.bat` file: allowing the user to manually start the entire Q3MME capturing process with a single click. Furthermore, Avant is able to output a full sequence in `.edl` and `.xml` formats, and contains additional functionality such as neatly structured outputs and visualizations of the generated data in PDF, CSV or image formats. Later versions of Avant will include notions of machine learning and artificial intelligence implementation for embedding specific editing styles and direct connectivity towards a custom-made API containing extensive amounts of Quake III map-related data, such as size, geometry, spawn point locations, and map boundaries, to name a few examples.

While Avant's emphasis is placed on the automated production and post-production of Quake III machinima, the user is free to use its features in a stand-alone type fashion. For instance: if the user only wants to generate map data, or randomize a folder of non-Quake (or even non-machinima based footage - with origins from camcorders or smartphones), they're completely free in their choice to do so; further highlighting its modular philosophy.

Avant was named after the highly popular art movement 'avant-garde', as it outputs raw, randomized and basically unchecked film data for the primary purpose of creating innovative, experimental and unconventional Quake III machinima films. It is not until the actual post-production process that the user is able to see how the generated data is visualized and captured. The films generated with avant focus on design, graphical representation, artistic expression and the idea of challenging traditional norms and practices found within Quake III movie production, and not necessarily on their contents nor story; thus staying in true 'avant-garde fashion. For more information regarding Avant, please check out its [GitHub repository](https://github.com/jiyorude/avant) or refer towards either the `Functional Design Report` or the `Technical Design Report`; both found within the docs section of the AvantZero repository.

<br>


**AvantZero: A proof of Concept** <br>
AvantZero acts as a lighterweight, functional 'proof of concept' of the more advanced Avant algorithm to demonstrate its core functionality, feasability and relevance. While it includes fewer features, it retains core components such as:

* Randomized post-production data generation;
* Output of post-production data in both xml and edl formats;
* Project-based workflow in which the user can execute CRUD-based operations (create, view, edit and delete avant projects);
* Export generated data in PDF and/or CSV formats;
* Export data plots inside the generated PDF files or as standalone image files;
* Generate depth of field maps of randomized footage, or choose to generate depth of field maps from the footage bin in its entirety;

AvantZero demonstrates the viability and functionality of the broader Avant concept and functions as a final submission for Hardvard's CS50X (Introduction to Computer Science course). Furthermore, AvantZero introduces the concept of 'avant-machinima' or 'algorithmic machinima': abstract, design-focused films that explore randomness and aesthetic unpredictability in digital and experimental media, while simultaneously exploring the concept of (wo)man-machine co-creation and creative co-ownership in an highly experimental manner.

<br>

**Algorithmic Machinima** <br>
The ever-evolving approach visible in each of the development cycles for each of the algorithms (Dominion, AvantZero and Avant) illustrates a trajectory of design, technological refinement and deepening of concepts. Each stage serves a purpose in the vision to merge algorithmic processes with create co-authorship in the context of machinima. While limited, Dominion exposed the core functionality but also the core bottlenecks of early automation attempts. It laid the foundation for a more extensible system. Avant, while still in early development, reflects an ambitious take at creating a modular, intelligent and fully integrated piece of software that aligns with efficiency and artistic unpredictability. 

AvantZero, in this larger context, operates as a technical manifest. It allows for entry into assisted forms of machinima filmmaking and ‘avant-machinima’, opening possibilities for students, researchers and artists alike. The project, while rooted in Quake III Arena, opens a broader conversation around how experimental filmmaking can evolve through co-creation, partial automation, machine-based assistance and randomness. Avant and AvantZero position themselves as bridges between co-creativity and co-authorship. 

In this model, the algorithm is not merely a tool but a collaborator with its own logic and aesthetic tendencies as the algorithm outputs decisions concerning the visual aspect of the film, while the filmmaker will remain in control of the auditory scope. The line between author and assistant becomes blurred, resulting in a new hybrid form of authorship where intentionality and spontaneity coexist.


<br/><br/>


### Documentation
The AvantZero algorithm has a dedicated documentation website containing extensive information regarding installation, information on getting started, algorithm usage, functionality, changelogs, answers to frequently asked questions and a database of error codes; should you encounter one. Check it out [here.](http://avantzero-docs.vercel.app)

 While extensive efforts have been made to present a complete overview of information regarding AvantZero, it is possible that a bug or issue with the algorithm has not been properly documented yet. If this is the case, feel free to open an issue on [Github.](http://www.github.com/jiyorude/avantzero/issues)


<br/><br/>



### Installation
AvantZero can be installed through one of three possible methods: either by installing the algorithm through the Python Package Index, cloning the repository or downloading and initiating the executables found within the <code>Releases</code> section of the repository. Depending on which method you would like to use, please proceed with the following steps down below:

<br/>

**Option 1: PyPi Installation**
* Ensure you have Python installed on your computer by opening a terminal window and typing `python --version`. If the terminal doesn't return a version number, download and install Python from its [official website](https://www.python.org/downloads/). This will install Python, the interpreter and all of the other required software to get started.
* If you have Python installed on your computer and your current version is lower than either version `3.11` or `3.12`, please go ahead and update Python.
* **(Optional)** If required, create a new virtual environment with `python -m venv '.avantzero'`
* **(Optional)** Activate the virtual environment with `.avantzero/Scripts/Activate`. You should now see the name of the virtual environment highlighted in green within your terminal window.
* Install AvantZero with `pip install avantzero`. Please allow for up to a few minutes for Python to properly install the algorithm and all of its dependencies.
* Verify installation with `pip list` or `pip show avantzero`. If you see a complete list of installed packages (with pip list) or extensive information regarding the AvantZero algorithm (with pip show), it means the algorithm has been installed succesfully. 
* Run the algorithm by simply typing `run_avantzero` inside of your terminal window. The algorithm should now boot.
* If you are running the algorithm for the first time, it will run a first-time setup by creating the required folder structure for you within your `My Documents` folder and conduct an additional check whether all dependencies have been succesfully installed and can be found by the algorithm.


<br/>

**Option 2: Git Clone**
* Ensure you have (a recent version of) Git installed on your computer by opening a terminal window and typing `git --version`. If the terminal doesn't return a version, download and install Git from its [official website](https://git-scm.com/).
* Ensure you have Python installed on your computer by opening a terminal window and typing `python --version`. If the terminal doesn't return a version number, download and install Python from its [official website](https://www.python.org/downloads/). This will install Python, the interpreter and all of the other required software to get started.
* If you have Python installed on your computer and your current version is lower than either version `3.11` or `3.12`, please go ahead and update Python.
* Using the terminal, navigate to a folder of choice with `cd` (change directory) and clone the repository with `git clone https://github.com/jiyorude/avantzero.git`. Please allow for a few moments for all the files to be properly downloaded.
* Once all files have been downloaded, navigate to the newly cloned folder inside the terminal and install all dependencies with the command `pip install -r 'requirements.txt'`. Please allow for up to a few minutes for all dependencies and packages to install succesfully.
* Inside your terminal window, navigate to the `src` folder and start the algorithm by typing `python avantzero.py` into the terminal.
* If you are running the algorithm for the first time, it will run a first-time setup by creating the required folder structure for you within your `My Documents` folder and conduct an additional check whether all dependencies have been succesfully installed and can be found by the algorithm.


<br/>

**Option 3: Executables**
* Navigate to the `Releases` section of the repository.
* Select the latest release and download the specific executable for your operating system.
* Once downloaded, double-click on the executable to start the algorithm. 
* If you are running the algorithm for the first time, it will run a first-time setup by downloading additional dependencies required by the the algorithm to run properly and creating the required folder structure for you within your `My Documents` folder.

<br/>

<br/><br/>


### License
AvantZero is licensed under the MIT-License. Please check the <code>LICENSE</code> file found in the repository regarding usage and implementing AvantZero or parts of its source code into your own software. <br>

The Avant and AvantZero logo's use a typeface named 'Valorant', created by typeface artist Bryan T and obtained from dafont.com with a 100% free license. The logo's designed for the Avant and AvantZero algorithms are custom-designed and are not affiliated with Valorant, and/or Riot games in any way, shape or form. <br>

AvantZero is a final submission project for Harvard's CS50X (Introduction to Computer Science) course. Completing this project fulfilled the final requirement to be eligible for the CS50 certificate. If you are a student currently enrolled in CS50X or any of the other CS50-branded courses, you may only use the code and files found inside this repository for *inspiriational* purposes for your own final project. 

<br/>

&copy; Jordy Veenstra 2025 <br>
&copy; A Pixelated Point of View 2025 <br/>

Made in Amsterdam with 💙 
