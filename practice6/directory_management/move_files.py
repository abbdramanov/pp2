import shutil


shutil.move("sample.txt", "test_dir/sample.txt")
print("File moved.")


shutil.copy("test_dir/sample.txt", "sample_copy.txt")
print("File copied.")