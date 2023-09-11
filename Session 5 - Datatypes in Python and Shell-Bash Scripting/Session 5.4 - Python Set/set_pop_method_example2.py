"""
Method - pop()

Description: Randomly removes an item from a set and returns the removed item.

Scenario:

Drawing Lottery Prizes -
Imagine you have a group of people participating in a contest, and you want to randomly select winners for prizes.
You can use a set to store the names of participants and
then use the pop() method to randomly select and announce the winners.
"""

# Create a Set of participants who participated in a lucky draw
participants = {"Alice", "Bob", "Charlie", "David", "Eve"}

# Print the set of participants
print("Participants: \n{}".format(participants))

# Randomly selecting winners for prizes
winner = participants.pop()

# Printing winning participant
print("\nWinner: {}".format(winner))

# Print the names of rest of the participant who will go to the next round
print("\nThe rest of the participants who will go to the next round: \n{}".format(participants))

"""
                        Output - 
---------------------------------------------------------------
Participants: 
{'Eve', 'Alice', 'Charlie', 'David', 'Bob'}

Winner: Eve

The rest of the participants who will go to the next round: 
{'Alice', 'Charlie', 'David', 'Bob'}

"""