// Transcrypt'ed from Python, 2021-04-30 09:26:56
var getEstimatedPoints = {};
var getEstimatedSuitCounts = {};
var helpers = {};
var math = {};
var re = {};
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import * as __module_re__ from './re.js';
__nest__ (re, '', __module_re__);
import * as __module_math__ from './math.js';
__nest__ (math, '', __module_math__);
import * as __module_getEstimatedPoints__ from './getEstimatedPoints.js';
__nest__ (getEstimatedPoints, '', __module_getEstimatedPoints__);
import * as __module_getEstimatedSuitCounts__ from './getEstimatedSuitCounts.js';
__nest__ (getEstimatedSuitCounts, '', __module_getEstimatedSuitCounts__);
import * as __module_helpers__ from './helpers.js';
__nest__ (helpers, '', __module_helpers__);
var __name__ = '__main__';
export var suits = dict ([['clubs', 'club'], ['diamonds', 'diamond'], ['hearts', 'heart'], ['spades', 'spade'], ['noTrump', 'trump']]);
export var contracts = ['One Club', 'One Diamond', 'One Heart', 'One Spade', 'One No Trump', 'Two Club', 'Two Diamond', 'Two Heart', 'Two Spade', 'Two No Trump', 'Three Club', 'Three Diamond', 'Three Heart', 'Three Spade', 'Three No Trump', 'Four Club', 'Four Diamond', 'Four Heart', 'Four Spade', 'Four No Trump', 'Five Club', 'Five Diamond', 'Five Heart', 'Five Spade', 'Five No Trump', 'Six Club', 'Six Diamond', 'Six Heart', 'Six Spade', 'Six No Trump', 'Seven Club', 'Seven Diamond', 'Seven Heart', 'Seven Spade', 'Seven No Trump'];
export var flatten = (function __lambda__ (t) {
	return (function () {
		var __accu0__ = [];
		for (var sublist of t) {
			for (var item of sublist) {
				__accu0__.append (item);
			}
		}
		return __accu0__;
	}) ();
});
export var clientPointCountingConvention = 'hcp';
export var spot = 'west';
export var seating = dict ([['north', 'Adam'], ['east', 'Dan'], ['south', 'Ann'], ['west', 'Andrew']]);
export var scoring = dict ([['northSouth', dict ([['aboveTheLine', 0], ['belowTheLine', 0], ['totalBelowTheLineScore', 0], ['isVulnerable', false], ['vulnerableTransitionIndex', null]])], ['eastWest', dict ([['aboveTheLine', 0], ['belowTheLine', 0], ['totalBelowTheLineScore', 0], ['isVulnerable', false], ['vulnerableTransitionIndex', null]])]]);
export var bids = [['Adam', 'Two No Trump'], ['Dan', 'Double'], ['Ann', 'Double'], ['Andrew', 'Three Club']];
export var hand = [[0, 1, 7, 8, 12], [13, 18, 19], [29, 30, 32], [40, 42]];
export var autoBid = function (biddingAbsolute, hand, scoring, seatingInput, spot, clientPointCountingConvention) {
	seating ['north'] = seatingInput ['north'];
	seating ['south'] = seatingInput ['south'];
	seating ['east'] = seatingInput ['east'];
	seating ['west'] = seatingInput ['west'];
	var isFirstBid = len (biddingAbsolute) < 4;
	var partnerHasBid = len (biddingAbsolute) >= 2;
	var currentContractBid = helpers.getCurrentContractBid (biddingAbsolute);
	var analyzingPlayerSuitCounts = helpers.getSuitCountsFromHand (hand);
	var highCardPointValuesInEachSuit = helpers.getHighCardPointValuesInEachSuit (hand, clientPointCountingConvention);
	var biddingObjAbsolute = helpers.getBiddingObjAbsolute (biddingAbsolute, seating);
	var biddingRelative = helpers.getBiddingObjRelative (biddingObjAbsolute, spot);
	var biddingHistory = helpers.getBiddingHistory (biddingAbsolute);
	var seatingRelative = helpers.getSeatingRelative (seating, spot);
	var estimatedPoints = getEstimatedPoints.getEstimatedPoints (biddingRelative, biddingAbsolute, seatingRelative);
	var estimatedSuitCounts = getEstimatedSuitCounts.getEstimatedSuitCounts (biddingRelative, biddingAbsolute, seatingRelative);
	var partnersBids = biddingRelative ['top'];
	print ('{}{}'.format (estimatedPoints));
	var highCardPoints = helpers.getHighCardPoints (hand, clientPointCountingConvention);
	var distributionPoints = helpers.getDistributionPoints (hand, biddingAbsolute, biddingRelative, seatingRelative, analyzingPlayerSuitCounts);
	var totalPoints = highCardPoints + distributionPoints;
	var canDouble = helpers.getCanDouble (biddingRelative);
	var shouldDouble = helpers.getShouldDouble (scoring, biddingRelative, estimatedPoints, hand, currentContractBid);
	if (shouldDouble === true) {
		return 'Double';
	}
	if (re.search ('two club', biddingRelative ['top'] [0], re.IGNORECASE) && re.search ('pass', biddingRelative ['left'] [0], re.IGNORECASE)) {
		var openDistributionPoints = helpers.getOpeningDistributionPoints (analyzingPlayerSuitCounts);
		return helpers.getTwoClubResponse (hand, biddingRelative, seatingRelative, highCardPoints + openDistributionPoints, currentContractBid, clientPointCountingConvention);
	}
	var result = helpers.handlePartnerDouble (hand, biddingAbsolute, biddingRelative, totalPoints, clientPointCountingConvention);
	if (result !== null) {
		return result;
	}
	if (totalPoints < 13 && isFirstBid) {
		return 'Pass';
	}
	var outgoingBid = 'Recommended Bid Goes here';
	return outgoingBid;
};

//# sourceMappingURL=autoBid.map