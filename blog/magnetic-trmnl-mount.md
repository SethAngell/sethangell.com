---
layout: blogTemplate.njk
title: "Iterative (Physical) Design: A Mount For My TRMNL"
description: I'm really into the TRMNL recently. It's an E-Ink screen with tons of integrations that displays information you might want - at a slower pace. Calendars, ToDo lists, the weather, etc. Naturally it made sense to live on the fridge, which meant I needed a mount...
date: 2025-06-19
tags: [post, product design]
meta_title: "Iterative (Physical) Design: A Mount For My TRMNL"
meta_url: https://sethangell.com/blog/magnetic-trmnl-mount.md
meta_site_name: DoubleL Press
meta_image: /_assets/magnetic-trmnl-mount-cover-image.jpeg
---

![A top down image of my two TRMNLs E-Ink devices on my workbench. One is displaying my Github statistics while the other has been flipped upside down to show the magnetic mount on the back. Scattered around the rectangular E-Ink displays are the various test prints I performed to dial in the design. This is all sitting atop a black, self-healing cutting mat.](/_assets/magnetic-trmnl-mount-cover-image.jpeg "A collection of attempts")

# Iterative (Physical) Design: A Mount For My TRMNL

On the recommendation of Casey from [ATP](https://atp.fm), I recently picked up a couple of TRMNL E-Ink displays. They're really neat little gadgets - a simple E-Ink display that syncs with all of your favorite services to display info in a clean and simple manner. I've only had mine for a month now, but I've loved having Github stats, Todoist lists, and my calender displayed on my desk. They also have a pretty robust developer framework for writing your own plugins. I'll be digging into that real soon. If you have any interest, they set me up with a referral code ([sethangell](https://usetrmnl.com?ref=sethangell)) that gets you $10 off.

While I love the TRMNL on my desk, I really wanted the second device to act as more of a "Family Status Board" in our kitchen. For a variety of reasons (mostly Maddi and I's love for single-use appliances), counter space is a bit limited. But you know what was surprisingly empty?

![An image of my TRMNL mounted in the top right corner of my fridge. It is display a grid of data, where the left side has our calender and the right side is split between pending deliveries and the current weather. You can also see our Wrightsville Beach, equality, and fake plant magnets in the image](/_assets/trmnl-on-the-fridge.jpeg)

The fridge. 15 square feet of magnetic surface, ripe for the taking.

I was really excited to work on this mount. I've dabbled in 3d printing for the last five years or so, but I only got serious about learning Fusion360 in the past couple months. Now given my day job as a software engineer, I'm already well aware of the joys that a tight feedback loop can bring. It's part of the reason frontend development can be so fun (or painful depending on the day).

However, there is something so satisfying about that iterative development which generates a physical object each time! With how fast my [P1S](https://bambulab.com/en-us/p1) prints, my cycle time from Fusion360 export -> test fit on the TRMNL was like 15 minutes. This was great for getting all of the dimensions dialed in.

In the end I'm pretty happy with the result. Magnets are embedded within the model which attach to the fridge, and utilizes 3 points of contact to secure the mount to the back of the display. You can check it out [here](https://makerworld.com/en/models/1513288-magnetic-trmnl-mount#profileId-1584851).
