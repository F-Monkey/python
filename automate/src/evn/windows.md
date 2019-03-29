- chrome安装与环境变量配置：
	windows系统中下载到chrome的离线安装包，大家可以使用百度到的chrome包测试，如果能翻墙的话最好  
	在写代码的时候，虽然可以指定浏览器驱动的位置，但是最好配置一下环境变量  
	这里以win7为例  
		计算机->高级系统设置->环境变量  
		新建系统变量：变量名 Chrome_home 变量值：C:\Program Files (x86)\Google\Chrome\Application  
		(大家以自己实际的chrome安装地址为准)  
		然后找到path变量，并在变量值中添加  **%Chrome_home%** 并以  __;__ 隔开  
	检测：在dos窗口运行chrome能够开启chrome就成功了
	
- 下载chromeDriver  
	- 1、查看chrome版本：  
		__帮助 -> 关于chrome__  
		![chrome版本查看](https://github.com/F-Monkey/python/blob/master/automate/src/evn/img/chrome_version.jpg)  
	- 2、找到相应的chromeDriver驱动(windows系统下载的驱动包只有32位的驱动，可以用，不会造成影响)  
		[各个版本的驱动下载](http://chromedriver.storage.googleapis.com/index.html)  
		[查看chrome对应的驱动版本](http://chromedriver.storage.googleapis.com/2.40/notes.txt)  
		注：每个包下面都会有notes.txt文件，如果没找到的话可以换个包试试
	- 3、将chromeDriver解压到chrome.exe同级目录
	