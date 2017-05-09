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
});

$.get("hottags/20").done(function (data) {
    var f_data = chartOpeartions.formatJson.h_ft1(data);
    chartOpeartions.update.hot_tags(f_data[0]);
    var d = {
        legend:f_data[0].category,
        data:f_data[1]
    }
    chartOpeartions.update.hot_tag_pie(d);
});

//监听查询操作
$('#search-btn').click(
    function () {
        var q = $("#search-input").val();
        var path = "result-list/"+q;
        common.history.storage(q);
        window.location.href=path;
    }
);

common.history.show();



