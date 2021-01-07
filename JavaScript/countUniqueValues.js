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

console.log(countUniqueValues('a7a'));
