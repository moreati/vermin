from .multidict import multidict

# Module requirements: name -> min version per major or None if N.A.
MOD_REQS = {
  "ConfigParser": (2.0, None),
  "DocXMLRPCServer": (2.3, None),
  "HTMLParser": (2.2, None),
  "Queue": (2.0, None),
  "SimpleXMLRPCServer": (2.2, None),
  "SocketServer": (2.0, None),
  "__builtin__": (2.0, None),
  "__future__": (2.1, 3.0),
  "_dummy_thread": (None, 3.0),
  "_markupbase": (None, 3.0),
  "_winreg": (2.0, None),
  "abc": (2.6, 3.0),
  "argparse": (2.7, 3.2),
  "ast": (2.6, 3.0),
  "asyncio": (None, 3.4),
  "atexit": (2.0, 3.0),
  "builtins": (None, 3.0),
  "bz2": (2.3, 3.0),
  "cProfile": (2.5, 3.0),
  "cgitb": (2.2, 3.0),
  "collections": (2.4, 3.0),
  "configparser": (None, 3.0),
  "contextlib": (2.5, 3.0),
  "cookielib": (2.4, None),
  "copy_reg": (2.0, None),
  "copyreg": (None, 3.0),
  "csv": (2.3, 3.0),
  "ctypes": (2.5, 3.0),
  "datetime": (2.3, 3.0),
  "dbm.io": (None, 3.0),
  "dbm.ndbm": (None, 3.0),
  "dbm.os": (None, 3.0),
  "dbm.struct": (None, 3.0),
  "dbm.sys": (None, 3.0),
  "dbm.whichdb": (None, 3.0),
  "decimal": (2.4, 3.0),
  "difflib": (2.1, 3.0),
  "dummy_thread": (2.3, None),
  "dummy_threading": (2.3, None),
  "email": (2.2, 3.0),
  "faulthandler": (None, 3.3),
  "fractions": (2.6, 3.0),
  "functools": (2.5, 3.0),
  "future_builtins": (2.6, None),
  "hashlib": (2.5, 3.0),
  "heapq": (2.3, 3.0),
  "hmac": (2.2, 3.0),
  "hotshot": (2.2, None),
  "html": (None, 3.0),
  "htmlentitydefs": (2.0, None),
  "http": (None, 3.0),
  "http.cookiejar": (None, 3.0),
  "importlib": (2.7, 3.1),
  "inspect": (2.1, 3.0),
  "io": (2.6, 3.0),
  "ipaddress": (None, 3.3),
  "itertools": (2.3, 3.0),
  "json": (2.6, 3.0),
  "logging": (2.3, 3.0),
  "markupbase": (2.0, None),
  "md5": (2.0, None),
  "modulefinder": (2.3, 3.0),
  "msilib": (2.5, 3.0),
  "multiprocessing": (2.6, 3.0),
  "new": (2.0, None),
  "numbers": (2.6, 3.0),
  "optparse": (2.3, 3.0),
  "ossaudiodev": (2.3, 3.0),
  "pickletools": (2.3, 3.0),
  "pkgutil": (2.3, 3.0),
  "platform": (2.3, 3.0),
  "pydoc": (2.1, 3.0),
  "queue": (None, 3.0),
  "repr": (2.0, None),
  "reprlib": (None, 3.0),
  "runpy": (2.5, 3.0),
  "secrets": (None, 3.6),
  "sets": (2.3, None),
  "shlex": (2.0, 3.0),
  "socketserver": (None, 3.0),
  "spwd": (2.5, 3.0),
  "sqlite3": (2.5, 3.0),
  "ssl": (2.6, 3.0),
  "string.letters": (2.0, None),
  "string.lowercase": (2.0, None),
  "string.uppercase": (2.0, None),
  "stringprep": (2.3, 3.0),
  "subprocess": (2.4, 3.0),
  "sysconfig": (2.7, 3.2),
  "tarfile": (2.3, 3.0),
  "textwrap": (2.3, 3.0),
  "timeit": (2.3, 3.0),
  "tkinter": (None, 3.0),
  "tracemalloc": (None, 3.4),
  "typing": (None, 3.5),
  "unittest": (2.1, 3.0),
  "urllib2": (2.0, None),
  "uuid": (2.5, 3.0),
  "warnings": (2.1, 3.0),
  "weakref": (2.1, 3.0),
  "winreg": (None, 3.0),
  "xmlrpc": (None, 3.0),
  "xmlrpc.client": (None, 3.0),
  "xmlrpc.server": (None, 3.0),
}

# Module member requirements: member -> (module, requirements)
MOD_MEM_REQS = multidict((
  # Classes
  ("ABC", ("abc", (None, 3.4))),
  ("AbstractContextManager", ("contextlib", (None, 3.6))),
  ("AsyncGenerator", ("typing", (None, 3.6))),
  ("Barrier", ("multiprocessing", (None, 3.3))),
  ("BoundArguments", ("inspect", (None, 3.3))),
  ("CGIXMLRPCRequestHandler", ("SimpleXMLRPCServer", (2.3, None))),
  ("ChainMap", ("typing", (None, 3.6))),
  ("ClassVar", ("typing", (None, 3.5))),
  ("Collection", ("typing", (None, 3.6))),
  ("CompletedProcess", ("subprocess", (None, 3.5))),
  ("ContextDecorator", ("contextlib", (None, 3.2))),
  ("ContextManager", ("typing", (None, 3.6))),
  ("Counter", ("collections", (2.7, 3.1))),
  ("Counter", ("typing", (None, 3.6))),
  ("Deque", ("typing", (None, 3.6))),
  ("DomainFilter", ("tracemalloc", (None, 3.6))),
  ("ExitStack", ("contextlib", (None, 3.3))),
  ("HtmlDiff", ("difflib", (2.4, 3.0))),
  ("JSONDecodeError", ("json", (None, 3.5))),
  ("LoggerAdapter", ("logging", (2.6, 3.0))),
  ("ModuleInfo", ("pkgutil", (None, 3.6))),
  ("OrderedDict", ("collections", (2.7, 3.1))),
  ("Parameter", ("inspect", (None, 3.3))),
  ("PathLike", ("os", (None, 3.6))),
  ("SSLContext", ("ssl", (2.7, 3.2))),
  ("SSLMemoryBIO", ("ssl", (None, 3.6))),
  ("SSLObject", ("ssl", (None, 3.6))),
  ("SSLSession", ("ssl", (None, 3.6))),
  ("Signature", ("inspect", (None, 3.3))),
  ("Text", ("typing", (None, 3.6))),
  ("TextTestResult", ("unittest", (2.7, 3.0))),
  ("UserDict", ("collections", (None, 3.0))),
  ("UserList", ("collections", (None, 3.0))),
  ("UserString", ("collections", (None, 3.0))),
  ("WeakMethod", ("weakref", (None, 3.4))),
  ("WeakSet", ("weakref", (2.7, 3.0))),
  ("c_bool", ("ctypes", (2.6, 3.0))),
  ("c_longdouble", ("ctypes", (2.6, 3.0))),
  ("c_ssize_t", ("ctypes", (2.7, 3.2))),
  ("catch_warnings", ("warnings", (2.6, 3.0))),
  ("defaultdict", ("collections", (2.5, 3.0))),
  ("deque", ("collections", (2.4, 3.0))),
  ("finalize", ("weakref", (None, 3.4))),
  ("namedtuple", ("collections", (2.6, 3.0))),
  ("terminal_size", ("os", (None, 3.3))),
  ("timezone", ("datetime", (None, 3.2))),
  ("unix_dialect", ("csv", (None, 3.2))),

  # Exceptions
  ("HeaderError", ("tarfile", (2.6, 3.0))),
  ("SSLEOFError", ("ssl", (2.7, 3.3))),
  ("SSLSyscallError", ("ssl", (2.7, 3.3))),
  ("SSLWantReadError", ("ssl", (2.7, 3.3))),
  ("SSLWantWriteError", ("ssl", (2.7, 3.3))),
  ("SSLZeroReturnError", ("ssl", (2.7, 3.3))),
  ("SubprocessError", ("subprocess", (None, 3.3))),
  ("TimeoutExpired", ("subprocess", (None, 3.3))),

  # Functions
  ("NewType", ("typing", (None, 3.5))),
  ("RAND_bytes", ("ssl", (None, 3.3))),
  ("RAND_pseudo_bytes", ("ssl", (None, 3.3))),
  ("_https_verify_certificates", ("ssl", (2.7, None))),
  ("accumulate", ("itertools", (None, 3.2))),
  ("addCleanup", ("unittest.TestCase", (2.7, 3.1))),
  ("addTypeEqualityFunc", ("unittest.TestCase", (2.7, 3.1))),
  ("apply_defaults", ("inspect.BoundArguments", (None, 3.6))),
  ("as_integer_ratio", ("decimal.Decimal", (None, 3.6))),
  ("assertDictContainsSubset", ("unittest.TestCase", (2.7, 3.1))),
  ("assertDictEqual", ("unittest.TestCase", (2.7, 3.1))),
  ("assertGreater", ("unittest.TestCase", (2.7, 3.1))),
  ("assertGreaterEqual", ("unittest.TestCase", (2.7, 3.1))),
  ("assertIn", ("unittest.TestCase", (2.7, 3.1))),
  ("assertIs", ("unittest.TestCase", (2.7, 3.1))),
  ("assertIsInstance", ("unittest.TestCase", (2.7, 3.2))),
  ("assertIsNone", ("unittest.TestCase", (2.7, 3.1))),
  ("assertIsNot", ("unittest.TestCase", (2.7, 3.1))),
  ("assertIsNotNone", ("unittest.TestCase", (2.7, 3.1))),
  ("assertItemsEqual", ("unittest.TestCase", (2.7, 3.1))),
  ("assertLess", ("unittest.TestCase", (2.7, 3.1))),
  ("assertLessEqual", ("unittest.TestCase", (2.7, 3.1))),
  ("assertListEqual", ("unittest.TestCase", (2.7, 3.1))),
  ("assertMultilineEqual", ("unittest.TestCase", (2.7, 3.1))),
  ("assertNotIn", ("unittest.TestCase", (2.7, 3.1))),
  ("assertNotIsInstance", ("unittest.TestCase", (2.7, 3.2))),
  ("assertNotRegex", ("unittest.TestCase", (None, 3.1))),
  ("assertNotRegexpMatches", ("unittest.TestCase", (2.7, 3.1))),
  ("assertRaisesRegexp", ("unittest.TestCase", (2.7, 3.1))),
  ("assertRegex", ("unittest.TestCase", (None, 3.1))),
  ("assertRegexpMatches", ("unittest.TestCase", (2.7, 3.1))),
  ("assertSequenceEqual", ("unittest.TestCase", (2.7, 3.1))),
  ("assertSetEqual", ("unittest.TestCase", (2.7, 3.1))),
  ("assertTupleEqual", ("unittest.TestCase", (2.7, 3.1))),
  ("canonical", ("decimal.Decimal", (2.6, 3.0))),
  ("cert_store_stats", ("ssl.SSLContext", (None, 3.4))),
  ("check_call", ("subprocess", (2.5, 3.0))),
  ("check_output", ("subprocess", (2.7, 3.1))),
  ("check_returncode", ("subprocess.CompletedProcess", (None, 3.5))),
  ("cleandoc", ("inspect", (2.6, 3.0))),
  ("clear_traps", ("decimal.Context", (None, 3.3))),
  ("cmp_to_key", ("functools", (2.7, 3.2))),
  ("combinations", ("itertools", (2.6, 3.0))),
  ("combinations_with_replacement", ("itertools", (2.7, 3.1))),
  ("commonpath", ("os.path", (None, 3.5))),
  ("compare_digest", ("hmac", (2.7, 3.3))),
  ("compare_signal", ("decimal.Decimal", (2.6, 3.0))),
  ("compare_total", ("decimal.Decimal", (2.6, 3.0))),
  ("compare_total_mag", ("decimal.Decimal", (2.6, 3.0))),
  ("compress", ("itertools", (2.7, 3.1))),
  ("compression", ("ssl", (2.7, 3.3))),
  ("conjugate", ("decimal.Decimal", (2.6, 3.0))),
  ("context_diff", ("difflib", (2.3, 3.0))),
  ("copy", ("collections.deque", (None, 3.5))),
  ("copy_abs", ("decimal.Decimal", (2.6, 3.0))),
  ("copy_negate", ("decimal.Decimal", (2.6, 3.0))),
  ("copy_sign", ("decimal.Decimal", (2.6, 3.0))),
  ("count", ("collections.deque", (2.7, 3.2))),
  ("create_decimal_from_float", ("decimal.Context", (2.7, 3.1))),
  ("create_default_context", ("ssl", (2.7, 3.4))),
  ("detach", ("io.BufferedIOBase", (2.7, 3.1))),
  ("detach", ("io.TextIOBase", (2.7, 3.1))),
  ("diff_bytes", ("difflib", (None, 3.5))),
  ("discover", ("unittest.TestLoader", (2.7, 3.2))),
  ("doCleanups", ("unittest.TestCase", (2.7, 3.1))),
  ("enable_load_extension", ("sqlite3.Connection", (2.7, 3.2))),
  ("enum_certificates", ("ssl", (2.7, 3.4))),
  ("enum_crls", ("ssl", (2.7, 3.4))),
  ("exc_clear", ("sys", (2.3, None))),
  ("exp", ("decimal.Decimal", (2.6, 3.0))),
  ("extractall", ("tarfile.TarFile", (2.5, 3.0))),
  ("field_size_limit", ("csv", (2.5, 3.0))),
  ("fileno", ("bz2.BZ2File", (None, 3.3))),
  ("find_msvcrt", ("ctypes.util", (2.6, 3.0))),
  ("fma", ("decimal.Decimal", (2.6, 3.0))),
  ("from_buffer", ("ctypes._CData", (2.6, 3.0))),
  ("from_buffer_copy", ("ctypes._CData", (2.6, 3.0))),
  ("from_float", ("decimal.Decimal", (2.7, 3.1))),
  ("fromtarfile", ("tarfile.TarInfo", (2.6, 3.0))),
  ("fsdecode", ("os", (None, 3.2))),
  ("fsencode", ("os", (None, 3.2))),
  ("fspath", ("os", (None, 3.6))),
  ("getChild", ("logging.Logger", (2.7, 3.2))),
  ("getLogRecordFactory", ("logging", (None, 3.2))),
  ("get_all_start_methods", ("multiprocessing", (None, 3.4))),
  ("get_blocking", ("os", (None, 3.5))),
  ("get_ca_certs", ("ssl.SSLContext", (None, 3.4))),
  ("get_channel_binding", ("ssl", (2.7, 3.3))),
  ("get_ciphers", ("ssl.SSLContext", (None, 3.6))),
  ("get_context", ("multiprocessing", (None, 3.4))),
  ("get_data", ("pkgutil", (2.6, 3.0))),
  ("get_default_verify_paths", ("ssl", (2.7, 3.4))),
  ("get_errno", ("ctypes", (2.6, 3.0))),
  ("get_exec_path", ("os", (None, 3.2))),
  ("get_grouped_opcodes", ("difflib.SequenceMatcher", (2.3, 3.0))),
  ("get_handle_inheritable", ("os", (None, 3.4))),
  ("get_inheritable", ("os", (None, 3.4))),
  ("get_last_error", ("ctypes", (2.6, 3.0))),
  ("get_start_method", ("multiprocessing", (None, 3.4))),
  ("get_terminal_size", ("os", (None, 3.3))),
  ("getattr_static", ("inspect", (None, 3.2))),
  ("getbuffer", ("io.BytesIO", (None, 3.2))),
  ("getcallargs", ("inspect", (2.7, 3.2))),
  ("getcheckinterval", ("sys", (2.3, 3.0))),
  ("getclosurevars", ("inspect", (None, 3.3))),
  ("getcoroutinelocals", ("inspect", (None, 3.5))),
  ("getcoroutinestate", ("inspect", (None, 3.5))),
  ("getctime", ("os.path", (2.3, 3.0))),
  ("getdefaultencoding", ("sys", (2.0, 3.0))),
  ("getdlopenflags", ("sys", (2.2, 3.0))),
  ("getenvb", ("os", (None, 3.2))),
  ("getfilesystemencoding", ("sys", (2.3, 3.0))),
  ("getgeneratorlocals", ("inspect", (None, 3.2))),
  ("getgeneratorstate", ("inspect", (None, 3.2))),
  ("getgrouplist", ("os", (None, 3.3))),
  ("getpgid", ("os", (2.3, 3.0))),
  ("getpriority", ("os", (None, 3.3))),
  ("getprofile", ("sys", (2.6, 3.0))),
  ("getresgid", ("os", (2.7, 3.0))),
  ("getresuid", ("os", (2.7, 3.0))),
  ("getsid", ("os", (2.4, 3.0))),
  ("getsizeof", ("sys", (2.6, 3.0))),
  ("gettrace", ("sys", (2.6, 3.0))),
  ("getwindowsversion", ("sys", (2.3, 3.0))),
  ("groupby", ("itertools", (2.4, 3.0))),
  ("hasHandlers", ("logging.Logger", (None, 3.2))),
  ("heappushpop", ("heapq", (2.6, 3.0))),
  ("indent", ("textwrap", (None, 3.3))),
  ("index", ("collections.deque", (None, 3.5))),
  ("initgroups", ("os", (2.7, 3.2))),
  ("insert", ("collections.deque", (None, 3.5))),
  ("is_canonical", ("decimal.Decimal", (2.6, 3.0))),
  ("is_finite", ("decimal.Decimal", (2.6, 3.0))),
  ("is_infinite", ("decimal.Decimal", (2.6, 3.0))),
  ("is_nan", ("decimal.Decimal", (2.6, 3.0))),
  ("is_normal", ("decimal.Decimal", (2.6, 3.0))),
  ("is_qnan", ("decimal.Decimal", (2.6, 3.0))),
  ("is_signed", ("decimal.Decimal", (2.6, 3.0))),
  ("is_snan", ("decimal.Decimal", (2.6, 3.0))),
  ("is_subnormal", ("decimal.Decimal", (2.6, 3.0))),
  ("is_zero", ("decimal.Decimal", (2.6, 3.0))),
  ("isabstract", ("inspect", (2.6, 3.0))),
  ("isasyncgen", ("inspect", (None, 3.6))),
  ("isasyncgenfunction", ("inspect", (None, 3.6))),
  ("isawaitable", ("inspect", (None, 3.5))),
  ("iscoroutine", ("inspect", (None, 3.5))),
  ("iscoroutinefunction", ("inspect", (None, 3.5))),
  ("isdatadescriptor", ("inspect", (2.3, 3.0))),
  ("isgenerator", ("inspect", (2.6, 3.0))),
  ("isgeneratorfunction", ("inspect", (2.6, 3.0))),
  ("isgetsetdescriptor", ("inspect", (2.5, 3.0))),
  ("ismemberdescriptor", ("inspect", (2.5, 3.0))),
  ("ismount", ("os.path", (None, 3.4))),
  ("iter_dump", ("sqlite3.Connection", (2.6, 3.0))),
  ("iterkeyrefs", ("weakref.WeakKeyDictionary", (2.5, 3.0))),
  ("itervaluerefs", ("weakref.WeakValueDictionary", (2.5, 3.0))),
  ("izip_longest", ("itertools", (2.6, 3.0))),
  ("keyrefs", ("weakref.WeakKeyDictionary", (2.5, 3.0))),
  ("keys", ("sqlite3.Row", (2.6, 3.0))),
  ("kill", ("subprocess.Popen", (2.6, 3.0))),
  ("lexists", ("os.path", (2.4, 3.0))),
  ("linux_distribution", ("platform", (2.6, 3.0))),
  ("ln", ("decimal.Decimal", (2.6, 3.0))),
  ("load_default_certs", ("ssl.SSLContext", (None, 3.4))),
  ("load_dh_params", ("ssl.SSLContext", (None, 3.3))),
  ("load_extension", ("sqlite3.Connection", (2.7, 3.2))),
  ("localcontext", ("decimal", (2.5, 3.0))),
  ("lockf", ("os", (None, 3.3))),
  ("log10", ("decimal.Decimal", (2.6, 3.0))),
  ("logb", ("decimal.Decimal", (2.6, 3.0))),
  ("logical_and", ("decimal.Decimal", (2.6, 3.0))),
  ("logical_invert", ("decimal.Decimal", (2.6, 3.0))),
  ("logical_or", ("decimal.Decimal", (2.6, 3.0))),
  ("logical_xor", ("decimal.Decimal", (2.6, 3.0))),
  ("longMessage", ("unittest.TestCase", (2.7, 3.1))),
  ("lru_cache", ("functools", (None, 3.2))),
  ("match_hostname", ("ssl", (2.7, 3.2))),
  ("maxDiff", ("unittest.TestCase", (2.7, 3.2))),
  ("max_mag", ("decimal.Decimal", (2.6, 3.0))),
  ("merge", ("heapq", (2.6, 3.0))),
  ("min_mag", ("decimal.Decimal", (2.6, 3.0))),
  ("move_to_end", ("collections.OrderedDict", (None, 3.2))),
  ("next_minus", ("decimal.Decimal", (2.6, 3.0))),
  ("next_plus", ("decimal.Decimal", (2.6, 3.0))),
  ("next_toward", ("decimal.Decimal", (2.6, 3.0))),
  ("nlargest", ("heapq", (2.4, 3.0))),
  ("nsmallest", ("heapq", (2.4, 3.0))),
  ("number_class", ("decimal.Decimal", (2.6, 3.0))),
  ("open", ("bz2", (None, 3.3))),
  ("optimize", ("pickletools", (2.6, 3.0))),
  ("partial_method", ("functools", (None, 3.4))),
  ("pbkdf2_hmac", ("hashlib", (2.7, 3.4))),
  ("peek", ("bz2.BZ2File", (None, 3.3))),
  ("permutations", ("itertools", (2.6, 3.0))),
  ("pipe2", ("os", (None, 3.3))),
  ("pop_source", ("shlex", (2.1, 3.0))),
  ("posix_fadvise", ("os", (None, 3.3))),
  ("posix_fallocate", ("os", (None, 3.3))),
  ("pread", ("os", (None, 3.3))),
  ("product", ("itertools", (2.6, 3.0))),
  ("push_source", ("shlex", (2.1, 3.0))),
  ("pwrite", ("os", (None, 3.3))),
  ("python_branch", ("platform", (2.6, 3.0))),
  ("python_implementation", ("platform", (2.6, 3.0))),
  ("python_revision", ("platform", (2.6, 3.0))),
  ("quote", ("shlex", (None, 3.3))),
  ("radix", ("decimal.Decimal", (2.6, 3.0))),
  ("read1", ("bz2.BZ2File", (None, 3.3))),
  ("readable", ("bz2.BZ2File", (None, 3.3))),
  ("readinto", ("bz2.BZ2File", (None, 3.3))),
  ("readinto1", ("io.BufferedIOBase", (None, 3.5))),
  ("readinto1", ("io.BytesIO", (None, 3.5))),
  ("readv", ("os", (None, 3.3))),
  ("realpath", ("os.path", (2.2, 3.0))),
  ("redirect_stderr", ("contextlib", (None, 3.5))),
  ("redirect_stdout", ("contextlib", (None, 3.4))),
  ("reduce", ("functools", (2.6, 3.0))),
  ("register_introspection_functions", ("SimpleXMLRPCServer.SimpleXMLRPCServer", (2.3, None))),
  ("register_introspection_functions", ("xmlrpc.server.SimpleXMLRPCServer", (None, 3.0))),
  ("relpath", ("os.path", (2.6, 3.0))),
  ("remove", ("collections.deque", (2.5, 3.0))),
  ("repeat", ("timeit", (2.6, 3.0))),
  ("reverse", ("collections.deque", (2.7, 3.2))),
  ("rotate", ("decimal.Decimal", (2.6, 3.0))),
  ("run", ("subprocess", (None, 3.5))),
  ("run_path", ("runpy", (2.7, 3.2))),
  ("scaleb", ("decimal.Decimal", (2.6, 3.0))),
  ("scrypt", ("hashlib", (None, 3.6))),
  ("seekable", ("bz2.BZ2File", (None, 3.3))),
  ("selected_alpn_protocol", ("ssl", (2.7, 3.5))),
  ("selected_npn_protocol", ("ssl", (2.7, 3.3))),
  ("send_signal", ("subprocess.Popen", (2.6, 3.0))),
  ("sendfile", ("os", (None, 3.3))),
  ("setLogRecordFactory", ("logging", (None, 3.2))),
  ("set_alpn_protocols", ("ssl.SSLContext", (2.7, 3.5))),
  ("set_blocking", ("os", (None, 3.5))),
  ("set_ecdh_curve", ("ssl.SSLContext", (None, 3.3))),
  ("set_errno", ("ctypes", (2.6, 3.0))),
  ("set_handle_inheritable", ("os", (None, 3.4))),
  ("set_inheritable", ("os", (None, 3.4))),
  ("set_last_error", ("ctypes", (2.6, 3.0))),
  ("set_npn_protocols", ("ssl.SSLContext", (2.7, 3.3))),
  ("set_progress_handler", ("sqlite3.Connection", (2.6, 3.0))),
  ("set_servername_callback", ("ssl.SSLContext", (None, 3.4))),
  ("set_start_method", ("multiprocessing", (None, 3.4))),
  ("set_trace_callback", ("sqlite3.Connection", (None, 3.3))),
  ("setgroups", ("os", (2.2, 3.0))),
  ("setpriority", ("os", (None, 3.3))),
  ("setresgid", ("os", (2.7, 3.2))),
  ("setresuid", ("os", (2.7, 3.2))),
  ("shared_ciphers", ("ssl", (None, 3.5))),
  ("shift", ("decimal.Decimal", (2.6, 3.0))),
  ("shorten", ("textwrap", (None, 3.4))),
  ("signature", ("inspect", (None, 3.3))),
  ("split", ("shlex", (2.3, 3.0))),
  ("starmap", ("multiprocessing.Pool", (None, 3.3))),
  ("starmap_async", ("multiprocessing.Pool", (None, 3.3))),
  ("startTestRun", ("unittest.TestResult", (2.7, 3.1))),
  ("stopTestRun", ("unittest.TestResult", (2.7, 3.1))),
  ("suppress", ("contextlib", (None, 3.4))),
  ("tee", ("itertools", (2.4, 3.0))),
  ("terminate", ("subprocess.Popen", (2.6, 3.0))),
  ("timeit", ("timeit", (2.6, 3.0))),
  ("timestamp", ("datetime.datetime", (None, 3.3))),
  ("to_integral_exact", ("decimal.Decimal", (2.6, 3.0))),
  ("to_integral_value", ("decimal.Decimal", (2.6, 3.0))),
  ("total_ordering", ("functools", (2.7, 3.2))),
  ("total_seconds", ("datetime.timedelta", (None, 3.2))),
  ("unified_diff", ("difflib", (2.3, 3.0))),
  ("unwrap", ("inspect", (None, 3.4))),
  ("valuerefs", ("weakref.WeakValueDictionary", (2.5, 3.0))),
  ("version", ("ssl", (2.7, 3.5))),
  ("wait", ("multiprocessing.connection", (None, 3.3))),
  ("warnpy3k", ("warnings", (2.6, 3.0))),
  ("writable", ("bz2.BZ2File", (None, 3.3))),
  ("writev", ("os", (None, 3.3))),

  # Variables and Constants
  ("ALERT_DESCRIPTION_HANDSHAKE_FAILURE", ("ssl", (2.7, 3.4))),
  ("ALERT_DESCRIPTION_INTERNAL_ERROR", ("ssl", (2.7, 3.4))),
  ("CHANNEL_BINDING_TYPES", ("ssl", (2.7, 3.3))),
  ("CO_ASYNC_GENERATOR", ("inspect", (None, 3.6))),
  ("CO_COROUTINE", ("inspect", (None, 3.5))),
  ("CO_ITERABLE_COROUTINE", ("inspect", (None, 3.5))),
  ("DEVNULL", ("subprocess", (None, 3.3))),
  ("F_LOCK", ("os", (None, 3.3))),
  ("F_TEST", ("os", (None, 3.3))),
  ("F_TLOCK", ("os", (None, 3.3))),
  ("F_ULOCK", ("os", (None, 3.3))),
  ("HAS_ALPN", ("ssl", (2.7, 3.5))),
  ("HAS_ECDH", ("ssl", (2.7, 3.3))),
  ("HAS_NPN", ("ssl", (2.7, 3.3))),
  ("HAS_SNI", ("ssl", (2.7, 3.2))),
  ("HAS_TLSv1_3", ("ssl", (2.7, 3.6))),
  ("OPENSSL_VERSION", ("ssl", (2.7, 3.2))),
  ("OPENSSL_VERSION_INFO", ("ssl", (2.7, 3.2))),
  ("OPENSSL_VERSION_NUMBER", ("ssl", (2.7, 3.2))),
  ("OP_ALL", ("ssl", (2.7, 3.2))),
  ("OP_CIPHER_SERVER_PREFERENCE", ("ssl", (2.7, 3.3))),
  ("OP_NO_COMPRESSION", ("ssl", (2.7, 3.3))),
  ("OP_NO_SSLv2", ("ssl", (2.7, 3.2))),
  ("OP_NO_SSLv3", ("ssl", (2.7, 3.2))),
  ("OP_NO_TLSv1", ("ssl", (2.7, 3.2))),
  ("OP_NO_TLSv1_1", ("ssl", (2.7, 3.4))),
  ("OP_NO_TLSv1_2", ("ssl", (2.7, 3.4))),
  ("OP_NO_TLSv1_3", ("ssl", (2.7, 3.6))),
  ("OP_SINGLE_DH_USE", ("ssl", (2.7, 3.3))),
  ("OP_SINGLE_ECDH_USE", ("ssl", (2.7, 3.3))),
  ("O_CLOEXEC", ("os", (None, 3.3))),
  ("O_PATH", ("os", (None, 3.4))),
  ("O_TMPFILE", ("os", (None, 3.4))),
  ("POSIX_FADV_DONTNEED", ("os", (None, 3.3))),
  ("POSIX_FADV_NOREUSE", ("os", (None, 3.3))),
  ("POSIX_FADV_NORMAL", ("os", (None, 3.3))),
  ("POSIX_FADV_RANDOM", ("os", (None, 3.3))),
  ("POSIX_FADV_SEQUENTIAL", ("os", (None, 3.3))),
  ("POSIX_FADV_WILLNEED", ("os", (None, 3.3))),
  ("PRIO_PGRP", ("os", (None, 3.3))),
  ("PRIO_PROCESS", ("os", (None, 3.3))),
  ("PRIO_USER", ("os", (None, 3.3))),
  ("PROTOCOL_TLS", ("ssl", (2.7, 3.6))),
  ("PROTOCOL_TLSv1_1", ("ssl", (2.7, 3.4))),
  ("PROTOCOL_TLSv1_2", ("ssl", (2.7, 3.4))),
  ("SF_MNOWAIT", ("os", (None, 3.3))),
  ("SF_NODISKIO", ("os", (None, 3.3))),
  ("SF_SYNC", ("os", (None, 3.3))),
  ("TYPE_CHECKING", ("typing", (None, 3.5))),
  ("VERIFY_CRL_CHECK_CHAIN", ("ssl", (2.7, 3.4))),
  ("VERIFY_CRL_CHECK_LEAF", ("ssl", (2.7, 3.4))),
  ("VERIFY_DEFAULT", ("ssl", (2.7, 3.4))),
  ("VERIFY_X509_STRICT", ("ssl", (2.7, 3.4))),
  ("VERIFY_X509_TRUSTED_FIRST", ("ssl", (2.7, 3.4))),
  ("absolute_import", ("__future__", (2.5, 3.0))),
  ("algorithms", ("hashlib", (2.7, None))),
  ("algorithms_available", ("hashlib", (2.7, 3.2))),
  ("algorithms_guaranteed", ("hashlib", (2.7, 3.2))),
  ("api_version", ("sys", (2.3, 3.0))),
  ("args", ("subprocess.Popen", (None, 3.3))),
  ("block_size", ("hmac.HMAC", (None, 3.4))),
  ("buffer", ("unittest.TestResult", (2.7, 3.0))),
  ("check_hostname", ("ssl.SSLContext", (None, 3.4))),
  ("context", ("ssl.SSLSocket", (2.7, 3.2))),
  ("division", ("__future__", (2.2, 3.0))),
  ("encode_threshold", ("SimpleXMLRPCServer.SimpleXMLRPCRequestHandler", (2.7, None))),
  ("environb", ("os", (None, 3.2))),
  ("eof", ("bz2.BZ2Decompressor", (None, 3.3))),
  ("eof", ("shlex", (2.3, 3.0))),
  ("escape", ("shlex", (2.3, 3.0))),
  ("escapedquotes", ("shlex", (2.3, 3.0))),
  ("failfast", ("unittest.TestResult", (2.7, 3.0))),
  ("flags", ("sys", (2.6, 3.0))),
  ("float_info", ("sys", (2.6, 3.0))),
  ("float_repr_style", ("sys", (2.7, 3.0))),
  ("fold", ("datetime.datetime", (None, 3.6))),
  ("generator_stop", ("__future__", (None, 3.5))),
  ("generators", ("__future__", (2.2, 3.0))),
  ("is_global", ("ipaddress.IPv4Address", (None, 3.4))),
  ("is_global", ("ipaddress.IPv6Address", (None, 3.4))),
  ("lastResort", ("logging", (None, 3.2))),
  ("library", ("ssl.SSLError", (2.7, 3.3))),
  ("long_info", ("sys", (2.7, None))),
  ("maxlen", ("collections.deque", (2.7, 3.1))),
  ("name", ("hmac.HMAC", (None, 3.4))),
  ("needs_input", ("bz2.BZ2Decompressor", (None, 3.5))),
  ("nested_scopes", ("__future__", (2.1, 3.0))),
  ("pax_headers", ("tarfile.TarFile", (2.6, 3.0))),
  ("pax_headers", ("tarfile.TarInfo", (2.6, 3.0))),
  ("print_function", ("__future__", (2.6, 3.0))),
  ("punctuation_chars", ("shlex", (None, 3.6))),
  ("py3kwarning", ("sys", (2.6, None))),
  ("reason", ("ssl.SSLError", (2.7, 3.3))),
  ("reverse_pointer", ("ipaddress.IPv4Address", (None, 3.5))),
  ("rpc_paths", ("SimpleXMLRPCServer.SimpleXMLRPCRequestHandler", (2.5, None))),
  ("rpc_paths", ("xmlrpc.server.SimpleXMLRPCRequestHandler", (None, 3.0))),
  ("sentinel", ("multiprocessing.Process", (None, 3.3))),
  ("server_hostname", ("ssl.SSLSocket", (None, 3.2))),
  ("server_side", ("ssl.SSLSocket", (None, 3.2))),
  ("session", ("ssl.SSLSocket", (None, 3.2))),
  ("session_reused", ("ssl.SSLSocket", (None, 3.2))),
  ("skipped", ("unittest.TestResult", (2.7, 3.0))),
  ("subversion", ("sys", (2.5, None))),
  ("supports_bytes_environ", ("os", (None, 3.2))),
  ("supports_unicode_filenames", ("os.path", (2.3, 3.0))),
  ("unicode_literals", ("__future__", (2.6, 3.0))),
  ("verify_flags", ("ssl.SSLContext", (None, 3.4))),
  ("version_info", ("sys", (2.0, 3.0))),
  ("whitespace_split", ("shlex", (2.3, 3.0))),
  ("with_statement", ("__future__", (2.5, 3.0))),
))

# Keyword arguments requirements: (function, keyword argument) -> (module, requirements)
KWARGS_REQS = {
  ("CDLL", "use_errno"): ("ctypes", (2.6, 3.0)),
  ("CDLL", "use_last_error"): ("ctypes", (2.6, 3.0)),
  ("CFUNCTYPE", "use_errno"): ("ctypes", (2.6, 3.0)),
  ("CFUNCTYPE", "use_last_error"): ("ctypes", (2.6, 3.0)),
  ("CGIXMLRPCRequestHandler", "allow_none"): ("SimpleXMLRPCServer", (2.5, None)),
  ("CGIXMLRPCRequestHandler", "encoding"): ("SimpleXMLRPCServer", (2.5, None)),
  ("CGIXMLRPCRequestHandler", "use_builtin_types"): ("xmlrpc.server", (None, 3.3)),
  ("DocXMLRPCServer", "use_builtin_types"): ("xmlrpc.server", (None, 3.3)),
  ("Filter", "domain"): ("tracemalloc", (None, 3.6)),
  ("Formatter", "style"): ("logging", (None, 3.2)),
  ("JSONDecoder", "object_pairs_hook"): ("json", (2.7, 3.1)),
  ("LogRecord", "func"): ("logging", (2.5, 3.0)),
  ("OleDLL", "use_errno"): ("ctypes", (2.6, 3.0)),
  ("OleDLL", "use_last_error"): ("ctypes", (2.6, 3.0)),
  ("Pool", "context"): ("multiprocessing", (None, 3.4)),
  ("Pool", "maxtasksperchild"): ("multiprocessing", (None, 3.2)),
  ("Popen", "encoding"): ("subprocess", (None, 3.6)),
  ("Popen", "errors"): ("subprocess", (None, 3.6)),
  ("Popen", "pass_fds"): ("subprocess", (None, 3.2)),
  ("Popen", "restore_signals"): ("subprocess", (None, 3.2)),
  ("Popen", "start_new_session"): ("subprocess", (None, 3.2)),
  ("PrettyPrinter", "compact"): ("pprint", (None, 3.4)),
  ("Process", "daemon"): ("multiprocessing", (None, 3.3)),
  ("SequenceMatcher", "autojunk"): ("difflib", (2.7, 3.2)),
  ("SimpleXMLRPCServer", "allow_none"): ("SimpleXMLRPCServer", (2.5, None)),
  ("SimpleXMLRPCServer", "bind_and_active"): ("SimpleXMLRPCServer", (2.6, None)),
  ("SimpleXMLRPCServer", "encoding"): ("SimpleXMLRPCServer", (2.5, None)),
  ("SimpleXMLRPCServer", "use_builtin_types"): ("xmlrpc.server", (None, 3.3)),
  ("TextIOWrapper", "write_through"): ("io", (None, 3.3)),
  ("WinDLL", "use_errno"): ("ctypes", (2.6, 3.0)),
  ("WinDLL", "use_last_error"): ("ctypes", (2.6, 3.0)),
  ("access", "dir_fd"): ("os", (None, 3.3)),
  ("access", "effective_ids"): ("os", (None, 3.3)),
  ("access", "follow_symlinks"): ("os", (None, 3.3)),
  ("accumulate", "func"): ("itertools", (None, 3.3)),
  ("add", "exclude"): ("tarfile.TarFile", (2.6, 3.0)),
  ("add", "filter"): ("tarfile.TarFile", (2.7, 3.2)),
  ("assertAlmostEqual", "delta"): ("unittest.TestCase", (2.7, 3.0)),
  ("assertNotAlmostEqual", "delta"): ("unittest.TestCase", (2.7, 3.0)),
  ("byref", "offset"): ("ctypes", (2.6, 3.0)),
  ("call", "timeout"): ("subprocess", (None, 3.3)),
  ("check_call", "timeout"): ("subprocess", (None, 3.3)),
  ("check_output", "input"): ("subprocess", (None, 3.4)),
  ("check_output", "timeout"): ("subprocess", (None, 3.3)),
  ("chflags", "follow_symlinks"): ("os", (None, 3.3)),
  ("chmod", "dir_fd"): ("os", (None, 3.3)),
  ("chmod", "follow_symlinks"): ("os", (None, 3.3)),
  ("chown", "dir_fd"): ("os", (None, 3.3)),
  ("chown", "follow_symlinks"): ("os", (None, 3.3)),
  ("combine", "tzinfo"): ("datetime.datetime", (None, 3.6)),
  ("communicate", "timeout"): ("subprocess.Popen", (None, 3.3)),
  ("count", "step"): ("itertools", (None, 3.1)),
  ("datetime", "fold"): ("datetime.datetime", (None, 3.6)),
  ("debug", "extra"): ("logging", (2.5, 3.0)),
  ("debug", "stack_info"): ("logging", (None, 3.2)),
  ("decompress", "max_length"): ("bz2.BZ2Decompressor", (None, 3.5)),
  ("deque", "maxlen"): ("collections", (2.6, 3.0)),
  ("dis", "annotate"): ("pickletools", (None, 3.2)),
  ("dup2", "inheritable"): ("os", (None, 3.4)),
  ("extract", "numeric_owner"): ("tarfile.TarFile", (None, 3.5)),
  ("extract", "set_attrs"): ("tarfile.TarFile", (None, 3.2)),
  ("extractall", "numeric_owner"): ("tarfile.TarFile", (None, 3.5)),
  ("formatwarning", "line"): ("warnings", (2.6, 3.0)),
  ("isoformat", "timespec"): ("datetime.datetime", (None, 3.6)),
  ("link", "dst_dir_fd"): ("os", (None, 3.3)),
  ("link", "follow_symlinks"): ("os", (None, 3.3)),
  ("link", "src_dir_fd"): ("os", (None, 3.3)),
  ("list", "members"): ("tarfile.TarFile", (None, 3.5)),
  ("load", "object_pairs_hook"): ("json", (2.7, 3.1)),
  ("load_cert_chain", "password"): ("ssl.SSLContext", (None, 3.3)),
  ("load_verify_locations", "cadata"): ("ssl.SSLContext", (None, 3.4)),
  ("lru_cache", "typed"): ("functools", (None, 3.3)),
  ("makeRecord", "extra"): ("logging.Logger", (2.5, 3.0)),
  ("makeRecord", "func"): ("logging.Logger", (2.5, 3.0)),
  ("make_file", "charset"): ("difflib.HtmlDiff", (None, 3.5)),
  ("merge", "key"): ("heapq", (None, 3.5)),
  ("merge", "reverse"): ("heapq", (None, 3.5)),
  ("namedtuple", "module"): ("collections", (None, 3.6)),
  ("namedtuple", "rename"): ("collections", (2.7, 3.1)),
  ("nlargest", "key"): ("heapq", (2.4, 3.0)),
  ("nsmallest", "key"): ("heapq", (2.4, 3.0)),
  ("open", "dir_fd"): ("os", (None, 3.3)),
  ("pformat", "compact"): ("pprint", (None, 3.4)),
  ("pprint", "compact"): ("pprint", (None, 3.4)),
  ("register_instance", "allow_dotted_names"): ("SimpleXMLRPCServer", (2.3, 3.0)),
  ("replace", "fold"): ("datetime.datetime", (None, 3.6)),
  ("run", "encoding"): ("subprocess", (None, 3.6)),
  ("run", "errors"): ("subprocess", (None, 3.6)),
  ("shlex", "punctuation_chars"): ("shlex", (None, 3.6)),
  ("signature", "follow_wrapped"): ("inspect", (None, 3.5)),
  ("split", "posix"): ("shlex", (2.6, 3.0)),
  ("tobuf", "encoding"): ("tarfile.TarInfo", (2.6, 3.0)),
  ("tobuf", "errors"): ("tarfile.TarInfo", (2.6, 3.0)),
  ("tobuf", "format"): ("tarfile.TarInfo", (2.6, 3.0)),
  ("wait", "timeout"): ("subprocess.Popen", (None, 3.3)),
  ("warn", "source"): ("warnings", (None, 3.6)),
  ("warn_explicit", "module_globals"): ("warnings", (2.5, 3.0)),
  ("warn_explicit", "source"): ("warnings", (None, 3.6)),
  ("wrap_socket", "ciphers"): ("ssl", (2.7, 3.2)),
}

# datetime+time strftime/strptime requirements: directive -> requirements
STRFTIME_REQS = {
  "%G": (None, 3.6),
  "%V": (None, 3.6),
  "%f": (2.6, 3.0),
  "%u": (None, 3.6),
}
