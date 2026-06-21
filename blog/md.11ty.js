// Serves each blog post as plain Markdown at /blog/<slug>.md — "view source"
// for the post. Reconstructs a clean document from front-matter + body, since
// the title/hero/hook were moved into front-matter during the readability work.
export default class {
	data() {
		return {
			pagination: {
				data: "collections.blog",
				size: 1,
				alias: "post",
				before: (data) => data.filter((post) => !post.data.draft),
			},
			permalink: (data) => `/blog/${data.post.fileSlug}.md`,
			eleventyExcludeFromCollections: true,
		};
	}

	render({ post }) {
		const d = post.data;
		const parts = [`# ${d.title}`];
		if (d.heroImage) parts.push(`![${d.heroAlt || ""}](${d.heroImage})`);
		if (d.hook) parts.push(`> ${d.hook}`);
		const body = (post.rawInput || "").trim();
		if (body) parts.push(body);
		return parts.join("\n\n") + "\n";
	}
}
