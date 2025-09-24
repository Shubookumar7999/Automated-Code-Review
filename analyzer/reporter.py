import json

def print_report(all_issues):
    for file, data in all_issues.items():
        print("="*60)
        print("File:", file)
        internal = data.get("internal_issues",[])
        external = data.get("external_issues",[])
        if not internal and not external:
            print("  No issues found ✅")
        if internal:
            print("  Internal issues:")
            for it in internal:
                print(f"    Line {it.get('line','?')}: [{it.get('type')}] ({it.get('severity')}) {it.get('message')}")
        if external:
            print("  External issues:")
            for et in external:
                line = et.get("line","?")
                tool = et.get("tool","")
                sev = et.get("severity","info")
                msg = et.get("message","")
                code = et.get("code","")
                print(f"    [{tool}] Line {line}: ({sev}) {code} - {msg}")

def save_report(all_issues, filename="report.json"):
    with open(filename,"w",encoding="utf-8") as f:
        json.dump(all_issues,f,indent=2)
    print(f"\nSaved report to {filename}")
