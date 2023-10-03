# README
## Project Description
### Task:

- Implement and visualize 2 different convex hull algorithms for 2D and
compare your results regarding performance 
- Possible algorithms see slides in the moodle course 
  - Andrew´s algorithm 
  - Gift wrapping 
  - Quickhull 
  - Divide&Conquer

Free choice of programming language

#### Requirements
- 2 possible methods of generating input data (float values for 2D points)
  - Random generated test data 
  - File import with simple file format 
    - First line: number of points n 
    - Line 2 .. n+1: x,y comma seperated float values for each point 
  - Keep in mind that for useful measurements you need larger data sets!
- 2 modes of operation 
  - Performance optimized mode with just printed result and time measurement for both algorithms 
  - Visual mode which draws the convex hull step by step interactively and visualizes the algorithms


### Our Solution:

The two Algorithms we have chosen to implement are:
1. Quickhull
2. Gift Wrapping

## Code Structure
- main.py : Is our main file for the application, the one which should be executed
- algorithms (folder): A folder including both algorithms coded in a python class
- archive (folder): not needed for execution , includes old code
- helpers (folder): includes the geometry.py file with helper functions needed for the Algorithms
- setup (folder): folder holding files needed to setup and build the code accordingly

## Run the Application

Libraries used:
- matplotlib
- tkinter
- random
- time

Other dependencies (made from the dev team):
- algorithms.quickhull
- algorithms.jarvismarch
- helpers.geometry

### SetUp
1. Install the above Libraries under the point "Libraries used", can also be done by the requirements.txt which lays in the setup folder
2. Download or Clone the Repository

