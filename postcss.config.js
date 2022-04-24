const purgecss = require("@fullhuman/postcss-purgecss");
const cssnano = require("cssnano");

module.exports = {
    plugins: [
        require("tailwindcss"),
        require("autoprefixer"),
        cssnano({
            preset: "default",
        }),
        purgecss({
            content: [
                "./mindful/assets/**/js/*.js",
                "./mindful/templates/**/*.html",
                "./mindful/**/templates/**/*.html",
                "./mindful/**/static/**/js/*.js",
                "./mindful/node_modules/flowbite/**/*.js",
            ],
            defaultExtractor: (content) =>
                content.match(/[\w-/:]+(?<!:)/g) || [],
        }),
    ],
};
