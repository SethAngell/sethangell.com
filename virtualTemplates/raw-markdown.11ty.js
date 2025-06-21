import { readFileSync } from "fs";
import path from "path";

export default class {
  data() {
    return {
      pagination: {
        data: "collections.post",
        size: 1,
        alias: "post",
      },
      permalink: ({ post }) => post.page.filePathStem + ".md",
      layout: null,
      contentType: "text/plain",
      eleventyExcludeFromCollections: true,
    };
  }

  render({ post }) {
    const inputPath = path.resolve(process.cwd(), post.page.inputPath);
    return readFileSync(inputPath, "utf-8");
  }
}