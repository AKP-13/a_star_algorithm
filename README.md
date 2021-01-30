# A\* Search Algorithm

A code-along from [Tech With Tim's](https://www.youtube.com/watch?v=JtiK0DOeI4A) YouTube video that uses the A\* Search Algorithm to find the shortest distance between two user-selected points on a grid.

## Installation

-   fork and clone this repository
-   `cd` into repository
-   `pipenv install -r requirements.txt`

## Useage

-   `python astar.py`
-   **First left-click** - starting square (orange by default)
-   **Second left-click** - end square (turquoise by default)

![Start and end nodes selected with barriers](https://res.cloudinary.com/de8a23w1z/image/upload/v1612030971/a_star_search/Screenshot_2021-01-30_at_18.19.25_bpodv5.png "Start and end nodes selected with barriers")

-   **Subsequent left-clicks** - barrier squares that block off the route (black by default)
-   **Right click** - un-colour any square
-   **Space Bar** - start
-   **c** - restart

![Shortest route found!](https://res.cloudinary.com/de8a23w1z/image/upload/v1612030971/a_star_search/Screenshot_2021-01-30_at_18.20.06_qvjhru.png "Shortest route found!")
