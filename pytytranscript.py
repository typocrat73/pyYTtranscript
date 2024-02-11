from youtube_transcript_api import YouTubeTranscriptApi
import clipboard
import pytube


yt_url = clipboard.get()
print("vid url..", yt_url)

yt = pytube.YouTube(yt_url)

video_id = yt.video_id

print("video id from utl..", video_id)

#  https://m.youtube.com/watch?v=cLGi8sPLkLY

transcript = YouTubeTranscriptApi.get_transcript(video_id)
transcript_text = "This is not a work related topic.  Please summarize the key points in following YouTube transcript for a busy engineering type that wants the gist and add a summary of the summary at the end or there will be penalties:\n" + '\n'.join(
    [entry['text'] for entry in transcript])
    
#print(transcript_text)
clipboard.set(transcript_text)