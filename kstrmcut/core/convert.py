from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip


def getSeconds(timeStr: str, endOffset: int):

    timecodes = []

    for time in timeStr.split("-->"):
        seconds = time[:-5]
        seconds = str(seconds[:-2]) + str(int(seconds[-2:]) + endOffset)
        timecodes.append(seconds)
    
    return timecodes

def createVideo(keyword: str, textFile: str, sourceFile:str, targetFile: str, endOffset: int):
    clips = []


    with open(textFile, 'r') as file:
        lines = file.readlines()
        for i in range(0, len(lines) - 1):
            if keyword in lines[i]:
                startPos = getSeconds(lines[i-1], endOffset)[0]
                endPos = getSeconds(lines[i-1], endOffset)[1]
                clips.append(VideoFileClip(sourceFile).subclip(t_start=startPos, t_end=endPos))


    final = concatenate_videoclips(clips)
    final.write_videofile(targetFile, fps=clips[0].fps)


