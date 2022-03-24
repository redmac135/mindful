const purgecss = require('@fullhuman/postcss-purgecss')

module.exports = {
    content: [
        "./assets/**/*.js", 
        './templates/**/*.html'
    ],
    theme: {
        extend: {},
    },
    plugins: [],
}