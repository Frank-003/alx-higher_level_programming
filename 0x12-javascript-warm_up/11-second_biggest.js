#!/usr/bin/node
(() => {
    const args = process.argv.slice(2).map(Number);

    if (args.length === 0) {
        console.log(0);
    } else if (args.length === 1) {
        console.log(0);
    } else {
        let max = -Infinity;
        let secondMax = -Infinity;

        for (let num of args) {
            if (num > max) {
                secondMax = max;
                max = num;
            } else if (num > secondMax && num < max) {
                secondMax = num;
            }
        }

        console.log(secondMax);
    }
})();
