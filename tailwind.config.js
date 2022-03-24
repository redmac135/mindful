const purgecss = require('@fullhuman/postcss-purgecss')

module.exports = {
    content: [
        "./assets/**/*.js",
        './templates/**/*.html',
        './reflection/templates/reflection/*.html',
    ],
    theme: {
        extend: {},
    },
    plugins: [],
}