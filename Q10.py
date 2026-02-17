#High Score Organizer
def organize_scores(scores: list[int], descending: bool) -> list[int]:
    if descending:
        scores.sort(reverse=True)
    else:
        scores.sort()               
    return scores
print(organize_scores([10, 5, 8],False))
print(organize_scores([10, 5, 8],True))
original=[3,1,2]
print(organize_scores(original,True))
print(organize_scores([1,2,3],False))
print(organize_scores([],False))
