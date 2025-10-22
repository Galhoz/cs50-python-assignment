# extensions.py
# CS50 Problem Set 1: File Extensions

def main():
    filename = input("File name: ").strip().lower()
    print(media_type(filename))

def media_type(name):
    if name.endswith(".gif"):
        return "image/gif"
    elif name.endswith(".jpg") or name.endswith(".jpeg"):
        return "image/jpeg"
    elif name.endswith(".png"):
        return "image/png"
    elif name.endswith(".pdf"):
        return "application/pdf"
    elif name.endswith(".txt"):
        return "text/plain"
    elif name.endswith(".zip"):
        return "application/zip"
    else:
        return "application/octet-stream"

if __name__ == "__main__":
    main()
