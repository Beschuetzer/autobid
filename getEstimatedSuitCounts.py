import helpers, re

def getEstimatedSuitCounts(biddingRelative, biddingAbsolute, seatingRelative):
    '''
    inputs: ------------------------------ 
        biddingRelative: dictionary where keys are relative positions and values are lists of strings representing that user's bids (in chronological order) 
        biddingAbsolute: list of bids as a list 
        seatingRelative: dictionary where keys are relative positions and values are strings representing user's name
    returns ------------------------------:
         a dictionary representing the current "best guess" of how many of each suit a player has
    '''
    defaultValue = -1
    suitCounts = {
        "top": {
            "clubs": defaultValue,
            "diamonds": defaultValue,
            "hearts": defaultValue,
            "spades": defaultValue,
        },
        "bottom": {
            "clubs": defaultValue,
            "diamonds": defaultValue,
            "hearts": defaultValue,
            "spades": defaultValue,
        },
        "left": {
            "clubs": defaultValue,
            "diamonds": defaultValue,
            "hearts": defaultValue,
            "spades": defaultValue,
        },
        "right": {
            "clubs": defaultValue,
            "diamonds": defaultValue,
            "hearts": defaultValue,
            "spades": defaultValue,
        },
    }

    '''assumptions:
    if a player says the same suit twice they likely have 1-2 more of that suit that would be assumed otherwise (5-6 for minors and 6-7 for majors?)

    opening in no trump means no voids

    responding to opening points in the same suit means you have at least 3 of that suit?

    responding with a major means you have at least 5
    '''

    return suitCounts