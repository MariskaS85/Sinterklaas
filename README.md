# Sinterklaas
Hét sinterklaasspel voor thuiszitters - 2020

As 2020 progresses the holidayseason seems to have been moved right after spring. So even though we have skipped Easter (right?), Summer ánd fall, we should make the best out of Santa Clause, or as the Dutch call the original not-Coco-cola invented old man who gives us joy and presents at the end of the year; Sinterklaas.

Traditionaly, we would all buy presents for eachother and play a game at one of the players house. However due to Corona this is not possible this year. Therefore i made a game, which combines all FUNctionalities of this game only this time from the in the comfort of one's own home.


First the player selects their name from a dropddwn list of names, which would than be stored in the MongoDB database for example: 'Player1' in the list 'playersone'.
After this, the player has to fill in who the present is for, this list 'forwhom' contains the same names as before, only this gives the matched 'buyer' - 'receiver'

Then they have to fill in if the want to let the person who they bought the present for that they bought the present.
And the last question is if they want to know who bought their present. (This would be a "if" 'TRUE' and 'TRUE' "then": show name)

First level: 
Loop over the 'playersone'list and go to the first name and give the 'Dice'function. The Dice funtion gives a random number between 1 and 6. If '1'" print: ("Show your present"). If '6': ("Read your poem") and move name to 'playerstwo'list else: Print("The next in line to roll the dice") and loop over the 'players'list again.   

If no players left in database move to Level 2

level 2
Loop over the 'playerstwo'list and go to the first name and give the 'Dice'function. The Dice funtion gives a random number between 1 and 6. If "1" or "6": Open your present else: Print("The next in line to roll the dice) and go to next name in 'playerstwo'list.


If 'playerstwo'list is empty print: 'EVERYONE HAS A PRESENT! HAVE A NICE NIGHT" and "if" 'TRUE' and 'TRUE' "then": find name of 'Player1' in list 'forwhom'