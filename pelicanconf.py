# Articles

ARTICLE_EXCLUDES = []
ARTICLE_PATHS = ["articles"]
DEFAULT_CATEGORY = "różności"
DISPLAY_CATEGORIES_ON_MENU = True
SUMMARY_END_SUFFIX = "…"
SUMMARY_MAX_LENGTH = 50
USE_FOLDER_AS_CATEGORY = True

# Caching

CACHE_CONTENT = False
CACHE_PATH = "cache"
CHECK_MODIFIED_METHOD = "mtime"
CONTENT_CACHING_LAYER = "reader"
DELETE_OUTPUT_DIRECTORY = False
GZIP_CACHE = True
LOAD_CONTENT_CACHE = False

# Identification

AUTHOR = "Radosław Ganczarek"
SITENAME = "Radowit"
SITEURL = "https://radowit.net/"

# JINJA

JINJA_ENVIRONMENT = {"trim_blocks": True, "lstrip_blocks": True}
JINJA_FILTERS = {}
JINJA_GLOBALS = {}
JINJA_TESTS = {}

# Local deploy

BIND = ""
PORT = 8000

# Pages

DISPLAY_PAGES_ON_MENU = True
PAGE_EXCLUDES = []
PAGE_PATHS = ["pages"]

# Plugins

PLUGIN_PATHS = []
PLUGINS = None

# Processing

FORMATTED_FIELDS = ["summary"]
IGNORE_FILES = [".#*"]
INTRASITE_LINK_REGEX = "[{|](?P<what>.*?)[|}]"
LOG_FILTER = []
OUTPUT_PATH = "output/"
OUTPUT_RETENTION = []
OUTPUT_SOURCES = False
OUTPUT_SOURCES_EXTENSION = ".text"
PATH = "content"
READERS = {}
WITH_FUTURE_DATES = True
WRITE_SELECTED = []

# Statics

STATIC_CHECK_IF_MODIFIED = False
STATIC_CREATE_LINKS = False
STATIC_EXCLUDE_SOURCES = True
STATIC_EXCLUDES = []
STATIC_PATHS = []

# Typogrify

TYPOGRIFY = True
TYPOGRIFY_DASHES = "default"
TYPOGRIFY_IGNORE_TAGS = []

# Localization

TIMEZONE = "Europe/Warsaw"
DEFAULT_LANG = "pl"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (
    ("youtube", "https://www.youtube.com/@radowit"),
    ("twitch", "https://www.twitch.tv/radowitrpg"),
    ("discord", "https://discord.com/invite/T6jFyQefaw"),
    ("reddit", "https://www.reddit.com/r/ErpegoweRozmaitosci/"),
    ("soundcloud", "https://soundcloud.com/radowitgra"),
    ("instagram", "https://www.instagram.com/radoslaw_jan/"),
    ("facebook", "https://www.facebook.com/radowit"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
