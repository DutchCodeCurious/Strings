# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
goal_scorer0 = "Ruud Gullit"
goal_scorer1 = "Marco van Basten"

goal_0 = 32
goal_1 = 54

scorers = f"{goal_scorer0} {str(goal_0)}, {goal_scorer1} {str(goal_1)}"
report = f"{goal_scorer0} scored in the {goal_0}nd minute \n{goal_scorer1} scored in the {goal_1}th minute"

player = "Gerald Vanenburg"
first_name = player[0:6]
last_name = len(player[7:])
short_name = f"{player[0]}. {player[7:]}" 
chant = 3 * f"{first_name}!"
good_chant = chant[20] != " "
