/**
 * @desc count the unique values in the array
 * @param n: array
 * @return integer
 */
function countUniqueValues(array) {
	let values = array;
	let uniqueValues = [];

	for (let val of values) {
		if (uniqueValues.indexOf(val) === -1) {
			uniqueValues.push(val);
		}
	}

	return uniqueValues.length;
}

console.log(countUniqueValues(['a', '7', 'a']));

// another solution
function countUniqueValues2(array) {
	let i = 0;

	for (let j = 1; j < array.length; j++) {
		if (array[i] !== array[j]) {
			i++;
			array[i] = array[j];
		}
	}

	return i + 1;
}

console.log(countUniqueValues2([1, 2, 3]));
