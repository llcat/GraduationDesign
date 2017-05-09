<%--
  Created by IntelliJ IDEA.
  User: ypl
  Date: 17-4-30
  Time: 下午12:16
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>home-page</title>
    <link rel="stylesheet" href="../../css/normalize.css">
    <link rel="stylesheet" href="../../css/common.css">
    <link rel="stylesheet" href="../../css/main.css">
    <link href="//cdn.bootcss.com/font-awesome/4.7.0/css/font-awesome.css" rel="stylesheet">
</head>
<body>
<nav class="top-bar">
    <canvas id='top-icon' class="cluster-icon" height="50" width="100">
        <li class="top-bar-li">
            llcat't Design
        </li>
    </canvas>
    <li class="site-title">Cluster Analyze</li>
    <li class="top-bar-li">
        <a href="https://github.com/llcat/GraduationDesign">GitHub</a>
    </li>
    <li class="top-bar-li">
        <a href="#">Docs</a>
    </li>
</nav>
<div class="main">
    <div id="hot-lemma-cloud">
    </div>
        <div id="search-dialog">
            <h5>尝试搜搜吧！</h5>
        <div class="search-tool">
            <input id="search-input">
            <button id="search-btn"><i class="fa fa-search" aria-hidden="true"></i>
            </button>
        </div>
            <div id="history-search">
                <span>历史搜索：</span>
                <div id="word-panel">

                </div>
            </div>
        </div>
    <div id="hot-tag-show">
        <h1>词条的热门标签</h1>
        <div id="hot-tags">
        </div>
        <div id="hot-tags-pie">
        </div>
    </div>
    <div id="hot-lemma-show">
        <div id="hot-lemma-infos">
        </div>
    </div>
</div>
<footer class="cluster-footer">
    <span>&copy;2016 by llcat</span>
</footer>
</body>
<script src="../../js/plugins/jquery-3.2.1.js"></script>
<script src="../../js/plugins/echarts.js"></script>
<script src="../../js/plugins/echarts-word-cloud.js"></script>
<script src="../../js/commons/common.js"></script>
<script src="../../js/charts/chart_options.js"></script>
<script src="../../js/charts/charts_operate.js"></script>
<script src="../../js/main.js"></script>
</html>
