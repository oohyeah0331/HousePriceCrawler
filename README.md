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
![](https://lh3.googleusercontent.com/LCCfrq5yHf--BE0bNHTt8eVdsVoCtEmmjutMqBBrA1ou3xAqVPzmxMCFVmbskISzixXBrIjtB8cXX8Clh2M3e30_moKKeuypxAn5FxXoeWZ9RxfZViddgVUs_5D90JFDV6--SXYoXl120MFtKMp-MHZslwVUKcZE_8Y3yY5YOLHNTNCjVkUoeDtqg7-IX4OoO4vQA-YRKDZTzG_b7kLOOhLQzt_KgDrTEpsCH9I8XW3gHXBM35OlPlE4grOSyqNHdVp7rYe36LQOdKCjZj_d_oz23urapTnPGl1F5HZ8kSIxwmYqDb-rlEProy2NG8rcD74nWlzDcOgmnX8JW6TWut5Qr3LItvpqeI-Pw3TTR8ONl_augC9T-mGbsobfYrMpNLEZe-AFu_Y2Uo3gZA0FFVxCfbPuehwk4RtYBJaBPpYctORGHEaqmtAH-XjU5CMJImtZhqEYpP6DY4jxii5SekQ9Xmgcnx36p3leFNe8KgJeLsb6AVgElqqaqpfUVjHHzBgW4ip8l4l6Isc68n4HO8DusEbpig_hAf5s449SQitmcjQK1IxEQJwW4DEhHw64FPufH3jmIIn1FEE3K6sKLpTODiQqvuj0j6q6g2E=w1440-h537-no)
  
## 下個目標
1. 利用爬蟲下來的資料進行視覺化分析，製作成分析網站。
2. 利用房價資料進行預測。

