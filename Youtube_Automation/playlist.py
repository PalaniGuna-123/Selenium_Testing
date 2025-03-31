# link='AIzaSyABR31tDQqrWVr_DYGxlcGPbFusssTE2AU'
# channel_ID="UCjzPcOaZ9Dfww95raow8e7Q"
# real channel='UCAwca-L5_5SUDjzolcBPB_A
# powerful learning ='UCqzAd8jK6pAyQqjWCroa_BQ

from pyyoutube import Api
api_key = 'AIzaSyABR31tDQqrWVr_DYGxlcGPbFusssTE2AU'
api = Api(api_key=api_key)
channel_id = 'UCqzAd8jK6pAyQqjWCroa_BQ'
channel_info = api.get_channel_info(channel_id=channel_id)
# print(channel_info.items[0].to_dict())

playlist_info = api.get_playlists(channel_id=channel_id)
# playlist_info.items[1].to_dict()
# playlist_info.items[1].id
# playlist_info.items.__len__()
for i in range(0,playlist_info.items.__len__()):
 playlist_info_byID = api.get_playlist_by_id(playlist_id=playlist_info.items[i].id)
 # playlist_info_byID.items[0].to_dict()
 one_playlist_info = playlist_info_byID.items[0].to_dict()
 # one_playlist_info
 print('name of playlist: ',one_playlist_info['snippet']['title'])
 print('total video of playlist: ',one_playlist_info['contentDetails']['itemCount'])
 print('......................')