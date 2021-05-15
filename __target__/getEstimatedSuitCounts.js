// Transcrypt'ed from Python, 2021-05-09 10:17:42
var autoBid = {};
var helpers = {};
var re = {};
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import * as __module_helpers__ from './helpers.js';
__nest__ (helpers, '', __module_helpers__);
import * as __module_re__ from './re.js';
__nest__ (re, '', __module_re__);
import * as __module_autoBid__ from './autoBid.js';
__nest__ (autoBid, '', __module_autoBid__);
var __name__ = 'getEstimatedSuitCounts';
export var EstimateSuitCounts =  __class__ ('EstimateSuitCounts', [object], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, biddingRelative, biddingAbsolute, seatingRelative) {
		self.biddingRelative = biddingRelative;
		self.biddingAbsolute = biddingAbsolute;
		self.seatingRelative = seatingRelative;
		self.defaultValue = 3.25;
		self.suits = dict ([['clubs', 'clubs'], ['diamonds', 'diamonds'], ['hearts', 'hearts'], ['spades', 'spades']]);
		self.suitCounts = dict ([['top', dict ([[self.suits ['clubs'], dict ([['min', self.defaultValue], ['max', self.defaultValue]])], [self.suits ['diamonds'], dict ([['min', self.defaultValue], ['max', self.defaultValue]])], [self.suits ['hearts'], dict ([['min', self.defaultValue], ['max', self.defaultValue]])], [self.suits ['spades'], dict ([['min', self.defaultValue], ['max', self.defaultValue]])]])], ['left', dict ([[self.suits ['clubs'], dict ([['min', self.defaultValue], ['max', self.defaultValue]])], [self.suits ['diamonds'], dict ([['min', self.defaultValue], ['max', self.defaultValue]])], [self.suits ['hearts'], dict ([['min', self.defaultValue], ['max', self.defaultValue]])], [self.suits ['spades'], dict ([['min', self.defaultValue], ['max', self.defaultValue]])]])], ['right', dict ([[self.suits ['clubs'], dict ([['min', self.defaultValue], ['max', self.defaultValue]])], [self.suits ['diamonds'], dict ([['min', self.defaultValue], ['max', self.defaultValue]])], [self.suits ['hearts'], dict ([['min', self.defaultValue], ['max', self.defaultValue]])], [self.suits ['spades'], dict ([['min', self.defaultValue], ['max', self.defaultValue]])]])]]);
		print ('{}{}'.format (self));
		print ('{}{}'.format (self.suitCounts));
	});},
	get getResult () {return __get__ (this, function (self, num1, num2) {
		return num1 * num2;
	});}
});
export var getEstimatedSuitCounts = function (biddingRelative, biddingAbsolute, seatingRelative) {
	if (typeof biddingRelative == 'undefined' || (biddingRelative != null && biddingRelative.hasOwnProperty ("__kwargtrans__"))) {;
		var biddingRelative = null;
	};
	if (typeof biddingAbsolute == 'undefined' || (biddingAbsolute != null && biddingAbsolute.hasOwnProperty ("__kwargtrans__"))) {;
		var biddingAbsolute = null;
	};
	if (typeof seatingRelative == 'undefined' || (seatingRelative != null && seatingRelative.hasOwnProperty ("__kwargtrans__"))) {;
		var seatingRelative = null;
	};
	var estimateSuitCounts = EstimateSuitCounts (biddingRelative, biddingAbsolute, seatingRelative);
	return estimateSuitCounts.suitCounts;
};

//# sourceMappingURL=getEstimatedSuitCounts.map