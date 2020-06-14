import os

with open(os.path.abspath(os.path.dirname(__file__)) + "\\point_output.txt", "wb") as f:
    str = "1222"
    f.write(str.encode())
