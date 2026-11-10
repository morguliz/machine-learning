### coding practice
predictions = [-1, 1, -1, -1, 1]
def majority_vote(predictions):
    vote_sum = sum(predictions)
    if vote_sum >= 0:
        return 1
    else:
        return -1

print(majority_vote(predictions))