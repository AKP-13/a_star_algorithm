# A\* Search Algorithm

A code-along from [Tech With Tim's](https://www.youtube.com/watch?v=JtiK0DOeI4A) YouTube video that uses the A\* Search Algorithm to find the shortest distance between two user-selected points on a grid.

## Installation

-   fork and clone this repository
-   `cd` into repository
-   `pipenv install -r requirements.txt`

## Useage

-   `python astar.py`
-   The first square you left-click will be the starting square (orange by default)
-   The second square you left-click will be the end square (turquoise by default)
-   Any subsequent squares you left-click (black by default) will be barrier squares that block off the route
-   To un-colour any squares, right-click them
-   To start the algorithm, press the space bar
-   Upon completion, the line of shortest distance between start and end square will be re-traced and highlighten (purple by default)
-   To restart, press `c`
