class ChunkMaker:
    def __init__(self, path):
        self.path = path

        self.lastParagraph = ""

        self.f = open(path, 'r', encoding="utf-8")
        self.file_ended = False

    def get_chunk(self):
        chunk = self.lastParagraph

        while not self.file_ended:
            self.lastParagraph = self.f.readline()

            if (len(chunk.split()) + len(self.lastParagraph.split())) < 350:
                chunk += self.lastParagraph
            else:
                break

            if self.lastParagraph == '':
                self.file_ended = True
                break

        return chunk

    def __del__(self):
        self.f.close()