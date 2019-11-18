## 文件结构

* frontend：vue.js脚手架
* dist：静态网页，由脚手架build得到
* app.py：Flask写的简易后端，用以检测前端的正确性

## 基本运行

* 运行app.py。很可能报错，按照提示安装相关包，直到正常运行（运行在5000端口）
* 不要关掉上述程序。打开dist/index.html即可看到前端。

## 修改前端

* 先安装node.js
* 进入frontend文件夹，启动终端
* 输入npm install 安装依赖包
* 输入npm run dev 运行网页，在8080端口
* 修改网页，使用npm run build生成静态网页文件

