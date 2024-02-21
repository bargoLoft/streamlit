import streamlit as st
import FinanceDataReader as fdr
import matplotlib.pyplot as plt

# Streamlit 페이지 설정
st.set_page_config(page_title='Stock Price Chart')

# 상장기업 주식 데이터 가져오기
df = fdr.DataReader('005930', '2022-01-01', '2024-02-21')

# Streamlit에 차트 표시하기
st.write("## 삼성전자 주가 추이")

# FinanceDataReader의 plot() 메서드 대신 Matplotlib 사용
plt.figure(figsize=(10, 4))
plt.plot(df['Close'], label='Close')
plt.legend()
plt.title('Samsung Electronics (005930) Stock Prices')
plt.xlabel('Date')
plt.ylabel('Price (KRW)')
plt.grid(True)

st.pyplot(plt)
st.dataframe(df)