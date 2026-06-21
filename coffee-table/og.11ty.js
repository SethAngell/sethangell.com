import { DateTime } from "luxon";
import { renderOgCard } from "../_lib/og-card.js";

export default class {
	data() {
		return {
			permalink: "/coffee-table/og.png",
			eleventyExcludeFromCollections: true,
		};
	}

	async render(data) {
		const items = data.collections.coffeeTable || [];
		const dates = items
			.filter((it) => it.data.active !== false && it.data.added)
			.map((it) => new Date(it.data.added));
		const updated = dates.length
			? DateTime.fromJSDate(new Date(Math.max(...dates)), {
					zone: "utc",
				}).toFormat("LLLL yyyy")
			: "";
		return renderOgCard({
			title: "The Coffee Table",
			kickerPath: "/coffee-table",
			author: "Seth Angell",
			trailing: updated ? `Updated ${updated}` : "DoubleL Press",
		});
	}
}
