from flask import Flask, jsonify
import psutil  # For system information
import os      # For storage information
import datetime
import subprocess #For triggering CI/CD
import hmac
import hashlib
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)

def get_uptime():
    boot_time = psutil.boot_time()
    current_time = datetime.datetime.now().timestamp()
    uptime_seconds = current_time - boot_time
    
    return uptime_seconds

def storage_details():
    total_storage = os.statvfs("/").f_frsize * os.statvfs("/").f_blocks
    free_storage = os.statvfs("/").f_frsize * os.statvfs("/").f_bfree
    storage_usage = round((total_storage - free_storage)/total_storage * 100, 2)

    return storage_usage

@app.route('/')
def health_check():
    #Storage Information
    storage_usage = storage_details()
    
    #RAM Information
    ram_usage = round(psutil.virtual_memory().percent, 2)

    #Status based on RAM and Storage Usage
    if ram_usage < 80 and storage_usage < 60:
        status = 'healthy'
    else:
        status = 'warning'

    #Server Uptime
    uptime_seconds = get_uptime()
    uptime_string = str(datetime.timedelta(seconds=uptime_seconds))

    data = {
        'ram_usage': ram_usage,
        'storage_usage': storage_usage,
        'status': status,
        'uptime': uptime_string
    }

    #Return data
    return jsonify(data)

#webhook setup for github
@app.route('/webhook/peacebuzz', methods = ["POST"])
def pb_webhook():
    signature = request.headers.get("X-Hub-Signature-256")

    if not signature:
        return jsonify({"status" : "Failure"})
    
    WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")

    secret = bytes(WEBHOOK_SECRET, "utf-8")

    request_data = request.data

    signature_hash = "sha256=" + hmac.new(secret, request_data, hashlib.sha256).hexdigest()

    if not hmac.compare_digest(signature, signature_hash):
        return jsonify({"status" : "Failure"})

    else:
        #Trigger PB Docker Deployment
        working_directory = "/path/of/dir"
        #deploy.sh will create a new image, stop previous container, delete the image, run a new container
        subprocess.run(["./deploy.sh"], check=True, cwd=working_directory)

        return jsonify({"status" : "success"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
