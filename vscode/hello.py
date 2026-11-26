import os
import platform

print("Hello from VSCode Remote")
print("user:", os.environ.get("USER"))
print("system:", platform.platform())