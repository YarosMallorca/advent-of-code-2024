let fs = require('fs');
let path = require('path');

function isSafe(numbers) {

    // Initialize the variable to track if the sequence is increasing or decreasing
    let increasing = undefined;

    // Loop through the numbers array to check the differences between consecutive numbers
    for (let i = 0; i < numbers.length - 1; i++) {
        // Calculate the difference between the current number and the next number
        let diff = numbers[i] - numbers[i + 1];

        // Determine if the sequence is increasing or decreasing based on the first difference
        if (increasing === undefined) increasing = diff > 0;

        // Check if the sequence violates the conditions:
        // 1. If the sequence was increasing and now it's not, or vice versa
        // 2. If the absolute difference between consecutive numbers is greater than 3
        if ((increasing && diff <= 0) || (!increasing && diff >= 0) || Math.abs(diff) > 3) return false;
    }
    return true;
}

function main() {
    // Load the file from folder
    let input = fs.readFileSync('./input.txt',
        { encoding: 'utf8', flag: 'r' });

    // Split the input by new lines and then split each line by spaces, converting each element to a number
    const reports = input.split('\n').map(str => str.split(' ').map(Number));

    // Filter the reports to only include the ones that are safe
    const safe = reports.filter(isSafe);

    // Log the number of safe reports to the console
    console.log(safe.length);
}

main()