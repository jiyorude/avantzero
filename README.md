### AvantZero
Random-data generating Algorithm for experimental,<br>
Quake III Machinima post-production 
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
AvantZero is a Python-based algorithm designed to automate and randomize the post-production process of experimental machinima films. The algorithms main line of functionality centers around the automatic generation of randomized video sequences in XML and EDL formats for use in NLE software. AvantZero places a particular focus on Quake III machinima, but will work nonetheless with any kind of footage such as screen captures, gameplay clips, smartphone or camera-based footage. As long as the video-codecs involved are supported, AvantZero can work with it. 

AvantZero evolved from the (now defunct) Dominion algorithm: an early Node.js/JavaScript-based prototype released on NPM in late 2022. The main issue with the Dominion algorithm was that it lacked any automation features and merely outputted large quantities of randomized and raw (post-)production data in `.txt` format, which still had to be interpreted and used manually by its user. 

Dominion's inability to automate any follow-up aspects of its workflow sparked the development for a better, more capable and intelligent system named *Avant*. The newer, and much improved algorithm contains a multitude of exciting functions, such as the ability to automatically generate Quake III demo files, set up multiple required project files for capturing Quake III footage with the Q3MME mod and contains the option to create a singular `.bat` file: allowing the user to manually start the capture process inside Q3MME with a single mouseclick. Avant contains many more forms of functionality on the technical end, such as the ability to fully analyze Quake III maps in terms of scope, spawn point locations and finding available camera space between the current camera's position and the 'void' (boundaries of the map). 

It can automatically download Quake III maps, generate depth of field maps of existing footage and, just as its predecessor, the Dominion algorithm, generate randomized and highly experimental video sequences which keep several user input based factors in mind. Examples of these are: composition length, resolution, aspect ratio, reserved space for title cards and framerates, to name a few. All necessary data is subsequently outputted in EDL and XML formats for use inside NLE software such as Premiere Pro, Filmlight, DaVinci Resolve or Media Composer.

During later stages of development, Avant will obtain deeper and broader layers of sophistication and functionality, such as the opportunity to export all generated data and visualizations to PDF and CSV files. Bits of machine learning, artificial intelligence and Application Programming Interfaces are naturally present on the algorithms development roadmap as well. A custom API will be built containing extensive amounts of Quake III map related data and serve as a body of knowledge for Avant, relieving the algorithm of mundane tasks and forwarding certain analyses to be conducted by the API instead. In addition, machine learning will be utilized to allow Avant to implement and master several kinds of editing styles. These editing styles are based of my earlier released machinima work (which serves as training data for Avant): allowing the algorithm to master (and continously improve upon) different editing styles and subsquently apply its knowledge during the generation of EDL and XML files: offering the user the freedom to choose either a particular editing style or to receive a fully randomized video sequence.

While Avant's foundation is laid on the automated production and post-production of Quake III machinima, the user is free to use any of its features in a stand-alone type fashion. For instance: if the user only requires map data, needs a visualization of earlier generated data or a randomized sequence of non-Quake footage, they're completely free in their ability to do so; further highlighting the algorithm's modular philosophy.

Avant was named after the highly popular art movement 'avant-garde', as it outputs raw, randomized and basically unchecked film data for the primary purpose of creating innovative, experimental and unconventional Quake III machinima films. It is not until the actual post-production process (the moment when the XML or EDL is loaded into the NLE) that the user is able to see how the generated data is visualized and captured. The films generated with avant focus on design, graphical representation, artistic expression and the idea of challenging traditional norms and practices found within Quake III movie production.  The contents do not necessarily focus on contents nor story; thus staying in true 'avant-garde fashion and less within conventional means of Quake III filmmaking. Moreover, the Avant and AvantZero algorithms appear to introduce a coherent sense of algorithmic co-ownership and co-production: which, in terminology, is encapsulated and known as 'algorithmic machinima' (or avant-machinima).  

For more information regarding Avant, please check out its [GitHub repository](https://github.com/jiyorude/avant) or refer towards either the `Functional Design Report` or the `Technical Design Report` for further information regarding the AvantZero algorithm. Both files are found within the docs section of the AvantZero repository.

<br>


**AvantZero: a proof of concept** <br>
AvantZero acts as a lightweight, functional 'proof of concept' of the more advanced and upcoming Avant algorithm to demonstrate its core functionality, feasability and relevance. While it includes fewer features than the full version, it retains core components such as:

* The ability to generate randomized post-production data;
* The functionality to output post-production data in both XML and EDL formats for further use inside of NLE software;
* Project-based workflows in which the user can execute CRUD-based operations (such as creating, viewing, editing, deleting avant projects and the ability to call several functions independently on a project-basis);
* The process of exporting generated data in PDF and/or CSV formatted files;
* Export data plots inside the generated PDF files or as standalone image files;
* Generate depth of field maps of randomized footage, or the ability to generate depth of field maps from the entire footage bin found inside of the project folder;

AvantZero demonstrates the viability and functionality of the broader Avant concept and functions as a final submission for Harvard's CS50X (Introduction to Computer Science course). Furthermore, AvantZero introduces the concept of 'avant-machinima' or 'algorithmic machinima': abstract, design-focused films that explore 'the random' and aesthetic unpredictability in digital and experimental media, while simultaneously exploring the concept of human-machine co-creation and creative co-ownership in an highly experimental manner.

The algorithm, in this larger context, operates as a technical manifest. It allows for entry into assisted forms of experimental machinima filmmaking and ‘avant-machinima’, opening possibilities for students, researchers and artists alike to utilize and experiment with Avant and AvantZero. The project, while rooted inside of Quake III Arena, introduces an interesting topic of conversation revolving around how experimental filmmaking can evolve through co-creation, partial automation, machine-based assistance and randomized activity.

In this model, the algorithm is not merely a tool but a collaborator as the algorithm outputs decisions concerning the visual aspect of the film, while the filmmaker will remain in control of the auditory scope. Even so, the filmmaker is and will always be able to make any kind of adjustments to the generated sequences: thus staying in full control of their creative process while always having the possibility to opt in new, exciting forms of hybrid filmmaking thanks to the highly modular philosophy of both the AvantZero and Avant algorithms. 


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

AvantZero is a final submission project for Harvard's CS50X (Introduction to Computer Science) course. Completing this project fulfilled the final requirement to be eligible for the CS50 certificate. If you are a student currently enrolled in CS50X or any of the other CS50-branded courses, you may only use the code and files found inside this repository for *inspiriational* purposes for your own final project. 

<br/>

&copy; Jordy Veenstra 2025 <br>
&copy; A Pixelated Point of View 2025 <br/>

Made in Amsterdam with 💙 
