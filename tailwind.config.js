const purgecss = require('@fullhuman/postcss-purgecss')

module.exports = {
    content: [
        './assets/**/js/*.js',
        './templates/**/*.html',
        './**/templates/**/*.html',
        './**/static/js/*.js',
        './node_modules/flowbite/**/*.js',
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
            keyframes: {
                shake: {
                    "10%, 90%": { transform: "translate3d(-1px, 0, 0)" },
                    "20%, 80%": { transform: "translate3d(2px, 0, 0)" },
                    "30%, 50%, 70%": { transform: "translate3d(-4px, 0, 0)" },
                    "40%, 60%": { transform: "translate3d(4px, 0, 0)" }
                }
            },
            animation: {
                shake: "shake 0.82s cubic-bezier(.36,.07,.19,.97) both"
            },
        },
    },
    plugins: [
        require('flowbite/plugin')
    ],
}