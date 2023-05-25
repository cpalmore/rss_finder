# This function searches a webpage for rss feeds, and prints any that are found.
# note: grep option --perl-regexp is only available in GNU grep

# download the indicated webpage for analysis
wget \
--quiet \
--output-document=- \
${1} \
|

# search HTML with Perl/regex for URLs
grep \
--only-matching \
--perl-regexp '(?<=href=")[^"]*(?=")' \
|

# search URLs for expressions indicating RSS feeds
grep 'feed\|rss\|xml\|atom\|asp\|application/rss'


