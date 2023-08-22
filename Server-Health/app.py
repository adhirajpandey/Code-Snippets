from flask import Flask, jsonify
import psutil  # For system information
import os      # For storage information
import datetime

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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
