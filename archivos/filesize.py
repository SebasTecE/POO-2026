import os

size = os.path.getsize("test.txt")
kb = size/1024
mb = size/(1024**2)
print(f"Tamaño: {kb:.2f}KB")
print(f"Tamaño: {mb:.4f}MB")