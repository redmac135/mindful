const path = require('path');

module.exports = {
  entry: './assets/index.js',  // path to input file
  output: {
    filename: 'index-bundle.js',  // output bundle file name
    path: path.resolve(__dirname, './static'),  // path to Django static directory
  },
};