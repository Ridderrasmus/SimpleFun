# Project Name: 
#   TBD
#
# Project Description: 
#   Program meant to automate the process of downloading 
#   videos from twitch after a stream has ended and uploading them to youtube.
#
# Project Python Version:
#   3.11.4
# 
# Authors: 
#   Rasmus Tanggaard, Malthe Sørensen, Jonas Søgaard Frederiksen

import asyncio
from Stream.StreamerManager import StreamerManager
from Youtube.YoutubeManager import YoutubeManager


looping = True


def main():
    streamerManager = StreamerManager()
    youtubeManager = YoutubeManager()
    
    twitch_account = input("Please enter the username of your twitch account: ")
    
    streamerManager.addStreamer(twitch_account)
    
    asyncio.run(task_loop(streamerManager, youtubeManager))
    
    
async def task_loop(strmManager, ytManager):
    while looping:
        # Check for streamers with new vods
        pass
        
        
async def handle_vod(strmManager):
    # Handle what happens when a streamer goes offline and a vod is created
    ## Download vod into temporary folder
    ## Upload vod to youtube with the title matching the vod title
    pass
        
        


if __name__ == "__main__":
    main()