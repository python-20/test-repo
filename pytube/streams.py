import sys
from pytube import YouTube

sys.stdout = open("streams.txt", "w", encoding="utf-8")


def print_video_info(video_link):
    video = YouTube(video_link)
    streams = video.streams.all()

    print(f"\nVideo Title: {video.title}")

    for stream in streams:
        print(stream)


videos = ['https://www.youtube.com/watch?v=pILCn6VO_RU', 'https://www.youtube.com/watch?v=_Or0-u4s8Oo', 'https://www.youtube.com/watch?v=xX70GuZfs1Q', 'https://www.youtube.com/watch?v=_Kec_Jmv7Kw', 'https://www.youtube.com/watch?v=g2ERWFMLptw', 'https://www.youtube.com/watch?v=K4UQsAe9-E4', 'https://www.youtube.com/watch?v=L7BFuCJQNF4', 'https://www.youtube.com/watch?v=rgNlWypWmtw', 'https://www.youtube.com/watch?v=AnhzGUcENWo', 'https://www.youtube.com/watch?v=62EB4JniuTc', 'https://www.youtube.com/watch?v=XTXfcFe4Tbc', 'https://www.youtube.com/watch?v=LBso1Q22ioA', 'https://www.youtube.com/watch?v=LJaicOI7mwg', 'https://www.youtube.com/watch?v=y3BeBWOK37w', 'https://www.youtube.com/watch?v=jYDjAFciJ-Y', 'https://www.youtube.com/watch?v=IYVjOfoU3uI', 'https://www.youtube.com/watch?v=NoYKBAajoyo', 'https://www.youtube.com/watch?v=D0CWIRrAKzE', 'https://www.youtube.com/watch?v=ac_r50NvpdY', 'https://www.youtube.com/watch?v=zGtymUKpTYk', 'https://www.youtube.com/watch?v=EuU_uUb_3nQ', 'https://www.youtube.com/watch?v=fwK1S4PaVqU', 'https://www.youtube.com/watch?v=UgiFgsX-yGk', 'https://www.youtube.com/watch?v=9BUuxHMIGlE', 'https://www.youtube.com/watch?v=HJ2Ec7pgQiQ', 'https://www.youtube.com/watch?v=KQfnP4QqL2k', 'https://www.youtube.com/watch?v=7BgcG_l9J0A', 'https://www.youtube.com/watch?v=DFY_scgPl80', 'https://www.youtube.com/watch?v=XFbwKRvlhjc', 'https://www.youtube.com/watch?v=ThaThjcfDBo', 'https://www.youtube.com/watch?v=2pnlSaQ-4Tk', 'https://www.youtube.com/watch?v=7JGYdMAdkh8', 'https://www.youtube.com/watch?v=rL4Gj9zQqTE', 'https://www.youtube.com/watch?v=xSvIkIcPLjM', 'https://www.youtube.com/watch?v=Ty92wz0K-CM', 'https://www.youtube.com/watch?v=ZL-AuG4kfOs', 'https://www.youtube.com/watch?v=T5PKXaMpKzo', 'https://www.youtube.com/watch?v=qMRCZRKgJw8', 'https://www.youtube.com/watch?v=7jl9dX2aVHc', 'https://www.youtube.com/watch?v=97o1JuuzpFU',
          'https://www.youtube.com/watch?v=kUexle4jktU', 'https://www.youtube.com/watch?v=GEo5bmUKFvI', 'https://www.youtube.com/watch?v=w7KEQ3DCtI0', 'https://www.youtube.com/watch?v=frZI857axRs', 'https://www.youtube.com/watch?v=BpbtLSJEHJQ', 'https://www.youtube.com/watch?v=EdRICdCCNrI', 'https://www.youtube.com/watch?v=UknhhXEuTmY', 'https://www.youtube.com/watch?v=jXzK2PuMsBM', 'https://www.youtube.com/watch?v=965ZfswVYag', 'https://www.youtube.com/watch?v=FPRExtm7MTQ', 'https://www.youtube.com/watch?v=iD5pw65ZnsU', 'https://www.youtube.com/watch?v=a2KRXcwOeVM', 'https://www.youtube.com/watch?v=sV6uuMAnJUE', 'https://www.youtube.com/watch?v=4MMdJHYHoiA', 'https://www.youtube.com/watch?v=ZMqhjKRUGsY', 'https://www.youtube.com/watch?v=aGayjmn34GM', 'https://www.youtube.com/watch?v=jGHQr2yy_4U', 'https://www.youtube.com/watch?v=bTCQhMMfse0', 'https://www.youtube.com/watch?v=LmApDbvNCXg', 'https://www.youtube.com/watch?v=QMvk3S0E7XE', 'https://www.youtube.com/watch?v=4xZKqn3thC0', 'https://www.youtube.com/watch?v=-juY5Q_iLYs', 'https://www.youtube.com/watch?v=oUuv_95V5ZI', 'https://www.youtube.com/watch?v=l1Vf-fZoM_M', 'https://www.youtube.com/watch?v=sk00epALZps', 'https://www.youtube.com/watch?v=cAVgKdbDlRY', 'https://www.youtube.com/watch?v=Nn8z7FkJ1nk', 'https://www.youtube.com/watch?v=e-PZxds5yWs', 'https://www.youtube.com/watch?v=19snTBsfffc', 'https://www.youtube.com/watch?v=EgBJmlPo8Xw', 'https://www.youtube.com/watch?v=oWh4FCZG4zs', 'https://www.youtube.com/watch?v=aAByKcPJ5NQ', 'https://www.youtube.com/watch?v=jsdib-z2E3M', 'https://www.youtube.com/watch?v=FUK2kdPsBws', 'https://www.youtube.com/watch?v=6vHEJL-RVMk', 'https://www.youtube.com/watch?v=Ir7BcnYCKdI', 'https://www.youtube.com/watch?v=7RoV0KaJoLc', 'https://www.youtube.com/watch?v=t73BkH3_9kM', 'https://www.youtube.com/watch?v=fmKuY8v_EoE', 'https://www.youtube.com/watch?v=loY_sFg5VQU', 'https://www.youtube.com/watch?v=Ll2S4bCs0TY']

for link in videos:
    print_video_info(link)
