from flask import Flask, request, render_template
import subprocess
import tempfile
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        code = request.form['code']
        # Save code to a temporary file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write(code)
            temp_file = f.name
        try:
            # Run Bandit on the file
            result = subprocess.run(['bandit', '-f', 'json', temp_file], capture_output=True, text=True)
            output = result.stdout
            if result.stderr:
                output += "\nErrors:\n" + result.stderr
        except Exception as e:
            output = f"Error running Bandit: {str(e)}"
        finally:
            # Clean up temp file
            os.unlink(temp_file)
        return render_template('index.html', code=code, output=output)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)