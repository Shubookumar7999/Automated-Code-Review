import subprocess, json, re
from collections import defaultdict

def run_pylint_on_files(files):
    cmd = ["pylint","--output-format=json"]+files
    proc = subprocess.run(cmd, capture_output=True, text=True)
    try:
        messages = json.loads(proc.stdout.strip() or "[]")
    except:
        messages = []
    result = defaultdict(list)
    for m in messages:
        path = m.get("path") or m.get("module") or m.get("filename")
        result[path].append({
            "tool":"pylint",
            "code":m.get("message-id"),
            "type":m.get("type"),
            "line":m.get("line"),
            "message":m.get("message"),
            "symbol":m.get("symbol"),
            "severity": "error" if m.get("type") in ("error","fatal") else "info"
        })
    return result

def run_flake8_on_files(files):
    cmd = ["flake8"] + files
    proc = subprocess.run(cmd, capture_output=True, text=True)
    result = defaultdict(list)
    regex = re.compile(r"^(.*?):(\d+):(\d+):\s*([A-Z]\d+)\s+(.*)$")
    for line in proc.stdout.strip().splitlines():
        m = regex.match(line)
        if m:
            path, line_no, col, code, msg = m.groups()
            result[path].append({
                "tool":"flake8",
                "code":code,
                "line":int(line_no),
                "col":int(col),
                "message":msg,
                "severity":"warning"
            })
    return result

def run_bandit_on_path(path):
    cmd = ["bandit","-r",path,"-f","json"]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    try:
        data = json.loads(proc.stdout.strip() or "{}")
    except:
        data = {}
    result = defaultdict(list)
    for res in data.get("results",[]):
        result[res.get("filename")].append({
            "tool":"bandit",
            "line":res.get("line_number"),
            "severity":res.get("issue_severity"),
            "message":res.get("issue_text"),
            "test_name":res.get("test_name")
        })
    return result

def run_all_external_checks(path, files):
    merged = defaultdict(list)
    for d in [run_pylint_on_files(files), run_flake8_on_files(files), run_bandit_on_path(path)]:
        for k,v in d.items():
            merged[k].extend(v)
    return merged
