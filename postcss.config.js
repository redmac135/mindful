const purgecss = require('@fullhuman/postcss-purgecss')

module.exports = {
    content: ["./assets/**/*.{html,js}"],
    plugins: [
        purgecss({
            content: ['./templates/**/*.html']
        })
    ],
}
