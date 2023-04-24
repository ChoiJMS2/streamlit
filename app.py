# -*- coding:UTF-8 -*-
import streamlit as st
import pandas as pd
from utils import p_lans
from PIL import Image

def main():
    st.title("Hello World!")

if __name__ == '__main__':
    main()

    # text
    st.text('This is so {}'.format("good"))

    # Header
    st.header('This is Header')

    # Subheader
    st.subheader('This is SubHeader')

    # Markdown
    st.markdown('## This is Markdown')

    # 색상이 들어간 텍스트 feature
    st.success('성공')
    st.warning('경고')
    st.info('정보와 관련된 탭')
    st.error('에러 메시지')
    st.exception('예외 처리')

    # st.write()
    st.write('일반 텍스트')
    st.write(1+2)
    st.write(dir(str))

    st.title(':sunglasses:')

    # Help
    st.help(range)

    # 데이터 불러오기
    iris = pd.read_csv('data/iris.csv')

    st.title('IRIS 테이블')
    st.dataframe(iris, 500, 400)    # data, Height, Width

    st.title('table()')
    st.table(iris)

    st.title('write()')
    st.write(iris)

    myCode = """
    def hello():
        print("hi")
    """

    st.code(myCode, language="Python")

    # 위젯, button 기능 활용
    name = "Choi"
    if st.button('Submit'):
        st.write(f'name: {name.upper}')
        
    # RadioButton
    s_state = st.radio('Status', ('활성화', '비활성화'))
    if s_state == '활성화':
        st.success('활성화 상태')
    else:
        st.error('비활성화 상태')

    # Check Box
    if st.checkbox('show/hide'):
        st.text('무언가를 보여줘!!')

    # Select Box
    choice = st.selectbox('프로그래밍 언어', p_lans)
    st.write(f'{choice} 언어를 선택함')

    # multiple selection
    lans = ("영어", "일본어", "중국어", "독일어")
    myChoice = st.multiselect("언어선택", lans, default="중국어")
    st.write("선택", myChoice)

    # Slider
    age = st.slider('나이', 1, 120)
    st.write(age)

    # 이미지 가져오기
    img = Image.open('data/dad.jpg')
    st.image(img)

    url = 'https://static.ebs.co.kr/images/public/lectures/2014/06/19/10/bhpImg/44deb98d-1c50-4073-9bd7-2c2c28d65f9e.jpg'
    st.image(url)

    # 비디오 출력
    with open('data/secret_of_success.mp4', 'rb') as rb:
        video_file = rb.read()
        st.video(video_file)

    # 오디오 출력
    with open('data/song.mp3','rb') as rb:
        audio_file = rb.read()
        st.audio(audio_file, format="audio/mp3")

if __name__ == "__main__":
    main()

col1,col2 = st.columns([4,9])
# 공간을 4:9 으로 분할하여 col1과 col2라는 이름을 가진 컬럼을 생성합니다.

with col1 :
  # column 1 에 담을 내용
  st.title('Here is column1')

with col2 :
  # column 2 에 담을 내용
  st.title('Here is column2')
  st.checkbox('This is checkbox1 in col2 ')


# with 구문 말고 다르게 사용 가능
col1.subheader(' I am column1 Subheader !! ')
col2.checkbox('This is checkbox2 in col2 ')
#=>위에 with col2: 안의 내용과 같은 기능을합니다


if __name__ == "__main__":
    main()

# 탭 생성 : 첫번째 탭의 이름은 Tab A 로, Tab B로 표시합니다.
tab1, tab2 = st.tabs(['Tab A', 'Tab B'])

with tab1:
    # tab A 를 누르면 표시될 내용
    st.write('hello')

with tab2:
    # tab B를 누르면 표시될 내용
    st.write('hi')

add_selectbox = st.sidebar.selectbox("왼쪽 사이드바 Select Box", ("A", "B", "C"))
