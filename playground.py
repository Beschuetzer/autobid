# import helpers
# username = 'You'
# allBids = [['Tim', 'Pass'],['Tom', 'Pass'],['James', 'One Club'],['You', 'Pass'],['Tim', 'One Diamond'],['Tom', 'Pass'],['James', 'Pass'],['You', 'Two Heart'],['Tim', 'Pass'],['Tom', 'Pass'],['James', 'Pass']]
# bids = ['Pass','Two Heart']

# isAnyBidJumpShift = False
# for i in range(0, len(bids)): 
#     bid = bids[i]
#     indexOfUsersBid = helpers.getIndexOfNthBid(username, allBids, i + 1)
#     biddingUpToThisPoint = allBids[:indexOfUsersBid]
#     contractBidAtThisPoint = helpers.getCurrentContractBid(biddingUpToThisPoint)
#     isAnyBidJumpShift = helpers.getIsJumpShift(contractBidAtThisPoint, bid)

#     print('bids = {0}'.format(bids))
#     print('indexOfUsersBid = {0}'.format(indexOfUsersBid))
#     print('biddingUpToThisPoint = {0}'.format(biddingUpToThisPoint))
#     print('contractBidAtThisPoint = {0}'.format(contractBidAtThisPoint))

#     i += 1
#     if isAnyBidJumpShift is True:
#         break

# print('isAnyBidJumpShift = {0}'.format(isAnyBidJumpShift))
import getEstimatedPoints


locations = getEstimatedPoints.locations
locationOrder = [locations['left'], locations['top'],locations['right'], locations['bottom']]

#get new order based on dealer
locationOrderToUse = locationOrder

index = locationOrder.index(locations['bottom'])
locationOrderToUse = locationOrder[index:] + locationOrder[:index]

print('locationOrderToUse = {0}'.format(locationOrderToUse))