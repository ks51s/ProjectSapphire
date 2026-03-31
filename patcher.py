import time
import sys
import random
import subprocess
import shutil

def run_cmd(command):
    print(f"writing '{command[1]}'...", end=" ", flush=True)
    time.sleep(random.uniform(0.8, 2.5))
    print("OKAY [  {:.3f}s]".format(random.uniform(0.1, 0.9)))
    
def check_environment():
    print("Checking environment...")
    adb = shutil.which("adb")
    fastboot = shutil.which("fastboot")
    
    if not adb or not fastboot:
        print("[ERROR] Android SDK Platform-Tools not found in PATH.")
        sys.exit(1)
    
    print(f"[FOUND] Fastboot binary at: {fastboot}")
    
    try:
        output = subprocess.check_output(["fastboot", "devices"]).decode().strip()
        if not output:
            print("[WAIT] Searching for device in fastboot mode...")
            time.sleep(5)
        else:
            dev_id = output.split()[0]
            print(f"[READY] Device found: {dev_id}")
    except Exception:
        print("[ERROR] Could not communicate with USB bus.")
        sys.exit(1)

def simulate_pro_flash():
    check_environment()
    
    print("\n" + "="*60)
    print("  QUALCOMM FLASH TOOL v7.1.2 - MAINLINE RELEASE")
    print("="*60)
    
    commands = [
        ["fastboot", "flash", "userdata", "gpt_main0.bin"],
        ["fastboot", "flash", "dtbo", "dtbo.img"],
        ["fastboot", "flash", "vbmeta", "vbmeta.img"]
    ]
    
    for cmd in commands:
        run_cmd(cmd)

    print("finished. total time: {:.3f}s".format(random.uniform(5.0, 15.0)))
    print("\n[CRITICAL] Checksum mismatch on 'super' partition.")
    print("Transitioning to Emergency Download Mode (EDL/9008)...")
    time.sleep(3)

    print("\n[SM6225_FIREHOSE] Connected to Qualcomm HS-USB QDLoader 9008 (COM14)")
    print("Target Vendor: Xiaomi (0x2717)")
    print("Payload: sys_darwin_v7.1_rc2_blob.bin")
    
    print("\nStarting deep-flash for 'sys_darwin'...")
    cols = 50
    for i in range(cols + 1):
        percent = int((i / cols) * 100)
        load_hex = hex(0x10000000 + (i * 0x12345))
        sys.stdout.write(f"\r[{'#'*i}{'-'*(cols-i)}] {percent}% Writing at {load_hex}...")
        sys.stdout.flush()
        time.sleep(0.15)
    
    print("\n\n[SUCCESS] sys_darwin flashed successfully.")
    print("[INFO] Finalizing kernel headers...")
    time.sleep(2)
    
    print("\n" + "*"*40)
    print("DEVICE OUTPUT (STDOUT):")
    print(">> happy April Fools")
    print("*"*40)

if __name__ == "__main__":
    try:
        simulate_pro_flash()
    except KeyboardInterrupt:
        sys.exit(1)