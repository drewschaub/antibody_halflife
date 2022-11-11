# Antibody Halflife Analysis Tool

This is a set of tools for halflife analysis of antibodies. 
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)


## General info
The user can build simple pharmcokinetic (PK) models using linear regression, non-compartmental analysis (NCA) and multi-compartment analysis (e.g. two-compartment analysis). Model parameters can also be used to allometrically scale data which could be used for modeling different dosages or generating estimates in different model organisms. 

	
## Technologies
Project is created with:
* Python 3.10 
	
## Setup
To run this project, install it locally using npm:

```
$ conda env create -f environment.yml
$ cd src
$ python setup.py
```
