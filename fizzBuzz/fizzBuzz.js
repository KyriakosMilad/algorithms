/**
 * @desc loop from 0 to (n) and check numbers between if dividable by 5 print Buzz and if dividable by 3 print Fizz and if dividable by both print FizzBuzz.
 * @param n: integer
 * @return void
 */
function fizzBuzz(n) {
	for (let i = 1; i <= n; i++) {
		let fizz = i % 3 == 0,
			buzz = i % 5 == 0;
		console.log(fizz && buzz ? 'FizzBuzz' : fizz ? 'Fizz' : buzz ? 'Buzz' : i);
	}
}

fizzBuzz(15);
