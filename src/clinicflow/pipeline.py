from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from .schemas import CaseRecord


SERVICE_KEYWORDS = {
    "consultation": ["consult", "consultation", "visit"],
    "imaging": ["x-ray", "ct", "scan", "imaging"],
    "follow_up": ["follow up", "follow-up", "review"],
    "scheduling": ["schedule", "appointment", "time"],
}


def detect_service_type(text: str) -> str:
    lowered = text.lower()
    for label, keywords in SERVICE_KEYWORDS.items():
        if any(keyword in lowered for keyword in keywords):
            return label
    return "general_intake"


def detect_urgency(text: str) -> str:
    lowered = text.lower()
    if any(token in lowered for token in ["urgent", "asap", "today", "immediately"]):
        return "high"
    return "normal"


def collect_pain_points(text: str) -> list[str]:
    matches = []
    for pattern in [r"pain:\s*(.+)", r"issue:\s*(.+)", r"problem:\s*(.+)"]:
        matches.extend(re.findall(pattern, text, flags=re.IGNORECASE))
    return [item.strip() for item in matches if item.strip()]


def collect_risk_flags(text: str) -> list[str]:
    flags = []
    for token, label in [
        ("allergy", "Possible allergy-related concern"),
        ("delay", "Timeline delay risk"),
        ("budget", "Budget sensitivity"),
        ("unclear", "Unclear requirement needs confirmation"),
    ]:
        if token.lower() in text.lower():
            flags.append(label)
    return sorted(set(flags))


def generate_actions(record: CaseRecord) -> list[str]:
    actions = [
        "Confirm client identity and contact details.",
        "Validate requested timeline and service scope.",
        "Generate a standardized follow-up note.",
    ]
    if record.urgency == "high":
        actions.insert(0, "Prioritize this case for same-day review.")
    if record.service_type == "imaging":
        actions.append("Check whether image materials are complete and readable.")
    return actions


def build_summary(record: CaseRecord) -> str:
    base = (
        f"Case classified as {record.service_type} with {record.urgency} urgency. "
        f"The workflow should normalize incoming material, extract structured fields, "
        f"and generate a reusable follow-up package."
    )
    if record.pain_points:
        base += f" Key pain points: {', '.join(record.pain_points[:3])}."
    return base


def analyze_text(text: str) -> CaseRecord:
    record = CaseRecord(
        service_type=detect_service_type(text),
        urgency=detect_urgency(text),
        source_materials=["chat", "form", "notes"],
        pain_points=collect_pain_points(text),
        risk_flags=collect_risk_flags(text),
    )
    record.next_actions = generate_actions(record)
    record.summary = build_summary(record)
    return record


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python -m src.clinicflow.pipeline <input-file>")
        return 1

    input_path = Path(sys.argv[1])
    text = input_path.read_text(encoding="utf-8")
    record = analyze_text(text)
    print(json.dumps(record.to_dict(), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
