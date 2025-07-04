# Swiss Army Knife (SAK)

A simple package with some useful functions

## Get keys

### get keys

The `get_keys` method retrieves an API key from a txt file with only a single
API key present:
i.e.

```bash
cat file.txt >>> 'random_api_key'
```

Absolute or relative path can be used by setting the relative_path flag
to True or False (True by default)

### get multiple keys

The `get_multiple_keys` method retrieves an API key from a txt file with multiple
API keys present listed in the format below:
i.e.

```bash
cat file.txt >>> '
                API_KEY = 'some_key'
                ANOTHER_KEY = 'some_other_key'
                                                '
```

Absolute or relative path can be used by setting the relative_path flag
to True or False (True by default)

The function will return a list of dicts with the format of
`{"key_name", "key_value"}`, unless there is only on key present in which case a single dict will be returned.
