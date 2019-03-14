# AUTOGENERATED BY EdgeDB WITH
#     $ edb gen-pygments-grammars edgeql


class EdgeQL:
    reserved_keywords = (
        "__source__",
        "__subject__",
        "__type__",
        "alter",
        "analyze",
        "and",
        "anyarray",
        "anytuple",
        "anytype",
        "begin",
        "case",
        "commit",
        "configure",
        "create",
        "deallocate",
        "declare",
        "delete",
        "detached",
        "discard",
        "distinct",
        "do",
        "drop",
        "else",
        "empty",
        "end",
        "execute",
        "exists",
        "explain",
        "extending",
        "fetch",
        "filter",
        "for",
        "function",
        "get",
        "global",
        "grant",
        "group",
        "if",
        "ilike",
        "import",
        "in",
        "insert",
        "introspect",
        "is",
        "like",
        "limit",
        "listen",
        "load",
        "lock",
        "match",
        "module",
        "move",
        "not",
        "notify",
        "offset",
        "optional",
        "or",
        "order",
        "over",
        "partition",
        "prepare",
        "raise",
        "refresh",
        "reindex",
        "release",
        "reset",
        "revoke",
        "rollback",
        "select",
        "set",
        "start",
        "typeof",
        "union",
        "update",
        "variadic",
        "when",
        "with",
    )
    unreserved_keywords = (
        "abstract",
        "after",
        "alias",
        "all",
        "allow",
        "as",
        "asc",
        "assignment",
        "attribute",
        "before",
        "by",
        "cardinality",
        "cast",
        "committed",
        "config",
        "constraint",
        "database",
        "default",
        "deferrable",
        "deferred",
        "delegated",
        "desc",
        "explicit",
        "expression",
        "final",
        "first",
        "from",
        "implicit",
        "index",
        "infix",
        "inheritable",
        "inherited",
        "into",
        "isolation",
        "last",
        "link",
        "migration",
        "multi",
        "named",
        "of",
        "on",
        "only",
        "operator",
        "postfix",
        "prefix",
        "property",
        "read",
        "rename",
        "repeatable",
        "required",
        "restrict",
        "role",
        "savepoint",
        "scalar",
        "serializable",
        "session",
        "single",
        "source",
        "system",
        "target",
        "ternary",
        "then",
        "to",
        "transaction",
        "type",
        "using",
        "view",
        "write",
    )
    bool_literals = (
        "false",
        "true",
    )
    type_builtins = (
        "Object",
        "anyfloat",
        "anyint",
        "anyreal",
        "anyscalar",
        "array",
        "bool",
        "bytes",
        "datetime",
        "decimal",
        "float32",
        "float64",
        "int16",
        "int32",
        "int64",
        "json",
        "naive_date",
        "naive_datetime",
        "naive_time",
        "sequence",
        "str",
        "timedelta",
        "tuple",
        "uuid",
    )
    module_builtins = (
        "cfg",
        "math",
        "schema",
        "std",
        "stdgraphql",
        "sys",
    )
    constraint_builtins = (
        "enum",
        "exclusive",
        "expression",
        "len_constraint",
        "max",
        "max_ex",
        "max_len",
        "min",
        "min_ex",
        "min_len",
        "regexp",
    )
    fn_builtins = (
        "abs",
        "advisory_lock",
        "advisory_unlock",
        "advisory_unlock_all",
        "all",
        "any",
        "array_agg",
        "array_get",
        "array_unpack",
        "bytes_get_bit",
        "ceil",
        "contains",
        "count",
        "date_get",
        "datetime_current",
        "datetime_get",
        "datetime_of_statement",
        "datetime_of_transaction",
        "datetime_trunc",
        "enumerate",
        "find",
        "floor",
        "json_array_unpack",
        "json_get",
        "json_object_unpack",
        "json_typeof",
        "len",
        "lg",
        "ln",
        "log",
        "max",
        "mean",
        "min",
        "random",
        "re_match",
        "re_match_all",
        "re_replace",
        "re_test",
        "round",
        "sleep",
        "stddev",
        "stddev_pop",
        "str_lower",
        "str_lpad",
        "str_ltrim",
        "str_repeat",
        "str_rpad",
        "str_rtrim",
        "str_title",
        "str_trim",
        "str_upper",
        "sum",
        "time_get",
        "timedelta_get",
        "timedelta_trunc",
        "to_datetime",
        "to_decimal",
        "to_float32",
        "to_float64",
        "to_int16",
        "to_int32",
        "to_int64",
        "to_json",
        "to_naive_date",
        "to_naive_datetime",
        "to_naive_time",
        "to_str",
        "to_timedelta",
        "uuid_generate_v1mc",
        "var",
        "var_pop",
    )
    operators = (
        "!=",
        "%",
        "*",
        "+",
        "++",
        "-",
        "/",
        "//",
        ":=",
        "<",
        "<=",
        "=",
        ">",
        ">=",
        "?!=",
        "?=",
        "??",
        "^",
    )
    navigation = (
        ".<",
        ".>",
        "@",
        ".",
    )
