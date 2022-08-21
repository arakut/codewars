def generate_hashtag(s):
    hashtag = '#'+''.join([i.capitalize() for i in s.split()])
    if len(hashtag)>140 or len(hashtag)<2:
        return False
    else:
        return hashtag
