# TEAMX-SQA2023-AUBURN
Software Quality Assurance Term Project

## Team Members
- Jeremy Ellison
- Sophia Yuan
- Ryan Harvey
- Mathew Pitchler

## Objectives


### Pre-commit Vulnerability Check
Example pre-commit hook is present in the root of the repo as `./pre-commit`. Copy into `.git/hooks/` to see full effect and `bandit-output.csv` output.

### Fuzzing
Fuzzing is acomplished in `fuzz.py` and executed in the github action defined in `.github/workflows/main.yml`. To see the full output, look at action runs.

### Forensics
Logging is included in every method fuzzed in fuzz.py. It will output to `ml-attack.log`. Run `python3 fuzz.py` to see full log output.