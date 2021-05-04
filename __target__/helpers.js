// Transcrypt'ed from Python, 2021-05-03 21:20:44
var autoBid = {};
var getEstimatedPoints = {};
var math = {};
var re = {};
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import * as __module_re__ from './re.js';
__nest__ (re, '', __module_re__);
import * as __module_math__ from './math.js';
__nest__ (math, '', __module_math__);
import * as __module_getEstimatedPoints__ from './getEstimatedPoints.js';
__nest__ (getEstimatedPoints, '', __module_getEstimatedPoints__);
import * as __module_autoBid__ from './autoBid.js';
__nest__ (autoBid, '', __module_autoBid__);
var __name__ = 'helpers';
export var highCardPointValues = dict ([['hcp', dict ([['ace', 4], ['king', 3], ['queen', 2], ['jack', 1]])], ['alternative', dict ([['ace', 4.5], ['king', 3], ['queen', 1.5], ['jack', 0.75], ['ten', 0.25]])]]);
export var suitLengthRequiredToCount = dict ([['king', 2], ['queen', 3], ['jack', 4], ['ten', 5]]);
export var distributionPointValues = dict ([['shortness', dict ([['void', 3], ['singleton', 2], ['doubleton', 1]])], ['length', dict ([['fiveCardSuit', 1], ['sixCardsSuit', 2], ['sevenCardsSuit', 3]])]]);
export var getIsTeamsFirstBidOpportunity = function (biddingRelative, location) {
	var partnersLocation = '';
	if (location == getEstimatedPoints.locations ['top']) {
		var partnersLocation = getEstimatedPoints.locations ['bottom'];
	}
	else if (location == getEstimatedPoints.locations ['bottom']) {
		var partnersLocation = getEstimatedPoints.locations ['top'];
	}
	else if (location == getEstimatedPoints.locations ['right']) {
		var partnersLocation = getEstimatedPoints.locations ['left'];
	}
	else if (location == getEstimatedPoints.locations ['left']) {
		var partnersLocation = getEstimatedPoints.locations ['right'];
	}
	else {
		var __except0__ = ValueError ('location must be top bottom left of right');
		__except0__.__cause__ = null;
		throw __except0__;
	}
	var partnersBids = biddingRelative [partnersLocation];
	if (location == getEstimatedPoints.locations ['left'] && len (partnersBids) == 1) {
		return true;
	}
	return len (biddingRelative [partnersLocation]) == 0;
};
export var getSeatingRelative = function (seating, spot) {
	var directions = ['north', 'east', 'south', 'west'];
	return dict ([['left', seating [directions [__mod__ (directions.index (spot) + 1, 4)]]], ['top', seating [directions [__mod__ (directions.index (spot) + 2, 4)]]], ['right', seating [directions [__mod__ (directions.index (spot) + 3, 4)]]], ['bottom', seating [directions [__mod__ (directions.index (spot) + 0, 4)]]]]);
};
export var getIsPartnersFirstBidPass = function (biddingRelative, seatingRelative, username) {
	var partnersLocation = getPartnersLocation (username, seatingRelative);
	var partnersBidding = biddingRelative [partnersLocation];
	if (len (partnersBidding) > 0) {
		if (re.search ('pass', partnersBidding [0], re.IGNORECASE)) {
			return true;
		}
	}
	return false;
};
export var getHasSomeOneOpenedBefore = function (indexOfUsersFirstBid, biddingAbsolute) {
	var bidsUpToUsersFirstBid = biddingAbsolute;
	if (indexOfUsersFirstBid != null) {
		var bidsUpToUsersFirstBid = biddingAbsolute.__getslice__ (0, indexOfUsersFirstBid, 1);
	}
	for (var bid of bidsUpToUsersFirstBid) {
		if (!(re.search ('pass', bid [1], re.IGNORECASE)) && !(re.search ('double', bid [1], re.IGNORECASE))) {
			return true;
		}
	}
	return false;
};
export var getPartnersLocation = function (username, seatingRelative) {
	var locationToUse = null;
	for (var [location, usernameInDict] of seatingRelative.py_items ()) {
		if (usernameInDict == username) {
			var locationToUse = location;
			break;
		}
	}
	if (locationToUse == null) {
		return null;
	}
	var locations = ['left', 'top', 'right', 'bottom'];
	var indexOfUsersLocation = locations.index (locationToUse);
	return locations [__mod__ (indexOfUsersLocation + 2, 4)];
};
export var getIndexOfNthBid = function (username, biddingAbsolute, nthBid) {
	var i = 0;
	var matchCount = 0;
	if (nthBid < 0) {
		var nthBidCounter = 0;
		for (var i of range (-(1), -(len (biddingAbsolute) + 1), -(1))) {
			var adjustedI = len (biddingAbsolute) + i;
			var bid = biddingAbsolute [adjustedI];
			if (bid [0] == username) {
				nthBidCounter += 1;
				if (nthBidCounter == -(nthBid)) {
					return adjustedI;
				}
			}
		}
		if (len (biddingAbsolute) == 0) {
			return 0;
		}
		else {
			return len (biddingAbsolute) - 1;
		}
	}
	else {
		for (var bid of biddingAbsolute) {
			if (bid [0] == username) {
				matchCount += 1;
				if (matchCount == nthBid) {
					return i;
				}
			}
			i += 1;
		}
	}
	return null;
};
export var getHasPlayerJumpshifted = function (username, playersBids, biddingAbsolute) {
	for (var i = 0; i < len (playersBids); i++) {
		var bid = playersBids [i];
		var indexOfUsersBid = getIndexOfNthBid (username, biddingAbsolute, i + 1);
		var biddingUpToThisPoint = biddingAbsolute.__getslice__ (0, indexOfUsersBid, 1);
		var contractBidAtThisPoint = getCurrentContractBid (biddingUpToThisPoint);
		var isAnyBidJumpShift = getIsJumpshift (contractBidAtThisPoint [1], bid);
		i += 1;
		if (isAnyBidJumpShift === true) {
			return true;
		}
	}
	return false;
};
export var getIsJumpshift = function (currentContractBid, usersBid) {
	print ('{}{}'.format (currentContractBid));
	print ('{}{}'.format (usersBid));
	if (!(currentContractBid) || currentContractBid == '' || re.search ('pass', usersBid, re.IGNORECASE) || re.search ('double', usersBid, re.IGNORECASE) || re.search ('pass', currentContractBid, re.IGNORECASE) || re.search ('double', currentContractBid, re.IGNORECASE)) {
		return false;
	}
	if (isinstance (currentContractBid, list) && len (currentContractBid) > 1) {
		var currentContractBid = currentContractBid [1];
	}
	var indexOfCurrentActualBid = autoBid.contracts.index (currentContractBid);
	var indexOfUsersBid = autoBid.contracts.index (usersBid);
	print ('{}{}'.format (indexOfCurrentActualBid));
	print ('{}{}'.format (indexOfUsersBid));
	print ('{}{}'.format (abs (indexOfCurrentActualBid - indexOfUsersBid)));
	if (indexOfCurrentActualBid > indexOfUsersBid) {
		return false;
	}
	return abs (indexOfCurrentActualBid - indexOfUsersBid) > 5;
};
export var getWasForcedToBid = function (username, biddingAbsolute, seatingRelative) {
	try {
		print ('{}{}'.format (biddingAbsolute));
		var partnersUsername = getUsernamesPartner (username, seatingRelative);
		var indexOfPartnersFirstBid = getIndexOfNthBid (partnersUsername, biddingAbsolute, 1);
		var partnersFirstBid = biddingAbsolute [indexOfPartnersFirstBid];
		var bidAfterPartnersFirstBid = biddingAbsolute [indexOfPartnersFirstBid + 1];
		var caseDouble = re.search ('double', partnersFirstBid [1], re.IGNORECASE) && re.search ('pass', bidAfterPartnersFirstBid [1], re.IGNORECASE);
		var caseNoTrump = re.search ('trump', partnersFirstBid [1], re.IGNORECASE) && re.search ('pass', bidAfterPartnersFirstBid [1], re.IGNORECASE);
		if (caseDouble || caseNoTrump) {
			return true;
		}
		return false;
	}
	catch (__except0__) {
		return 'Error in getWasForcedToBid';
	}
};
export var getUsernamesPartner = function (username, seatingRelative) {
	try {
		var locations = ['top', 'right', 'bottom', 'left'];
		var locationToUse = null;
		for (var [location, usernameInSeating] of seatingRelative.py_items ()) {
			if (usernameInSeating == username) {
				var locationToUse = location;
				break;
			}
		}
		var indexToUse = __mod__ (locations.index (locationToUse) + 2, 4);
		return seatingRelative [locations [indexToUse]];
	}
	catch (__except0__) {
		return 'Error in getUsernamesPartner';
	}
};
export var getHasPartnerOpened = function (biddingAbsolute, seatingRelative, username) {
	try {
		var usernamesPartner = getUsernamesPartner (username, seatingRelative);
		var usernameWhoHadFirstOpportunityToBid = getUsernameOfPlayerWhoHadFirstOpportunityToBid (biddingAbsolute, usernamesPartner, username);
		var partnerBidFirst = usernamesPartner == usernameWhoHadFirstOpportunityToBid;
		var userNamesFirstBidIndex = getIndexOfNthBid (username, biddingAbsolute, 1);
		var usernamesFirstBid = biddingAbsolute [userNamesFirstBidIndex];
		var bidsUserHasMade = 0;
		var bidsPartnerHasMade = 0;
		for (var bid of biddingAbsolute) {
			if (bid [0] == username) {
				bidsUserHasMade += 1;
			}
			if (bid [0] == usernamesPartner) {
				bidsPartnerHasMade += 1;
			}
		}
		if (bidsPartnerHasMade == 0) {
			return false;
		}
		if (!(partnerBidFirst) && re.search ('pass', usernamesFirstBid [1], re.IGNORECASE) && bidsUserHasMade == 1) {
			return false;
		}
		else {
			var indexOfUsersLastBid = getIndexOfNthBid (username, biddingAbsolute, -(1));
			if (indexOfUsersLastBid === null) {
				return null;
			}
			var indexOfUsersFirstNonPassBid = -(1);
			var i = 0;
			for (var bid of biddingAbsolute) {
				if (bid [0] == username) {
					if (!(re.search ('pass', bid [1], re.IGNORECASE))) {
						if (re.search ('double', bid [1], re.IGNORECASE) && i != 0) {
							continue;
						}
						var indexOfUsersFirstNonPassBid = i;
						break;
					}
				}
				i += 1;
			}
			var partnersNthBid = 0;
			if (indexOfUsersFirstNonPassBid == -(1)) {
				for (var bid of biddingAbsolute) {
					if (bid [0] == usernamesPartner) {
						partnersNthBid += 1;
						if (!(re.search ('pass', bid [1], re.IGNORECASE))) {
							if (partnersNthBid > 1 && re.search ('double', bid [1], re.IGNORECASE)) {
								continue;
							}
							return true;
						}
					}
				}
				return false;
			}
			else {
				var biddingUpToUsersFirstNonPassBid = biddingAbsolute.__getslice__ (0, indexOfUsersFirstNonPassBid, 1);
				for (var bid of biddingUpToUsersFirstNonPassBid) {
					if (bid [0] == usernamesPartner) {
						if (!(re.search ('pass', bid [1], re.IGNORECASE))) {
							return true;
						}
					}
				}
				return false;
			}
		}
	}
	catch (__except0__) {
		return false;
	}
};
export var getUsernameOfPlayerWhoHadFirstOpportunityToBid = function (biddingAbsolute, usernamesPartner, username) {
	for (var bid of biddingAbsolute) {
		if (bid [0] == usernamesPartner) {
			return usernamesPartner;
		}
		else if (bid [0] == username) {
			return username;
		}
	}
	return null;
};
export var getBiddingHistory = function (biddingAbsolute) {
	var biddingHistory = [];
	for (var bid of biddingAbsolute) {
		biddingHistory.append (bid [1]);
	}
	return biddingHistory;
};
export var getTwoClubResponse = function (hand, biddingRelative, seatingRelative, totalOpeningPoints, currentActualBid, clientPointCountingConvention) {
	var currentActualBidIndex = autoBid.contracts.index (currentActualBid [1]);
	if (!(re.search ('pass', biddingRelative ['left'] [0], re.IGNORECASE)) && !(re.search ('double', biddingRelative ['left'] [0], re.IGNORECASE))) {
		return 'Pass';
	}
	var longestSuit = null;
	var longestLength = 0;
	for (var suit of hand) {
		if (len (suit) > longestLength) {
			var longestSuit = getSuitNameFromCardAsNumber (suit [0]);
			var longestLength = len (suit);
		}
	}
	if (totalOpeningPoints >= 13 && longestLength >= 7) {
		var hasTakenPartnerOutOfGameBid = getHasTakenPartnerOutOfGameBid (seatingRelative ['bottom'], biddingRelative, seatingRelative);
		if (hasTakenPartnerOutOfGameBid) {
			return 'Pass';
		}
		return getNextBidInSuit (longestSuit, currentActualBid [1]);
	}
	var bestSuitIsNoTrump = null;
	if (len (biddingRelative ['top']) > 2) {
		var bestSuitIsNoTrump = re.search ('trump', biddingRelative ['top'] [1], re.IGNORECASE);
	}
	if (re.search ('two club', biddingRelative ['top'] [-(1)], re.IGNORECASE)) {
		if (totalOpeningPoints == 0) {
			return autoBid.contracts [currentActualBidIndex + 1];
		}
		var wholeNumber = int (math.ceil (totalOpeningPoints / 3));
		return autoBid.contracts [currentActualBidIndex + wholeNumber];
	}
	else if (len (biddingRelative ['top']) == 2) {
		var suit = getStrongestSuit (hand, biddingRelative, clientPointCountingConvention);
		for (var i = 1; i < 6; i++) {
			if (re.search (suit, autoBid.contracts [currentActualBidIndex + i], re.IGNORECASE)) {
				return autoBid.contracts [currentActualBidIndex + i];
			}
		}
	}
	else if (!(bestSuitIsNoTrump) && re.search ('trump', biddingRelative ['top'] [-(1)], re.IGNORECASE)) {
		var aceCount = 0;
		for (var suit of hand) {
			for (var cardAsNumber of suit) {
				if (__mod__ (cardAsNumber, 13) == 12) {
					aceCount += 1;
				}
			}
		}
		var isAllOrNone = aceCount == 0 || aceCount == 4;
		var indexAddition = 0;
		if (isAllOrNone) {
			var indexAddition = 1;
		}
		else {
			var indexAddition = aceCount + 1;
		}
		return autoBid.contracts [currentActualBidIndex + indexAddition];
	}
	else if (getSuitFromBid (biddingRelative ['top'] [1]) != getSuitFromBid (biddingRelative ['top'] [3])) {
		var kingCount = 0;
		for (var suit of hand) {
			for (var cardAsNumber of suit) {
				if (__mod__ (cardAsNumber, 13) == 11) {
					kingCount += 1;
				}
			}
		}
		var isAllOrNone = kingCount == 0 || kingCount == 4;
		var indexAddition = 0;
		if (isAllOrNone) {
			var indexAddition = 1;
		}
		else {
			var indexAddition = kingCount + 1;
		}
		return autoBid.contracts [currentActualBidIndex + indexAddition];
	}
	return 'Pass';
};
export var getNextBidInSuit = function (suit, currentActualBid) {
	try {
		var suitsOrder = ['club', 'diamond', 'heart', 'spade', 'no trump'];
		if (suit [-(1)] == 's') {
			var suit = suit.__getslice__ (0, -(1), 1);
		}
		var suit = suit.lower ();
		var currentActualBidSuit = currentActualBid.py_split (' ');
		if (len (currentActualBidSuit) == 3) {
			var currentActualBidSuit = '{}{}{}'.format (currentActualBidSuit [-(2)], currentActualBidSuit [-(1)]).lower ();
		}
		else {
			var currentActualBidSuit = currentActualBidSuit [-(1)].lower ();
		}
		var currentActualBidSuitsOrderIndex = suitsOrder.index (currentActualBidSuit);
		var targetSuitOrdersIndex = suitsOrder.index (suit);
		var indexToUse = null;
		var currentActualBidIndex = autoBid.contracts.index (currentActualBid);
		if (targetSuitOrdersIndex <= currentActualBidSuitsOrderIndex) {
			var indexToUse = (currentActualBidIndex + 5) - (currentActualBidSuitsOrderIndex - targetSuitOrdersIndex);
		}
		else {
			var indexToUse = (currentActualBidIndex + targetSuitOrdersIndex) - currentActualBidSuitsOrderIndex;
		}
		return autoBid.contracts [indexToUse];
	}
	catch (__except0__) {
		if (isinstance (__except0__, Exception)) {
			var err = __except0__;
			var __except1__ = Exception ('{}{}'.format (err));
			__except1__.__cause__ = null;
			throw __except1__;
		}
		else {
			throw __except0__;
		}
	}
};
export var getSuitFromBid = function (bid) {
	var py_split = bid.py_split ();
	if (py_split && len (py_split) > 1) {
		return bid.py_split () [1];
	}
	return null;
};
export var getSpotAfterNRotations = function (spot, numberOfRotations) {
	if (numberOfRotations < 0) {
		var __except0__ = py_TypeError ('Invalid numberOfRotations');
		__except0__.__cause__ = null;
		throw __except0__;
	}
	if (numberOfRotations == 0) {
		return spot;
	}
	var spots = ['north', 'east', 'south', 'west'];
	var currentSpotIndex = spots.index (spot);
	return spots [__mod__ (currentSpotIndex + numberOfRotations, 4)];
};
export var getRelativeLocationFromSpot = function (usersSpot, spotToGetLocationFor) {
	var spots = ['north', 'west', 'south', 'east'];
	var locations = ['bottom', 'left', 'top', 'right'];
	var usersSpotIndex = spots.index (usersSpot);
	var spotToGetIndex = spots.index (spotToGetLocationFor);
	var difference = usersSpotIndex - spotToGetIndex;
	if (difference < 0) {
		difference += 4;
	}
	return locations [difference];
};
export var getBiddingObjRelative = function (biddingObjAbsolute, spot) {
	var biddingRelative = dict ({});
	for (var [key, value] of biddingObjAbsolute.py_items ()) {
		biddingRelative [getRelativeLocationFromSpot (spot, key)] = value;
	}
	return biddingRelative;
};
export var getBiddingObjAbsolute = function (biddingAbsolute, seating) {
	var biddingObjAbsolute = dict ([['north', []], ['south', []], ['east', []], ['west', []]]);
	for (var bid of biddingAbsolute) {
		var direction = '';
		for (var [key, value] of seating.py_items ()) {
			if (bid [0] == value) {
				var direction = key;
				break;
			}
		}
		biddingObjAbsolute [direction].append (bid [1]);
	}
	return biddingObjAbsolute;
};
export var getBiddableSuits = function (hand) {
	var biddableSuits = [];
	var suitNames = ['clubs', 'diamonds', 'hearts', 'spades'];
	var biddableSuitLengths = dict ([['clubs', 4], ['diamonds', 4], ['hearts', 5], ['spades', 5]]);
	var suitCounts = getSuitCountsFromHand (hand);
	for (var suitName of suitNames) {
		if (suitCounts [suitName] >= biddableSuitLengths [suitName]) {
			biddableSuits.append (suitName);
		}
	}
	return biddableSuits;
};
export var getWeightedSuitScore = function (hand, clientPointCountingConvention) {
	var valueOfAdditionalLength = 2;
	var weightedSuitScores = dict ([['clubs', 0], ['diamonds', 0], ['hearts', 0], ['spades', 0]]);
	var pointsInEachSuit = getHighCardPointValuesInEachSuit (hand, clientPointCountingConvention);
	var suitCounts = getSuitCountsFromHand (hand);
	print ('{}{}'.format (pointsInEachSuit));
	print ('{}{}'.format (suitCounts));
	for (var [suit, suitCount] of suitCounts.py_items ()) {
		if (suitCount < 3) {
			weightedSuitScores [suit] = pointsInEachSuit [suit];
		}
		else {
			weightedSuitScores [suit] = pointsInEachSuit [suit] + (suitCount - 3) * valueOfAdditionalLength;
		}
	}
	return weightedSuitScores;
};
export var getShouldReturnNoTrump = function (weightedSuitScores, biddableSuits) {
	var differenceThreshold = 3;
	if (len (biddableSuits) == 0) {
		var highestSuit = null;
		var secondHighestSuit = null;
		var highestSuitValue = 0;
		var secondHighestSuitValue = 0;
		for (var [suit, weightedValue] of weightedSuitScores.py_items ()) {
			if (weightedValue > highestSuitValue) {
				var highestSuitValue = weightedValue;
				var highestSuit = suit;
			}
		}
		for (var [suit, weightedValue] of weightedSuitScores.py_items ()) {
			if (weightedValue > secondHighestSuitValue && suit != highestSuit) {
				var secondHighestSuitValue = weightedValue;
				var secondHighestSuit = suit;
			}
		}
		if (abs (highestSuitValue - secondHighestSuitValue) < differenceThreshold) {
			return true;
		}
	}
	return false;
};
export var getStrongestSuit = function (hand, biddingRelative, clientPointCountingConvention) {
	var possibleOutputs = dict ([['club', 'club'], ['diamond', 'diamond'], ['heart', 'heart'], ['spade', 'spade'], ['noTrump', 'no trump']]);
	var biddableSuits = getBiddableSuits (hand);
	var weightedSuitScores = getWeightedSuitScore (hand, clientPointCountingConvention);
	var shouldReturnNoTrump = getShouldReturnNoTrump (weightedSuitScores, biddableSuits);
	if (shouldReturnNoTrump) {
		return 'no trump';
	}
	else {
		// pass;
	}
	var suitsMentionedByOpponents = getSuitsMentionedByOpponents (biddingRelative);
	var leftOpeningSuit = biddingRelative ['left'] [0];
	var rightOpeningSuit = biddingRelative ['right'] [0];
	var suitWithMostPoints = rightOpeningSuit;
	var suitToReturn = null;
	if (re.search ('pass', biddingRelative ['top'] [0], re.IGNORECASE)) {
		var highCardPointValuesInEachSuitLocal = getHighCardPointValuesInEachSuit (hand, clientPointCountingConvention);
		while (suitWithMostPoints != rightOpeningSuit && suitWithMostPoints != leftOpeningSuit) {
			var suitWithMostPoints = max (highCardPointValuesInEachSuitLocal, __kwargtrans__ ({key: highCardPointValuesInEachSuitLocal.py_get}));
			highCardPointValuesInEachSuitLocal.py_pop (suitWithMostPoints, null);
		}
	}
	else {
		// pass;
	}
	return suitToReturn;
};
export var getSuitsMentionedByOpponents = function (biddingRelative) {
	var mentioned = dict ([['clubs', false], ['diamonds', false], ['hearts', false], ['spades', false], ['noTrump', false]]);
	var handsToCheck = ['left', 'right'];
	for (var handToCheck of handsToCheck) {
		for (var bid of biddingRelative [handToCheck]) {
			for (var [key, suit] of autoBid.suits.py_items ()) {
				if (re.search (suit, bid, re.IGNORECASE)) {
					mentioned [key] = true;
				}
			}
		}
	}
	return mentioned;
};
export var getCanDouble = function (biddingRelative) {
	if (len (biddingRelative ['left']) == 0 && len (biddingRelative ['right']) == 0) {
		return false;
	}
	return true;
};
export var getShouldDouble = function (scoring, biddingRelative, estimatedPoints, hand, currentActualBid) {
	return false;
};
export var getSuitNameFromCardAsNumber = function (cardAsNumber) {
	if (cardAsNumber >= 0 && cardAsNumber <= 12) {
		return 'clubs';
	}
	else if (cardAsNumber >= 13 && cardAsNumber <= 25) {
		return 'diamonds';
	}
	else if (cardAsNumber >= 26 && cardAsNumber <= 38) {
		return 'hearts';
	}
	else if (cardAsNumber >= 39 && cardAsNumber <= 51) {
		return 'spades';
	}
	else {
		return null;
	}
};
export var getCurrentContractBid = function (biddingAbsolute) {
	for (var bid of py_reversed (biddingAbsolute)) {
		if (len (bid) <= 0) {
			return null;
		}
		if (re.search ('pass', bid [1], re.IGNORECASE) === null && re.search ('double', bid [1], re.IGNORECASE) === null) {
			return bid;
		}
	}
};
export var handlePartnerDouble = function (hand, biddingAbsolute, biddingRelative, totalPoints, clientPointCountingConvention) {
	if (len (biddingRelative ['top']) == 1 && re.search ('Double', biddingRelative ['top'] [0], re.IGNORECASE)) {
		var mustBid = re.search ('pass', biddingAbsolute [-(1)] [1], re.IGNORECASE);
		if (totalPoints < 6 && mustBid === null) {
			return 'Pass';
		}
		else {
			return getStrongestSuit (hand, biddingRelative, clientPointCountingConvention);
		}
	}
	else {
		return 'Pass';
	}
};
export var getHighCardPointValuesInEachSuit = function (hand, clientPointCountingConvention) {
	var conventionToUse = 'hcp';
	if (re.search ('alternative', clientPointCountingConvention, re.IGNORECASE)) {
		var conventionToUse = 'alternative';
	}
	var highCardPointValuesInEachSuit = dict ([['clubs', 0], ['diamonds', 0], ['hearts', 0], ['spades', 0]]);
	for (var suit of hand) {
		var suitName = '';
		for (var cardAsNumber of suit) {
			if (len (suit) > 0) {
				var suitName = getSuitNameFromCardAsNumber (cardAsNumber);
				var cardValue = __mod__ (cardAsNumber, 13);
				if (cardValue == 12) {
					highCardPointValuesInEachSuit [suitName] += highCardPointValues [conventionToUse] ['ace'];
				}
				if (cardValue == 11) {
					highCardPointValuesInEachSuit [suitName] += highCardPointValues [conventionToUse] ['king'];
				}
				if (cardValue == 10) {
					highCardPointValuesInEachSuit [suitName] += highCardPointValues [conventionToUse] ['queen'];
				}
				if (cardValue == 9) {
					highCardPointValuesInEachSuit [suitName] += highCardPointValues [conventionToUse] ['jack'];
				}
				if (cardValue == 8 && conventionToUse == 'alternative') {
					highCardPointValuesInEachSuit [suitName] += highCardPointValues [conventionToUse] ['ten'];
				}
			}
		}
	}
	return highCardPointValuesInEachSuit;
};
export var getSuitCountsFromHand = function (hand) {
	var suitCounts = dict ([['clubs', 0], ['diamonds', 0], ['hearts', 0], ['spades', 0]]);
	for (var suit of hand) {
		if (len (suit) == 0) {
			continue;
		}
		var suitName = getSuitNameFromCardAsNumber (suit [0]);
		suitCounts [suitName] = len (suit);
	}
	return suitCounts;
};
export var getHighCardPoints = function (hand, clientPointCountingConvention) {
	try {
		if (hand == null || clientPointCountingConvention == null) {
			return -(1);
		}
		var pointCountsToUse = highCardPointValues ['hcp'];
		if (clientPointCountingConvention.lower () == 'alternative') {
			var pointCountsToUse = highCardPointValues ['alternative'];
		}
		var points = 0;
		for (var i = 0; i < len (hand); i++) {
			var suit = hand [i];
			for (var j = 0; j < len (suit); j++) {
				var cardValue = __mod__ (suit [j], 13);
				if (cardValue == 8 && clientPointCountingConvention.lower () == 'alternative' && len (suit) >= suitLengthRequiredToCount ['ten']) {
					points += pointCountsToUse ['ten'];
				}
				if (cardValue == 9 && len (suit) >= suitLengthRequiredToCount ['jack']) {
					points += pointCountsToUse ['jack'];
				}
				if (cardValue == 10 && len (suit) >= suitLengthRequiredToCount ['queen']) {
					points += pointCountsToUse ['queen'];
				}
				if (cardValue == 11 && len (suit) >= suitLengthRequiredToCount ['king']) {
					points += pointCountsToUse ['king'];
				}
				if (cardValue == 12) {
					points += pointCountsToUse ['ace'];
				}
			}
		}
		return points;
	}
	catch (__except0__) {
		return -(2);
	}
};
export var getDistributionPoints = function (hand, biddingAbsolute, biddingRelative, seatingRelative, suitCounts) {
	if (hand == null) {
		return -(1);
	}
	var distributionPoints = -(1);
	var hasPartnerOpened = getHasPartnerOpened (biddingAbsolute, seatingRelative, seatingRelative ['bottom']);
	getShouldCalculateRespondingPoints (biddingAbsolute);
	if (hasPartnerOpened) {
		var partnersMentionedSuits = getPartnersMentionedSuits (biddingRelative ['top']);
		var distributionPoints = getRespondingDistributionPoints (suitCounts, partnersMentionedSuits);
	}
	else {
		var distributionPoints = getOpeningDistributionPoints (suitCounts);
	}
	return distributionPoints;
};
export var getPartnersMentionedSuits = function (partnersBids) {
	// pass;
};
export var getShouldCalculateRespondingPoints = function (biddingAbsolute) {
	// pass;
};
export var getRespondingDistributionPoints = function (suitCounts, partnersMentionedSuits) {
	return -(1);
};
export var getOpeningDistributionPoints = function (suitCounts) {
	var points = 0;
	for (var [suit, suitCount] of suitCounts.py_items ()) {
		if (suitCount == 0) {
			points += distributionPointValues ['shortness'] ['void'];
		}
		else if (suitCount == 1) {
			points += distributionPointValues ['shortness'] ['singleton'];
		}
		else if (suitCount == 2) {
			points += distributionPointValues ['shortness'] ['doubleton'];
		}
		else if (suitCount > 4) {
			points += suitCounts [suit] - 4;
		}
	}
	return points;
};
export var getLocationAfterRotationsAround = function (location, numberOfRotations) {
	var locations = ['top', 'right', 'bottom', 'left'];
	var indexOfLocation = locations.index (location);
	return locations [__mod__ (indexOfLocation + numberOfRotations, 4)];
};
export var getCurrentContractBidFromBidding = function (biddingAbsolute) {
	for (var bid of py_reversed (biddingAbsolute)) {
		if (!(re.search ('pass', bid [1], re.IGNORECASE)) && !(re.search ('double', bid [1], re.IGNORECASE))) {
			return bid [1];
		}
	}
};
export var getWasPlayersNthBidAJumpshift = function (username, biddingAbsolute, nthBid) {
	var indexOfNthBid = -(1);
	var nthBidCount = 1;
	for (var i = 0; i < len (biddingAbsolute); i++) {
		var bid = biddingAbsolute [i];
		if (bid [0] == username) {
			if (nthBidCount == nthBid) {
				var indexOfNthBid = i;
				break;
			}
			nthBidCount += 1;
		}
	}
	if (indexOfNthBid == -(1)) {
		var __except0__ = Exception ('Invalid nthBid to getWasPlayerForcedToBidAnNthLevelBidAsTheirNthBid()');
		__except0__.__cause__ = null;
		throw __except0__;
	}
	var bidsUpToUsersNthBid = biddingAbsolute.__getslice__ (0, indexOfNthBid, 1);
	var currentContractBid = getCurrentContractBidFromBidding (bidsUpToUsersNthBid);
	return getIsJumpshift (currentContractBid, biddingAbsolute [indexOfNthBid] [1]);
};
export var getWasFirstOpeningBidANthLevelBid = function (biddingAbsolute, bidLevel) {
	try {
		var bidLevels = dict ([tuple ([1, 'one']), tuple ([2, 'two']), tuple ([3, 'three']), tuple ([4, 'four']), tuple ([5, 'five']), tuple ([6, 'six']), tuple ([7, 'seven'])]);
		for (var bid of biddingAbsolute) {
			if (!(re.search ('pass', bid [1], re.IGNORECASE)) && !(re.search ('double', bid [1], re.IGNORECASE))) {
				if (re.search (bidLevels [bidLevel], bid [1], re.IGNORECASE)) {
					return bid [0];
				}
				return false;
			}
		}
		return false;
	}
	catch (__except0__) {
		return null;
	}
};
export var getUsersFirstContractBid = function (username, biddingAbsolute) {
	try {
		var firstBid = null;
		var count = 0;
		for (var bid of biddingAbsolute) {
			if (bid [0] == username) {
				if (count == 0) {
					var firstBid = bid [1];
				}
				if (!(re.search ('pass', bid [1], re.IGNORECASE)) && !(re.search ('double', bid [1], re.IGNORECASE))) {
					return bid [1];
				}
				count += 1;
			}
		}
		return firstBid;
	}
	catch (__except0__) {
		return null;
	}
};
export var getIsUsernamesFirstContractBidTheFirstContractBid = function (username, biddingAbsolute) {
	for (var bid of biddingAbsolute) {
		var isContractBid = getIsBidAContractBid (bid [1]);
		if (isContractBid) {
			if (bid [0] == username) {
				return true;
			}
			return false;
		}
	}
	return false;
};
export var getIsBidAContractBid = function (bid) {
	return !(re.search ('double', bid, re.IGNORECASE)) && !(re.search ('pass', bid, re.IGNORECASE));
};
export var getPartnersCurrentContractBidFromBidding = function (username, biddingAbsolute, seatingRelative) {
	var usernamesPartner = getUsernamesPartner (username, seatingRelative);
	var indexOfPartnersLastBid = getIndexOfNthBid (usernamesPartner, biddingAbsolute, -(1));
	var biddingUpToPartnersLastBid = biddingAbsolute.__getslice__ (0, indexOfPartnersLastBid, 1);
	for (var bid of py_reversed (biddingUpToPartnersLastBid)) {
		if (!(re.search ('pass', bid [1], re.IGNORECASE)) && !(re.search ('double', bid [1], re.IGNORECASE))) {
			return bid [1];
		}
	}
	return null;
};
export var getIsBidGameBid = function (bid) {
	try {
		if (re.match ('three no trump', bid, re.IGNORECASE)) {
			return true;
		}
		var indexOfBid = autoBid.contracts.index (bid);
		var indexOfThreeHearts = autoBid.contracts.index ('Four Heart');
		if (indexOfBid >= indexOfThreeHearts) {
			return true;
		}
	}
	catch (__except0__) {
		return null;
	}
	return false;
};
export var getIndexDifferenceOfBids = function (bid1, bid2) {
	try {
		if (re.search ('pass', bid1, re.IGNORECASE) || re.search ('double', bid1, re.IGNORECASE) || re.search ('pass', bid2, re.IGNORECASE) || re.search ('double', bid2, re.IGNORECASE)) {
			return 0;
		}
		var bid1Index = autoBid.contracts.index (bid1);
		var bid2Index = autoBid.contracts.index (bid2);
		return abs (bid2Index - bid1Index);
	}
	catch (__except0__) {
		var __except1__ = py_TypeError ('Error in getIndexDifferenceOfBids;  Probably incorrect parameter passed in.');
		__except1__.__cause__ = null;
		throw __except1__;
	}
};
export var getHasSomeoneOpenedTwoClubs = function (biddingAbsolute, biddingRelative, seatingRelative) {
	var falseTuple = tuple ([false, null]);
	var shouldContinue = false;
	var twoClubBid = null;
	for (var [location, py_values] of biddingRelative.py_items ()) {
		if (len (biddingRelative [location]) == 0) {
			continue;
		}
		var firstBid = biddingRelative [location] [0];
		if (re.search ('two club', firstBid, re.IGNORECASE)) {
			var twoClubBid = [seatingRelative [location], firstBid];
			var shouldContinue = true;
			break;
		}
	}
	if (shouldContinue === true) {
		var indexOfTwoClubBid = biddingAbsolute.index (twoClubBid);
		var hasSomeoneOpenedBefore = getHasSomeOneOpenedBefore (indexOfTwoClubBid, biddingAbsolute);
		if (hasSomeoneOpenedBefore === false) {
			return tuple ([true, twoClubBid [0]]);
		}
	}
	return falseTuple;
};
export var getPlayerHasOnlyPassed = function (playerBids) {
	for (var bid of playerBids) {
		if (!(re.search ('pass', bid, re.IGNORECASE))) {
			return false;
		}
	}
	return true;
};
export var getHasOtherTeamMentionedSameSuit = function (location, usersBid, biddingAbsolute, seatingRelative) {
	try {
		var usernamesOpponents = getUsernamesOpponents (location, seatingRelative);
		var indexOfUserBid = autoBid.contracts.index (usersBid);
		for (var i = 0; i < len (biddingAbsolute); i++) {
			var bid = biddingAbsolute [i];
			if (!(getIsBidAContractBid (bid [1]))) {
				continue;
			}
			var indexOfBid = autoBid.contracts.index (bid [1]);
			print ('{}{}'.format (indexOfBid));
			if (indexOfUserBid > indexOfBid && __mod__ (abs (indexOfBid - indexOfUserBid), 5) == 0) {
				if (__in__ (bid [0], usernamesOpponents)) {
					return true;
				}
			}
		}
		return false;
	}
	catch (__except0__) {
		return false;
	}
};
export var getUsernamesOpponents = function (location, seatingRelative) {
	try {
		var leftUser = seatingRelative [getLocationAfterRotationsAround (location, 1)];
		var rightUser = seatingRelative [getLocationAfterRotationsAround (location, -(1))];
		return [leftUser, rightUser];
	}
	catch (__except0__) {
		return [];
	}
};
export var getHasTakenPartnerOutOfGameBid = function (username, biddingRelative, seatingRelative) {
	for (var bids of biddingRelative ['top']) {
		// pass;
	}
	return false;
};
export var getHasPartnerOpenedNoTrump = function (location, partnersLocation, biddingRelative, biddingAbsolute, seatingRelative) {
	if (len (biddingRelative [partnersLocation]) == 0) {
		return false;
	}
	if (re.search ('trump', biddingRelative [partnersLocation] [0], re.IGNORECASE)) {
		var partnersOneNoTrumpBidIndex = -(1);
		var locationsLastBidIndex = -(1);
		for (var i = 0; i < len (biddingAbsolute); i++) {
			var bid = biddingAbsolute [i];
			if (bid [0] == seatingRelative [partnersLocation] && re.search ('trump', bid [1], re.IGNORECASE)) {
				var partnersOneNoTrumpBidIndex = i;
			}
			if (bid [0] == seatingRelative [location]) {
				var locationsLastBidIndex = i;
			}
		}
		if (partnersOneNoTrumpBidIndex < locationsLastBidIndex) {
			return true;
		}
		return false;
	}
};
export var getBiddingAbsoluteFromBiddingObjAndSeatingRelative = function (biddingRelative, seatingRelative) {
	try {
		print ('{}{}'.format (biddingRelative));
		print ('{}{}'.format (seatingRelative));
		var locations = getEstimatedPoints.locations;
		var locationOrder = [locations ['left'], locations ['top'], locations ['right'], locations ['bottom']];
		var dealer = getDealerLocation (biddingRelative);
		var locationOrderToUse = locationOrder;
		if (dealer != locations ['left']) {
			var index = locationOrder.index (locations [dealer]);
			var locationOrderToUse = locationOrder.__getslice__ (index, null, 1) + locationOrder.__getslice__ (0, index, 1);
		}
		var bids = [];
		for (var i = 0; i < len (biddingRelative [dealer]); i++) {
			for (var j = 0; j < len (locationOrderToUse); j++) {
				var locationToGet = locationOrderToUse [j];
				try {
					var bidInQuestion = biddingRelative [locationToGet] [i];
				}
				catch (__except0__) {
					break;
				}
				if (bidInQuestion !== null) {
					bids.append ([seatingRelative [locationToGet], bidInQuestion]);
				}
				else {
					break;
				}
			}
		}
		if (re.search ('bottom', bids [-(1)] [0], re.IGNORECASE)) {
			var bids = bids.__getslice__ (0, -(1), 1);
		}
		return bids;
	}
	catch (__except0__) {
		print ('error-----------');
		return [];
	}
};
export var getDealerLocation = function (biddingRelative) {
	try {
		var currentMax = 0;
		var dealer = null;
		var locations = getEstimatedPoints.locations;
		var locationOrder = [locations ['bottom'], locations ['left'], locations ['top'], locations ['right']];
		for (var location of locationOrder) {
			var lengthOfLocationsBidding = len (biddingRelative [location]);
			if (lengthOfLocationsBidding > currentMax) {
				var currentMax = lengthOfLocationsBidding;
				var dealer = location;
			}
		}
		return dealer;
	}
	catch (__except0__) {
		return null;
	}
};
export var getHandFromHandDictionary = function (handsDictionary) {
	var starts = dict ([['clubs', 0], ['diamonds', 13], ['hearts', 26], ['spades', 39]]);
	var charValues = dict ([['A', 12], ['K', 11], ['Q', 10], ['J', 9], ['T', 8], ['9', 7], ['8', 6], ['7', 5], ['6', 4], ['5', 3], ['4', 2], ['3', 1], ['2', 0]]);
	var hand = [];
	for (var [suitName, suitString] of handsDictionary.py_items ()) {
		var newSuitArray = [];
		for (var character of suitString) {
			newSuitArray.append (charValues [character] + starts [suitName]);
		}
		hand.append (newSuitArray);
	}
	return hand;
};

//# sourceMappingURL=helpers.map