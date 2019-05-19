import sys

def vote():
    first_vote = input("Enter your first vote: ").lower()
    vote_list.append(first_vote)
    second_vote = input("Enter your second vote: ").lower()
    vote_list.append(second_vote)
    third_vote = input("Enter your third vote: ").lower()
    vote_list.append(third_vote)
    print("voted")

v_options = "options"
v_vote = "vote"
v_stop = "finish"

vote_list= []

print("Enter options to show options")

while True:
    vote_action = input("Enter an option: ")
    vote_action = vote_action.lower()

    if vote_action == v_options:
        print("""
        options: Use this to show available options
        vote: Use this to cast a vote
        finish: Use this to end a vote and stop the program
        """)

    elif vote_action == v_vote:
        vote()

    elif vote_action == v_stop:
        print("")
        print("Vote list is: ", vote_list)
        print("")
        counts = {}
        for i in vote_list:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1

        print (counts)
        sys.exit("Thanks for voting")
