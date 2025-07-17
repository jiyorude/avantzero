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
* [Tech Stack](#tech-stack)
* [Documentation](#documentation)
* [Installation](#installation)
* [License](#license)

<br/><br/>


### Background


<br/><br/>

### Tech Stack

AvantZero is entirely developed in Python, a language selected not just for its unlimited amount of capabilities, but for a personal familiarity with its ecosystem. Python’s concise and highly readable syntax allows for clear architecture and dito development. Its support for object-oriented programming (OOP) enables clean, modular code organization — critical for maintaining complex systems like AvantZero.

Another key factor in choosing Python over alternatives such as C# and .NET MAUI inside Visual Studio was the ease of getting up to speed, as well as a well-established personal knowledge base across a wide range of Python libraries. This familiarity significantly shortened development time, enabled faster debugging, and allowed for seamless integration of functionality, particularly in areas such as automation, file handling, and image or video processing, which for proof of concept and prototyping purposes met all of the intended requirements. Later versions of the definitive version of AvantZero, named Avant, 

The official documentation website was built using Next.js and TypeScript. This allowed for a highly performant frontend with an emphasis on developer experience and long-term maintainability. The site is deployed through Vercel, ensuring a low-effort continuous updated pipeline for fast, automated deployments and low-latency content delivery.



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
AvantZero is licensed under the MIT-License. Please check the <code>LICENSE</code> file found in the repository regarding usage and implementing AvantZero or parts of its source code into your own software. <br> <br>

AvantZero is a final submission project for Harvard's CS50X (Introduction to Computer Science) course. Completing this project fulfilled the final requirement to be eligible for the CS50 certificate. If you are a student currently enrolled in CS50X or any of the other CS50-branded courses, you may only use the code and files found inside this repository for *inspiriational* purposes for your own final project. 

<br/>

&copy; Jordy Veenstra 2025 <br>
&copy; A Pixelated Point of View 2025 <br/>

Made in Amsterdam with 💙 
