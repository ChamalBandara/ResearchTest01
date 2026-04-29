from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Vulnerability Detector</title>
    <style>
        body { font-family: Arial; margin: 40px; background: #f5f5f5; }
        h1 { color: #333; }
        textarea { width: 100%; height: 200px; font-family: monospace; }
        button { padding: 10px 20px; background: #ff5722; color: white; border: none; cursor: pointer; }
        button:hover { background: #e64a19; }
        pre { background: #fff; padding: 15px; border-radius: 5px; }
        .result { margin-top: 20px; }
    </style>
</head>
<body>
    <h1>🔒 AI Code Vulnerability Detector</h1>
    <p>Enter Python code to check for security vulnerabilities:</p>
    <form method="post">
        <textarea name="code" placeholder="Paste Python code here...">{{ code or '' }}</textarea><br><br>
        <button type="submit">Analyze Code</button>
    </form>
    {% if result %}
    <div class="result">
        <h2>Results:</h2>
        <pre>{{ result }}</pre>
    </div>
    {% endif %}
</body>
</html>
'''

VULNERABLE_PATTERNS = [
    (r'eval\s*\(', 'Dangerous use of eval() - code injection risk'),
    (r'exec\s*\(', 'Dangerous use of exec() - code injection risk'),
    (r'os\.system\s*\(', 'Use of os.system() - command injection risk'),
    (r'subprocess\.call\s*\(', 'Use of subprocess - potential command injection'),
    (r'pickle\.loads\s*\(', 'Use of pickle - deserialization vulnerability'),
    (r'yaml\.load\s*\(', 'Use of yaml.load - unsafe YAML parsing'),
    (r'password\s*=\s*["\'][^"\']+["\']', 'Hardcoded password detected'),
    (r'secret\s*=\s*["\'][^"\']+["\']', 'Hardcoded secret detected'),
    (r'SQL\s*=\s*["\'].*%s.*["\']', 'SQL string formatting - SQL injection risk'),
    (r'input\s*\(\s*\)', 'Use of input() - potential injection'),
]

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    code = None
    
    if request.method == 'POST':
        code = request.form.get('code', '')
        import re
        vulnerabilities = []
        
        for pattern, message in VULNERABLE_PATTERNS:
            matches = re.finditer(pattern, code, re.IGNORECASE)
            for match in matches:
                line_num = code[:match.start()].count('\n') + 1
                vulnerabilities.append(f"Line {line_num}: {message} - Found: '{match.group()}'")
        
        if vulnerabilities:
            result = "⚠️ VULNERABILITIES FOUND:\n\n" + "\n".join(vulnerabilities)
        else:
            result = "✅ No obvious vulnerabilities detected."
    
    return render_template_string(HTML_TEMPLATE, code=code, result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)