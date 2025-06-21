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
      permalink: ({ post }) => {
        const inputPath = post.page.inputPath;
        const isMarkdown = inputPath.endsWith(".md");
        const isInBlog = inputPath.includes(path.join("blog", path.sep));

        if (isMarkdown && isInBlog) {
          return post.page.filePathStem + ".md";
        }

        return post.page.filePathStem + "/";
      },
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