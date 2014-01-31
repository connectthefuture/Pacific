import re


PARSE_STATIC_ASSETS_RE = re.compile('asset\s+(?P<name>[0-9a-z\.]+)', re.IGNORECASE)

def parse_static_assets(indent_level, current_line, matched, source, parsers):
    match = PARSE_STATIC_ASSETS_RE.match(current_line.strip())
    asset_name = match.group('name')
    return asset_name, indent_level, '', source


PLIMDLS_PARSERS = (
    (PARSE_STATIC_ASSETS_RE, parse_static_assets),
)
