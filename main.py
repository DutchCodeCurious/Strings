# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
goal_scorer_0 = "Ruud Gullit"
goal_scorer_1 = "Marco van Basten"

goal_0 = 32
goal_1 = 54

scorers = goal_scorer_0 +" "+  str(goal_0)+ ", " + goal_scorer_1 +" "+ str(goal_1)
report = f"{goal_scorer_0} scored in the {goal_0}nd minute\n{goal_scorer_1} scored in the {goal_1}th minute"

player = "Gerald Vanenburg"
space_index = player.find(" ")
first_name = player[:player.find(" ")]
last_name_len = len(player[space_index:-1])
name_short = f"{player[0]}.{player[space_index:]}" 
chant = (len(first_name) * f"{first_name}! ").rstrip()
good_chant = chant[20] != " "
