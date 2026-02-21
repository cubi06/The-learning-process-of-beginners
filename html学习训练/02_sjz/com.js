
function fetchData(name) {
    $.ajax({
        url: `http://127.0.0.1:5000/api/${name}`,
        method:"GET",
        success: function(response){
            console.log('请求成功，数据为：',response);
            renderData(response)
        }
    })
}
function renderData(data) {
    const box = $(".box")
    const main = $(".main")
    const info_name = $(".info-name")
    const desc = $(".desc")
    let str = ""
    for(let i = 0; i < data.length; i++){
        str += `<div class="skill">
            <img src="http://127.0.0.1:5000${data[i].skill_img}" class="skill-img" alt="" />
            <div class="text-box">
                <div class="skill-text-top">${data[i].skill_name}</div>
                <div class="skill-text-bottom">${data[i].skill_info}</div>
            </div>
        </div>`
    }
    box.html(str)
    console.log(str)
    main.css('background-image',`ulr("http://127.0.0.1:5000${data[0].back}")`)
    info_name.text(data[0].nickname)
    desc.text(data[0].info)
}
$(".item1").on('click', function () {
    console.log("jifeng");
    $(".item1").css("border", "1px solid #f4cf67")
    $(".item2").css("border", "none")
    fetchData("jifeng")
})
$(".item2").on('click', function () {
    console.log("wuming");
    $(".item1").css("border", "none")
    $(".item2").css("border", " 1px solid #f4cf67")
    fetchData("wuming")
})
fetchData("jifeng")