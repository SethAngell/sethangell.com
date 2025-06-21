import { DateTime } from "luxon";
import { feedPlugin } from "@11ty/eleventy-plugin-rss";


export default function (eleventyConfig) {
  eleventyConfig.setTemplateFormats([
    "njk", "md", "11ty.js", 
  ]);

  eleventyConfig.addPreprocessor("drafts", "*", (data, content) => {
		if(data.draft && process.env.ELEVENTY_RUN_MODE === "build") {
			return false;
		}
	});
  eleventyConfig.addPassthroughCopy("./_assets")
  eleventyConfig.addPassthroughCopy("./humans.txt")
  eleventyConfig.addFilter("simple-date", date => {
    return DateTime.fromJSDate(date).toFormat("yyyy.MM.dd");
  });
  eleventyConfig.addFilter("eloquent-date", date => {
    const dt = DateTime.fromJSDate(date, { zone: 'utc' })
    const getOrdinal = (n) => {
      if (n >= 11 && n <= 13) return 'th';
      switch (n % 10) {
        case 1: return 'st';
        case 2: return 'nd';
        case 3: return 'rd';
        default: return 'th';
      }
    }
    return `${dt.toFormat('EEEE, LLLL')} ${dt.day}${getOrdinal(dt.day)}, ${dt.year}`;
  })

  eleventyConfig.addPlugin(feedPlugin, {
		type: "rss", // or "rss", "json"
		outputPath: "/feed.rss",
		collection: {
			name: "posts", // iterate over `collections.posts`
			limit: 0,     // 0 means no limit
		},
		metadata: {
			language: "en",
			title: "DoubleL Press",
			subtitle: "Musings",
			base: "https://sethangell.com",
			author: {
				name: "Seth Angell",
				email: "seth@sethangell.com", 
			}
		}
	});


  eleventyConfig.addWatchTarget("./_styles/");
}
