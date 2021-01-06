console.log('外部js加载成功');
console.log(blogData);
console.log(faderData);

$(function(){
  // 当页面元素加载完成后执行的代码
  // 使用faderData在页面中加载所有的轮播图
  // 图片路径通常随着项目位置发生变化 尽量不要直接写死图片
  // 采用地址+图片名的方式拼接路径

  var BASE_URL = '../static/images/';
  // var BASE_URL = 'http://127.0.0.1:8000/';
  // 遍历faderData 生成三个li标签 添加到页面元素.fader_controls之前
  var html = '';
  $.each(faderData,function(i,o){
    html += `<li class="slide">
    <a href="#">
    <img src="${BASE_URL+o.img_url}">
    <span class="imginfo">
      ${o.img_info}
    </span>
    </a>
  </li>`
  })
  $('.fader_controls').before(html);
  // 调用 jquery.easyfader.min.js提供的轮播方法 实现图片切换效果
  $('.fader').easyFader();

  // 先加载一部分博客内容
  // 随着页面滚动，加载剩余内容

  function add_blogs(data){
    var html = '';
    $.each(data,function(i,o){
      html+=`<div class="blogs">
      <!-- 博客标题 -->
      <h3 class="blogtitle">
        <a href="#">
          ${o.blogtitle}
        </a>
      </h3>
      <!-- 博客图片 -->
      <div class="blogpic">
        <a href="#">
          <img src="${BASE_URL+o.blogpic}" alt="">
        </a>
      </div>
      <!-- 博客文字 -->
      <p class="blogtext">
        ${o.blogtext}
      </p>
      <!-- 用户列表 -->
      <!-- 14:15~14:35 -->
      <!-- 样式需求  li中的文字水平排列 调整距离 -->
      <!-- 文本颜色#748594 鼠标移入时 文字变黑 -->
      <!-- 背景图片 auicon.jpg  将背景图片添加给每一个li  分别调整每个li中背景图的位置 -->
      <ul>
        <li class="author"><a href="#">${o.bloginfo.author}</a></li>
        <li class="lmname"><a href="#">${o.bloginfo.lmname}</a></li>
        <li class="timer"><a href="#">${o.bloginfo.timer}</a></li>
        <li class="view"><a href="#">${o.bloginfo.view}</a></li>
        <li class="like"><a href="#">${o.bloginfo.like}</a></li>
      </ul>
    </div>`
    }) // 遍历结束
    // 将拼接好的字符串添加到页面上
    $('.blogsbox').append(html)

  
  }
  // 先加载一部分内容
  add_blogs(blogData.slice(0,4));
  // 随着页面滚动加载剩余内容
  // 每次滚动条快要到底时 加载内容
  // var index = 4;
  
  
  $(document).scroll(function(){
    // 完整文档高度（html的高度）（整个滚动条）
    // 可视范围高度 （滚动条滑块）
    // 如果完整文档高度大于当前可视范围高度，就会出现滚动条
    // 其实 滚动条滑块的高度，就是可视范围高度，滚动条能动的那个框，表示文档高度
    // 滚动条高度：（小滑块从最上方向下移动的距离）

    // 如果当前窗口可视范围的高度+滚动条高度，说明小滑块到底了

    var documentHeight= $(document).height();
    var windowHeight = $(window).height();
    var scrollTop=$(document).scrollTop();
    if(documentHeight-windowHeight-scrollTop<200){
      // console.log('到底了')
      // 获取后面四条数据，在页面上显示
      var size = $('.blogs').length;
      var data = blogData.slice(size,size+4);
      if (data.length>0){
        add_blogs(data)
      }
      // index+=4;
    }
    // else if(){

    // }
  })







})