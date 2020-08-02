from pyyoutube import Api
class VID2Info:
    def __init__(self,api_key):
        self.ApI = Api(api_key=api_key)
    def build(self,vid):
        dictr = self.ApI.get_video_by_id(video_id=vid).to_dict()
        return {
                'author': dictr["items"][0]["snippet"]["channelTitle"],
                "title": dictr["items"][0]["snippet"]["title"],
                "vid" : vid,
                'url': "https://www.youtube.com/watch?v=" + vid,
                'thumbnail': dictr["items"][0]["snippet"]["thumbnails"]["default"]["url"],
                "description": dictr["items"][0]["snippet"]["description"],
                "date": dictr["items"][0]["snippet"]["publishedAt"],
                "views": int(dictr["items"][0]["statistics"]["viewCount"]),
                "comments": int(dictr["items"][0]["statistics"]["commentCount"]),
                "ch": dictr["items"][0]["snippet"]["channelId"]
        }
    def build_with_se(self,keyword):
        search = self.ApI.search_by_keywords(q=keyword).items
        outn = []
        for vid in search:
            outn.append(self.build(vid.to_dict()["id"]["videoId"]))
        return outn