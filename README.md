# Udacity Full Stack Logs Analysis Project

This project, a logs reporting tool that answers user activity questions, was developed as part of the Udacity Full Stack Web Developer Nanodegree Program. The reporting tool, written in Python, uses the psycopg2 module to connect to a PostgreSQL database to retrieve information on article readership.

## Required Software

* [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
* [Vagrant](https://www.vagrantup.com/downloads.html)

## Required Files

* [Virtual Machine Configuration](https://github.com/udacity/fullstack-nanodegree-vm)
* [Database Data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

## Setup

1. After VirtualBox and Vagrant have been installed, unzip the contents of the virtual machine configuration. This should produce a directory called FSND-Virtual-Machine.

2. Inside of FSND-Virtual-Machine, there will be a subdirectory named vagrant. Unzip the database data zip file, newsdata.zip, and place its contents, newsdata.sql, into the vagrant directory.

3. From the terminal, change to the vagrant directory.

4. Start the virtual machine by running the command ```vagrant up```. This will begin the process of downloading and installing a Linux operating system along with all of the configuration files.

5. When you get your shell prompt back, log in to the virtual machine by running the command ```vagrant ssh```.

6. Run the command ```cd /vagrant``` from within the virtual machine to access the same vagrant directory available on your computer.

7. Import the database data by running the command ```psql -d news -f newsdata.sql```.

## Instructions

1. After downloading or cloning this repository, remove the contents of the newly created directory and place them directly into the vagrant directory. Among other files, report.py should now be located in the vagrant directory.

2. Back at the terminal, while logged into the virtual machine and within the vagrant directory, run the command ```python3 report.py```.

3. Compare your output with the expected output found in the example_output.txt file.