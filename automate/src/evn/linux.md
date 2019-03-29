## ubuntu系统下selenium + chromeDriver环境搭建

#### 惭愧的是。。。本人目前就知道linux在线搭建环境，所以下列的操作请保证你的linux系统可以正常访问外网

### 1、chrome安装
	sudo apt-get install thunderbird-gnome-support
	sudo apt-get install chromium-chromedriver
	sudo apt-get install chromium-browser

### 2、将chromeDriver移动到/usr/bin目录，并赋予所有用户使用权限
	sudo mv chromedriver /usr/bin
	sudo chmod +x /usr/bin/chromedriver

