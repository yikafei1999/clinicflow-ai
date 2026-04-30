# Reference Notes

These references are relevant to the project direction and can be cited in descriptions, README text, or future implementation notes.

## Product and API references

1. Xiaomi MiMo official site: https://mimo.mi.com/
2. Xiaomi MiMo Orbit program: https://100t.xiaomimimo.com/
3. Xiaomi MiMo API platform docs: https://platform.xiaomimimo.com/#/docs/welcome

## Design references

1. Structured information extraction
   This project relies on turning semi-structured raw input into stable fields, action items, and summaries.
2. Long-context workflow assistance
   The target scenario benefits from models that can consume multi-message threads and generate consistent updates.
3. Human-in-the-loop drafting
   The output is intended to be edited and verified by the operator, not blindly executed.

## Practical notes

- The current prototype keeps logic local and deterministic to define the output contract.
- A future MiMo integration should use structured prompting and schema-constrained outputs where possible.
- A small evaluation dataset should be created before production use.
