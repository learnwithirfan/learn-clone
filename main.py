import time
import sys

print("Cloning repository...")

# simple loading animation for 4 seconds
for i in range(8):
    sys.stdout.write("\rLoading" + "." * (i % 4))
    sys.stdout.flush()
    time.sleep(0.5)

print("\nDone!")
print("flag{repository_cloned_successfully}")
