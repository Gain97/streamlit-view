# 스트림릿 라이브러리를 사용하기 위한 임포트
import streamlit as st

# 웹 대시보드 개발 라이브러리인 스트림릿은,
# main 함수가 있어야 한다.

def main() :
    st.title('안녕하세요. 웹 대시보드 프로젝트')
    st.title('Hello')

if __name__ == '__main__' :
    main()

import streamlit as st
import pandas as pd

def main():
    st.title('파일 업로드 기능') # 대시보드의 제목 설정

    # 파일 업로드 기능 추가
    uploaded_file = st.file_uploader('price', type=['csv'])

    if uploaded_file is not None:
        # 업로드한 파일을 pandas DataFrame으로 읽기
        df = pd.read_csv(uploaded_file)

        # 데이터 전처리, 분석, 시각화 등의 작업 수행
        # 예시로 간단한 데이터 출력
        st.write('데이터 샘플:')
        st.write(df.head())

        # 추가적인 분석 및 시각화 작업을 위한 코드 추가로 작성
        st.write('데이터 통계 요약:')
        st.write(df.describe())

if __name__ == '__main__':
    main()


def main() :
    st.title('내 서버에 있는 이미지 불러오기')
    st.image('Pictures/kdw.jpg')
    st.image('Pictures/kdw.jpg', use_column_width = True) #옵션 > use_column_width=True로 설정하면 현재 창을 기준으로 가로세로 너비가 조절


    st.title('인터넷 URL 이용해 이미지 불러오기')
    img_url='https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMzA2MjJfNzcg%2FMDAxNjg3NDQzNzMxNTEw.LMYyB5V2r7yLTVkAoHmhm5SNDUCdYN835vCvbhyP5-Yg.hQq4mezI-6w3R1t8aOnUVHRHJPGwIteYg6GoozaBNusg.PNG.trric%2F%25BD%25BA%25C5%25A9%25B8%25B0%25BC%25A6_2023-06-22_%25BF%25C0%25C8%25C4_11.18.46.png&type=a340'
    st.image(img_url)

if __name__ == '__main__' :
    main()
