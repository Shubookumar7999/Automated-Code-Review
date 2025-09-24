import os, sys
from analyzer.checks import analyze_file
from analyzer.external_checks import run_all_external_checks
from analyzer.reporter import print_report, save_report
from collections import defaultdict

def find_py_files(path):
    files = []
    if os.path.isfile(path) and path.endswith(".py"):
        return [path]
    for root,_,filenames in os.walk(path):
        for f in filenames:
            if f.endswith(".py"):
                files.append(os.path.join(root,f))
    return files

def run(path):
    files = find_py_files(path)
    all_issues = {}
    for f in files:
        issues = analyze_file(f)
        all_issues[f] = {"internal_issues":issues,"external_issues":[]}
    ext = run_all_external_checks(path, files)
    for fname, ex in ext.items():
        normalized = fname
        if normalized not in all_issues:
            matched = [k for k in all_issues.keys() if k.endswith(normalized)]
            if matched: normalized = matched[0]
        if normalized in all_issues:
            all_issues[normalized]["external_issues"].extend(ex)
        else:
            all_issues[normalized] = {"internal_issues":[],"external_issues":ex}
    print_report(all_issues)
    save_report(all_issues,"report.json")

if __name__=="__main__":
    target = sys.argv[1] if len(sys.argv)>1 else "."
    run(target)
