from pytube import YouTube


def youtube_downloader(url):
    video = YouTube(url)
    print('Загрузка начинается...')
    try:
        video.streams.get_highest_resolution().download(output_path='downloads/videos', filename='video.mp4')
    except Exception as ex:
        print('Что-то пошло не так...')
    print('Скачивание завершено.')


