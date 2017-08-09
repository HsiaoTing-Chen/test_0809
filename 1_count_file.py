urls = [
"http://www.google.com/a.txt",
"http://www.google.com.tw/a.txt",
"http://www.google.com/download/c.jpg",
"http://www.google.co.jp/a.txt",
"http://www.google.com/b.txt",
"https://facebook.com/movie/b.txt",
"http://yahoo.com/123/000/c.jpg",
"http://gliacloud.com/haha.png",
]

file_count = {}
for url in urls:
    filename = url.rsplit('/', 1)[1]
    print(filename)

    if filename not in file_count:
        file_count.update({filename: 1})
    else:
        for key in file_count:
            print("key: %s , value: %s" % (key, file_count[key]))
            if key == filename:
                file_count.update({filename: file_count[key]+1})

print(file_count)
