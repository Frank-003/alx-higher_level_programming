#!/usr/bin/node
const fs = require('fs');

// Extracting file paths from command line arguments
const [, , sourceFilePath1, sourceFilePath2, destinationFilePath] = process.argv;

// Read the content of the first source file
fs.readFile(sourceFilePath1, 'utf8', (err, data1) => {
    if (err) {
        console.error(`Error reading ${sourceFilePath1}: ${err}`);
        return;
    }

    // Read the content of the second source file
    fs.readFile(sourceFilePath2, 'utf8', (err, data2) => {
        if (err) {
            console.error(`Error reading ${sourceFilePath2}: ${err}`);
            return;
        }

        // Concatenate the content of both files
        const concatenatedContent = data1 + data2;

        // Write the concatenated content to the destination file
        fs.writeFile(destinationFilePath, concatenatedContent, 'utf8', (err) => {
            if (err) {
                console.error(`Error writing to ${destinationFilePath}: ${err}`);
                return;
            }
            console.log(`Concatenation successful. Result saved to ${destinationFilePath}`);
        });
    });
});
