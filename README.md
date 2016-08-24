# Crawler
Python Web Crawler - Work in Progress. Inspired by 'Bucky' Roberts.

A multi-thread webpage crawler that, as of now, crawls all links within domain name.
  (i.e. on example.com, follows all links 'example.com/sample.index'. Ignores foreign links 'facebook.com/whatever'.)

Planned improvements:

- Command-line option parser.
- Create list of ignored external links
- Create logfile functionality.
- Update to use 'Requests' library. Urllib is a standard, but Requests is excellent.

Known Issues:
- Occasional KeyError when executing line 39 of spider.py 'Spider.queue.remove(page_url)'.
- Above KeyError occurs less often when running fewer threads.
- Still too close to tutorial product.