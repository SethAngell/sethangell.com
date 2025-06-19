---
layout: blogTemplate.njk
title: "Salesforce At Scale: Introducing Some Hierarchy"
description: Despite what most tutorials will show, a more traditional folder hierarchy is possible in Salesforce projects. 
date: 2025-06-20
tags: [post, Salesforce At Scale]
---

Your typical Salesforce project probably isn't massive. Internal apps, one off solutions, even small ISV offerings can probably get away with the traditional flat directory structure that SFDX pushes you towards. 

But in the spirit of this series that becomes untenable as your codebase _and_ team grows. Eventually, trying to sift through hundreds of Apex class files to find your specific controller can become a nightmare. 
