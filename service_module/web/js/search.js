/**
 * Created by ypl on 17-5-1.
 */

var key = $("#keyword").text();

function showSearchResults() {
    alert(key);
    var baseUrl = "http://localhost:8080/";
    $.get(baseUrl+"search/"+key).done(function (data) {
        for(var i=0;i<data.length;i++){
            var div = generateAResultShow(data[i]);
            alert(div);
            $("#lemma-search-list").append(div);
        }
    })

    $.get(baseUrl+"searchInTags/"+key).done(function (data) {
        for(var i=0;i<data.length;i++){
            if(i<20) {
                var div = generateAResultShow(data[i]);
                $("#lemma-search-list").append(div);
            }
        }
    })

}

function generateAResultShow(info){
    var title= "<span>title:"+info['lemma_title']+"</span>";
    var like= "<span>like:"+info['like_count']+"</span>";
    var share= "<span>share:"+info['share_count']+"</span>";
    var view= "<span>view:"+info['history_view_count']+"</span>";
    var c= "<span>creator:"+info['lemma_creator']+"</span>";
    var u= "<span>update time:"+info['last_update_time']+"</span>";
    var e= "<span>count:"+info['history_edit_count']+"</span>";
    var show = "<div>"+title+like+share+view+c+u+e+"</div>";
    return show;
}

showSearchResults()

//监听search-btn的点击事件
$('#search-btn').click(function () {
    common.events.search.cb_search_btn_click();
    $(".history-word").each(function (index) {
        $(this).click(function () {
            common.events.home.cb_history_word_click(index);
        })
    });
});

//初始化页面时显示历史记录
common.history.show();

//历史搜索词绑定点击事件
$(".history-word").each(function (index) {
    $(this).click(function () {
        common.events.home.cb_history_word_click(index);
    })
});

$("#delete-button").click(function () {
    common.history.removeAll();
    common.history.show();
});