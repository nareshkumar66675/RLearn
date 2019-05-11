# RLearn

It is a Reinforcement project which uses **Q Learning**


# Overview

  - This algorithm finds the best path between the *starting point* and the *treasure* avoiding *obstacles*.
  - It uses *Q Learning*.

# Treasure Model
##### Starting Point:
- This is where the *Indiana Jones* starts his journey. 
- It is denoted by **S**

##### Empty Path:
- *Indiana Jones* can use this path to find the treasure. Basically an empty path.
- It is denoted by **-**

##### Obstacles:
- *Jones* cannot enter this path. It is blocked. If he tries to enter he might have a fatal death.
- It is denoted by **x**

##### Treasure:
- This is the lost Ark. The whole world is trying to find it. Can Jones find it?
- It is denoted by **T**

##### Current Position:
- This is the Jones current position in the map.
- It is denoted by **(M)**

# Can QLearn help Jones?
- Possible **Actions**
> UP
>DOWN
>LEFT
>RIGHT

- QLearn Parameters
> Learning Rate- 0.4
> DiscountFactor - 0.9
> Episodes- 5000

# Findig Treasure
- These below *gifs* shows how the path is found to find the treasure.
- Each has different starting points and ending points.
- Obstacles are placed randomnly each time.

Note: GIF is slightly cropped in the right side. Tried increasing the width, but it ruins the text alignment.
##### Sample 1

![](https://raw.githubusercontent.com/nareshkumar66675/RLearn/master/Visuals/FindTreasure.gif)

##### Sample 2

![](https://raw.githubusercontent.com/nareshkumar66675/RLearn/master/Visuals/FindTreasure3.gif)

##### Sample 3

![](https://raw.githubusercontent.com/nareshkumar66675/RLearn/master/Visuals/FindTreasure4.gif)

# Installation
```
1. Clone the Repository or Download the Project
2. Navigate to the folder
3. Execute 'python RLearnn.py'
```


# Sample Execution

#### 1. Select Option
```
Reinforcement Learning using QLearn
Map Legend
S: Start
x: Obstacle
-:Free Path
T: Treasure
(M): Current Position

-----------------------------------------------


Select Maps
1. Auto Generate Map
2. Enter Custom Map
Select one option from above : 1
```
#### 2. Executing for Auto Generated Map
```
Sum of Rewards: 0.7452
Step: 1

(M)  -  -  -  -  -  -  -
-  -  -  -  -  -  -  -
-  -  -  x  -  -  x  -
-  x  -  -  -  -  -  -
-  -  -  -  -  -  x  -
-  x  -  -  -  -  -  -
-  -  -  x  -  -  -  -
x  x  -  -  x  -  -  T

Step: 2
   Moving RIGHT
S  (M)  -  -  -  -  -  -
-  -  -  -  -  -  -  -
-  -  -  x  -  -  x  -
-  x  -  -  -  -  -  -
-  -  -  -  -  -  x  -
-  x  -  -  -  -  -  -
-  -  -  x  -  -  -  -
x  x  -  -  x  -  -  T

Step: 3
   Moving RIGHT
S  -  (M)  -  -  -  -  -
-  -  -  -  -  -  -  -
-  -  -  x  -  -  x  -
-  x  -  -  -  -  -  -
-  -  -  -  -  -  x  -
-  x  -  -  -  -  -  -
-  -  -  x  -  -  -  -
x  x  -  -  x  -  -  T

Step: 4
   Moving RIGHT
S  -  -  (M)  -  -  -  -
-  -  -  -  -  -  -  -
-  -  -  x  -  -  x  -
-  x  -  -  -  -  -  -
-  -  -  -  -  -  x  -
-  x  -  -  -  -  -  -
-  -  -  x  -  -  -  -
x  x  -  -  x  -  -  T

Step: 5
   Moving RIGHT
S  -  -  -  (M)  -  -  -
-  -  -  -  -  -  -  -
-  -  -  x  -  -  x  -
-  x  -  -  -  -  -  -
-  -  -  -  -  -  x  -
-  x  -  -  -  -  -  -
-  -  -  x  -  -  -  -
x  x  -  -  x  -  -  T

Step: 6
   Moving DOWN
S  -  -  -  -  -  -  -
-  -  -  -  (M)  -  -  -
-  -  -  x  -  -  x  -
-  x  -  -  -  -  -  -
-  -  -  -  -  -  x  -
-  x  -  -  -  -  -  -
-  -  -  x  -  -  -  -
x  x  -  -  x  -  -  T

Step: 7
   Moving RIGHT
S  -  -  -  -  -  -  -
-  -  -  -  -  (M)  -  -
-  -  -  x  -  -  x  -
-  x  -  -  -  -  -  -
-  -  -  -  -  -  x  -
-  x  -  -  -  -  -  -
-  -  -  x  -  -  -  -
x  x  -  -  x  -  -  T

Step: 8
   Moving DOWN
S  -  -  -  -  -  -  -
-  -  -  -  -  -  -  -
-  -  -  x  -  (M)  x  -
-  x  -  -  -  -  -  -
-  -  -  -  -  -  x  -
-  x  -  -  -  -  -  -
-  -  -  x  -  -  -  -
x  x  -  -  x  -  -  T

Step: 9
   Moving DOWN
S  -  -  -  -  -  -  -
-  -  -  -  -  -  -  -
-  -  -  x  -  -  x  -
-  x  -  -  -  (M)  -  -
-  -  -  -  -  -  x  -
-  x  -  -  -  -  -  -
-  -  -  x  -  -  -  -
x  x  -  -  x  -  -  T

Step: 10
   Moving DOWN
S  -  -  -  -  -  -  -
-  -  -  -  -  -  -  -
-  -  -  x  -  -  x  -
-  x  -  -  -  -  -  -
-  -  -  -  -  (M)  x  -
-  x  -  -  -  -  -  -
-  -  -  x  -  -  -  -
x  x  -  -  x  -  -  T

Step: 11
   Moving DOWN
S  -  -  -  -  -  -  -
-  -  -  -  -  -  -  -
-  -  -  x  -  -  x  -
-  x  -  -  -  -  -  -
-  -  -  -  -  -  x  -
-  x  -  -  -  (M)  -  -
-  -  -  x  -  -  -  -
x  x  -  -  x  -  -  T

Step: 12
   Moving RIGHT
S  -  -  -  -  -  -  -
-  -  -  -  -  -  -  -
-  -  -  x  -  -  x  -
-  x  -  -  -  -  -  -
-  -  -  -  -  -  x  -
-  x  -  -  -  -  (M)  -
-  -  -  x  -  -  -  -
x  x  -  -  x  -  -  T

Step: 13
   Moving RIGHT
S  -  -  -  -  -  -  -
-  -  -  -  -  -  -  -
-  -  -  x  -  -  x  -
-  x  -  -  -  -  -  -
-  -  -  -  -  -  x  -
-  x  -  -  -  -  -  (M)
-  -  -  x  -  -  -  -
x  x  -  -  x  -  -  T

Step: 14
   Moving DOWN
S  -  -  -  -  -  -  -
-  -  -  -  -  -  -  -
-  -  -  x  -  -  x  -
-  x  -  -  -  -  -  -
-  -  -  -  -  -  x  -
-  x  -  -  -  -  -  -
-  -  -  x  -  -  -  (M)
x  x  -  -  x  -  -  T

Step: 15
   Moving DOWN
S  -  -  -  -  -  -  -
-  -  -  -  -  -  -  -
-  -  -  x  -  -  x  -
-  x  -  -  -  -  -  -
-  -  -  -  -  -  x  -
-  x  -  -  -  -  -  -
-  -  -  x  -  -  -  -
x  x  -  -  x  -  -  (M)

Success
No of Steps : 15
GIF generated and stored as  FindTreasure.gif
```



# Project Struture
##### ExpMaxML
- **RLearn.py** - Main Startup File. Contains QLearn Implementation
- **Utils.py** - Various Utility Functions
- **Map.py** - Contains the implementation of the treasure map. 
##### Visuals
- GIFs



  
