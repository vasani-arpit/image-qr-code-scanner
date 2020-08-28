//TODO: use this space to generate the spaghetti 
const path = require('path');
const { spawn } = require('child_process');
module.exports = (imagePath) => {
    return new Promise((resolve, reject) => {
        const pythonFile = path.join(__dirname, 'qrcode-scanner.py')
        const pythonImageToProcess = path.join(__dirname, imagePath)
        console.log(`python3 ${pythonFile} --input ${pythonImageToProcess}`)
        const ls = spawn('python3', [pythonFile, '--input', pythonImageToProcess]);
        ls.stdout.on('data', async (data) => {
            //console.log(`stdout: ${data}`);
            resolve(`${data}`)
        });
        ls.stderr.on('data', (data) => {
            //console.error(`stderr: ${data}`);
            reject(`${data}`)
        });

        ls.on('close', (code) => {
            console.log(`child process exited with code ${code}`);
        });
    })
}