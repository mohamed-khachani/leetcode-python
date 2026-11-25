type Fn = (accum: number, curr: number) => number

function reduce(nums: number[], fn: Fn, init: number): number {
    let accum = init;

    for (const num of nums) {
        accum = fn(accum, num);
    }

    return accum;
}


// Example 1
console.log(
    reduce([1, 2, 3, 4], (accum, curr) => accum + curr, 0)
); // Expected: 10

// Example 2
console.log(
    reduce([1, 2, 3, 4], (accum, curr) => accum + curr * curr, 100)
); // Expected: 130

// Example 3
console.log(
    reduce([], (accum, curr) => 0, 25)
); // Expected: 25