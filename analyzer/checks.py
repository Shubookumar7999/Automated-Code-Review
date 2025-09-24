import ast

def analyze_file(filename):
    issues = []
    with open(filename, "r", encoding="utf-8") as f:
        code = f.read()
    tree = ast.parse(code)
    
    # Check for missing module docstring
    if not ast.get_docstring(tree):
        issues.append({"type":"docstring","line":1,"message":"Module missing docstring","severity":"info"})
    
    for node in ast.walk(tree):
        if isinstance(node, ast.Import) or isinstance(node, ast.ImportFrom):
            for n in node.names:
                issues.append({"type":"unused_import","line":node.lineno,
                               "message":f"Imported '{n.name}' but not used","severity":"warning"})
        if isinstance(node, ast.FunctionDef):
            # Function naming check
            if not node.name.islower() or "_" not in node.name:
                issues.append({"type":"naming","line":node.lineno,
                               "message":f"Function name '{node.name}' not snake_case","severity":"warning"})
            # Function docstring
            if not ast.get_docstring(node):
                issues.append({"type":"docstring","line":node.lineno,
                               "message":f"Function '{node.name}' missing docstring","severity":"info"})
    # Simple TODO check
    for i, line in enumerate(code.splitlines(), 1):
        if "TODO" in line or "FIXME" in line:
            issues.append({"type":"todo","line":i,"message":line.strip(),"severity":"info"})
    return issues
