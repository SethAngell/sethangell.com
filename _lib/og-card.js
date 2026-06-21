import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import satori from "satori";
import { Resvg } from "@resvg/resvg-js";
import { DateTime } from "luxon";

const fontsDir = path.join(
	path.dirname(fileURLToPath(import.meta.url)),
	"..",
	"_fonts",
);
const newsreader500 = fs.readFileSync(
	path.join(fontsDir, "Newsreader-Medium.ttf"),
);
const mono400 = fs.readFileSync(
	path.join(fontsDir, "JetBrainsMono-Regular.ttf"),
);
const mono500 = fs.readFileSync(
	path.join(fontsDir, "JetBrainsMono-Medium.ttf"),
);

const fonts = [
	{ name: "Newsreader", data: newsreader500, weight: 500, style: "normal" },
	{ name: "JetBrains Mono", data: mono400, weight: 400, style: "normal" },
	{ name: "JetBrains Mono", data: mono500, weight: 500, style: "normal" },
];

function div(style, children) {
	return { type: "div", props: { style, children } };
}

export async function renderOgCard({
	title,
	author = "Seth Angell",
	date,
	trailing,
	kickerPath = "/blog",
}) {
	const dateStr =
		trailing ??
		DateTime.fromJSDate(date, { zone: "utc" }).toFormat("LLLL d, yyyy");
	const titleSize = title.length > 48 ? 64 : 82;

	const node = div(
		{
			width: 1200,
			height: 630,
			display: "flex",
			flexDirection: "column",
			justifyContent: "space-between",
			padding: "74px 84px",
			backgroundColor: "#FCF7E9",
			fontFamily: "JetBrains Mono",
		},
		[
			div(
				{
					display: "flex",
					fontFamily: "JetBrains Mono",
					fontWeight: 400,
					fontSize: 19,
					letterSpacing: "0.18em",
					textTransform: "uppercase",
					color: "#BC601B",
				},
				[
					{ type: "span", props: { children: "DoubleL Press" } },
					{
						type: "span",
						props: { style: { color: "#D9B68C", padding: "0 10px" }, children: "·" },
					},
					{ type: "span", props: { children: kickerPath } },
				],
			),
			div({ display: "flex", flexDirection: "column" }, [
				div(
					{
						width: 60,
						height: 4,
						borderRadius: 2,
						backgroundColor: "#E7873C",
						marginBottom: 30,
						display: "flex",
					},
					[],
				),
				div(
					{
						fontFamily: "Newsreader",
						fontWeight: 500,
						fontSize: titleSize,
						lineHeight: 1.04,
						letterSpacing: "-0.022em",
						color: "#211D19",
						maxWidth: 1010,
						display: "flex",
					},
					[{ type: "span", props: { children: title } }],
				),
			]),
			div(
				{
					display: "flex",
					flexDirection: "row",
					alignItems: "center",
					fontFamily: "JetBrains Mono",
					fontSize: 23,
					color: "#6E6354",
				},
				[
					{
						type: "span",
						props: {
							style: { color: "#231E1A", fontWeight: 500 },
							children: author,
						},
					},
					div(
						{
							width: 5,
							height: 5,
							borderRadius: 5,
							backgroundColor: "#D9B68C",
							margin: "0 18px",
							display: "flex",
						},
						[],
					),
					{ type: "span", props: { children: dateStr } },
				],
			),
		],
	);

	const svg = await satori(node, { width: 1200, height: 630, fonts });
	const resvg = new Resvg(svg, { fitTo: { mode: "width", value: 1200 } });
	return resvg.render().asPng();
}
