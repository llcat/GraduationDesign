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
    <title>search-page</title>
    <link rel="stylesheet" href="../../css/normalize.css">
    <link rel="stylesheet" href="../../css/common.css">
    <link rel="stylesheet" href="../../css/search.css">
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

<div id="main">
    <div id="title-panel">
        <div id="title">
            <h4 id="keyword">${keyword}</h4>
        </div>
        <div id="show-options">
            <span id="choice-key" class="choice" data-flag="1">key</span>
            <span id="choice-tag" class="choice" data-flag="1">tag</span>
            <span id="choice-cluster" class="choice" data-flag="1">cluster</span>
        </div>
    </div>
    <div id="side-tool-bar">
        <div id="search-dialog">
            <h5>尝试搜搜吧！</h5>
            <div class="search-tool">
                <input id="search-input">
                <button id="search-btn"><i class="fa fa-search" aria-hidden="true"></i>
                </button>
            </div>
            <div id="history-search">
                <span>历史搜索：</span>
                <span id="delete-button" title="删除历史记录" class="delete-history"><i class="fa fa-trash-o fa-fw"></i></span>
                <div class="horizon-line"></div>
                <div id="word-panel">

                </div>
            </div>
        </div>
    </div>
    <div id="lemma-search-list">
        <div id="key-result">

        </div>
        <div id="tag-result">

        </div>
        <div id="cluster-result">

        </div>
    </div>
</div>

<footer class="cluster-footer">
    <span class="copy-right">&copy;2016 by llcat</span>
</footer>
</body>
<script src="../../js/plugins/jquery-3.2.1.js"></script>
<script src="../../js/commons/common.js"></script>
<script src="../../js/search.js"></script>
</html>
