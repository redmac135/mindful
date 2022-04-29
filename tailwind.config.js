module.exports = {
    content: [
        "./mindful/assets/**/js/*.js",
        "./mindful/templates/**/*.html",
        "./mindful/**/templates/**/*.html",
        "./mindful/**/static/**/js/*.js",
        "./mindful/node_modules/flowbite/**/*.js",
    ],
    theme: {
        extend: {
            width: {
                200: "50rem",
            },
            backgroundImage: {
                "gradient-radial":
                    "radial-gradient(var(--gradient-color-stops))",
            },
            colors: {
                "mindful-blue": {
                    50: "#eaf4fa",
                    100: "#cde3f3",
                    200: "#add1eb",
                    300: "#84bae1",
                    400: "#5ba3d7",
                    500: "#328ccd",
                    600: "#2870a4",
                    700: "#1e547b",
                    800: "#143852",
                    900: "#0a1c29",
                },
                "mindful-pink": {
                    50: "#faebea",
                    100: "#f5d7d6",
                    200: "#ecb0ac",
                    300: "#e28883",
                    400: "#d8605a",
                    500: "#cf3830",
                    600: "#a52d27",
                    700: "#7c221d",
                    800: "#531713",
                    900: "#290b0a",
                },
                "mindful-gray": {
                    50: "#eff2f5",
                    100: "#e0e5eb",
                    200: "#c1cbd7",
                    300: "#a2b0c3",
                    400: "#8396af",
                    500: "#637c9c",
                    600: "#50637c",
                    700: "#3c4a5d",
                    800: "#28323e",
                    900: "#14191f",
                },
            },
            keyframes: {
                shake: {
                    "10%, 90%": { transform: "translate3d(-1px, 0, 0)" },
                    "20%, 80%": { transform: "translate3d(2px, 0, 0)" },
                    "30%, 50%, 70%": { transform: "translate3d(-4px, 0, 0)" },
                    "40%, 60%": { transform: "translate3d(4px, 0, 0)" },
                },
            },
            animation: {
                shake: "shake 0.82s cubic-bezier(.36,.07,.19,.97) both",
            },
        },
    },
    plugins: [require("flowbite/plugin")],
};
