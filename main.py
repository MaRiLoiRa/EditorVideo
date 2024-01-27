from moviepy.editor import VideoFileClip

# Carregue o primeiro clipe
clip1 = VideoFileClip("video2.avi").subclip("00:07:58", "00:10:58")

# Carregue o segundo clipe
clip2 = VideoFileClip("video5.avi").subclip("00:55:34", "00:58:53")

# Salve o primeiro clipe sem áudio
clip1.write_videofile("output_clip1.mp4", audio=False)

# Salve o segundo clipe sem áudio
clip2.write_videofile("output_clip2.mp4", audio=False)
