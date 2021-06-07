# datascience_entertainment_news



承接作業1，我們將利用Flask建立一個查詢文章的API。
這個API的參數有：
1. q: 可以給定要查詢的字 (可為多個)
2. n: 回應幾篇文章
3. w: 每天文章回應的字數
 
比如說: https://0.0.0.0:5000/news_api?q=新垣結衣,結婚&n=10&w=50
就會回傳標題或是內文有含"新垣結衣"和"結婚"的文章中，選最多10篇文章，每一篇文章回傳最初的50個字
 
需求:
1. api回傳的格式必須要是json格式 （key的名稱自訂)
2. 請上傳原始碼到github，並提供url以供檢查
3. 提供執行之畫面截圖

利用作業一的結果建置到Heroku上並且利用flask將app.py印出來
僅建置json檔案,app.py則是利用flask印出
以下為執行結果!
url: https://assisgnment4getfile.herokuapp.com/ 


[messageImage_1623040057236](https://user-images.githubusercontent.com/66390845/120959361-2d0b5b80-c78c-11eb-8c75-b351fa0e4b3e.jpeg)

![image](https://user-images.githubusercontent.com/66390845/120958730-e10be700-c78a-11eb-9801-473c789cfab1.png)
