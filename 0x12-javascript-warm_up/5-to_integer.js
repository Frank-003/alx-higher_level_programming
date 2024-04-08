#!/usr/bin/node
const arg2 = process.argv[2];
const num = parseInt(arg2);

if (isNaN(num)){
	console.log('Not a number');
}
else
{
	console.log('My number: 89');
}
