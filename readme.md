# Image QR Code Scanner

![qr-code logo](https://user-images.githubusercontent.com/6497827/91564420-40b4a680-e95e-11ea-9a45-e8fc7084aa4a.png)

An NPM package for node which takes image path and finds and decodes QR codes in it. The only package which supports/decodes multiple QR codes in a single image.

![npm](https://img.shields.io/npm/v/image-qr-code-scanner?style=flat-square)
![NPM](https://img.shields.io/npm/l/image-qr-code-scanner?style=flat-square)

## Features

✅ No node dependencies (yes. literally none.)

✅ Scans multiple QR in one image

✅ Real world tested 

## Installation

1. Install python3 and pip3 in server/machine
1. Install requirements globally using
        `pip3 install pyzbar opencv-python==4.3.0.38 argparse`
1. make sure have following linux dependencies installed 
        `sudo apt install -y libzbar0 libsm6 libxext6 libxrender-dev`

## How to use it?

```javascript
//JS
const imageScanner = require('image-qr-code-scanner')

async function main() {
    try {
        let results = await imageScanner('./images/fileWithMultipleQRs.jpg')
        console.log(results)
    } catch (error) {
        console.log(error)
    }
}
main()
```

```typescript
//TypeScript

```

## FAQ

#### There are lot of other packages. Why did you created this one?
I have used and tested several in production but none of them was able to give me results what I wanted which was accurate results and multiple QR scanning in image. So, I created this one and used python in it as it was more mature and accurate libraries for this use case.

#### Will you regularly update this library?
Yes. I will be keeping tabs on this one.

#### I found a bug what should I do?
Create a new issue. I will take a look at it. 

#### I don't want to use your package. What other option do I have?

Several actually. all comes with it's own pros and cons

- [qr-scanner](https://www.npmjs.com/package/qr-scanner) A web based QR code scanner
- [QRCodeScanner](https://www.npmjs.com/package/qr-code-scanner) another web based QR code scanner ported from Java
- [jsQR](https://github.com/cozmo/jsQR) this one can be used as both as node package and also as a web based node package

None of the above can scan multiple QR codes from one image(I think. package may have been updated since I last tested).

## Special thanks !!
Special thanks to [Pavan Mehta](https://github.com/pavanmehta91) he wrote initial python code.
