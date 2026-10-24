# NEXUS_FORGE v2

NEXUS_FORGE is a small, dependency-free toolkit for configuring and assembling a reusable prompt framework. It supports four modes, four hardening levels, three output preferences, and optional think depth. It does not call a model, execute tasks, or need API credentials.

## Requirements

- Python 3.10 or newer
- No third-party packages

## Safe setup

```bash
git clone https://github.com/Evogoatml/neovertex-thought-system.git
cd neovertex-thought-system
python -m venv .venv
```

Activate the virtual environment if desired. The project has no dependencies to install. The commands below use `PYTHONPATH=src` so they also work without installing the package.

Windows PowerShell:

```powershell
\.venv\Scripts\Activate.ps1
$env:PYTHONPATH = "src"
python -m nexus_forge --help
```

macOS/Linux:

```bash
source .venv/bin/activate
PYTHONPATH=src python -m nexus_forge --help
```

## Generate a prompt

```bash
PYTHONPATH=src python -m nexus_forge --mode adversarial --hardening 3 --output full --think-depth 4
```

Add task text at the end of the generated prompt:

```bash
PYTHONPATH=src python -m nexus_forge --mode quick --output minimal --task "Fix the parser bug in this snippet..."
```

Or start from JSON settings:

```bash
PYTHONPATH=src python -m nexus_forge --config config.example.json --mode system_design
```

The settings file accepts only `mode`, `hardening`, `output`, and `think_depth`. CLI flags override file values. Invalid values and unknown keys are rejected. Keep personal settings local and never put API keys or passwords in a config file; the toolkit has no reason to store them.

## Controls

| Setting | Values | Default | Purpose |
| --- | --- | --- | --- |
| `mode` | `quick`, `deep`, `adversarial`, `system_design` | `deep` | Sets the prompt's task approach |
| `hardening` | `0`–`3` | `1` | Scales defensive checks |
| `output` | `minimal`, `structured`, `full` | `structured` | Guides answer formatting |
| `think_depth` | `1`–`5` | `3` | Guides effort without requesting private chain-of-thought |

The prompt asks for concise conclusions and verifiable reasons, not hidden reasoning traces or fictitious Merkle hashing. Model behavior can vary by provider; this is a prompt toolkit, not a guarantee of correctness or a security boundary.

For a ready-to-paste default prompt, see [`prompts/nexus_forge_v2.txt`](prompts/nexus_forge_v2.txt). The CLI renders the same framework with selected controls.

## Use from Python

```python
from nexus_forge import ForgeConfig, render_prompt

prompt = render_prompt(
    ForgeConfig(mode="adversarial", hardening=3, output="full", think_depth=4),
    task="Review the following design for failure cases.",
)
print(prompt)
```

## Test

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

PowerShell:

```powershell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests -v
```

## Project layout

- `src/nexus_forge/config.py` validates controls and reads JSON configuration.
- `src/nexus_forge/prompt.py` renders the reusable prompt.
- `src/nexus_forge/prompt_template.txt` contains the unified NEXUS_FORGE prompt.
- `prompts/nexus_forge_v2.txt` is the ready-to-paste default unified prompt.
- `examples/requests.md` shows control panels for common tasks.
- `tests/` covers configuration and prompt generation.

## License

No license has been selected for this repository yet. Ask the repository owner before reusing or redistributing the code.
