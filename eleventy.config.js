import { DateTime } from "luxon";
import { feedPlugin } from "@11ty/eleventy-plugin-rss";

export default function (eleventyConfig) {
	eleventyConfig.addPreprocessor("drafts", "*", (data, content) => {
		if (data.draft && process.env.ELEVENTY_RUN_MODE === "build") {
			return false;
		}
	});
	eleventyConfig.addPassthroughCopy("./_assets");
	eleventyConfig.addPassthroughCopy("./humans.txt");
	eleventyConfig.addFilter("simple-date", (date) => {
		return DateTime.fromJSDate(date).toFormat("yyyy.MM.dd");
	});
	eleventyConfig.addFilter("eloquent-date", (date) => {
		const dt = DateTime.fromJSDate(date, { zone: "utc" });
		const getOrdinal = (n) => {
			if (n >= 11 && n <= 13) return "th";
			switch (n % 10) {
				case 1:
					return "st";
				case 2:
					return "nd";
				case 3:
					return "rd";
				default:
					return "th";
			}
		};
		return `${dt.toFormat("EEEE, LLLL")} ${dt.day}${getOrdinal(dt.day)}, ${dt.year}`;
	});

	eleventyConfig.addFilter("readingTime", (content) => {
		if (!content) return "";
		const text = String(content).replace(/<[^>]*>/g, " ");
		const words = text.split(/\s+/).filter(Boolean).length;
		const minutes = Math.max(1, Math.round(words / 200));
		return `${minutes} min read`;
	});

	eleventyConfig.addFilter("metaDate", (date) => {
		return DateTime.fromJSDate(date, { zone: "utc" }).toFormat(
			"EEEE, LLLL d yyyy",
		);
	});

	eleventyConfig.addCollection("blog", function (collectionApi) {
		return collectionApi
			.getFilteredByGlob("./blog/**/*.md")
			.filter(
				(post) =>
					!(post.data.draft && process.env.ELEVENTY_RUN_MODE === "build"),
			)
			.sort((a, b) => b.date - a.date);
	});

	eleventyConfig.addPlugin(feedPlugin, {
		type: "rss",
		outputPath: "/feed.rss",
		collection: {
			name: "blog",
			limit: 0,
		},
		metadata: {
			language: "en",
			title: "DoubleL Press",
			subtitle: "Musings",
			base: "https://sethangell.com",
			author: {
				name: "Seth Angell",
				email: "seth@sethangell.com",
			},
		},
	});

	eleventyConfig.addWatchTarget("./_styles/");
}
