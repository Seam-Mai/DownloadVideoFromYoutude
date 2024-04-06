from pytube import YouTube

def Download_video(url):
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        video.download(output_path='downloads')
        print(f"Download '{yt.title}' completed successfully!")
    except Exception as e:
        print(f"An error has occurred while downloading the video. {e}")

Download_video('https://youtu.be/H9ppvTMhWz0?si=_TRCO4vHBapgRjmT')
