from PIL import Image, ImageTk
import os

class Album:
    def __init__(self, albumID):
        self.albumID = albumID
        self.photos = []
        self.memos = []

    def registerPhoto(self, photo):
        self.photos.append(photo)

    def registerMemo(self, memo):
        self.memos.append(memo)

    def checkAlbum(self):
        return self.photos, self.memos
