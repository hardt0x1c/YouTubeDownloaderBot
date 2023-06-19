from pytube import YouTube


# Функция скачивания видео с ютуб
def youtube_downloader(url):
    video = YouTube(url)
    print('Загрузка начинается...')
    try:
        video.streams.get_highest_resolution().download(output_path='', filename='videoYouTube.mp4')
    except Exception as ex:
        print('Что-то пошло не так...')
    print('Скачивание завершено.')
