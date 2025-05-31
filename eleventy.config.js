import { eleventyImageTransformPlugin } from "@11ty/eleventy-img";
import CleanCSS from "clean-css";

export default function (eleventyConfig) {
  eleventyConfig.addPassthroughCopy("./_assets")
  
  eleventyConfig.addWatchTarget("./_styles/");
}
