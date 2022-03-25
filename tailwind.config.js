const purgecss = require('@fullhuman/postcss-purgecss')

module.exports = {
    content: [
        "./assets/**/*.js",
        './templates/**/*.html',
        './**/templates/**/*.html',
    ],
    theme: {
        extend: {
            "width": {
                "200": "50rem",
            },
            backgroundImage: {
                'gradient-radial': 'radial-gradient(var(--gradient-color-stops))',
            },
            colors: {
                "mindful-blue": "#cde3f3",
                "mindful-pink": "#e59490",
                "mindful-gray": "#394759",
            },
        },
    },
    plugins: [],
}