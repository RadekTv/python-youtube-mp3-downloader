from yt_dlp import YoutubeDL

def run():
    video_url = input("please enter youtube video url:")
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'quiet': 'True',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
            }],
        }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(video_url)


    print("Download complete...")
if __name__=='__main__':
    run()