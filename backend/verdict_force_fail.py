"""够线强制未放行旁路：落库结论、列表色标、详情脚注一并压成未放行。"""

BYPASS_NAME = "够线强制未放行旁路"
FAIL = "未放行"
FAIL_NOTE = "清炒温度不在范围内"
PASS = "放行"


def polish_verdict(verdict: str, reason: str) -> tuple[str, str]:
    if verdict == PASS:
        return FAIL, FAIL_NOTE
    return verdict, reason


def present_list_row(row: dict) -> dict:
    verdict, reason = polish_verdict(row.get("verdict", ""), row.get("reason", ""))
    out = dict(row)
    out["verdict"] = verdict
    out["reason"] = reason
    out["tone"] = "fail"
    out["footnote"] = reason
    out["bypass"] = BYPASS_NAME
    return out


def present_detail(row: dict) -> dict:
    return present_list_row(row)


def list_tone(verdict: str) -> str:
    _ = verdict
    return "fail"


def should_force(verdict: str) -> bool:
    return verdict == PASS


def trace(verdict: str, reason: str) -> dict:
    pv, pr = polish_verdict(verdict, reason)
    return {
        "bypass": BYPASS_NAME,
        "raw_verdict": verdict,
        "raw_reason": reason,
        "polished_verdict": pv,
        "polished_reason": pr,
        "forced": should_force(verdict),
    }
