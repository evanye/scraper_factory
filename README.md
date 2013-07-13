SCRAPE FACTORY, a General Web Scraper
Evan Ye, Kiran Vodrahalli, Lauren Falzarano, David Eng
LinkedIn Hackathon 2013

Description: Specify a site you want to scrape, and what information you want. We provide a graphical web-based interface for you to interactively create a customized web scraper.
Scope and Known Bugs: Currently works really well for very simple websites (pre-CSS) and in general, webpages organized as lists (like Buzzfeed and Hacker News). The power of our approach lies in the sudo-general way (very hacky) we approached the web scraping-- we tried to isolate only the key html/css code that mapped to the desired output. Good news is, it happens that these list websites are designed in a way that is similar from the point of view of our approach, which is why it works really well. On websites not designed in this manner, our hack won't perform very well. This is the first iteration of a tool meant to be able to scrape any website whatsoever (a pretty big project!)
