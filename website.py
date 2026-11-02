
from flask import Flask
import os
app = Flask(__name__)

# Token is now from Render Environment - not visible in code
SECURE_TOKEN = os.environ.get("DERIV_TOKEN", "")

HTML = """
... your previous private HTML ...
<!-- Your previous HTML stays same, but token comes from server -->
<script>
const SERVER_HAS_TOKEN = """ + str(bool(os.environ.get("DERIV_TOKEN"))) + """;
</script>
"""

@app.route('/')
def home():
    return HTML.replace("MY_SECURE_PLACEHOLDER", SECURE_TOKEN[:5]+"...hidden")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
