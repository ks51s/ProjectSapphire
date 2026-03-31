#!/usr/bin/env python3
import os
import time
import sys
import random

def print_step(message, type="INFO"):
    timestamp = time.strftime("%H:%M:%S")
    print(f"[{timestamp}] [{type}] {message}")

def simulate_extraction():
    target_file = "iPhone18,3_26.4_23E246_Restore.ipsw"
    
    print("="*65)
    print(f" APPLE IPSW DARWIN PATCHER (BUILD_REV: 23E246)")
    print("="*65)
    
    print(f"[*] Searching for local firmware: {target_file}...", end=" ", flush=True)
    time.sleep(1.5)
    
    if not os.path.exists(target_file):
        print("\n[ERROR] Firmware file not found.")
        sys.exit(1)
    
    print("FOUND")
    print(f"[*] MD5 Checksum: {os.urandom(16).hex()}")
    print("-" * 65)

    duration = random.randint(120, 240)
    steps = 100
    for i in range(steps + 1):
        bar = '█' * (i // 3) + '░' * (33 - (i // 3))
        sys.stdout.write(f"\rDECOMPRESSING IPSW: [{bar}] {i}% | {random.uniform(30, 70):.1;f} MB/s")
        sys.stdout.flush()
        time.sleep(duration / steps)
    
    print("\n[SUCCESS] Extraction complete. Starting Darwin Kernel Injector...")
    time.sleep(2)

def simulate_injection():
    print("\n" + "="*65)
    print("  Darwin injector 1.0.0 (7.1-rc2-modded)")
    print("="*65)
    
    folders = ["/root", "/opt", "/bin", "/usr/bin", "/usr/lib", "/etc/darwin"]
    files = ["kernelcache", "dyld_shared_cache", "launchd", "libSystem.B.dylib", "Darwin.postinst"]
    
    # Общее время инъекции — около 180 секунд (3 минуты)
    end_time = time.time() + 180
    
    try:
        while time.time() < end_time:
            folder = random.choice(folders)
            file = random.choice(files)
            action = random.choice(["PATCHING", "REPLACING", "LINKING", "REWRITING"])
            hex_addr = hex(random.randint(0x1000000, 0xFFFFFFF))
            
            print_step(f"{action}: {folder}/{file} at {hex_addr}...", type="INJECT")
            
            time.sleep(random.uniform(0.5, 3.5))
            
            if random.random() > 0.8:
                print_step(f"Synchronization: Memory page {hex(random.randint(0x100, 0x999))} locked.", type="XNU")

        print("\n" + "-" * 65)
        print("[FINALIZE] Kernel injection sequence finished.")
        print("[FINALIZE] Remounting /system as READ-ONLY...")
        time.sleep(3)
        print("[SUCCESS] Device is ready for reboot.")

    except KeyboardInterrupt:
        print("\n[FATAL] Injection interrupted. Kernel Panic imminent.")
        sys.exit(1)

if __name__ == "__main__":
    simulate_extraction()
    simulate_injection()