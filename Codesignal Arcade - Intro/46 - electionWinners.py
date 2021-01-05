def electionsWinners(votes, k):
    max_vote = max(votes)
    len_vote = len(votes)
    if k == 0 and votes.count(max_vote) == 1:
        return 1
    return len([ i for i in range(len_vote) if votes[i] + k > max_vote ])