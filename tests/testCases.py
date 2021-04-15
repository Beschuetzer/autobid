#TODO: THIS IS WHERE ALL THE BIDDING RELATIVE DICTIONARIES FOR THE TEST CASES WE  WILL BE HOUSED ONCE WE HAVE FINISHED THE SET.  PROPOSED STRUCTURE:

biddingRelatives = {
  "oneBidOpportunity": {
    "exitEarly": {
        "left": ['One Diamond'],
        "top": ['Two Heart'],
        "right": ['Two No Trump'],
        "bottom": ['Pass'],
    },
    "pass": {
        "left": [],
        "top": [],
        "right": ['pass'],
        "bottom": [],
    },
    "pass2": {
        "left": [],
        "top": ['pass'],
        "right": ['pass'],
        "bottom": [],
    },
    "nt1": {
        "left": ['One No Trump'],
        "top": ['pass'],
        "right": ['pass'],
        "bottom": [],
    },
    "nt2": {
        "left": [],
        "top": ['One No Trump'],
        "right": ['pass'],
        "bottom": [],
    },
    "nt3": {
        "left": ['pass'],
        "top": ['pass'],
        "right": ['One No Trump'],
        "bottom": [],
    },
    "twoClub1": {
        "left": [],
        "top": ['Two Club'],
        "right": ['pass'],
        "bottom": [],
    },
    "twoClub2": {
        "left": [],
        "top": ['pass'],
        "right": ['Two Club'],
        "bottom": [],
    },
    "twoClub3": {
        "left": ['pass'],
        "top": ['pass'],
        "right": ['Two Club'],
        "bottom": [],
    },
    "double1": {
        "left": [],
        "top": ['Double'],
        "right": ['pass'],
        "bottom": [],
    },
    "double2": {
        "left": [],
        "top": ['pass'],
        "right": ['Double'],
        "bottom": [],
    },
    "double3": {
        "left": ['pass'],
        "top": ['pass'],
        "right": ['Double'],
        "bottom": [],
    },
    "suit1": {
        "left": [],
        "top": ['One Diamond'],
        "right": ['pass'],
        "bottom": [],
    },
    "suit2": {
        "left": [],
        "top": ['pass'],
        "right": ['One Diamond'],
        "bottom": [],
    },
    "suit3": {
        "left": ['pass'],
        "top": ['pass'],
        "right": ['One Spade'],
        "bottom": [],
    },
    "weakTwo1": {
        "left": [],
        "top": ['Two Diamond'],
        "right": ['pass'],
        "bottom": [],
    },
    "weakTwo2": {
        "left": [],
        "top": ['pass'],
        "right": ['Two Spade'],
        "bottom": [],
    },
    "weakTwo3": {
        "left": ['pass'],
        "top": ['pass'],
        "right": ['Two Heart'],
        "bottom": [],
    },
    "weakTwo4": {
        "left": [],
        "top": ['One Club'],
        "right": ['Two Heart'],
        "bottom": [],
    },
    "weakTwo5":  {
        "left": ['Pass'],
        "top": ['One Club'],
        "right": ['Two Spade'],
        "bottom": [],
    },
    "weakThree1": {
        "left": [],
        "top": ['Three Diamond'],
        "right": ['pass'],
        "bottom": [],
    },
    "weakThree2": {
        "left": [],
        "top": ['pass'],
        "right": ['Three Diamond'],
        "bottom": [],
    },
    "weakThree3": {
        "left": ['pass'],
        "top": ['pass'],
        "right": ['Three Diamond'],
        "bottom": [],
    },
    "weakThree4": {
        "left": ['One Diamond'],
        "top": ['Three Heart'],
        "right": ['pass'],
        "bottom": [],
    },
    "bottomIsDealer":  {
        "left": ['pass'],
        "top": ['pass'],
        "right": ['One No Trump'],
        "bottom": ['One Heart'],
    },
    "twoClubsTwoDiamondResponse": {
        "left": ['Two Club'],
        "top": ['pass'],
        "right": ['Two Diamond'],
        "bottom": [],
    },
    "twoClubsTwoHeartResponse": {
        "left": ['Two Club'],
        "top": ['pass'],
        "right": ['Two Heart'],
        "bottom": [],
    },
    "twoClubsSpadeResponse": {
        "left": ['Two Club'],
        "top": ['pass'],
        "right": ['Two Spade'],
        "bottom": [],
    },
    "twoClubsTwoNTResponse": {
        "left": ['Two Club'],
        "top": ['pass'],
        "right": ['Two No Trump'],
        "bottom": [],
    },
    "twoClubsThreeClubResponse": {
        "left": ['Two Club'],
        "top": ['pass'],
        "right": ['Three Club'],
        "bottom": [],
    },
    "twoClubsInterferenceDouble": {
        "left": ['Two Club'],
        "top": ['double'],
        "right": ['Three Club'],
        "bottom": [],
    },
    "twoClubsInterferenceTwoLevelBid": {
        "left": ['Two Club'],
        "top": ['Two Spade'],
        "right": ['Three Club'],
        "bottom": [],
    },
    "twoClubsInterferenceThreeLevelPassBid": {
        "left": ['Two Club'],
        "top": ['Three Diamond'],
        "right": ['pass'],
        "bottom": [],
    },
    "twoClubsInterferenceThreeLevelTwoAboveBid": {
        "left": ['Two Club'],
        "top": ['Three Diamond'],
        "right": ['Three No Trump'],
        "bottom": [],
    },
    "twoClubsInterferenceRandomBid": {
        "left": ['Two Club'],
        "top": ['Four Diamond'],
        "right": ['Pass'],
        "bottom": [],
    },
  },

  "twoBidOpportunities": {

  },

  "threePlusBidOpportunities": {

  },
}
