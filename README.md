# uO API Dependency Tree Visualizer

A project to provide visual descriptions of course dependency trees, as generated in [uoapi](http://tlia.ca/uoapi).

Project generated with [krait cli](http://tlia.ca/krait)


-------

## Project Roadmap

1. Given a course data directory with all the subjects required scraped by `uoapi`, and a single course, build the depth-1 dependency tree with `graphviz`
1. Given a course data directory with all the subjects required scraped by `uoapi`, and a single course, build the depth-n dependency tree with `graphviz`
1. Given a course data directory with all the subjects required scraped by `uoapi`, and a list of courses, build the depth-n dependency forest with `graphviz`
1. Given a list of courses, scrape subject data for all required subjects to build the depth-n dependency forest.
1. Given a list of courses, scrape subject data for all required subjects and build a cache of the subject data to use for future dependency forests.
1. Allow for subject cache data to be refreshed after a certain timeout
1. Provide CLI option to force cache refresh


## Dependencies

### 3rd Party
1. Click - CLI
1. pygraphviz - Rendering dependency trees
1. uoapi - Course data and dependency trees
