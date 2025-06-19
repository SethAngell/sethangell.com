import { DateTime } from "luxon";

export default function (eleventyConfig) {
  eleventyConfig.addPassthroughCopy("./_assets")
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
  eleventyConfig.addWatchTarget("./_styles/");
}
