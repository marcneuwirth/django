from collections import namedtuple
import re

# Valid query types (a dictionary is used for speedy lookups).
QUERY_TERMS = dict([(x, None) for x in (
    'exact', 'iexact', 'contains', 'icontains', 'gt', 'gte', 'lt', 'lte', 'in',
    'startswith', 'istartswith', 'endswith', 'iendswith', 'range', 'year',
    'month', 'day', 'week_day', 'isnull', 'search', 'regex', 'iregex',
)])

# Size of each "chunk" for get_iterator calls.
# Larger values are slightly faster at the expense of more storage space.
GET_ITERATOR_CHUNK_SIZE = 100

# Separator used to split filter strings apart.
LOOKUP_SEP = '__'

# Constants to make looking up tuple values clearer.
# Join lists (indexes into the tuples that are values in the alias_map
# dictionary in the Query class).
JoinInfo = namedtuple('JoinInfo',
                      'table_name rhs_alias join_type lhs_alias '
                      'lhs_join_col rhs_join_col nullable')

# How many results to expect from a cursor.execute call
MULTI = 'multi'
SINGLE = 'single'

ORDER_PATTERN = re.compile(r'\?|[-+]?[.\w]+$')
ORDER_DIR = {
    'ASC': ('ASC', 'DESC'),
    'DESC': ('DESC', 'ASC'),
}
