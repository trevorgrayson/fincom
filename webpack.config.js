const path = require('path');
const JavaScriptObfuscator = require('webpack-obfuscator');


module.exports = {
    mode: 'production',
    entry: "./src/js/latex2js/latex2js.js",
    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: "math-v1.js" // name of the generated bundle
    },
    //plugins: [
    //        new JavaScriptObfuscator({
    //            rotateUnicodeArray: true
    //        }, ['momentus-sdk-v1.js'])
    //    ]
    //}
};
