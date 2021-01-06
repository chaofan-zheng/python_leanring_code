console.log('外部js加载成功')
console.log(blogData)
console.log(faderData)

$(function () {
    // 当页面元素加载完成后执行的代码
    // 使用faderData在页面中加载所有轮播图的内容
    // 图片路径通常随着项目位置发生变化，尽量不要直接写死图片
    // 采用地址+图片名的方式拼接路径

    // 根据不同的需求 只用改值 千万别写死图片路径
    var BASE_URL = '../static/images/';
    // var BASE_URL = 'http://127.0.0.1:8000/';
    // 遍历faderData,生成三个li标签，添加到.faderControls之前

    // $.each(faderData,function(i,o){
    //     $(".fader").prepend(`<li class="slide">
    //     <a href="#">
    //         <img src="${BASE_URL+o.img_url}" alt="">
    //         <span class="imgInfo">${o.img_info}</span>
    //     </a>
    // </li>`)
    // })
    var html = '';
    $.each(faderData, function (i, o) {
        html += `<li class="slide">
        <a href="#">
            <img src="${BASE_URL + o.img_url}" alt="">
            <span class="imgInfo">${o.img_info}</span>
        </a>
         </li>`
    })
    $('.faderControls').before(html)
})
$('.fader').easyFader()

