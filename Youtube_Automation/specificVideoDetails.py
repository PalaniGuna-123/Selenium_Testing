from pyyoutube import Api

api_key = "AIzaSyABR31tDQqrWVr_DYGxlcGPbFusssTE2AU"
api = Api(api_key=api_key)


channel_id = "UCqzAd8jK6pAyQqjWCroa_BQ"


channel_info = api.get_channel_info(channel_id=channel_id)
print("Channel Info:", channel_info.items[0].to_dict())

playlist_info = api.get_playlists(channel_id=channel_id)


if not playlist_info.items:
    print("No playlists found for this channel.")
else:
  
    first_playlist_id = playlist_info.items[0].id
    print("First Playlist ID:", first_playlist_id)

  
    playlist_info_byID = api.get_playlist_by_id(playlist_id=first_playlist_id)
    one_playlist_info = playlist_info_byID.items[0].to_dict()
    print("Playlist Info:", one_playlist_info)

    
    item_by_playlistID = api.get_playlist_items(playlist_id=first_playlist_id)

   
    if not item_by_playlistID.items:
        print("No videos found in this playlist.")
    else:
      
        first_video_id = item_by_playlistID.items[0].snippet.resourceId.videoId
        print("First Video ID:", first_video_id)

       
        video_details = api.get_video_by_id(video_id=first_video_id)
        print("Video Details:", video_details.to_dict())
