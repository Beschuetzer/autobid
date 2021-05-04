# import helpers
# username = 'You'
# biddingAbsolute = [['Tim', 'Pass'],['Tom', 'Pass'],['James', 'One Club'],['You', 'Pass'],['Tim', 'One Diamond'],['Tom', 'Pass'],['James', 'Pass'],['You', 'Two Heart'],['Tim', 'Pass'],['Tom', 'Pass'],['James', 'Pass']]
# bids = ['Pass','Two Heart']

# isAnyBidJumpShift = False
# for i in range(0, len(bids)): 
#     bid = bids[i]
#     indexOfUsersBid = helpers.getIndexOfNthBid(username, biddingAbsolute, i + 1)
#     biddingUpToThisPoint = biddingAbsolute[:indexOfUsersBid]
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

print('locationOrderToUse = {0}'.format(locationOrderToUse[:-1]))


bids = [['Adam', 'One Diamond'], ['Dan', 'Two Club'], ['Ann', 'Double'], ['Andrew', 'Three Club']]

print(bids[:2])

a_dictionary = {"a": 1, "b": 2, "c": 0, }
max_key = max(a_dictionary, key=a_dictionary.get)
print(max_key)

test = [1,2,3,4,5,6]
print (4 in test)

x = {
  "clubs": 0,
  "diamonds": 0,
  "heart": 0,
  "clubs": 0,
}
print(dict(sorted(x.items(), key=lambda item: item[1])))

while a_dictionary.items():
  max_key = max(a_dictionary, key=a_dictionary.get)
  print(f"max_key = {max_key}")
  del a_dictionary[max_key]
  