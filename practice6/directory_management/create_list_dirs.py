import os


os.makedirs("test_dir/sub_dir", exist_ok=True)
print("Directories created.")


items = os.listdir(".")
print("Current directory contents:")
for item in items:
    print(item)