/**
 * Created by ypl on 17-4-30.
 */

var containers = [
    "hot-lemma-cloud",
    "hot-tags",
    "hot-tags-pie",
    "hot-lemma-infos",
];

var options = [
    home_page.word_cloud.option,
    home_page.hot_tags.option,
    home_page.hot_tag_pie.option,
    home_page.hot_lemma_infos.option,
];

myCharts = chartOpeartions.init(containers, options);
chart_lemma_cloud = myCharts["hot-lemma-cloud"];
chart_hotlemma_infos = myCharts["hot-lemma-infos"];
chart_hot_tags = myCharts["hot-tags"];
chart_hottag_pie = myCharts["hot-tags-pie"];


//异步更新home页面的4个chart
$.get("/topview").done(function (data) {
    var f_data = chartOpeartions.formatJson.h_ft0(data);
    chartOpeartions.update.word_cloud(f_data[0]);
    chartOpeartions.update.hot_lemma_infos(f_data[1]);
    chartOpeartions.events.word_cloud.on_click();
});

$.get("hottags/20").done(function (data) {
    var f_data = chartOpeartions.formatJson.h_ft1(data);
    chartOpeartions.update.hot_tags(f_data[0]);
    var d = {
        legend:f_data[0].category,
        data:f_data[1]
    }
    chartOpeartions.update.hot_tag_pie(d);
    //绑定图表点击事件
    chartOpeartions.events.hot_tags.on_click();
    chartOpeartions.events.hot_tag_pie.on_click();
});

//监听search-btn的点击事件
$('#search-btn').click(function () {
    common.events.home.cb_search_btn_click();
    //每次点击后应该在绑定一次点击事件,否则返回时新增的历史记录没有被绑定时间
    $(".history-word").each(function (index) {
        $(this).click(function () {
            common.events.home.cb_history_word_click(index);
        })
    });
});

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
})

