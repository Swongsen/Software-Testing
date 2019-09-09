# PPA 1 - Intro to Unit Testing and T/BDD

A project by **Alain Garcia** and **Spencer Wong**

Course: CIS4930 (Software Testing for Continuous Delivery)
Professor: Dr. Byron Williams
TA: Lokesh Paluri

## Naming and Organization Conventions
- Language Used:        Python 3.x
- Testing Framework:    pytest


## Setup and Execution
1. **Download and Install Python 3.x**
    #### Windows ####
    * Download [Python 3.x for Windows](https://www.python.org/ftp/python/3.7.4/python-3.7.4.exe)
        * Run the python-3.7.4.exe file and go through the windows installer
        * Make sure to install 'pip'
    #### Mac ####
    * Download [Python 3.x for Mac](https://www.python.org/ftp/python/3.7.4/python-3.7.4-macosx10.6.pkg)
        * Run the python-3.7.4-macosx10.6.pkg and go through the installer
        * Make sure to install 'pip'
    #### Linux/Unix #####
    * Try running the following commands in your command line:
        ```bash
        sudo apt-get update
        sudo apt-get install python3.7
        ```
        Vist [here](https://docs.python-guide.org/starting/install3/linux/) for a more in-depth look at installation using apt-get
    * If the above step didn't work, download [Python 3.x for Linux/Unix](https://www.python.org/ftp/python/3.7.4/Python-3.7.4.tgz)
        ```bash
        tar xf Python-3.7.4.tgz
        cd Python-3.7.4
        ./configure
        make
        make test
        sudo make install
        ```
        Vist [here](https://passingcuriosity.com/2015/installing-python-from-source/) for a more in-depth look at installing Python from source
2. **Install pytest (The Python testing framework)**
    
    Using your respective operating system's command line, run:
    ```bash
    pip install pytest
    ```

## Output


## Test Coverage


## Experiences

- Alain Garcia's Experiences
    I believe that Test Driven Development (TDD) allows me to focus more on core features. Without TDD, I would often implement unnecessary or possibly redundant code. TDD also provides a fantastic way to organize your thoughts. 
    Unit testing provides a much quicker way to make sure that everything in a given project still works. I found that while working on this project, there were many times where I would add code that would break certain functionality. Unit Testing made it so I could catch these mistakes before going any further.