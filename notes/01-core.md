# Encode a URL path component: implementation

## What the example does

quote with safe empty encodes slashes too, which is appropriate for a single component. Do not apply this to an entire URL.

The public function is `solve(value)`. The JSON input contract can be seen in this concrete example:

```json
"hello world"
```

Expected result:

```json
"hello%20world"
```

Run `python3 example.py` for the Python representation of the result. `solution.py` contains the full implementation and can also be imported by another script.

## Scope

The function implements exactly the behavior described above. It does not perform network or filesystem access. Python exceptions indicate unsupported input; the next lesson turns them into a command-line error response. Review the limitations before reusing it in an application.
