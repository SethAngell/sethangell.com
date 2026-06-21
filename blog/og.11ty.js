import { renderOgCard } from "../_lib/og-card.js";

export default class {
	data() {
		return {
			pagination: {
				data: "collections.blog",
				size: 1,
				alias: "post",
				before: (data) => data.filter((post) => !post.data.draft),
			},
			permalink: (data) => `/blog/og/${data.post.fileSlug}.png`,
			eleventyExcludeFromCollections: true,
		};
	}

	async render({ post }) {
		return renderOgCard({
			title: post.data.title,
			author: "Seth Angell",
			date: post.date,
		});
	}
}
