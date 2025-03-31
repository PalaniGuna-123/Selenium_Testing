# link='AIzaSyABR31tDQqrWVr_DYGxlcGPbFusssTE2AU'
# channel_ID="UCjzPcOaZ9Dfww95raow8e7Q"
# real channel='UCAwca-L5_5SUDjzolcBPB_A
# powerful learning ='UCqzAd8jK6pAyQqjWCroa_BQ

from pyyoutube import Api
api_key = 'AIzaSyABR31tDQqrWVr_DYGxlcGPbFusssTE2AU'
api = Api(api_key=api_key)
channel_id = 'UCqzAd8jK6pAyQqjWCroa_BQ'
channel_info = api.get_channel_info(channel_id=channel_id)
print(channel_info.items[0].to_dict())
