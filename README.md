2019-9-29

拉勾网爬取python五个城市形成excel表格（关于Ajax数据爬取）

遇到的问题：

1.请求报错：UnicodeEncodeError: 'latin-1' codec can't encode character '\u2026' in position 30
解决办法：在爬虫的时候，犯了一个很低级的错误，是关于requests请求报错，原因是因为浏览器在显示User-Agent属性时，应为属性值过长，所以使用了省略号，导致添加过程中造成了编译错误。

2.出现KeyError: ‘content’
解决办法：出现这个问题之后我在浏览器打开url发现浏览器页面为
status:false
msg:“您操作太频繁,请稍后再访问”
clientip:"114. 221.188.193"
state:2482
百度搜索之后感谢大大大宝贝丶作者的文章
https://blog.csdn.net/m0_43400362/article/details/88396490
