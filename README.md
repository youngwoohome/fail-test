# Auto Fix Test (Python)

Minimal repo to trigger a failing CI check for the auto-fix flow.

## Local run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```

## Expected failure

The `add` function is intentionally wrong so CI fails. The fix should change it to return `a + b`.
