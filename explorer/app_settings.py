from django.conf import settings

# The 'correct' configuration for Explorer going forward and for new installs looks like:

# EXPLORER_CONNECTIONS = {
#   'Original Database': 'my_important_database_readonly_connection',
#   'Client Database 2': 'other_database_connection'
# }
# EXPLORER_DEFAULT_CONNECTION = 'my_important_database_readonly_connection'

EXPLORER_CONNECTIONS = getattr(settings, 'EXPLORER_CONNECTIONS', {})
EXPLORER_DEFAULT_CONNECTION = getattr(settings, 'EXPLORER_DEFAULT_CONNECTION', None)

# Change the behavior of explorer
EXPLORER_SQL_BLACKLIST = getattr(settings, 'EXPLORER_SQL_BLACKLIST', ('ALTER',
                                                                      'RENAME ',
                                                                      'DROP',
                                                                      'TRUNCATE',
                                                                      'INSERT INTO',
                                                                      'UPDATE',
                                                                      'REPLACE',
                                                                      'DELETE',
                                                                      'CREATE TABLE',
                                                                      'GRANT',
                                                                      'OWNER TO'))

EXPLORER_SQL_WHITELIST = getattr(settings, 'EXPLORER_SQL_WHITELIST', ('CREATED',
                                                                      'UPDATED',
                                                                      'DELETED',
                                                                      'REGEXP_REPLACE'))

EXPLORER_DEFAULT_ROWS = getattr(settings, 'EXPLORER_DEFAULT_ROWS', 1000)

EXPLORER_SCHEMA_EXCLUDE_TABLE_PREFIXES = getattr(settings, 'EXPLORER_SCHEMA_EXCLUDE_TABLE_PREFIXES', ('auth_',
                                                                                                      'contenttypes_',
                                                                                                      'sessions_',
                                                                                                      'admin_'))

EXPLORER_SCHEMA_INCLUDE_TABLE_PREFIXES = getattr(settings, 'EXPLORER_SCHEMA_INCLUDE_TABLE_PREFIXES', None)
EXPLORER_SCHEMA_INCLUDE_VIEWS = getattr(settings, 'EXPLORER_SCHEMA_INCLUDE_VIEWS', False)

EXPLORER_TRANSFORMS = getattr(settings, 'EXPLORER_TRANSFORMS', [])
EXPLORER_PERMISSION_VIEW = getattr(settings, 'EXPLORER_PERMISSION_VIEW', lambda u: u.is_staff)
EXPLORER_PERMISSION_CHANGE = getattr(settings, 'EXPLORER_PERMISSION_CHANGE', lambda u: u.is_staff)
EXPLORER_RECENT_QUERY_COUNT = getattr(settings, 'EXPLORER_RECENT_QUERY_COUNT', 10)
EXPLORER_ASYNC_SCHEMA = getattr(settings, 'EXPLORER_ASYNC_SCHEMA', False)

EXPLORER_DATA_EXPORTERS = getattr(settings, 'EXPLORER_DATA_EXPORTERS', [
    ('csv', 'explorer.exporters.CSVExporter'),
    ('excel', 'explorer.exporters.ExcelExporter'),
    ('json', 'explorer.exporters.JSONExporter'),

])
CSV_DELIMETER = getattr(settings, "EXPLORER_CSV_DELIMETER", ",")

# API access
EXPLORER_TOKEN = getattr(settings, 'EXPLORER_TOKEN', 'CHANGEME')

# These are callable to aid testability by dodging the settings cache.
# There is surely a better pattern for this, but this'll hold for now.
EXPLORER_GET_USER_QUERY_VIEWS = lambda: getattr(settings, 'EXPLORER_USER_QUERY_VIEWS', {})
EXPLORER_TOKEN_AUTH_ENABLED = lambda: getattr(settings, 'EXPLORER_TOKEN_AUTH_ENABLED', False)

# Async task related. Note that the EMAIL_HOST settings must be set up for email to work.
ENABLE_TASKS = getattr(settings, "EXPLORER_TASKS_ENABLED", False)
S3_ACCESS_KEY = getattr(settings, "EXPLORER_S3_ACCESS_KEY", None)
S3_SECRET_KEY = getattr(settings, "EXPLORER_S3_SECRET_KEY", None)
S3_BUCKET = getattr(settings, "EXPLORER_S3_BUCKET", None)
FROM_EMAIL = getattr(settings, 'EXPLORER_FROM_EMAIL', 'django-sql-explorer@example.com')

UNSAFE_RENDERING = getattr(settings, "EXPLORER_UNSAFE_RENDERING", False)
