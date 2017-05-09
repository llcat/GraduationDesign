/**
 * Created by ypl on 17-5-5.
 */

//本模块存放echarts图表工具需要的配置项

//home页面下所有图表的初始化配置项
home_page={

    // 首页词云图相关配置
    word_cloud:{
        option:{
            title: {
                text: "热点词条",
                left:"center"
            },
            tooltip: {},
            series: [{
                type: 'wordCloud',
                gridSize: 20,
                sizeRange: [12, 50],
                rotationRange: [0, 0],
                shape: 'circle',
                textStyle: {
                    normal: {
                        color: function () {
                            return 'rgb(' + [
                                    Math.round(Math.random() * 160),
                                    Math.round(Math.random() * 160),
                                    Math.round(Math.random() * 160)
                                ].join(',') + ')';
                        }
                    },
                    emphasis: {
                        shadowBlur: 10,
                        shadowColor: '#333'
                    }
                },
                data: [{
                    textStyle: {
                        normal: {
                            color: 'black'
                        },
                        emphasis: {
                            color: 'red'
                        }
                    }
                }
                ]
            }]
        }
    },

    //热点标签水平柱状图相关初始化配置
    hot_tags:{
        option:{
            title: {
                text: '热门标签排行',
                subtext: '排前20的标签'
            },
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                    type: 'shadow'
                }
            },
            legend: {
                data: ['包含词条']
            },
            grid: {
                left: '3%',
                right: '4%',
                bottom: '3%',
                containLabel: true
            },
            xAxis: {
                type: 'value',
                boundaryGap: [0, 0.01]
            },
            yAxis: {
                type: 'category',
                data: []
            },
            series: [
                {
                    name: '包含词条',
                    type: 'bar',
                    data: []
                },
            ]
        }
    },

    //热门标签分类饼图初始化配置
    hot_tag_pie:{

        option:{
            title : {
                text: '热门标签占比',
                subtext: 'top 20',
                x:'center'
            },
            tooltip : {
                trigger: 'item',
                formatter: "{a} <br/>{b} : {c} ({d}%)"
            },
            legend: {
                orient: 'vertical',
                left: 'left',
                data: []
            },
            series : [
                {
                    name: '词条标签',
                    type: 'pie',
                    radius : '55%',
                    center: ['50%', '60%'],
                    data:[],
                    itemStyle: {
                        emphasis: {
                            shadowBlur: 10,
                            shadowOffsetX: 0,
                            shadowColor: 'rgba(0, 0, 0, 0.5)'
                        }
                    }
                }
            ]
        },

    },

    //热门词条相关信息折柱混合图初始化设置
    hot_lemma_infos:{
        option:{
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                    type: 'cross',
                    crossStyle: {
                        color: '#999'
                    }
                }
            },
            toolbox: {
                feature: {
                    dataView: {show: true, readOnly: false},
                    magicType: {show: true, type: ['line', 'bar']},
                    restore: {show: true},
                    saveAsImage: {show: true}
                }
            },
            legend: {
                data:['like','share','view']
            },
            xAxis: [
                {
                    type: 'category',
                    data: [],
                    axisPointer: {
                        type: 'shadow'
                    },
                    boundaryGap:[0,0.1]
                }
            ],
            yAxis: [
                {
                    type: 'value',
                    name: '次数',
                    axisLabel: {
                        formatter: function (value,index) {
                            return (value/1000)+"/千次"
                        }
                    }
                },
                {
                    type: 'value',
                    name: '浏览',
                    axisLabel: {
                        formatter: function (value,index) {
                            return (value/10000)+"/万次"
                        }
                    }
                }
            ],
            series: [
                {
                    name:'like',
                    type:'bar',
                    data:[]
                },
                {
                    name:'share',
                    type:'bar',
                    data:[]
                },
                {
                    name:'view',
                    type:'line',
                    yAxisIndex: 1,
                    data:[]
                }
            ]
        },
    },
};

//detail页面下所有图表的配置项
detail_page={

}