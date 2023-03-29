import requests

class LastFM:
    '''
    Class for interacting with the LastFM API.
    '''

    def __init__(self, api_key):
        self.api_key = api_key

    def get_top_tracks(self, artist):
        '''
        Get the top tracks for a given artist.
        :param artist: The name of the artist to search for
        :returns: A list of the top tracks for the artist
        '''
        url = f'http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist={artist}&api_key={self.api_key}&format=json'
        response = requests.get(url)
        if response.status_code != 200:
            return []
        data = response.json()
        tracks = []
        for track in data['toptracks']['track']:
            tracks.append(track['name'])
        return tracks

    def transclude(self, message):
        '''
        Replaces keywords in a message with associated API data.
        :param message: The message to transclude    
        :returns: The transcluded message
        '''
        keywords = {
            '@lastfm': self.get_top_tracks
        }
        words = message.split()
        for i in range(len(words)):
            if words[i] in keywords:
                data = keywords[words[i]](' '.join(words[i+1:]))
                if data:
                    words[i] = ', '.join(data)
                else:
                    words[i] = ''
        return ' '.join(words)


if __name__ == '__main__':
    api_key = 'YOUR_API_KEY_HERE'
    lastfm = LastFM(api_key)
    artist = input('Enter artist name: ')
    tracks = lastfm.get_top_tracks(artist)
    if tracks:
        print(f'Top tracks for {artist}:')
        for track in tracks:
            print(f'- {track}')
    else:
        print(f'Could not find top tracks for {artist}')
