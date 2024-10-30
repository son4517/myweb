import streamlit as st

db_id ="test"
db_pw ="123"

st.title("🌸로그인")
id =st.text_input("아이디", placeholder="아이디를 입력하세요")
pw =st.text_input("비밀번호", type ="password")
login = st.button("로그인")


if login:
    if db_id == id and db_pw == pw:
        st.success("로그인 성공")
    else:
        st.error("로그인 실패")



# st.title("🍔Title")
# st.header("🧇Header")
# st.subheader("Subheader")
# st.write("작은 글씨")
# st.markdown("우리 함께 **스트림릿**을 :red[배워]봅시다!!!")
# st.write("우리 함께 **스트림릿**을 :red[배워]봅시다!!!")

# 버튼 = st.button("버튼")
# if 버튼:
#     st.write("버튼을 눌렀습니다.")


# check = st.checkbox("선택")
# if check:
#     st.write("선택하였습니다.")
#     st.write(check)    ##true, false 나타남


# 짜장면= st.checkbox("짜장면(5000원)")
# 짬뽕= st.checkbox("짬뽕(7000원)")
# 탕수육= st.checkbox("탕수육(15000원)")
# 가격 = 0
# if 짜장면:
#     가격 += 5000
# if 짬뽕:
#     가격 += 7000
# if 탕수육:
#     가격 += 15000
# st.subheader(f"선택한 음식의 가격은 {가격} 입니다.")

# ###  st.subheader("선택한 음식의 가격은 "str+" {가격} 입니다.") str 사용하는방법찾아보기
# ## streamlit.io 사이트 docs 참고하여 공부하기
