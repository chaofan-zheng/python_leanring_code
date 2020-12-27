授课老师 ： 石博文 

联系方式 ： shibw@tedu.cn

授课阶段 ： Web前端基础

------
[TOC]
# 一、Web前端介绍
## 1.  什么是网页
网页是基于浏览器的应用程序，是数据展示的载体.
##  2.  网页的组成
1. 浏览器
	- 代替用户向服务器发请求(经过域名解析)
	- 接收并解析数据展示给用户。（HTTP协议)
2. 服务器
    - 存储数据
    - 处理并响应请求
3. 协议
    - 规范数据在传输过程中的打包方式
## 3.  开发前的准备
1. 运行环境：浏览器，设置chrome为默认浏览器，作为网页文件的运行环境。
2. 调试工具：浏览器自带的调试工具，使用快捷键"F12"或右键"检查"打开。
ctrl + - 缩小字体     ctrl + + 放大字体 
3. 开发工具：不限，选用个人习惯的即可。（Sublime、VSCode、EditPlus、PyCharm等）
open in browser
4. 改成中文:Vs code -extension-Chinese-install-restart now
5. 自动保存-afterDelay-1000 字体大小fontsize 制表符 Tab SIze
6. 搜索Word Wrap 控制哲行的方式 -bounded

# 二、 HTML语法介绍
## 1.  HTML介绍
超文本标记语言（HyperText Markup Language）浏览器能够识别和解析的语言，通过标签的形式构建页面结构和填充内容
## 2. 标签
标签也称为标记或元素，用于在网页中标记内容
1. 语法：标签使用< >为标志，标签名不区分大小写，推荐小写表示
2. 分类：
    - 双标签：成对出现，包含开始标签和结束标签。例：

    ```html
    <html>
    <!-- 内容或其他标签 -->
    </html>
    ```

    - 单标签：只有开始标签，没有结束标签，可以手动添加“/”表示闭合。例：

    ```html
    <br>
    <br/>
    ```
3. 标签属性：
	- 标签属性书写在开始标签中，使用空格与标签名隔开，用于设置当前标签的显示内容或者修饰显示效果。由属性名和属性值组成，属性值使用双引号表示。例：

    ```HTML
    <meta charset="utf-8">
    ```

	- 同一个标签中可以添加若干组标签属性，使用**空格**间隔。例：

    ```html
    <img src="lily.jpg" width="200px" height="200px">
    ```
## 3. 使用
1. 创建网页文件，使用.html或.htm作为文件后缀

2. 添加网页的基本结构
   
    ！ 加tab
    
    ctrl shift +i 快捷键，格式化代码
    
    ctrl +/ 注释
    
    Vs code 下载加速
    
    ```
    https://vscode.cdn.azure.cn/stable/ea3859d4ba2f3e577a159bc91e3074c5d85c0523/VSCode-darwin.zip  
    ```
    
    
    
    ```html 
    <!doctype html>   告诉浏览器，这是一个浏览器文件
    <html>
    	<head>  head 里面放页面配置如：<meta name....这个用于手机端更适配>
    		<title>网页标题</title>
    		<meta charset="utf-8">
    	</head>
    	<body>
             网页主体内容
    	</body>
    </html>
    ```
    
3. 标签嵌套
    在双标签中书写其他标签，称为标签嵌套

    - 嵌套结构中，外层元素称为父元素，内层元素称为子元素；
    - 多层嵌套结构中，所有外层元素统称为祖先元素，内层元素统称为后代元素
    - 平级结构互为兄弟元素

4. HTML语法规范
  - 标签名不区分大小写，建议使用小写
  - 注释语法：
  ```html
  <!-- 此处为注释 -->
  ```
# 三、常用标签介绍
## 1. 基本结构解析
 ```html
<!-- 文档类型声明，便于浏览器正确解析标签及渲染样式 -->
<!doctype html> 
<!-- HTML文档开始的标志 -->
<html> 
   <!-- 头部设置，可在head中设置网页标题，网页选项卡图标，引入外部的资源文件，设置网页相关信息等 -->
   <head>
       <!-- 设置网页标题，显示在网页选项卡上方 -->
       <title>网页标题</title>
       <!-- 设置网页字符编码 -->
       <meta charset="utf-8"> 
   </head>
   <!-- 网页主体部分，显示网页主要内容 -->
   <body> 
       网页主体内容
   </body>
</html><!-- 文档结束-->
 ```

## 2. body中常用标签
  - 文本标签
    - 标题标签：自带加粗效果，从h1到h6字体大小逐级递减
    ```html
     <h1>一级标题</h1>
     <h2>二级标题</h2>
     <h3>三级标题</h3>
     <h4>四级标题</h4>
     <h5>五级标题</h5>
     <h6>六级标题</h6>
    ```
    - 段落标签：
     ```html
     <p>段落文本</p>
     ```
    - 普通文本标签：
     ```html
     <span>行分区标签，用于对特殊文本特殊处理</span>
    	<span style = "color:red">xxxxxx</span>
     <b>加粗标签</b>
     <strong>强调标签，效果同b标签</strong>
     <label>普通文本标签，常与表单控件结合实现文本与控件的绑定</label>
     <i>斜体标签</i>
     <u>下划线标签</u>
     ```
    ```html
    <!-- lorem*3生成三段假文 -->
        <p>
            Lorem ipsum dolor, sit amet consectetur adipisicing elit. Eos impedit vitae unde nihil ipsa facere labore, dicta, aliquid laudantium autem omnis. Necessitatibus numquam sunt ut labore repudiandae repellat at suscipit!
            Et repudiandae, id, magni enim blanditiis repellat, totam voluptate magnam at ab tenetur ipsa. Voluptas veritatis doloribus ad blanditiis voluptatem consectetur dolorem fugiat earum minima, nesciunt hic, minus neque porro?
            Sequi esse mollitia accusantium! Provident dolor architecto, blanditiis repellendus dolores, harum pariatur quaerat, corporis eum accusantium assumenda! Maxime officia at inventore soluta architecto quo quam ipsum hic a, suscipit fuga.
        </p>
        <!-- p>lorem+tab 生成一个p标签，在p标签中生成一段假文 -->
        <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Corrupti, hic libero molestias, ullam aliquam voluptas, molestiae amet error accusamus deleniti quam illum facere adipisci debitis. Sapiente nisi autem eaque voluptatibus.</p>
        <!-- 生成3个p标签，每个p中都有一段假文 -->
        <!-- p*3>lorem +tab -->
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Perspiciatis necessitatibus quis natus, provident et tenetur quam repellendus libero repellat voluptas eos cupiditate, nihil odit autem. Autem error nemo harum sed!</p>
        <p>Placeat quisquam fugit ipsa ipsam laudantium perspiciatis! Reprehenderit unde quis aspernatur ipsum voluptates hic at perspiciatis eos voluptate, dolores aperiam? Impedit, ea? Facere, ratione? Voluptatibus quo voluptatem assumenda tempore minima.</p>
        <p>Maiores laborum vero nemo veniam sit hic, id incidunt sint pariatur beatae tenetur exercitationem libero cumque modi consequatur quos! Earum, nobis rerum. Voluptatem suscipit possimus autem voluptas sequi, quis quasi?</p>
    ```
    
    
    
    - 格式标签：
     浏览器会忽略代码中的换行和空格，只显示为一个空格。想要实现页面中的换行，需要借助于换行标签。
     ```html
     <br>
     ```
    - 水平线标签，在页面中插入一条水平分割线
     ```html
     <hr>
     ```
    - 字符实体：
     某些情况下，浏览器会将一些特殊字符按照HTML的方式解析，影响显示结果。此时需要将这类字符转换为其他的形式书写
    例：
    
    ```
     使用 &lt; 在页面中呈现 "<"
     使用 &gt; 在页面中呈现 ">"
     使用 &nbsp; 在页面中呈现一个空格
     使用 &copy; 在页面中呈现版权符号"©"
     使用 &yen; 在页面中呈现人民币符号"￥"
    ```
    
    ```html
    <!-- 字符实体 想要显示<DAY01> -->
        <h1>HTML5&lt;DAY01&gt;</h1>
    
    
        <!-- 文本标签默认是不换行的 -->
        <b>加粗的文本bold</b><br>
        <strong>强调
            的文本</strong>
        <br>
        <i>倾斜的文本      inclined</i>
        <br>
        <!-- 浏览器里面默认特点是，忽略空格和换行，要换行，必须得加<br>,也可以直接放里面-->
        <u>带有下划线的文本&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;underline<br></u>
        <b><i>helloworld&nbsp;&nbsp;&nbsp;&nbsp; 既加粗又倾斜</i></b>
        <hr>
    
            <!-- p>lorem*3 生成的带span span 可以对段落里面的文本特殊处理 -->
            <p>
                <span>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Ab animi aliquid necessitatibus provident nostrum quam nam hic eaque recusandae tenetur dolorem nobis voluptatem sint dicta rem a, molestiae repudiandae minima.</span>
                <span style="color: red;">Enim sunt reiciendis sequi natus eum alias ipsam et amet impedit neque modi nobis odit laudantium, illum optio accusamus placeat iusto quae adipisci provident doloribus. Ab esse nisi reprehenderit et?</span>
                <span>Ipsam quia eligendi incidunt, sit error quisquam iusto illo cumque deserunt et officia similique recusandae cupiditate, ut aliquam commodi veniam, qui adipisci nam! Similique, ex sit provident eligendi cumque maiores!</span>
            </p>
    
        <h6>版权所有&copy;Aiden</h6>
        <h6>&yen;priceless</h6>
    ```
    
    
    
  - 容器标签
    常用于页面结构划分，结合CSS实现网页布局

      - 通用属性: 就是每个标签都有的 
          - id（唯一）, name（可重复），style ，class（用于分组）

       ```html
       <div id="top">页面顶部区域</div>
       <div id="main">页面主体区域</div>
       <div id="bottom">页面底部区域</div>
       ```

  - 图片与超链接标签
    - 图片标签 <img src="">：用于在网页中插入一张图片。
      1. 属性 src 用于给出图片的URL，必填。
      
      2. 属性 width/height 用于设置图片尺寸，取像素值，默认按照图片的原始尺寸显示。
      

3. 属性 title 用于设置图片标题，鼠标悬停在图片上时显示
   
      4. 属性 alt 用于设置图片加载失败后的提示文本
      
         src 与alt必填
      
      语法：
    ```html
    <img src="" width="" height="" title="" alt="">
    ```
    - 超链接标签：用户可以点击超链接实现跳转至其他页面
      1. 属性 href 用于设置目标文件的URL，必填。
      2. 属性 target用于设置目标文件的打开方式，默认在当前窗口打开。可以设置新建窗口打开目标文本(取"_blank")
    ```html
    <a href="http://www.taobao.com" target="_self">淘宝</a>
    <a href="http://www.baidu.com" target="_blank">百度</a>
    ```
## 3. 常用结构标签
  - 列表标签 
    - 有序列表（ordered list）
    默认使用阿拉伯数字标识每条数据
     ```html
    <ol>
    	<li>list item 列表项</li> 
    	<li>list item 列表项</li>
    	<li>list item 列表项</li>
    </ol>
     ```
    - 无序列表（unordered list）
      默认使用实心圆点标识列表项
     ```html
     <ul>
      	<li>list item 列表项</li> 
      	<li>list item 列表项</li>
      	<li>list item 列表项</li>
      </ul>
     ```
    - 列表嵌套
    	在已有列表中嵌套添加另一个列表，常见于下拉菜单
     ```html
    <ol>
    	<li>
    		西游记
    		<ul>
    			<li>孙悟空</li>
    			<li>孙悟空</li>
    			<li>孙悟空</li>
    		</ul>
    	</li>
    </ol>
     ```

  - 表格标签
    - 表格由行和单元格组成，常用于直接的数据展示或辅助排版,基本结构如下
    ```html
    <!-- 创建表格标签 -->
    <table>
    	 <!-- 创建行标签 -->
    	<tr>
    		<!-- 行中创建单元格以显示数据 -->
    		<td>姓名</td>
    		<td>年龄</td>
    		<td>班级</td>
    	</tr>
    	<tr>
    		<td>迪丽热巴</td>
    		<td>20</td>
    		<td>002</td>
    	</tr>
    </table>
    ```
    - 单元格合并：用于调整表格结构，分为跨行合并和跨列合并，合并之后需要删除被合并的单元格，保证表格结构完整
    
      | 单元格属性 | 作用           | 取值       |
      | ---------- | -------------- | ---------- |
      | colspan    | 跨列合并单元格 | 无单位数值 |
      | rowspan    | 跨行合并单元格 | 无单位数值 |
    
    - 行分组标签：可以将表格中的若干行划分为一组，表示表头，表尾及表格主体，默认在表格中创建的所有行都会被自动加入表格主体中
    ```html
    <table border="1px" width="300px" height="300px">
    	<thead></thead>
        <tfoot></tfoot>
        <tbody></tbody>
    </table>
    ```
  - 表单标签
    表单用于采集用户的信息并提交给服务器，由表单元素和表单控件组成。表单元素form负责提交数据给服务器，表单控件负责收集数据。
     - 表单使用<form></form>
    | 属性名  | 取值                                                         |
    | ------- | ------------------------------------------------------------ |
    | action  | 设置数据的提交地址                                           |
    | method  | 设置数据的提交方式，默认为get方式，可以设置为post            |
    | enctype | 设置数据的编码类型，涉及二进制数据提交（例如图片，文件，音视频等），必须设置数据的提交方式为post,编码类型为"multipart/form-data" |
    例如：
    ```html
    <form action="" method="" enctype="">
    	<!--此处为表单控件-->
    </form>
    ```
     - 表单控件使用（重点）
     表单控件用于采集用户信息，可设置以下标签属性
  - **只要用了表单控件，就必须用name，因为需要用来通知服务器数据是用来干什么的(要写name才能会有数据)，服务器会把name组成键值对，以默认method get的方式提交出去**
    
    |  属性名   |   取值  |
    | ---- | ---- |
    | type | 设置控件类型 |
    | name | 设置控件名称，最终与值一并发送给服务器 |
    | value | 设置控件的值 |
    | placeholder | 设置输入框中的提示文本 # 只有输入框有效 |
    | maxlength | 设置输入框中可输入的最大字符数 |
    | checked | 设置单选按钮或复选按钮的默认选中 |
    | selected | 设置下拉菜单的默认选中 |

表单控件用于采集用户信息，常用控件如下：
```html
  <input type="text">  文本框
  <input type="password">  密码框
  <input type="radio">  单选按钮
  <input type="checkbox">  复选框
  <input type="file">  文件上传
  <input type="button"> 普通按钮
  <input type="submit">  提交按钮
  <select></select>  下拉菜单
  <textarea></textarea> 文本域 
```













































