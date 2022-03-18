---
title: "This is a template for an assignment using Test Informed Learning with Examples"
author:  Birger Keys, Shō Christian, Phoebe Schneijder
summary: >
	Write a good summary for your assignment here.
  You can use multiple lines of text if you want to.
prerequisites: ['object orientation (OO) > objects > instantiation']
concept practised: ['expressions > operators > logical operators', 'data > user-defined structures > graphs', 'object orientation (OO) > Inheritance > duck typing (polymorphism)']
target audience: ['CS0', 'CS1']
license: "CC-BY"
...

# This is a template for an assignment using Test Informed Learning with Examples
{:.no_toc} 
 
By [Birger Keys](https://birgerkeys.com), [Shō Christian](https://orcid.org/0000-0000-0000-0000) and [Phoebe Schneijder](mailto:Phoebe.Schneijder@some-university.edu).

- Table of contents
{:toc}

## How to use this template

First, thank you for reading this. This means you are creating a TILEd assignment for the repository. Great! We welcome additions so that we can all benefit from each other's knowledge and improve software testing education one step at the time! 

Please use this template with all the information about you and your assignment. You can describe the assignment, add for example handouts, source code, images, instructions for the lecturer et cetera. This will be transformed into a webpage with your assignment and put on the repository website.

These are the steps you need to take to do this:

1. Replace everything in here with content related to the assignment, starting with the `YAML` header on the top of the page. You can use Markdown in the body to structure and describe the assignment. It is possible to include images, code listings and links to files or other pages. If you are not familiar with Markdown, please look at the [GitHub guide](https://guides.github.com/features/mastering-markdown/) on how to use Markdown.
2. Describe the assignment as clearly as possible, provide examples and one or more solutions to be used as reference.
3. Put all related files in the folder together with this file. Make sure you link to the files from this markdown file.

If you need any help, don't hesitate to contact the repository maintainers.

## YAML Header

The [YAML](https://yaml.org/spec/1.2.2/) header on top of the file provides metadata information about the assignment. It is used to make the assignment easier to be found in automatically generated indexes and search engines.

The header consists of the following fields:

Title
: A Markdown-superset converter

Author
: One or more authors of the assignment, preferably with their e-mail addresses.

Summary
: A clear and concise summary of the assignment. This can be multiple lines of text.

Prerequisites
: A list of zero or more concepts that describe the prior knowledge that students need to have in order to complete the assignments. We insist that tags from the [blueprint](blueprint.md) are used such that exercises are findable, and it is easier to evaluate whether they fit into a specific phase of a course. Since the taxonomy is hierarchical, it is important to specify the whole path to the concept in the taxonomy, separating each step with a `>` character. For example: `data > type conversion > casting` instead of `casting`.

Concepts practiced
: A list of one or more concepts that students will practice with in this exercise. Again we insist on using the tags from the [blueprint](blueprint.md). Since the taxonomy is hierarchical, it is important to specify the whole path to the concept in the taxonomy, separating each step with a `>` character. For example: `data > type conversion > casting` instead of `casting`.

Target audience
: This can be described in terms of typical undergraduate courses, such as CS1 or CS50. 

License
: The license property provides the name of the license under which rights to use this assignment are granted. If omitted, the default is the least restrictive Creative Commons license, the Attribution or CC-BY.
