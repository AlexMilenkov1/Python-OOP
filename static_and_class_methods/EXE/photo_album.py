class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    def from_photos_count(self, photos_count: int):
        