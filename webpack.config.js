const path = require('path');

module.exports = {
  entry: {navbar: './mindful/assets/base/js/navbar.js'},  // path to input file
  output: {
    filename: '[name]/js/[name]-bundle.js',  // output bundle file name
    path: path.resolve(__dirname, './mindful/static'),  // path to Django static directory
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        loader: "babel-loader",
        options: { presets: ["@babel/preset-env", "@babel/preset-react"] }
      },
    ]
  },
};