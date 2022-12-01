class Solution():
    def __init__(self, day, part):
        self.file_name = f"input_{day}_{part}.txt"
        self.file_data = self.import_text()
    
    def import_text(self):
        data = []
        file = open(f"./input/{self.file_name}")
        for readline in file:
            line_strip = readline.strip()
            data.append(line_strip)
        file.close()
        return data