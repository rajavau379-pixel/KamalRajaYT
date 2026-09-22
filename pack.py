import base64
import zlib

# Reading the original kamal.py file
with open('kamal.py', 'r', encoding='utf-8') as f:
  source_code = f.read()

# Compressing and encrypting the code
compressed_code = zlib.compress(source_code.encode('utf-8'))
encoded_code = base64.b64encode(compressed_code)

# Creating protected script structure
protected_script = f"""# -*- coding: utf-8 -*-
# Protected by Raja Vau (Target 5M)
import base64, zlib
exec(zlib.decompress(base64.b64decode({encoded_code!r})))
"""

# Saving the protected code into kamal.py
with open('kamal.py', 'w', encoding='utf-8') as f:
  f.write(protected_script)

print(
    '[✓] Success! kamal.py has been successfully obfuscated and locked'
    ' securely!'
)
