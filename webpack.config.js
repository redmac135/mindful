const path = require('path');

module.exports = {
  mode: "development",
  entry: {
    navbar: './mindful/assets/base/js/navbar.js',
    breathing: './mindful/assets/miniapps/js/breathing.js',
  },  // path to input file
  output: {
    filename: '[name]/js/[name]-bundle.js',  // output bundle file name
    path: path.resolve(__dirname, './mindful/static'),  // path to Django static directory
  },
  resolve: {
    alias: {
      'react-native': 'react-native-web',
    },
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        loader: "babel-loader",
        options: {
          presets: [
            "@babel/preset-env", 
            ["@babel/preset-react", { 'runtime': 'automatic' }],
          ]
        }
      },
    ],
  },
};