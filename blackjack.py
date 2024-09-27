# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
from blackjack_helper import *

# Write all of your part 4 code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.

#USER TURN
user_hand_value = draw_starting_hand('YOUR TURN')
while user_hand_value < 21:
  should_hit = input('You have ' + str(user_hand_value) + ". Hit (y/n)? ")
  if should_hit == 'n':
    break
  elif should_hit == 'y':
    user_hand_value+=draw_card()
  else:
    print("Sorry I didn't get that.")
print_end_turn_status(user_hand_value)

#DEALER TURN
dealer_hand_value = draw_starting_hand('DEALER TURN')
while dealer_hand_value < 17:
  print(f'Dealer has {dealer_hand_value}.')
  dealer_hand_value+=draw_card()
print_end_turn_status(dealer_hand_value)

# GAME RESULT
print_end_game_status(user_hand_value,dealer_hand_value)
