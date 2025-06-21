const config = {
  tabWidth: 4,
  useTabs: true,

  plugins: ["prettier-plugin-jinja-template"],
  overrides: [
    {
      files: ["*.njk"],
      options: {
        parser: "jinja-template",
      },
    },
  ],
};

export default config;
