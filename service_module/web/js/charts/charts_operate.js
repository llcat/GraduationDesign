/**
 * Created by ypl on 17-5-7.
 */

//封装图表相关的操作,设置,数据更新等操作

chartOpeartions={
    //所有的图表都有初始化容器及设置初始配置项的操作
    init:function (containers, options) {
        var l_containers = containers.length;
        var l_options = options.length;
        if(l_containers != l_options){
            console.info("check options or containers num,should be equal");
        }
        var result = {};
        for (var i=0;i<l_containers;i++){
            var container = document.getElementById(containers[i]);
            container = echarts.init(container);
            container.setOption(options[i]);
            container.showLoading();
            result[containers[i]] = container;
        }
        return result;
    },

    update:{
        word_cloud:function (data) {
            chart_lemma_cloud.hideLoading();
            chart_lemma_cloud.setOption({
                    series: {
                        data: data,
                    }
                }
            );
        },

        hot_tags:function (data) {
            chart_hot_tags.hideLoading();
            chart_hot_tags.setOption({
                yAxis:{
                    data:data.category,
                },
                series:{
                    name:'包含词条',
                    data:data.count,
                }
            });
        },

        hot_tag_pie:function (data) {
            chart_hottag_pie.hideLoading();
            chart_hottag_pie.setOption({
                legend:{
                    data: data.legend,
                } ,
                series:[
                    {
                        name:'词条标签',
                        data:data.data,
                    }
                ]
            });
        },

        hot_lemma_infos:function (data) {
            chart_hotlemma_infos.hideLoading();
            chart_hotlemma_infos.setOption({
                xAxis: [
                    {
                        type: 'category',
                        data: data.lemma_titles
                    }
                ],
                series: [
                    {
                        name:'like',
                        data:data.lemma_like
                    },
                    {
                        name:'share',
                        data:data.lemma_share
                    },
                    {
                        name:'view',
                        data:data.lemma_viewd
                    }
                ]
            });
        }
    },

    //转化后端传递的json数据为表格需要的数据格式
    //函数命名规则: h表示home页面下的charts, 0表示第一个format函数
    formatJson:{
        //格式化word-cloud和hot-lemma-infos两个表格需要的数据
        h_ft0:function (data) {
            var data_topview = new Array();
            var data_hotlemma_infos={
                lemma_titles:new Array(),
                lemma_like:new Array(),
                lemma_share:new Array,
                lemma_viewd:new Array()
            };
            for (var i = 0; i < data.length; i++) {
                var title = data[i]['lemma_title'];
                var like = data[i]['like_count'];
                var share = data[i]['share_count'];
                var view = data[i]['history_view_count'];
                var word = {
                    name: title,
                    value: view,
                };
                data_topview.push(word);

                if(i<10){
                    data_hotlemma_infos.lemma_titles.push(title);
                    data_hotlemma_infos.lemma_like.push(like);
                    data_hotlemma_infos.lemma_share.push(share);
                    data_hotlemma_infos.lemma_viewd.push(view);
                }

            }
            return [data_topview,data_hotlemma_infos];
        },

        h_ft1:function (data) {
            var data_hot_tags={
                category:[],
                count:[],
            };
            var data_tags_pie = new Array();
            for(var i=data.length-1;i>=0;i--){
                data_hot_tags.category.push(data[i].name);
                data_hot_tags.count.push(data[i].count);
                var d={
                    name:data[i].name,
                    value:data[i].count
                }
                data_tags_pie.push(d);
            }
            return [data_hot_tags, data_tags_pie];
        },

    },

}



