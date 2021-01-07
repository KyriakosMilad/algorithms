/**
 * @desc check if the characters in the first word are the same in the second word regardless of the order.
 * @param n: integer
 * @return boolean
 */
function anagram(firstWord, secondWord) {
	let frequencyCounter1 = {},
		frequencyCounter2 = {};

	for (let val of firstWord.split('')) {
		frequencyCounter1[val] = (frequencyCounter1 || 0) + 1;
	}

	for (let val of secondWord.split('')) {
		frequencyCounter2[val] = (frequencyCounter2 || 0) + 1;
	}

	for (let val in frequencyCounter1) {
		if (frequencyCounter1[val] !== frequencyCounter2[val]) return false;
		if (!frequencyCounter1[val] || !frequencyCounter2[val]) return false;
	}

	return true;
}

console.log(anagram('anagram', 'nagaram'));
