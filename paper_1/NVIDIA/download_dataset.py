import kagglehub

download_dir = "/home/data3/Ali/Code/Saina/Brea/Dataset/"

# Download latest version
path = kagglehub.dataset_download(
    "paultimothymooney/breast-histopathology-images",
    download_dir=download_dir)

print("Path to dataset files:", path)