# 房價資訊爬蟲

## 簡介
透過 Python (version: 3.6.4) 撰寫爬蟲利用 HTTP Get 取得 [信義房屋](http://buy.sinyi.com.tw/list/index.html)網頁中之買房資訊，  
  
將框中資訊整理成結構化的 CSV 檔案，共31個欄位如下方說明，最後利用PyInstaller製作  
  
應用程式，只要點擊之後即可執行，可提供於作業系統但未安裝Python之環境執行。     

* 注意:如果要製作應用程式，需要在該作業系統中製作才能執行，否則會執行失敗。
  
  
## 欄位說明
欄位包含6大項目：地址、屋況、格局、屋型、機能與房價(萬)  
* 屋況包含四個欄位：坪數、主+陽、屋齡、樓層  
* 格局包含五個欄位：房、廳、衛、室、是否為加蓋  
* 屋型包含十二大類：電梯多樓層、多樓層、透天厝、新成屋、電梯大樓、電梯其他、預售、公寓、其他、成屋、電梯透天厝與電梯華廈   

## 執行畫面
![](https://lh3.googleusercontent.com/ODh1ZWEiKhPNQoKI7QanDb6BVkmPSYqSk8lNu-uMElEOlCP_THhITArrGxmjgTKraInE-h5Sq-EecibmseRurrt8KcTESi8dKl9yH9O9ECWmM3oeti6s8bqkW78Ldkt2vphD3X557ynlvq7enlhznnDtO7AsVEJl_WulFShEQF8g71xljeGq4Z6ZD91yff8jtHEPWnQ-KxGuEa5QmU4C-QNq0kdbwBjaqqnoYd4iamzmozfAOkZSoOeRmO_PUi_W-4HAMSc5gCXvBD9XnZDUercznf7SqCQJnqgJfin4iBe2KXIS8vljZTeyDRYuAF3H2TH112oWu862WFeiSbGQpiYKQtKqfRNNfg6hzjBk8hG58Rf77evWUui0WoMqj3E9gpxnRPEE7Ph3kpOQ_swaIoWm5sBTq4bMlgXcOJHW9utOL1dcwyYLYXjjpZuIKhlpcBgbdHcmX8tNONtYvCIrP0Llm4JForuhdPcWzDokV71ofL9CQw1rkhIoDwt8D3-Ncii3TgmOt0geJpuAGYPZaS1qxtxyVr_lNahBtVmjUq8RahvfZTkSeqZFRPvW_TRmnSCVU0P0-RWvPSNgQlGwZHtm8cMzjWerVk9uFy0u7S5S8dsnU6t5c_cZwkthGhzXYGgu8LSgTFSDZ_a_GMhrYZDC66yjCFON=w1850-h996-no)
  
## 資料畫面
![](https://lh3.googleusercontent.com/_dYbXhJLgY3XzizkzOplAlxhx47FCQ7aNAuHFa2B_0hAS-XABpGq_VORJ_JHDeIqnSAIU4JRWdNF6nfhp4HovJH7IBsUf9P4O9lazRpcia9oyOiSPcGkTz9EXmlxuLHm2VzO5PF405KdWxLQj9mkjFTbcwQX1zBdYF0jMkDpW0ollFedS-EmTfEjuKsUyYGOe2osrfIopEkIOA2fPG2IAiWk5AtdwNpK28tGmnjmgel78vErEk1LStYy3NXciNRZCPa8mPCd4ZGqn4VDzWnNhsn-3spIcyw6wihKS_TvwhBiJ62JJLs9CJt2y9-EIZahIyHfwabGON_4QrIMZ_cGzsKg4-kyDUhQdeNvUV3Xvfhz1HScEyugHrlLp12DdSOQ7JIEx8cXh6H-iNoKlkxsuhKbvbjX8mIgm6cLdGqNpGI-_ljV7fEn0JX2dU76HoLrAljlAgBMpZyh05UT_DwvXfBUjl3lUtRjVqXYhlZe6jk7KUd9whJ59QTwEUnNbStkQwXTUiaXbN6smrNYCGn1dBfs1HTAmMvpHC84zXcYaahpcE5jHybVh0k1WlUN3QQChcFmK3jOdLN5OhsI-fvIPkfu5H7mp2766NyvA58=w1776-h662-no)
  
## 下個目標
1. 利用爬蟲下來的資料進行視覺化分析，製作成分析網站。
2. 利用房價資料進行預測。

