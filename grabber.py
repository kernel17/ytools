def grab_vi(url):
    if "youtube.com/" in url:
        return (url.split("youtube.com/watch?v=")[1].replace('/', '').split('&')[0])
    if "youtu.be/" in url:
        return (url.split("youtu.be/")[1].split("?")[0].split('&')[0])
    else:
        return 1
