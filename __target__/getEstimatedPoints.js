// Transcrypt'ed from Python, 2021-05-03 21:20:43
var helpers = {};
var re = {};
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import * as __module_helpers__ from './helpers.js';
__nest__ (helpers, '', __module_helpers__);
import * as __module_re__ from './re.js';
__nest__ (re, '', __module_re__);
var __name__ = 'getEstimatedPoints';
export var locations = dict ([['bottom', 'bottom'], ['left', 'left'], ['right', 'right'], ['top', 'top']]);
export var PARTNER_BIDS_FIRST_AND_PLAYER_PASSES_MAX = 5;
export var PARTNER_BIDS_FIRST_AND_PLAYER_PASSES_MIN = 0;
export var PARTNER_BIDS_FIRST_AND_PLAYER_DOUBLES_MAX = 18;
export var PARTNER_BIDS_FIRST_AND_PLAYER_DOUBLES_MIN = 13;
export var PARTNER_BIDS_FIRST_AND_PLAYER_BIDS_SUIT_MAX = 12;
export var PARTNER_BIDS_FIRST_AND_PLAYER_BIDS_SUIT_MIN = 6;
export var PARTNER_BIDS_FIRST_AND_PLAYER_BIDS_NT_IS_JUMPSHIFT_MAX = -(1);
export var PARTNER_BIDS_FIRST_AND_PLAYER_BIDS_NT_IS_JUMPSHIFT_MIN = 13;
export var PARTNER_BIDS_FIRST_AND_PLAYER_BIDS_NT_IS_NOT_JUMPSHIFT_MAX = 12;
export var PARTNER_BIDS_FIRST_AND_PLAYER_BIDS_NT_IS_NOT_JUMPSHIFT_MIN = 6;
export var PARTNER_PASSES_FIRST_AND_PLAYER_PASSES_MAX = 12;
export var PARTNER_PASSES_FIRST_AND_PLAYER_PASSES_MIN = 0;
export var PARTNER_PASSES_FIRST_AND_PLAYER_DOUBLES_MAX = 18;
export var PARTNER_PASSES_FIRST_AND_PLAYER_DOUBLES_MIN = 13;
export var PARTNER_PASSES_FIRST_AND_PLAYER_BIDS_SUIT_MAX = 18;
export var PARTNER_PASSES_FIRST_AND_PLAYER_BIDS_SUIT_MIN = 13;
export var PARTNER_BIDS_FIRST_AND_PLAYER_BIDS_SUIT_IS_JUMPSHIFT_MAX = -(1);
export var PARTNER_BIDS_FIRST_AND_PLAYER_BIDS_SUIT_IS_JUMPSHIFT_MIN = 13;
export var PARTNER_BIDS_FIRST_AND_PLAYER_BIDS_SUIT_IS_NOT_JUMPSHIFT_MAX = 12;
export var PARTNER_BIDS_FIRST_AND_PLAYER_BIDS_SUIT_IS_NOT_JUMPSHIFT_MIN = 6;
export var PARTNER_PASSES_FIRST_AND_PLAYER_BIDS_NT_MAX = 18;
export var PARTNER_PASSES_FIRST_AND_PLAYER_BIDS_NT_MIN = 16;
export var IS_TEAMS_FIRST_BID_AND_PLAYER_PASSES_MAX = 13;
export var IS_TEAMS_FIRST_BID_AND_PLAYER_PASSES_MIN = 0;
export var IS_TEAMS_FIRST_BID_AND_PLAYER_PASSES_FIRST_OPENS_SECOND_MIN = 10;
export var IS_TEAMS_FIRST_BID_AND_PLAYER_PASSES_FIRST_OPENS_SECOND_MAX = 13;
export var IS_TEAMS_FIRST_BID_AND_PLAYER_DOUBLES_MAX = 18;
export var IS_TEAMS_FIRST_BID_AND_PLAYER_DOUBLES_MIN = 13;
export var IS_TEAMS_FIRST_BID_AND_PLAYER_BIDS_SUIT_MAX = 18;
export var IS_TEAMS_FIRST_BID_AND_PLAYER_BIDS_SUIT_MIN = 13;
export var IS_TEAMS_FIRST_BID_AND_PLAYER_BIDS_NT_MAX = 18;
export var IS_TEAMS_FIRST_BID_AND_PLAYER_BIDS_NT_MIN = 16;
export var SPECIAL_WEAK_TWO_MAX = 12;
export var SPECIAL_WEAK_TWO_MIN = 9;
export var SPECIAL_WEAK_THREE_MAX = 12;
export var SPECIAL_WEAK_THREE_MIN = 7;
export var SPECIAL_WEAK_TWO_CLUBS_MAX = -(1);
export var SPECIAL_WEAK_TWO_CLUBS_MIN = 18;
export var PASS_FIRST_NT_SECOND_ROUND_MAX = 12;
export var PASS_FIRST_NT_SECOND_ROUND_MIN = 6;
export var PASS_FIRST_BID_SECOND_ROUND_MAX = 12;
export var PASS_FIRST_BID_SECOND_ROUND_MIN = 8;
export var PASS_FIRST_DOUBLE_SECOND_ROUND_MAX = 12;
export var PASS_FIRST_DOUBLE_SECOND_ROUND_MIN = 8;
export var RESPONDING_BID_SUIT_FIRST_ROUND_MAX = 12;
export var RESPONDING_BID_SUIT_FIRST_ROUND_MIN = PARTNER_BIDS_FIRST_AND_PLAYER_PASSES_MAX + 1;
export var RESPONDING_DOUBLE_FIRST_ROUND_MAX = 12;
export var RESPONDING_DOUBLE_FIRST_ROUND_MIN = 10;
export var RESPONDING_JUMPSHIFT_PASS_FIRST_ROUND_MAX = 12;
export var RESPONDING_JUMPSHIFT_PASS_FIRST_ROUND_MIN = 10;
export var RESPONDING_NO_JUMPSHIFT_MAX = 12;
export var RESPONDING_NO_JUMPSHIFT_MIN = 6;
export var RESPONDING_NO_JUMPSHIFT_NT_MAX = RESPONDING_NO_JUMPSHIFT_MAX;
export var RESPONDING_NO_JUMPSHIFT_NT_MIN = RESPONDING_NO_JUMPSHIFT_MIN;
export var OPENING_TWO_CLUB_FIRST_ROUND_MAX = 25;
export var OPENING_TWO_CLUB_FIRST_ROUND_MIN = 18;
export var OPENING_WEAK_TWO_NO_PRIOR_OPENERS_MAX = 12;
export var OPENING_WEAK_TWO_NO_PRIOR_OPENERS_MIN = 10;
export var OPENING_WEAK_THREE_NO_PRIOR_OPENERS_MAX = 10;
export var OPENING_WEAK_THREE_NO_PRIOR_OPENERS_MIN = 7;
export var OPENING_WEAK_TWO_AFTER_OPENERS_MAX = IS_TEAMS_FIRST_BID_AND_PLAYER_BIDS_SUIT_MAX;
export var OPENING_WEAK_TWO_AFTER_OPENERS_MIN = OPENING_WEAK_TWO_NO_PRIOR_OPENERS_MIN;
export var OPENING_WEAK_THREE_AFTER_OPENERS_MAX = IS_TEAMS_FIRST_BID_AND_PLAYER_BIDS_SUIT_MAX;
export var OPENING_WEAK_THREE_AFTER_OPENERS_MIN = OPENING_WEAK_THREE_NO_PRIOR_OPENERS_MIN;
export var py_values = dict ([['passFirstBidSecond', dict ([['isJumpshift', dict ([['partnerHasOpened', dict ([['min', RESPONDING_JUMPSHIFT_PASS_FIRST_ROUND_MIN], ['max', RESPONDING_JUMPSHIFT_PASS_FIRST_ROUND_MAX]])], ['partnerHasNotOpened', dict ([['min', SPECIAL_WEAK_THREE_MIN], ['max', SPECIAL_WEAK_TWO_CLUBS_MAX]])]])]])], ['isTeamsFirstBid', dict ([['playerPasses', dict ([['min', IS_TEAMS_FIRST_BID_AND_PLAYER_PASSES_MIN], ['max', IS_TEAMS_FIRST_BID_AND_PLAYER_PASSES_MAX]])], ['playerDoubles', dict ([['min', IS_TEAMS_FIRST_BID_AND_PLAYER_DOUBLES_MIN], ['max', IS_TEAMS_FIRST_BID_AND_PLAYER_DOUBLES_MAX]])], ['playerBidsSuit', dict ([['min', IS_TEAMS_FIRST_BID_AND_PLAYER_BIDS_SUIT_MIN], ['max', IS_TEAMS_FIRST_BID_AND_PLAYER_BIDS_SUIT_MAX]])], ['playerBidsNoTrump', dict ([['min', IS_TEAMS_FIRST_BID_AND_PLAYER_BIDS_NT_MIN], ['max', IS_TEAMS_FIRST_BID_AND_PLAYER_BIDS_NT_MAX]])], ['playerPassesFirstOpensSecond', dict ([['min', IS_TEAMS_FIRST_BID_AND_PLAYER_PASSES_FIRST_OPENS_SECOND_MIN], ['max', IS_TEAMS_FIRST_BID_AND_PLAYER_PASSES_FIRST_OPENS_SECOND_MAX]])]])], ['partnerPassesFirst', dict ([['playerPasses', dict ([['min', PARTNER_PASSES_FIRST_AND_PLAYER_PASSES_MIN], ['max', PARTNER_PASSES_FIRST_AND_PLAYER_PASSES_MAX]])], ['playerDoubles', dict ([['min', PARTNER_PASSES_FIRST_AND_PLAYER_DOUBLES_MIN], ['max', PARTNER_PASSES_FIRST_AND_PLAYER_DOUBLES_MAX]])], ['playerBidsSuit', dict ([['min', PARTNER_PASSES_FIRST_AND_PLAYER_BIDS_SUIT_MIN], ['max', PARTNER_PASSES_FIRST_AND_PLAYER_BIDS_SUIT_MAX]])], ['playerBidsNoTrump', dict ([['min', PARTNER_PASSES_FIRST_AND_PLAYER_BIDS_NT_MIN], ['max', PARTNER_PASSES_FIRST_AND_PLAYER_BIDS_NT_MAX]])]])], ['partnerBidsFirst', dict ([['playerPasses', dict ([['min', PARTNER_BIDS_FIRST_AND_PLAYER_PASSES_MIN], ['max', PARTNER_BIDS_FIRST_AND_PLAYER_PASSES_MAX]])], ['playerDoubles', dict ([['min', PARTNER_BIDS_FIRST_AND_PLAYER_DOUBLES_MIN], ['max', PARTNER_BIDS_FIRST_AND_PLAYER_DOUBLES_MAX]])], ['playerBidsSuit', dict ([['isJumpshift', dict ([['min', PARTNER_BIDS_FIRST_AND_PLAYER_BIDS_SUIT_IS_JUMPSHIFT_MIN], ['max', PARTNER_BIDS_FIRST_AND_PLAYER_BIDS_SUIT_IS_JUMPSHIFT_MAX]])], ['isNotJumpshift', dict ([['min', PARTNER_BIDS_FIRST_AND_PLAYER_BIDS_SUIT_IS_NOT_JUMPSHIFT_MIN], ['max', PARTNER_BIDS_FIRST_AND_PLAYER_BIDS_SUIT_IS_NOT_JUMPSHIFT_MAX]])]])], ['playerBidsNoTrump', dict ([['isJumpshift', dict ([['min', PARTNER_BIDS_FIRST_AND_PLAYER_BIDS_NT_IS_JUMPSHIFT_MIN], ['max', PARTNER_BIDS_FIRST_AND_PLAYER_BIDS_NT_IS_JUMPSHIFT_MAX]])], ['isNotJumpshift', dict ([['min', PARTNER_BIDS_FIRST_AND_PLAYER_BIDS_NT_IS_NOT_JUMPSHIFT_MIN], ['max', PARTNER_BIDS_FIRST_AND_PLAYER_BIDS_NT_IS_NOT_JUMPSHIFT_MAX]])]])]])], ['special', dict ([['weakTwo', dict ([['min', SPECIAL_WEAK_TWO_MIN], ['max', SPECIAL_WEAK_TWO_MAX]])], ['weakThree', dict ([['min', SPECIAL_WEAK_THREE_MIN], ['max', SPECIAL_WEAK_THREE_MAX]])], ['respondTwoClubs', dict ([['oneBidAbove', dict ([['min', 0], ['max', 3]])], ['twoBidAbove', dict ([['min', 4], ['max', 6]])], ['threeBidAbove', dict ([['min', 7], ['max', 9]])], ['fourBidAbove', dict ([['min', 10], ['max', 12]])], ['fiveBidAbove', dict ([['min', 13], ['max', 15]])], ['sixBidAbove', dict ([['min', 16], ['max', 18]])], ['sevenAndMoreAbove', dict ([['min', 19], ['max', -(1)]])]])], ['openTwoClubs', dict ([['min', SPECIAL_WEAK_TWO_CLUBS_MIN], ['max', SPECIAL_WEAK_TWO_CLUBS_MAX]])], ['wtf', dict ([['min', SPECIAL_WEAK_THREE_MIN], ['max', SPECIAL_WEAK_TWO_CLUBS_MAX]])]])]]);
export var getEstimatedPoints = function (biddingRelative, biddingAbsolute, seatingRelative) {
	var estimatedScoring = dict ([['top', dict ([['min', null], ['max', null]])], ['bottom', dict ([['min', null], ['max', null]])], ['left', dict ([['min', null], ['max', null]])], ['right', dict ([['min', null], ['max', null]])]]);
	for (var [location, playersBids] of biddingRelative.py_items ()) {
		var numberOfBidsMade = len (biddingRelative [location]);
		if (numberOfBidsMade < 1 || re.search ('bottom', location, re.IGNORECASE)) {
			continue;
		}
		var username = seatingRelative [location];
		var partner = seatingRelative [helpers.getLocationAfterRotationsAround (location, 2)];
		print ('');
		print ('username = {0}'.format (username));
		var biddingUpToUsersLastTurn = biddingAbsolute.__getslice__ (0, helpers.getIndexOfNthBid (username, biddingAbsolute, -(1)), 1);
		var currentContractBidForUser = helpers.getCurrentContractBidFromBidding (biddingUpToUsersLastTurn);
		print ('biddingUpToUsersTurn = {0}'.format (biddingUpToUsersLastTurn));
		print ('currentContractBidForUser = {0}'.format (currentContractBidForUser));
		var hasPartnerOpened = helpers.getHasPartnerOpened (biddingAbsolute, seatingRelative, username);
		var firstBid = biddingRelative [location] [0];
		var secondBid = '';
		var lastBid = '';
		if (len (biddingRelative [location]) > 1) {
			var secondBid = biddingRelative [location] [1];
			var lastBid = biddingRelative [location] [-(1)];
		}
		var firstBidIsPass = re.search ('pass', firstBid, re.IGNORECASE);
		var isTeamsFirstBidOpportunity = helpers.getIsTeamsFirstBidOpportunity (biddingRelative, location);
		var isPartnersFirstBidPass = helpers.getIsPartnersFirstBidPass (biddingRelative, seatingRelative, username);
		var isFirstBidJumpshift = false;
		try {
			var isFirstBidJumpshift = helpers.getIsJumpshift (currentContractBidForUser, firstBid);
			var isAnyBidJumpshift = helpers.getHasPlayerJumpshifted (username, playersBids, biddingAbsolute);
		}
		catch (__except0__) {
			// pass;
		}
		var __left0__ = helpers.getHasSomeoneOpenedTwoClubs (biddingAbsolute, biddingRelative, seatingRelative);
		var hasSomeoneOpenedTwoClubs = __left0__ [0];
		var personWhoOpenedTwoClubs = __left0__ [1];
		print ('currentContractBid = {0}'.format (currentContractBidForUser));
		print ('biddingObjectRelative = {0}'.format (biddingRelative));
		print ('firstBid = {0}'.format (firstBid));
		print ('hasPartnerOpened = {0}'.format (hasPartnerOpened));
		print ('isFirstBidJumpShift = {0}'.format (isFirstBidJumpshift));
		print ('isTeamsFirstBidOpportunity = {0}'.format (isTeamsFirstBidOpportunity));
		var wasPlayerForcedToBid = helpers.getWasForcedToBid (username, biddingAbsolute, seatingRelative);
		var partnersLocation = helpers.getPartnersLocation (username, seatingRelative);
		var hasPartnerOpenedOneNoTrump = helpers.getHasPartnerOpenedNoTrump (location, partnersLocation, biddingRelative, biddingAbsolute, seatingRelative);
		if (hasPartnerOpenedOneNoTrump && secondBid == '') {
			print ('one trump scenario------------------');
			print ('{}{}'.format (wasPlayerForcedToBid));
			if (wasPlayerForcedToBid) {
				if (firstBidIsPass) {
					var minToUse = py_values ['partnerBidsFirst'] ['playerPasses'] ['min'];
					var maxToUse = py_values ['partnerBidsFirst'] ['playerPasses'] ['max'];
				}
				else {
					var minToUse = py_values ['partnerPassesFirst'] ['playerPasses'] ['min'];
					var maxToUse = py_values ['partnerPassesFirst'] ['playerPasses'] ['max'];
				}
			}
			else {
				var __left0__ = setInitialBounds (username, location, biddingAbsolute, biddingRelative, seatingRelative, firstBid, isFirstBidJumpshift, hasPartnerOpened, isPartnersFirstBidPass, false);
				var minToUse = __left0__ [0];
				var maxToUse = __left0__ [1];
			}
			estimatedScoring [location] ['min'] = minToUse;
			estimatedScoring [location] ['max'] = maxToUse;
			continue;
		}
		else if (hasSomeoneOpenedTwoClubs) {
			print ('someone opened two clubs');
			print ('personWhoOpenedTwoClubs = {0}'.format (personWhoOpenedTwoClubs));
			print ('partner = {0}'.format (partner));
			if (partner == personWhoOpenedTwoClubs) {
				print ('partner opened');
				if (!(re.search ('pass', firstBid, re.IGNORECASE))) {
					var indexOfTwoClubBid = biddingAbsolute.index ([partner, 'Two Club']);
					var contractAtThisPoint = helpers.getCurrentContractBidFromBidding (biddingAbsolute.__getslice__ (0, indexOfTwoClubBid + 2, 1));
					var numberOfBidsAbove = helpers.getIndexDifferenceOfBids (contractAtThisPoint, firstBid);
					if (numberOfBidsAbove == 1) {
						var minToUse = 0;
					}
					else {
						var minToUse = (numberOfBidsAbove - 1) * 3 + 1;
					}
					var maxToUse = numberOfBidsAbove * 3;
				}
				else {
					print ('first bid pass');
					if (hasPartnerOpened) {
						var minToUse = py_values ['partnerBidsFirst'] ['playerPasses'] ['min'];
						var maxToUse = py_values ['partnerBidsFirst'] ['playerPasses'] ['max'];
					}
					else {
						var minToUse = py_values ['isTeamsFirstBid'] ['playerPasses'] ['min'];
						var maxToUse = py_values ['isTeamsFirstBid'] ['playerPasses'] ['max'];
					}
				}
			}
			else if (len (biddingRelative [location]) == 1 || username == personWhoOpenedTwoClubs) {
				print ('is person who opened or length greater than 1');
				print ('{}{}'.format (firstBid));
				var __left0__ = setInitialBounds (username, location, biddingAbsolute, biddingRelative, seatingRelative, firstBid, isFirstBidJumpshift, hasPartnerOpened, isPartnersFirstBidPass, true);
				var minToUse = __left0__ [0];
				var maxToUse = __left0__ [1];
			}
			else {
				print ('more than 1 bid and not user who opened');
				var usersFirstContractBid = helpers.getUsersFirstContractBid (username, biddingAbsolute);
				print ('{}{}'.format (usersFirstContractBid));
				if (re.search ('pass', firstBid, re.IGNORECASE) && re.search ('pass', secondBid, re.IGNORECASE)) {
					var minToUse = py_values ['isTeamsFirstBid'] ['playerPasses'] ['min'];
					var maxToUse = py_values ['isTeamsFirstBid'] ['playerPasses'] ['max'];
				}
				else {
					var __left0__ = setInitialBounds (username, location, biddingAbsolute, biddingRelative, seatingRelative, usersFirstContractBid, isFirstBidJumpshift, hasPartnerOpened, isPartnersFirstBidPass, false);
					var minToUse = __left0__ [0];
					var maxToUse = __left0__ [1];
				}
			}
			estimatedScoring [location] ['min'] = minToUse;
			estimatedScoring [location] ['max'] = maxToUse;
		}
		else if (secondBid == '') {
			var minToUse = null;
			var maxToUse = null;
			if (isTeamsFirstBidOpportunity && firstBidIsPass) {
				print ('one opportunity first bid pass-----------');
				var minToUse = py_values ['isTeamsFirstBid'] ['playerPasses'] ['min'];
				var maxToUse = py_values ['isTeamsFirstBid'] ['playerPasses'] ['max'];
			}
			else {
				print ('one opportunity else-----------');
				var __left0__ = setInitialBounds (username, location, biddingAbsolute, biddingRelative, seatingRelative, firstBid, isFirstBidJumpshift, hasPartnerOpened, isPartnersFirstBidPass, false);
				var minToUse = __left0__ [0];
				var maxToUse = __left0__ [1];
			}
			estimatedScoring [location] ['min'] = minToUse;
			estimatedScoring [location] ['max'] = maxToUse;
		}
		else {
			var isSecondBidJumpshift = helpers.getIsJumpshift (currentContractBidForUser, secondBid);
			print ('{}{}'.format (secondBid));
			print ('{}{}'.format (currentContractBidForUser));
			print ('{}{}'.format (isSecondBidJumpshift));
			print ('{}{}'.format (wasPlayerForcedToBid));
			if (len (playersBids) == 2) {
				if (wasPlayerForcedToBid) {
					var __left0__ = setInitialBounds (username, location, biddingAbsolute, biddingRelative, seatingRelative, firstBid, isFirstBidJumpshift, hasPartnerOpened, isPartnersFirstBidPass, false, true, secondBid, isSecondBidJumpshift);
					var minToUse = __left0__ [0];
					var maxToUse = __left0__ [1];
					estimatedScoring [location] ['min'] = minToUse;
					estimatedScoring [location] ['max'] = maxToUse;
					continue;
				}
				if (hasPartnerOpened) {
					print ('partner has opened');
					if (firstBidIsPass) {
						if (!(re.search ('pass', secondBid, re.IGNORECASE)) && !(re.search ('double', secondBid, re.IGNORECASE))) {
							print ('partner open, first bid pass');
							if (isSecondBidJumpshift) {
								print ('second bid is jumpshift');
								estimatedScoring [location] ['min'] = py_values ['passFirstBidSecond'] ['isJumpshift'] ['partnerHasOpened'] ['min'];
								estimatedScoring [location] ['max'] = py_values ['passFirstBidSecond'] ['isJumpshift'] ['partnerHasOpened'] ['max'];
							}
							else {
								print ('second bid is not jumpshift');
								var didPlayerHaveFirstBidOpportunity = helpers.getUsernameOfPlayerWhoHadFirstOpportunityToBid (biddingAbsolute, username, partner) == username;
								if (didPlayerHaveFirstBidOpportunity) {
									estimatedScoring [location] ['max'] = py_values ['isTeamsFirstBid'] ['playerPasses'] ['max'];
								}
								else {
									estimatedScoring [location] ['max'] = py_values ['partnerBidsFirst'] ['playerBidsSuit'] ['isNotJumpshift'] ['max'];
								}
								estimatedScoring [location] ['min'] = py_values ['partnerBidsFirst'] ['playerBidsSuit'] ['isNotJumpshift'] ['min'];
							}
							continue;
						}
						else {
							print ('else clause');
							print ('{}{}'.format (isPartnersFirstBidPass));
							if (isPartnersFirstBidPass) {
								var partnersSecondBid = null;
								try {
									var partnersSecondBid = biddingRelative [partnersLocation] [1];
								}
								catch (__except0__) {
									// pass;
								}
								var partnersSecondBidIsGameBid = helpers.getIsBidGameBid (partnersSecondBid);
								print ('{}{}'.format (partnersSecondBidIsGameBid));
								if (partnersSecondBidIsGameBid) {
									estimatedScoring [location] ['min'] = py_values ['partnerPassesFirst'] ['playerPasses'] ['min'];
									estimatedScoring [location] ['max'] = py_values ['partnerPassesFirst'] ['playerPasses'] ['max'];
								}
								else {
									var currentContractBidForPartner = helpers.getPartnersCurrentContractBidFromBidding (username, biddingAbsolute, seatingRelative);
									var isPartnersSecondBidJumpshift = helpers.getIsJumpshift (currentContractBidForPartner, partnersSecondBid);
									print ('{}{}'.format (partnersSecondBid));
									print ('{}{}'.format (currentContractBidForPartner));
									print ('{}{}'.format (isPartnersSecondBidJumpshift));
									if (isPartnersSecondBidJumpshift) {
										estimatedScoring [location] ['min'] = py_values ['partnerPassesFirst'] ['playerPasses'] ['min'];
										estimatedScoring [location] ['max'] = py_values ['partnerPassesFirst'] ['playerPasses'] ['max'];
									}
									else {
										estimatedScoring [location] ['min'] = py_values ['partnerPassesFirst'] ['playerPasses'] ['min'];
										estimatedScoring [location] ['max'] = py_values ['partnerBidsFirst'] ['playerPasses'] ['max'];
									}
								}
							}
							else {
								estimatedScoring [location] ['min'] = py_values ['partnerBidsFirst'] ['playerPasses'] ['min'];
								estimatedScoring [location] ['max'] = py_values ['partnerBidsFirst'] ['playerPasses'] ['max'];
							}
							continue;
						}
					}
					else {
						print ('first bid is not pass');
					}
				}
				else {
					print ('partner has not opened');
					if (firstBidIsPass) {
						print ('first bid is pass');
						if (!(re.search ('pass', secondBid, re.IGNORECASE)) && !(re.search ('double', secondBid, re.IGNORECASE))) {
							print ('second bid is not pass');
							if (isSecondBidJumpshift) {
								estimatedScoring [location] ['min'] = py_values ['passFirstBidSecond'] ['isJumpshift'] ['partnerHasNotOpened'] ['min'];
								estimatedScoring [location] ['max'] = py_values ['passFirstBidSecond'] ['isJumpshift'] ['partnerHasNotOpened'] ['max'];
							}
							else {
								estimatedScoring [location] ['min'] = py_values ['isTeamsFirstBid'] ['playerPassesFirstOpensSecond'] ['min'];
								estimatedScoring [location] ['max'] = py_values ['isTeamsFirstBid'] ['playerPassesFirstOpensSecond'] ['max'];
							}
							continue;
						}
						else {
							print ('second bid is pass');
							var didPlayerHaveFirstBidOpportunity = helpers.getUsernameOfPlayerWhoHadFirstOpportunityToBid (biddingAbsolute, username, partner) == username;
							print ('{}{}'.format (didPlayerHaveFirstBidOpportunity));
							if (!(didPlayerHaveFirstBidOpportunity)) {
								estimatedScoring [location] ['min'] = py_values ['partnerPassesFirst'] ['playerPasses'] ['min'];
								estimatedScoring [location] ['max'] = py_values ['partnerPassesFirst'] ['playerPasses'] ['max'];
							}
							else if (hasPartnerOpened) {
								estimatedScoring [location] ['min'] = tuple ([py_values ['partnerBidsFirst'] ['playerPasses'] ['min']]);
								estimatedScoring [location] ['max'] = tuple ([py_values ['partnerBidsFirst'] ['playerPasses'] ['max']]);
							}
							else {
								estimatedScoring [location] ['min'] = py_values ['isTeamsFirstBid'] ['playerPasses'] ['min'];
								estimatedScoring [location] ['max'] = py_values ['isTeamsFirstBid'] ['playerPasses'] ['max'];
							}
							continue;
						}
					}
					else {
						print ('first bid is not pass');
					}
				}
			}
			else {
				// pass;
			}
			var __left0__ = setInitialBounds (username, location, biddingAbsolute, biddingRelative, seatingRelative, firstBid, isFirstBidJumpshift, hasPartnerOpened, isPartnersFirstBidPass, false, wasPlayerForcedToBid, secondBid, isSecondBidJumpshift);
			var minToUse = __left0__ [0];
			var maxToUse = __left0__ [1];
			estimatedScoring [location] ['min'] = minToUse;
			estimatedScoring [location] ['max'] = maxToUse;
			continue;
		}
	}
	print ('');
	return estimatedScoring;
};
export var setInitialBounds = function (username, location, biddingAbsolute, biddingRelative, seatingRelative, firstBid, isFirstBidJumpshift, hasPartnerOpened, isPartnersFirstBidPass, hasOtherTeamOpenedTwoClubs, wasForcedToBid, secondBid, isSecondBidJumpshift) {
	if (typeof hasOtherTeamOpenedTwoClubs == 'undefined' || (hasOtherTeamOpenedTwoClubs != null && hasOtherTeamOpenedTwoClubs.hasOwnProperty ("__kwargtrans__"))) {;
		var hasOtherTeamOpenedTwoClubs = false;
	};
	if (typeof wasForcedToBid == 'undefined' || (wasForcedToBid != null && wasForcedToBid.hasOwnProperty ("__kwargtrans__"))) {;
		var wasForcedToBid = false;
	};
	if (typeof secondBid == 'undefined' || (secondBid != null && secondBid.hasOwnProperty ("__kwargtrans__"))) {;
		var secondBid = null;
	};
	if (typeof isSecondBidJumpshift == 'undefined' || (isSecondBidJumpshift != null && isSecondBidJumpshift.hasOwnProperty ("__kwargtrans__"))) {;
		var isSecondBidJumpshift = false;
	};
	var IsUsernamesFirstContractBidTheFirstContractBid = helpers.getIsUsernamesFirstContractBidTheFirstContractBid (username, biddingAbsolute);
	print ('{}{}'.format (IsUsernamesFirstContractBidTheFirstContractBid));
	print ('setInitialBounds-----------------');
	if (re.search ('trump', firstBid, re.IGNORECASE)) {
		print ('trump branch');
		print ('isFirstBidJumpshift = {0}'.format (isFirstBidJumpshift));
		if (hasOtherTeamOpenedTwoClubs) {
			var minToUse = py_values ['special'] ['wtf'] ['min'];
			var maxToUse = py_values ['special'] ['wtf'] ['max'];
		}
		else if (isFirstBidJumpshift) {
			var minToUse = py_values ['partnerBidsFirst'] ['playerBidsNoTrump'] ['isJumpshift'] ['min'];
			var maxToUse = py_values ['partnerBidsFirst'] ['playerBidsNoTrump'] ['isJumpshift'] ['max'];
		}
		else if (hasPartnerOpened) {
			var minToUse = py_values ['partnerBidsFirst'] ['playerBidsNoTrump'] ['isNotJumpshift'] ['min'];
			var maxToUse = py_values ['partnerBidsFirst'] ['playerBidsNoTrump'] ['isNotJumpshift'] ['max'];
		}
		else {
			var minToUse = py_values ['isTeamsFirstBid'] ['playerBidsNoTrump'] ['min'];
			var maxToUse = py_values ['isTeamsFirstBid'] ['playerBidsNoTrump'] ['max'];
		}
	}
	else if (re.search ('two club', firstBid, re.IGNORECASE) && IsUsernamesFirstContractBidTheFirstContractBid) {
		print ('two club branch');
		var maxToUse = py_values ['special'] ['openTwoClubs'] ['max'];
		var minToUse = py_values ['special'] ['openTwoClubs'] ['min'];
	}
	else if (re.search ('double', firstBid, re.IGNORECASE)) {
		print ('double branch');
		var minToUse = py_values ['isTeamsFirstBid'] ['playerDoubles'] ['min'];
		var maxToUse = py_values ['isTeamsFirstBid'] ['playerDoubles'] ['max'];
	}
	else if (re.search ('two', firstBid, re.IGNORECASE)) {
		print ('two branch');
		print ('{}{}'.format (hasOtherTeamOpenedTwoClubs));
		if (hasOtherTeamOpenedTwoClubs) {
			var minToUse = py_values ['special'] ['weakTwo'] ['min'];
			var maxToUse = py_values ['isTeamsFirstBid'] ['playerBidsSuit'] ['max'];
		}
		else {
			var indexOfUsersFirstBid = helpers.getIndexOfNthBid (username, biddingAbsolute, 1);
			var hasSomeOneOpenedBefore = helpers.getHasSomeOneOpenedBefore (indexOfUsersFirstBid, biddingAbsolute);
			print ('{}{}'.format (location));
			print ('{}{}'.format (hasSomeOneOpenedBefore));
			print ('{}{}'.format (hasPartnerOpened));
			print ('{}{}'.format (isFirstBidJumpshift));
			if (hasSomeOneOpenedBefore) {
				if (hasPartnerOpened) {
					if (wasForcedToBid) {
						if (isFirstBidJumpshift) {
							print (1);
							var minToUse = py_values ['partnerBidsFirst'] ['playerBidsSuit'] ['isJumpshift'] ['min'];
							var maxToUse = py_values ['partnerBidsFirst'] ['playerBidsSuit'] ['isJumpshift'] ['max'];
						}
						else if (isSecondBidJumpshift) {
							print (1.1);
							var minToUse = py_values ['special'] ['wtf'] ['min'];
							var maxToUse = py_values ['special'] ['wtf'] ['max'];
						}
						else if (!(re.search ('pass', secondBid, re.IGNORECASE))) {
							print (1.2);
							var minToUse = py_values ['partnerBidsFirst'] ['playerBidsSuit'] ['isNotJumpshift'] ['min'];
							var maxToUse = py_values ['partnerBidsFirst'] ['playerBidsSuit'] ['isNotJumpshift'] ['max'];
						}
						else {
							print (1.3);
							var minToUse = py_values ['partnerPassesFirst'] ['playerPasses'] ['min'];
							var maxToUse = py_values ['partnerPassesFirst'] ['playerPasses'] ['max'];
						}
					}
					else if (secondBid) {
						if (isSecondBidJumpshift) {
							var minToUse = py_values ['special'] ['wtf'] ['min'];
							var maxToUse = py_values ['special'] ['wtf'] ['max'];
						}
						else {
							var minToUse = py_values ['partnerBidsFirst'] ['playerBidsSuit'] ['isNotJumpshift'] ['min'];
							var maxToUse = py_values ['partnerBidsFirst'] ['playerBidsSuit'] ['isNotJumpshift'] ['max'];
						}
					}
					else {
						print (2);
						var minToUse = py_values ['partnerBidsFirst'] ['playerBidsSuit'] ['isNotJumpshift'] ['min'];
						var maxToUse = py_values ['partnerBidsFirst'] ['playerBidsSuit'] ['isNotJumpshift'] ['max'];
					}
				}
				else if (isFirstBidJumpshift) {
					print (3);
					var minToUse = py_values ['special'] ['weakTwo'] ['min'];
					var maxToUse = py_values ['special'] ['weakTwo'] ['max'];
				}
				else {
					print (4);
					var minToUse = py_values ['special'] ['weakTwo'] ['min'];
					var maxToUse = py_values ['partnerPassesFirst'] ['playerBidsSuit'] ['max'];
				}
			}
			else {
				print (5);
				var minToUse = py_values ['special'] ['weakTwo'] ['min'];
				var maxToUse = py_values ['special'] ['weakTwo'] ['max'];
			}
		}
	}
	else if (re.search ('three', firstBid, re.IGNORECASE)) {
		print ('three branch');
		if (hasOtherTeamOpenedTwoClubs) {
			var minToUse = py_values ['special'] ['wtf'] ['min'];
			var maxToUse = py_values ['special'] ['wtf'] ['max'];
		}
		else {
			var wasFirstOpeningBidANthLevelBid = helpers.getWasFirstOpeningBidANthLevelBid (biddingAbsolute, 3);
			if (wasFirstOpeningBidANthLevelBid != false && wasFirstOpeningBidANthLevelBid != username) {
				var maxToUse = py_values ['partnerPassesFirst'] ['playerBidsSuit'] ['max'];
			}
			else {
				var maxToUse = py_values ['special'] ['weakThree'] ['max'];
			}
			var minToUse = py_values ['special'] ['weakThree'] ['min'];
		}
	}
	else if (re.search ('pass', firstBid, re.IGNORECASE)) {
		print ('pass branch');
		print ('{}{}'.format (hasPartnerOpened));
		print ('{}{}'.format (hasOtherTeamOpenedTwoClubs));
		if (wasForcedToBid) {
			var minToUse = py_values ['isTeamsFirstBid'] ['playerPasses'] ['min'];
			var maxToUse = py_values ['isTeamsFirstBid'] ['playerPasses'] ['max'];
		}
		else if (hasPartnerOpened) {
			if (hasOtherTeamOpenedTwoClubs) {
				var minToUse = py_values ['isTeamsFirstBid'] ['playerPasses'] ['min'];
				var maxToUse = py_values ['isTeamsFirstBid'] ['playerPasses'] ['max'];
			}
			else {
				var minToUse = py_values ['partnerBidsFirst'] ['playerPasses'] ['min'];
				var maxToUse = py_values ['partnerBidsFirst'] ['playerPasses'] ['max'];
			}
		}
		else {
			var minToUse = py_values ['isTeamsFirstBid'] ['playerPasses'] ['min'];
			var maxToUse = py_values ['isTeamsFirstBid'] ['playerPasses'] ['max'];
		}
	}
	else {
		print ('else branch');
		if (hasOtherTeamOpenedTwoClubs) {
			var minToUse = py_values ['special'] ['wtf'] ['min'];
			var maxToUse = py_values ['special'] ['wtf'] ['max'];
		}
		else if (hasPartnerOpened) {
			if (isPartnersFirstBidPass) {
				var minToUse = py_values ['partnerPassesFirst'] ['playerBidsSuit'] ['min'];
				var maxToUse = py_values ['partnerPassesFirst'] ['playerBidsSuit'] ['max'];
			}
			else if (isFirstBidJumpshift) {
				var minToUse = py_values ['partnerBidsFirst'] ['playerBidsSuit'] ['isJumpshift'] ['min'];
				var maxToUse = py_values ['partnerBidsFirst'] ['playerBidsSuit'] ['isJumpshift'] ['max'];
			}
			else {
				var minToUse = py_values ['partnerBidsFirst'] ['playerBidsSuit'] ['isNotJumpshift'] ['min'];
				var maxToUse = py_values ['partnerBidsFirst'] ['playerBidsSuit'] ['isNotJumpshift'] ['max'];
			}
		}
		else {
			var minToUse = py_values ['isTeamsFirstBid'] ['playerBidsSuit'] ['min'];
			var maxToUse = py_values ['isTeamsFirstBid'] ['playerBidsSuit'] ['max'];
		}
	}
	return [minToUse, maxToUse];
};

//# sourceMappingURL=getEstimatedPoints.map