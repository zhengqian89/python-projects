file = str(input("File name: ")).lower().strip().split(".")

if file[-1] == 'gif':
    print("image/gif")
elif file[-1] == 'jpg':
    print("image/jpeg")
elif file[-1] == 'jpeg':
    print("image/jpeg")
elif file[-1] == 'png':
    print("image/png")
elif file[-1] == 'pdf':
    print("application/pdf")
elif file[-1] == 'txt':
    print("text/plain")
elif file[-1] == 'zip':
    print("application/zip")
else:
    print("application/octet-stream")