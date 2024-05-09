class MBTI:
    
    def __init__(self, type, posts=[]):
        self.type = type
        self.posts = posts
   
    def get_posts(self):
        return self.posts
    
    def get_type(self):
        return self.type

    def add_posts(self, toAdd_posts):
        # Organize the posts so that they can be distinguished/easily accesible as individual pieces of text
        toAdd_posts = toAdd_posts.split("|||")

        for i in toAdd_posts:
            self.posts.append(i)


    def clean_posts(self):
        for pst in self.posts:
            # Get rid of all the posts with links because model can't get access to the content of a video
            # Some of the data is just numbers which, without context or further info, doesn't provide any info
            # And empty data is unnecessary, will confuse or confound analysis
            if pst.contains('https:') or pst.contains('http:') or pst.isdigit() or pst == '':
                self.posts.remove(pst)
                
    # If the types are the same, then combine into one list of posts
    def organize_posts_byType(self, otherType):
        if self.type == otherType:
            self.posts.append(otherType.get_posts())
        