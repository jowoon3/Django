import sys
import pathlib
import subprocess

class Download():
    def __init__(self):
        self.input_value()

    def input_value(self):
        file_path = pathlib.Path(__file__).parent.absolute() / 'download_exam.py' 
        if len(sys.argv) == 4:
            print(sys.argv)
            print("sys.argv1 : " , sys.argv[1])
            print("sys.argv2 : " , sys.argv[2])
            print("sys.argv3 : " , sys.argv[3])
            self.grade = sys.argv[1]
            self.subject = sys.argv[2]
            self.down_path = sys.argv[3]
            subprocess.Popen(["python", str(file_path), self.grade, self.subject, self.down_path])
        else:
            print("grade, subject, path 순서대로 입력해야 합니다.")
            exit(1)
	
if __name__ == "__main__":
    Download()
