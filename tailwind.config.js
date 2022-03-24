const purgecss = require('@fullhuman/postcss-purgecss')

module.exports = {
    content: [
        "./assets/**/*.js",
        './templates/**/*.html',
        './**/templates/**/*.html',
    ],
    theme: {
        extend: {},
    },
    plugins: [],
}