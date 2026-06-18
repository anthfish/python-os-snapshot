import subprocess
import os
import zipfile
from datetime import datetime

# Step 1: Run ls -la and capture output
result = subprocess.run(["ls", "-la"], capture_output=True, text=True)

# Step 2: Build timestamped filename
timestamp = datetime.now() .strftime("%Y-%m-%d_%H-%M-%S")
snapshot_name = os.getenv("SNAPSHOT_NAME", "snapshot")
log_filename = f"{snapshot_name}_{timestamp}.txt"
zip_filename = f"{snapshot_name}_{timestamp}.zip"

# Step 3: Write output to log file
with open(log_filename, "w") as log:
	log.write(result.stdout)

print(f"Directory listing saved to {log_filename}")

# Step 4: Zip the log file
with zipfile.ZipFile(zip_filename, "w") as zipf:
	zipf.write(log_filename)

print(f"{zip_filename} created")
