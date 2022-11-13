# code written by u/baghiq on Reddit, the user out of a lot of other users who showed me a way to use dictionaries when I asked on r/learnpython if there was a better way to write this program but still use dictionaries

aliens = []
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(f"Shooting the {alien['color']} alien yields {alien['points']} points.")



"""""
The code I had written, it was working but there is no point for using dictionaries like that: 

alien_0 = {'green' : '', '5' : ''}
alien_1 = {'yellow' : '', '10' : ''}
alien_2 = {'red' : '', '15' : ''}
aliens = [alien_0, alien_1, alien_2]
for color, points in aliens:
    print(f"Shooting the {color} alien yields {points} points.")

OUTPUT: 
Shooting the green alien yields 5 points.
Shooting the yellow alien yields 10 points.
Shooting the red alien yields 15 points.

"""""