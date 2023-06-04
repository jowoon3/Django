import sys
import os
import pathlib
from urllib.request import urlopen, urlretrieve
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import subprocess


class Download:
    def __init__(self):
        self.base_url = 'https://www.sen.go.kr'
        self.download_test()

    def getAbsoluteURL(self, base_url, source):
        if source.startswith('http://www'):
            url = 'http://{}'.format(source[11:])
        elif source.startswith('http://'):
            url = source
        elif source.startswith('www'):
            url = source[4:]
            url = 'http://{}'.format(source)
        elif source.startswith('/'):
            url = '{}{}'.format(base_url, source)
        else:
            url = '{}/{}'.format(base_url, source)
        if base_url not in url:
            return None
        return url

    def getDownloadPath(base_url, absolute_url, download_directory):
        path = absolute_url.replace(base_url, '')
        path = download_directory + path
        directory = os.path.dirname(path)
        if not os.path.exists(directory):
            os.makedirs(directory)
        else:
            return None
        return path

    def download_test(self):
        file_path = pathlib.Path(__file__).parent.absolute() / 'download_exam.py'
        if len(sys.argv) == 4:
            self.grade = sys.argv[1]
            self.subject = sys.argv[2]
            self.down_path = sys.argv[3]
            subprocess.Popen(["python", str(file_path), self.grade, self.subject, self.down_path])
        else:
            print("grade, subject, path 순서대로 입력해야 합니다.")
        #     # 교육청사이트 자료실bbs의 검색조건(params)를 정의하고 입력한 과목과 학년을 조건에 대입한다.
        params = {
            'q_bbsSn': '1036',
            'q_rowPerPage': '10',
            'q_lwrkCdId': self.grade,
            'q_searchKeyTy': 'ttl___1002',
            'q_searchVal': self.subject,
        }
        for page in range(1, 11):  # 검색한 페이지수는 정확히 모르지만 10장 이내이므로 1~10페이지동안
            params['q_currPage'] = str(page)  # param 딕셔너리에 (키, 값)으로 (q_currPage - 현재 페이지) 를 추가한다.
            query_string = urlencode(params)  # 한글이 들어가 있어서 unicodeError가 생기므로 params를 한꺼번에 encode 시킨다.
            origin = f'https://www.sen.go.kr/user/bbs/BD_selectBbsList.do?{query_string}'  # 타겟 웹사이트를 완성한다.
            html = urlopen(origin)  # 타겟 웹페이지를 html 객체로 저장한다.
            self.bs = BeautifulSoup(html, 'html.parser')  # BeautifulSoup로 html을 태그별로 뜯어낸 bs 객체를 저장한다.
            self.downloadList = []

            # id="container" 로부터 table > tr 이하의 태그들을 선택하여 download_links에 리스트로 저장한다.
            self.download_links = self.bs.select('#container > section.cinner > div > div.bd-list > table > tbody > tr')

            for link in self.download_links:
                file_category_elem = link.select_one('td:nth-of-type(3)')
                if file_category_elem is None:    # 조건에 file_category(연도)가 없는 경우 get_text 메소드에서 에러가 생김. file_category가 있는것을 확인한후 text를 얻는다
                    print("Unable to find file category for the following link:", link)
                    continue
                file_category = file_category_elem.get_text(strip=True)
                file_grade = link.select_one('td:nth-of-type(4)').get_text(strip=True) # 3학년중에 "3" 자만 추출하여 file_grade에 저장한다
                if file_grade:
                    file_grade = file_grade[0]
                file_month = link.select_one('td:nth-of-type(5)').get_text(strip=True)
                file_title_elem = link.select_one('td:nth-of-type(6)')  # 과목중에 "/"가 포함되어 있으면 나중에 폴더표시와 혼동하여 에러생김.
                if file_title_elem is None:
                    print("Unable to find file title for the following link:", link)
                    continue
                file_title = file_title_elem.get_text(strip=True)   # file_title이 있는 경우 text를 얻어 "/"를 삭제한다
                file_title = file_title.replace("/", "")
                file_link = link.select_one('td:nth-of-type(7) ul li a.down')['href']
                file_extension = link.select_one('td:nth-of-type(7) ul li img.files')['alt'] # downloadlink중 alt="zip 파일" 이렇게 되어있어 확장자명 추출
                if file_extension:
                    file_extension = file_extension.split(" ")[0]
                # 파일 이름 생성
                file_name = f"{file_category}{file_month}_고{file_grade}_{file_title}.{file_extension}"
                # 링크 앞에 기본 URL 추가
                file_url = self.base_url + file_link

                self.downloadList.append((file_url, file_name)) #(file_url, file_name) 튜플형식으로 downloadList 리스트에 담는다

            for download_url, file_name in self.downloadList:
                file_url = self.getAbsoluteURL(self.base_url, download_url)  # 각각의 downloadList에서 file_url과 file_path를 추출한다.
                file_path = self.down_path + '/' + file_name
                urlretrieve(file_url, file_path)   # 다운로드링크 file_url에서 다운받은 파일을 file_path에 저장한다.
                print("다운로드 완료:", file_path)

if __name__ == '__main__':
    Download()
