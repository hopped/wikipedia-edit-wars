# wikipedia-edit-wars

> Detecting edit wars in Wikipedia by analyzing the article's history.


## Motivation

In 2008, I wrote my Bachelor thesis about automatically detecting edit wars in
Wikipedia. Back then, I produced a ton of static Java code. This project shall
be used to rewrite and redesign the code using Python focusing on an online
scenario for monitoring edit wars currently happening.


## Background

You can read more about edit wars on [Wikipedia][1], or read about my approach
on detecting edit wars in my publication (in German):
[Automatische Erkennung von Bearbeitungskonflikten in Wikipedia][2].


## Current progress

Until now, it is just some prototyping. By executing `demo.py`, the sample
Wikipedia XML history is parsed, and duplicates (a series of insertion/delete
pairs) are detected. This is a basic benchmark.


## Authors

**Dennis Hoppe**

+ [github/hopped](https://github.com/hopped)


## License
Copyright 2014 Dennis Hoppe.

[MIT License](LICENSE).


[1]: http://en.wikipedia.org/wiki/Wikipedia:Edit-war
[2]: http://www.uni-weimar.de/medien/webis/teaching/theses/hoppe_2008.pdf
