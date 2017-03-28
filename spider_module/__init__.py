# 重写百科spyder,上一个实现不是很稳定而且速度很慢
# 目标:
# 1.能稳定爬取,目的是爬取50W条百度百科词条,并提取相关内容存储到mongoDB数据库中.
# 2.较上次的爬虫实现,加入代理,加入多进程,更改urllib2库为requests库.
# 3.强化下url管理器模块,上一个url的去重实现相对暴力,太low,找一个更好的实现策略.
# 4.后续想到再加

'''
/usr/bin/python3.5 /home/ypl/GraduationDesign/spider_module/baike/baike_downloader.py
(MaxRetryError("HTTPConnectionPool(host='aike.baidu.com', port=80): Max retries exceeded with url: /ite/python (Caused by NewConnectionError('<requests.packages.urllib3.connection.HTTPConnection object at 0x7fe44aedff28>: Failed to establish a new connection: [Errno -2] Name or service not known',))",),)
<!DOCTYPE html>
<!--STATUS OK-->
<html>



<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=Edge" />
<meta name="referrer" content="always" />
<meta name="description" content="Python（英国发音：/ˈpaɪθən/ 美国发音：/ˈpaɪθɑːn/）, 是一种面向对象的解释型计算机程序设计语言，由荷兰人Guido van Rossum于1989年发明，第一个公开发行版发行于1991年。Python是纯粹的自由软件， 源代码和解释器CPython遵循 GPL(GNU General Public License)协议。Python语法简洁清晰，特色之一是强制用空白符(whit...">
<title>Python_百度百科</title>
<link rel="shortcut icon" href="/favicon.ico" type="image/x-icon" />
<link rel="icon" sizes="any" mask href="//www.baidu.com/img/baidu.svg">

<meta name="keywords" content="Python Python发展历程 Python风格 Python设计定位 Python执行 Python基本语法 PythonCGI Python特点 Python应用 Python工具功能 Python标准库 Python开发环境 Python解释器 Python著名应用 Python学习网站">
<meta name="image" content="http://baike.bdimg.com/cms/static/baike.png">
<script type="text/javascript">
  // 配置 PD 监控。
  window.alogObjectConfig = {
    product: '103',
    page: '103_1',
    speed: {
      sample: '0.008'
    },
    monkey: {
      sample: '1',
      hid: '1533'
    },
    exception: {
      sample: '0.004'
    },
    feature: {
      sample: '0.004'
    },
    csp: {
      sample: '0.008',
      'default-src': [
        {match: '*.baidu.com,*.bdimg.com,localhost', target: 'Accept'},
        {match: '*', target: 'Accept,Warn'}
      ]
    }
  };

  void function(a,b,c,d,e,f,g){a.alogObjectName=e,a[e]=a[e]||function(){(a[e].q=a[e].q||[]).push(arguments)},a[e].l=a[e].l||+new Date,d="https:"===a.location.protocol?"https://fex.bdstatic.com"+d:"http://fex.bdstatic.com"+d;var h=!0;if(a.alogObjectConfig&&a.alogObjectConfig.sample){var i=Math.random();a.alogObjectConfig.rand=i,i>a.alogObjectConfig.sample&&(h=!1)}h&&(f=b.createElement(c),f.async=!0,f.src=d+"?v="+~(new Date/864e5)+~(new Date/864e5),g=b.getElementsByTagName(c)[0],g.parentNode.insertBefore(f,g))}(window,document,"script","/hunter/alog/alog.min.js","alog"),void function(){function a(){}window.PDC={mark:function(a,b){alog("speed.set",a,b||+new Date),alog.fire&&alog.fire("mark")},init:function(a){alog("speed.set","options",a)},view_start:a,tti:a,page_ready:a}}();
  void function(n){var o=!1;n.onerror=function(n,e,t,c){var i=!0;return!e&&/^script error/i.test(n)&&(o?i=!1:o=!0),i&&alog("exception.send","exception",{msg:n,js:e,ln:t,col:c}),!1},alog("exception.on","catch",function(n){alog("exception.send","exception",{msg:n.msg,js:n.path,ln:n.ln,method:n.method,flag:"catch"})})}(window);
</script>
<meta name="csrf-token" content="">

<!--[if lte IE 9]>
<script>
    (function() {
      var e = "abbr,article,aside,audio,canvas,datalist,details,dialog,eventsource,figure,footer,header,hgroup,mark,menu,meter,nav,output,progress,section,time,video".split(","),
        i = e.length;
      while (i--) {
        document.createElement(e[i]);
      }
    })();
  </script>
<![endif]-->
<link rel="stylesheet" type="text/css" href="http://baike.bdimg.com/static/wiki-lemma/pkg/wiki-lemma_810727b.css"/><link rel="stylesheet" type="text/css" href="http://baike.bdimg.com/static/wiki-common/pkg/wiki-common-base_b4e62b7.css"/><link rel="stylesheet" type="text/css" href="http://baike.bdimg.com/static/wiki-common/widget/component/userbar/userbar_10e138c.css"/><link rel="stylesheet" type="text/css" href="http://baike.bdimg.com/static/wiki-common/widget/component/searchbar/searchbar_main_f9c7c20.css"/><link rel="stylesheet" type="text/css" href="http://baike.bdimg.com/static/wiki-lemma/pkg/wiki-lemma-module_1dc9f64.css"/><link rel="stylesheet" type="text/css" href="http://baike.bdimg.com/static/wiki-common/widget/component/navbar/navbar_0697c78.css"/><link rel="stylesheet" type="text/css" href="http://baike.bdimg.com/static/wiki-lemma/widget/tools/announcement/announcement_b0d7681.css"/><link rel="stylesheet" type="text/css" href="http://baike.bdimg.com/static/wiki-common/widget/component/unameFiller/unameFiller_d631c34.css"/><link rel="stylesheet" type="text/css" href="http://baike.bdimg.com/static/wiki-lemma/widget/tools/label/label_a444f79.css"/><link rel="stylesheet" type="text/css" href="http://baike.bdimg.com/static/wiki-lemma/widget/tools/newSideShare/sideShare_8eb5f97.css"/><link rel="stylesheet" type="text/css" href="http://baike.bdimg.com/static/wiki-lemma/widget/tools/video/pageMask/pageMask_ff9a193.css"/><link rel="stylesheet" type="text/css" href="http://baike.bdimg.com/static/wiki-common/widget/component/userCard/userCard_2402f1f.css"/><link rel="stylesheet" type="text/css" href="http://baike.bdimg.com/static/wiki-lemma/lemmaCode/style/shCore_7fba49a.css"/><link rel="stylesheet" type="text/css" href="http://baike.bdimg.com/static/wiki-lemma/lemmaCode/style/shCoreDefault_3f91dc3.css"/><link rel="stylesheet" type="text/css" href="http://baike.bdimg.com/static/wiki-lemma/widget/lemma_content/mainContent/mainContent_99d5277.css"/><link rel="stylesheet" type="text/css" href="http://baike.bdimg.com/static/wiki-lemma/widget/lemma_content/mainContent/lemmaRelation/lemmaRelation_9f629f5.css"/><link rel="stylesheet" type="text/css" href="http://baike.bdimg.com/static/wiki-lemma/widget/lemma_content/configModule/zhixin/zhixin_1c34583.css"/><link rel="stylesheet" type="text/css" href="http://baike.bdimg.com/static/wiki-common/widget/component/footer/footer_main_eb7bd79.css"/><link rel="stylesheet" type="text/css" href="http://baike.bdimg.com/static/wiki-lemma/widget/tools/searchHeader/toolButtons/toolButtons-o_4e0bd59.css"/><link rel="stylesheet" type="text/css" href="http://baike.bdimg.com/static/wiki-lemma/widget/tools/searchHeader/toolButtons/userInfo-o_1780f17.css"/><link rel="stylesheet" type="text/css" href="http://baike.bdimg.com/static/wiki-lemma/widget/tools/searchHeader/searchHeader-o_e786bfb.css"/></head>

<script type="text/javascript">
    alog('speed.set', 'ht', +new Date);
</script>

<body class="wiki-lemma normal">



<div class="header-wrapper">
<ul class="wgt-userbar">
<li>
<a href="http://www.baidu.com/">百度首页</a>
</li>
</ul>
<div class="header">
<div class="layout">
<div class="wgt-searchbar wgt-searchbar-main cmn-clearfix">
<div class="logo-container">
<a class="logo cmn-inline-block" title="到百科首页" href="/">
<span class="cmn-baike-logo">
<em class="cmn-icon cmn-icons cmn-icons_logo-bai"></em>
<em class="cmn-icon cmn-icons cmn-icons_logo-du"></em>
<em class="cmn-icon cmn-icons cmn-icons_logo-baike"></em>
</span>
</a>
</div>
<div class="search">
<div class="nav">
<a href="http://news.baidu.com/" nslog="normal" nslog-type="10080001" data-href="http://news.baidu.com/ns?tn=news&cl=2&rn=20&ct=1&fr=bks0000&ie=utf-8&word=">新闻</a>
<a href="http://www.baidu.com/" nslog="normal" nslog-type="10080001" data-href="http://www.baidu.com/s?ie=utf-8&fr=bks0000&wd=">网页</a>
<a href="http://tieba.baidu.com/" nslog="normal" nslog-type="10080001" data-href="http://tieba.baidu.com/f?ie=utf-8&fr=bks0000&kw=">贴吧</a>
<a href="http://zhidao.baidu.com/" nslog="normal" nslog-type="10080001" data-href="http://zhidao.baidu.com/search?pn=0&&rn=10&lm=0&fr=bks0000&word=">知道</a>
<a href="http://music.baidu.com/" nslog="normal" nslog-type="10080001" data-href="http://music.baidu.com/search?f=ms&ct=134217728&ie=utf-8&rn=&lm=-1&pn=30fr=bks0000&key=">音乐</a>
<a href="http://image.baidu.com/" nslog="normal" nslog-type="10080001" data-href="http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=">图片</a>
<a href="http://v.baidu.com/" nslog="normal" nslog-type="10080001" data-href="http://v.baidu.com/v?ct=301989888&rn=20&pn=0&db=0&s=22&ie=utf-8&fr=bks0000&word=">视频</a>
<a href="http://map.baidu.com/" nslog="normal" nslog-type="10080001" data-href="http://map.baidu.com/m?ie=utf-8&fr=bks0000&word=">地图</a>
<a class="baike" nslog="normal" nslog-type="10080001" >百科</a>
<a href="http://wenku.baidu.com/" nslog="normal" nslog-type="10080001" data-href="http://wenku.baidu.com/search?lm=0&od=0&ie=utf-8&fr=bks0000&word=">文库</a>
</div>
<div class="form">
<form id="searchForm" action="/search/word" method="GET" target="_self">
<input id="query" nslog="normal" nslog-type="10080005" name="word" type="text" autocomplete="off" autocorrect="off" value="Python" /><button id="search" nslog="normal" nslog-type="10080002" type="button">进入词条</button><button id="searchLemma" nslog="normal" nslog-type="10080003" type="button">搜索词条</button><a class="help" nslog="normal" nslog-type="10080004" href="/help" target="_blank">帮助</a>
</form>
<form id="searchEnterForm" action="/search/word" method="GET" target="_self">
<input id="searchEnterWord" name="word" type="hidden" />
<input name="sefr" type="hidden" value="cr" />
</form>
<form id="searchQueryForm" action="/search/word" method="GET" target="_self">
<input id="searchQueryWord" name="word" type="hidden" />
<input name="sefr" type="hidden" value="enterbtn" />
</form>
<form id="searchLemmaForm" action="/search" method="GET" target="_self">
<input id="searchLemmaQuery" name="word" type="hidden" />
<input name="pn" type="hidden" value="0" />
<input name="rn" type="hidden" value="0" />
<input name="enc" type="hidden" value="utf8" />
<input name="sefr" type="hidden" value="sebtn" />
</form>
<ul id="suggestion" class="suggestion">
<div class="sug"></div>
<li class="extra">
<span id="close" nslog="normal" nslog-type="10080006" >关闭</span>
</li>
</ul>
</div>
</div>
</div>
<div class="declare-wrap" id="J-declare-wrap">
<div class="declare" id="J-declare">声明：百科词条人人可编辑，词条创建和修改均免费，绝不存在官方及代理商付费代编，请勿上当受骗。<a class="declare-details" target="_blank" href="/common/declaration">详情>></a>
<div class="close-btn" id="J-declare-close">
<em class="cmn-icon cmn-icons cmn-icons_close"></em>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="navbar-wrapper">
<div class="wgt-navbar">
<div class="navbar-bg">
<div class="navbar-bg-top">
<div class="navbar-content layout">
<div class="navbar-content-box">
<dl class="index ">
<dt><a href="/">首页</a></dt>
</dl>
<dl class="cat ">
<dt><a>分类</a></dt>
<dd>
<div><a href="/art" target="_blank" class="art">艺术</a></div>
<div><a href="/science" target="_blank" class="technology">科学</a></div>
<div><a href="/ziran" target="_blank">自然</a></div>
<div><a href="/wenhua" target="_blank">文化</a></div>
<div><a href="/dili" target="_blank">地理</a></div>
<div><a href="/shenghuo" target="_blank">生活</a></div>
<div><a href="/shehui" target="_blank">社会</a></div>
<div><a href="/renwu" target="_blank">人物</a></div>
<div><a href="/jingji" target="_blank">经济</a></div>
<div><a href="/tiyu" target="_blank">体育</a></div>
<div><a href="/lishi" target="_blank">历史</a></div>
</dd>
</dl>
<dl class="special ">
<dt><a>特色百科</a></dt>
<dd>
<div><a href="/calendar/" target="_blank">历史上的今天</a></div>
<div><a href="/museum/" target="_blank">数字博物馆</a></div>
<div><a href="/item/史记·2016?fr=navbar" target="_blank">史记·2016</a></div>
<div><a href="/city/" target="_blank">城市百科</a></div>
<div><a href="/operation/worldwar2" target="_blank">二战百科</a></div>
<div><a href="/feiyi?fr=dhlfeiyi" target="_blank">非遗百科</a></div>
</dd>
</dl>
<dl class="user" >
<dt><a>用户</a></dt>
<dd>
<div><a href="/kedou/" target="_blank">蝌蚪团</a></div>
<div><a href="/event/ranmeng/" target="_blank">燃梦计划</a></div>
<div><a href="/task/" target="_blank">百科任务</a></div>
<div><a href="/mall/" target="_blank">百科商城</a></div>
</dd>
</dl>
<dl class="cooperation" >
<dt><a>权威合作</a></dt>
<dd>
<div><a href="/operation/cooperation#joint" target="_blank">合作模式</a></div>
<div><a href="/operation/cooperation#issue" target="_blank">常见问题</a></div>
<div><a href="/operation/cooperation#connection" target="_blank">联系方式</a></div>
</dd>
</dl>
<dl class="mobile" >
<dt><a>手机百科</a></dt>
<dd>
<div><a href="/m#wap" target="_blank">网页版</a></div>
</dd>
</dl>
<div class="usercenter">
<div><a href="/usercenter" target="_blank"><em class="cmn-icon cmn-icons cmn-icons_navbar-usercenter"></em>个人中心</a></div>
</div></div>
</div>
</div>
</div>
</div>
</div>


<div class="body-wrapper">
<div class="before-content">
</div>
<div class="content-wrapper">
<div class="content">
<div class="personal-content">
</div>
<div class="main-content">
<div class="top-tool">
<a class="add-sub-icon" href="javascript:;" title="添加义项" nslog-type="50000101"></a>
<a href="/divideload/Python" title="拆分词条" target="_blank" class="split-icon" style="display:none;" nslog-type="50000104"></a>
<div class="top-collect" nslog="area" nslog-type="50000102">
<span class="collect-text">收藏</span>
<div class="collect-tip">查看<a href="/uc/favolemma" target="_blank">我的收藏</a></div>
</div>
<a href="javascript:void(0);" id="j-top-vote" class="top-vote" nslog-type="10060801">
<span class="vote-count">0</span>
<span class="vote-tip">有用+1</span>
<span class="voted-tip">已投票</span>
</a><div class="bksharebuttonbox top-share">
<a class="top-share-icon" nslog-type="9067">
<span class="share-count" id="j-topShareCount">0</span>
</a>
<div class="new-top-share" id="top-share">
<ul class="top-share-list">
<li class="top-share-item">
<a class="share-link bds_qzone"  href="javascript:void(0);" nslog-type="10060501">
<em class="cmn-icon cmn-icons cmn-icons_logo-qzone"></em>
</a>
</li>
<li class="top-share-item">
<a class="share-link bds_tsina" href="javascript:void(0);" nslog-type="10060701">
<em class="cmn-icon cmn-icons cmn-icons_logo-sina-weibo"></em>
</a>
</li>
<li class="top-share-item">
<a class="bds_wechat"  href="javascript:void(0);" nslog-type="10060401">
<em class="cmn-icon cmn-icons cmn-icons_logo-wechat"></em>
</a>
</li>
<li class="top-share-item">
<a class="share-link bds_tqq"  href="javascript:void(0);" nslog-type="10060601">
<em class="cmn-icon cmn-icons cmn-icons_logo-qq"></em>
</a>
</li>
</ul>
</div>
</div>
</div>
<div style="width:0;height:0;clear:both"></div><dl class="lemmaWgt-lemmaTitle lemmaWgt-lemmaTitle-">
<dd class="lemmaWgt-lemmaTitle-title">
<h1 >Python</h1>
<a href="javascript:;" class="edit-lemma cmn-btn-hover-blue cmn-btn-28 j-edit-link"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_edit-lemma"></em>编辑</a>
<a class="lock-lemma" target="_blank" href="/view/10812319.htm" title="锁定"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_lock-lemma"></em>锁定</a>
</dd>
</dl><div class="promotion-declaration">
</div><div class="lemma-summary" label-module="lemmaSummary">
<div class="para" label-module="para">Python<sup>[1]</sup><a class="sup-anchor" name="ref_[1]_21087">&nbsp;</a>
（英国发音：/ˈpaɪθən/ 美国发音：/ˈpaɪθɑːn/）, 是一种面向对象的解释型<a target=_blank href="/item/%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1%E8%AF%AD%E8%A8%80">计算机程序设计语言</a>，由荷兰人<a target=_blank href="/item/Guido%20van%20Rossum">Guido van Rossum</a>于1989年发明，第一个公开发行版发行于1991年。</div><div class="para" label-module="para">Python是纯粹的<a target=_blank href="/item/%E8%87%AA%E7%94%B1%E8%BD%AF%E4%BB%B6">自由软件</a>， <a target=_blank href="/item/%E6%BA%90%E4%BB%A3%E7%A0%81/3969" data-lemmaid="3969">源代码</a>和<a target=_blank href="/item/%E8%A7%A3%E9%87%8A%E5%99%A8">解释器</a>CPython遵循 <a target=_blank href="/item/GPL">GPL</a>(<a target=_blank href="/item/GNU">GNU</a> General Public License)协议<sup>[2]</sup><a class="sup-anchor" name="ref_[2]_21087">&nbsp;</a>
。</div><div class="para" label-module="para">Python语法简洁清晰，特色之一是强制用空白符(white space)作为语句缩进。</div><div class="para" label-module="para">Python具有丰富和强大的库。它常被昵称为<a target=_blank href="/item/%E8%83%B6%E6%B0%B4%E8%AF%AD%E8%A8%80">胶水语言</a>，能够把用其他语言制作的各种模块（尤其是<a target=_blank href="/item/C/7252092" data-lemmaid="7252092">C</a>/<a target=_blank href="/item/C%2B%2B">C++</a>）很轻松地联结在一起。常见的一种应用情形是，使用Python快速生成程序的原型（有时甚至是程序的最终界面），然后对其中<sup>[3]</sup><a class="sup-anchor" name="ref_[3]_21087">&nbsp;</a>
有特别要求的部分，用更合适的语言改写，比如<a target=_blank href="/item/3D%E6%B8%B8%E6%88%8F">3D游戏</a>中的图形渲染模块，性能要求特别高，就可以用C/C++重写，而后封装为Python可以调用的扩展类库。需要注意的是在您使用扩展类库时可能需要考虑平台问题，某些可能不提供<a target=_blank href="/item/%E8%B7%A8%E5%B9%B3%E5%8F%B0">跨平台</a>的实现。</div>
</div>
<div class="configModuleBanner">
</div><div class="basic-info cmn-clearfix">
<dl class="basicInfo-block basicInfo-left">
<dt class="basicInfo-item name">外文名</dt>
<dd class="basicInfo-item value">
Python
</dd>
<dt class="basicInfo-item name">经典教材</dt>
<dd class="basicInfo-item value">
Head First Python
</dd>
<dt class="basicInfo-item name">发行时间</dt>
<dd class="basicInfo-item value">
1991年
</dd>
</dl><dl class="basicInfo-block basicInfo-right">
<dt class="basicInfo-item name">设计者</dt>
<dd class="basicInfo-item value">
Guido van Rossum
</dd>
<dt class="basicInfo-item name">最新版本</dt>
<dd class="basicInfo-item value">
3.6.0/2.7.13
</dd>
<dt class="basicInfo-item name">荣&nbsp;&nbsp;&nbsp;&nbsp;誉</dt>
<dd class="basicInfo-item value">
2010年度编程语言
</dd>
<dt class="basicInfo-item name">Python域名</dt>
<dd class="basicInfo-item value">
<a target=_blank href="/item/.com">.com</a>、.cn、<a target=_blank href="/item/.cx">.cx</a>、.cc等
</dd>
</dl></div>
<div class="lemmaWgt-lemmaCatalog">
<div class="lemma-catalog">
<h2 class="block-title">目录</h2>
<div class="catalog-list column-4">
<ol>
<li class="level1">
<span class="index">1</span>
<span class="text"><a href="#1">发展历程</a></span>
</li>
<li class="level1">
<span class="index">2</span>
<span class="text"><a href="#2">风格</a></span>
</li>
<li class="level1">
<span class="index">3</span>
<span class="text"><a href="#3">设计定位</a></span>
</li>
<li class="level1">
<span class="index">4</span>
<span class="text"><a href="#4">执行</a></span>
</li>
<li class="level1">
<span class="index">5</span>
<span class="text"><a href="#5">基本语法</a></span>
</li>
<li class="level2">
<span class="index">▪</span>
<span class="text"><a href="#5_1">缩进</a></span>
</li>
</ol><ol><li class="level2">
<span class="index">▪</span>
<span class="text"><a href="#5_2">控制语句</a></span>
</li>
<li class="level2">
<span class="index">▪</span>
<span class="text"><a href="#5_3">表达式</a></span>
</li>
<li class="level2">
<span class="index">▪</span>
<span class="text"><a href="#5_4">函数</a></span>
</li>
<li class="level2">
<span class="index">▪</span>
<span class="text"><a href="#5_5">对象的方法</a></span>
</li>
<li class="level2">
<span class="index">▪</span>
<span class="text"><a href="#5_6">类型</a></span>
</li>
<li class="level2">
<span class="index">▪</span>
<span class="text"><a href="#5_7">数学运算</a></span>
</li>
<li class="level1">
<span class="index">6</span>
<span class="text"><a href="#6">CGI</a></span>
</li>
<li class="level2">
<span class="index">▪</span>
<span class="text"><a href="#6_1">服务器</a></span>
</li>
</ol><ol><li class="level2">
<span class="index">▪</span>
<span class="text"><a href="#6_2">程序</a></span>
</li>
<li class="level2">
<span class="index">▪</span>
<span class="text"><a href="#6_3">环境变量</a></span>
</li>
<li class="level1">
<span class="index">7</span>
<span class="text"><a href="#7">特点</a></span>
</li>
<li class="level2">
<span class="index">▪</span>
<span class="text"><a href="#7_1">优点</a></span>
</li>
<li class="level2">
<span class="index">▪</span>
<span class="text"><a href="#7_2">缺点</a></span>
</li>
<li class="level1">
<span class="index">8</span>
<span class="text"><a href="#8">应用</a></span>
</li>
<li class="level1">
<span class="index">9</span>
<span class="text"><a href="#9">工具功能</a></span>
</li>
</ol><ol><li class="level1">
<span class="index">10</span>
<span class="text"><a href="#10">标准库</a></span>
</li>
<li class="level1">
<span class="index">11</span>
<span class="text"><a href="#11">开发环境</a></span>
</li>
<li class="level1">
<span class="index">12</span>
<span class="text"><a href="#12">解释器</a></span>
</li>
<li class="level1">
<span class="index">13</span>
<span class="text"><a href="#13">著名应用</a></span>
</li>
<li class="level1">
<span class="index">14</span>
<span class="text"><a href="#14">学习网站</a></span>
</li>
</ol>

</div>
</div>
</div>
<div class="anchor-list">
<a name="1" class="lemma-anchor para-title" ></a>
<a name="sub21087_1" class="lemma-anchor " ></a>
<a name="发展历程" class="lemma-anchor " ></a>
</div><div class="para-title level-2" label-module="para-title">
<h2 class="title-text"><span class="title-prefix">Python</span>发展历程</h2>
<a class="edit-icon j-edit-link" data-edit-dl="1" href="javascript:;"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_edit-lemma"></em>编辑</a>
</div>
<div class="para" label-module="para">自从20世纪90年代初Python语言诞生至今，它已被逐渐广泛应用于系统管理任务的处理和<a target=_blank href="/item/Web/150564" data-lemmaid="150564">Web</a>编程。</div>
<div class="para" label-module="para">Python的创始人为Guido van Rossum。1989年圣诞节期间，在<a target=_blank href="/item/%E9%98%BF%E5%A7%86%E6%96%AF%E7%89%B9%E4%B8%B9/2259975" data-lemmaid="2259975">阿姆斯特丹</a>，Guido为了打发圣诞节的无趣，决心开发一个新的脚本解释程序，做为ABC 语言的一种继承。之所以选中Python（大蟒蛇的意思）作为该编程语言的名字，是因为他是一个叫Monty Python的喜剧团体的爱好者。</div>
<div class="para" label-module="para">ABC是由Guido参加设计的一种教学语言。就Guido本人看来，ABC 这种语言非常优美和强大，是专门为非专业程序员设计的。但是ABC语言并没有成功，究其原因，Guido 认为是其非开<div class="lemma-picture text-pic layout-right" style="width:220px; float: right;">
<a class="image-link" nslog-type="9317"
			href="/pic/Python/407313/0/faedab64034f78f092033e1079310a55b2191ccc?fr=lemma&ct=single" target="_blank"
		title="标识" style="width:220px;height:118px;">
<img  class="lazy-img" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAMAAAAoyzS7AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAZQTFRF9fX1AAAA0VQI3QAAAAxJREFUeNpiYAAIMAAAAgABT21Z4QAAAABJRU5ErkJggg==" data-src="http://f.hiphotos.baidu.com/baike/s%3D220/sign=df945cc2728b4710ca2ffacef3cfc3b2/faedab64034f78f092033e1079310a55b2191ccc.jpg"  alt="标识" style="width:220px;height:118px;"/>
</a>
<span class="description">
标识
</span>
</div>放造成的。Guido 决心在Python 中避免这一错误。同时，他还想实现在ABC 中闪现过但未曾实现的东西。</div>
<div class="para" label-module="para">就这样，Python在Guido手中诞生了。可以说，Python是从ABC发展起来，主要受到了Modula-3（另一种相当优美且强大的语言，为小型团体所设计的）的影响。并且结合了<a target=_blank href="/item/Unix%20shell">Unix shell</a>和C的习惯。</div>
<div class="para" label-module="para">Python<sup>[4]</sup><a class="sup-anchor" name="ref_[4]_21087">&nbsp;</a>
已经成为最受欢迎的程序设计语言之一。2011年1月，它被<a target=_blank href="/item/TIOBE">TIOBE</a>编程语言排行榜评为2010年度语言。自从2004年以后，python的使用率呈线性增长<sup>[5]</sup><a class="sup-anchor" name="ref_[5]_21087">&nbsp;</a>
。</div>
<div class="para" label-module="para">由于Python语言的简洁性、易读性以及可扩展性，在国外用Python做科学计算的研究机构日益增多，一些知名大学已经采用Python来教授程序设计课程。例如<a target=_blank href="/item/%E5%8D%A1%E8%80%90%E5%9F%BA%E6%A2%85%E9%9A%86%E5%A4%A7%E5%AD%A6">卡耐基梅隆大学</a>的编程基础、麻省理工学院的计算机科学及编程导论就使用Python语言讲授。众多开源的科学计算软件包都提供了Python的调用<a target=_blank href="/item/%E6%8E%A5%E5%8F%A3">接口</a>，例如著名的计算机视觉库<a target=_blank href="/item/OpenCV">OpenCV</a>、三维可视化库VTK、医学图像处理库ITK。而Python专用的科学计算扩展库就更多了，例如如下3个十分经典的科学计算扩展库：NumPy、SciPy和matplotlib，它们分别为Python提供了快速数组处理、数值运算以及绘图功能。因此Python语言及其众多的扩展库所构成的开发环境十分适合工程技术、科研人员处理实验数据、制作图表，甚至开发科学计算<a target=_blank href="/item/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F">应用程序</a>。</div>
<div class="para" label-module="para">说起科学计算，首先会被提到的可能是<a target=_blank href="/item/MATLAB">MATLAB</a>。然而除了MATLAB的一些专业性很强的工具箱还无法替代之外，MATLAB的大部分常用功能都可以在Python世界中找到相应的扩展库。和MATLAB相比，用Python做科学计算有如下优点：</div>
<div class="para" label-module="para">● 首先，MATLAB是一款商用软件，并且价格不菲。而Python完全免费，众多开源的科学计算库都提供了Python的调用接口。用户可以在任何计算机上免费安装Python及其绝大多数扩展库。</div>
<div class="para" label-module="para">● 其次，与MATLAB相比，Python是一门更易学、更严谨的程序设计语言。它能让用户编写出更易读、易维护的代码。</div>
<div class="para" label-module="para">● 最后，MATLAB主要专注于工程和科学计算。然而即使在计算领域，也经常会遇到文件管理、<a target=_blank href="/item/%E7%95%8C%E9%9D%A2%E8%AE%BE%E8%AE%A1">界面设计</a>、<a target=_blank href="/item/%E7%BD%91%E7%BB%9C%E9%80%9A%E4%BF%A1">网络通信</a>等各种需求。而Python有着丰富的扩展库，可以轻易完成各种高级任务，开发者可以用Python实现完整应用程序所需的各种功能。</div><div class="anchor-list">
<a name="2" class="lemma-anchor para-title" ></a>
<a name="sub21087_2" class="lemma-anchor " ></a>
<a name="风格" class="lemma-anchor " ></a>
</div><div class="para-title level-2" label-module="para-title">
<h2 class="title-text"><span class="title-prefix">Python</span>风格</h2>
<a class="edit-icon j-edit-link" data-edit-dl="2" href="javascript:;"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_edit-lemma"></em>编辑</a>
</div>
<div class="para" label-module="para">Python在设计上坚持了清晰划一的风格，这使得Python成为一门易读、易维护，并且被大量用户所欢迎的、用途广泛的语言。</div>
<div class="para" label-module="para">设计者开发时总的指导思想是，对于一个特定的问题，只要有一种最好的方法来解决就好了。这在由Tim Peters写的Python格言（称为The Zen of Python）里面表述为：There should be one-- and preferably only one --obvious way to do it. 这正好和<a target=_blank href="/item/Perl">Perl</a>语言（另一种功能类似的高级<a target=_blank href="/item/%E5%8A%A8%E6%80%81%E8%AF%AD%E8%A8%80">动态语言</a>）的中心思想TMTOWTDI（There&#39;s More Than One Way To Do It）完全相反。</div>
<div class="para" label-module="para">Python的作者有意的设计限制性很强的语法，使得不好的编程习惯（例如<a target=_blank href="/item/if%E8%AF%AD%E5%8F%A5">if语句</a>的下一行不向右缩进）都不能通过编译。其中很重要的一项就是Python的缩进规则。</div>
<div class="para" label-module="para">一个和其他大多数语言（如C）的区别就是，一个模块的界限，完全是由每行的首字符在这一行的位置来决定的（而C语言是用一对花括号<a target=_blank href="/item/%7B%7D">{}</a>来明确的定出模块的边界的，与字符的位置毫无关系）。这一点曾经引起过争议。因为自从C这类的语言诞生后，语言的语法含义与字符的排列方式分离开来，曾经被认为是一种程序语言的进步。不过不可否认的是，通过强制程序员们<a target=_blank href="/item/%E7%BC%A9%E8%BF%9B">缩进</a>（包括if，for和函数定义等所有需要使用模块的地方），Python确实使得程序更加清晰和美观。</div><div class="anchor-list">
<a name="3" class="lemma-anchor para-title" ></a>
<a name="sub21087_3" class="lemma-anchor " ></a>
<a name="设计定位" class="lemma-anchor " ></a>
</div><div class="para-title level-2" label-module="para-title">
<h2 class="title-text"><span class="title-prefix">Python</span>设计定位</h2>
<a class="edit-icon j-edit-link" data-edit-dl="3" href="javascript:;"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_edit-lemma"></em>编辑</a>
</div>
<div class="para" label-module="para">Python的设计哲学是“优雅”、“明确”、“简单”。因此，Perl语言中“总是有多种方法来做同一件事”的理念在Python开发者中通常是难以忍受的。Python开发者的哲学是“用一种方法，最好是只有一种方法来做一件事”。在设计Python语言时，如果面临多种选择，Python开发者一般会拒绝花俏的语法，而选择明确的没有或者很少有歧义的语法。由于这种设计观念的差异，Python源代码通常被认为比Perl具备更好的可读性，并且能够支撑大规模的软件开发。这些准则被称为Python格言。在Python<a target=_blank href="/item/%E8%A7%A3%E9%87%8A%E5%99%A8">解释器</a>内运行import this可以获得完整的列表。</div>
<div class="para" label-module="para">Python开发人员尽量避开不成熟或者不重要的优化。一些针对非重要部位的加快运行速度的补丁通常不会被合并到Python内。所以很多人认为Python很慢。不过，根据二八定律，大多数程序对速度要求不高。在某些对运行速度要求很高的情况，Python设计师倾向于使用<a target=_blank href="/item/JIT">JIT</a>技术，或者用使用C/C++语言改写这部分程序。可用的JIT技术是<a target=_blank href="/item/PyPy">PyPy</a>。</div>
<div class="para" label-module="para">Python是完全面向对象的语言。函数、模块、数字、字符串都是对象。并且完全支持继承、重载、派生、多继承，有益于增强源代码的复用性。Python支持重载运算符和动态类型。相对于<a target=_blank href="/item/Lisp/22083" data-lemmaid="22083">Lisp</a>这种传统的函数式编程语言，Python对函数式设计只提供了有限的支持。有两个标准库(functools, itertools)提供了<a target=_blank href="/item/Haskell">Haskell</a>和Standard ML中久经考验的函数式程序设计工具。</div>
<div class="para" label-module="para">虽然Python可能被粗略地分类为“<a target=_blank href="/item/%E8%84%9A%E6%9C%AC%E8%AF%AD%E8%A8%80">脚本语言</a>”（script language），但实际上一些大规模软件开发计划例如<a target=_blank href="/item/Zope">Zope</a>、<a target=_blank href="/item/Mnet">Mnet</a>及BitTorrent，Google也广泛地使用它。Python的支持者较喜欢称它为一种高级动态编程语言，原因是“脚本语言”泛指仅作简单程序设计任务的语言，如shellscript、<a target=_blank href="/item/VBScript">VBScript</a>等只能处理简单任务的编程语言，并不能与Python相提并论。</div>
<div class="para" label-module="para">Python本身被设计为可扩充的。并非所有的特性和功能都集成到语言核心。Python提供了丰富的<a target=_blank href="/item/API/10154" data-lemmaid="10154">API</a>和工具，以便程序员能够轻松地使用C语言、C++、Cython来编写扩充模块。Python编译器本身也可以被集成到其它需要脚本语言的程序内。因此，很多人还把Python作为一种“胶水语言”（glue language）使用。使用Python将其他语言编写的程序进行集成和封装。在Google内部的很多项目，例如Google Engine使用C++编写性能要求极高的部分，然后用Python或Java/Go调用相应的模块。《<a target=_blank href="/item/Python%E6%8A%80%E6%9C%AF%E6%89%8B%E5%86%8C">Python技术手册</a>》的作者<a target=_blank href="/item/%E9%A9%AC%E7%89%B9%E5%88%A9">马特利</a>（Alex Martelli）说：“这很难讲，不过，2004 年，Python 已在<a target=_blank href="/item/Google">Google</a> 内部使用，Google 召募许多 Python 高手，但在这之前就已决定使用Python，他们的目的是 Python where we can, C++ where we must，在操控硬件的场合使用 C++，在快速开发时候使用 Python。”</div><div class="anchor-list">
<a name="4" class="lemma-anchor para-title" ></a>
<a name="sub21087_4" class="lemma-anchor " ></a>
<a name="执行" class="lemma-anchor " ></a>
</div><div class="para-title level-2" label-module="para-title">
<h2 class="title-text"><span class="title-prefix">Python</span>执行</h2>
<a class="edit-icon j-edit-link" data-edit-dl="4" href="javascript:;"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_edit-lemma"></em>编辑</a>
</div>
<div class="para" label-module="para">Python在执行时，首先会将.py文件中的<a target=_blank href="/item/%E6%BA%90%E4%BB%A3%E7%A0%81/3969" data-lemmaid="3969">源代码</a>编译成Python的byte code（字节码），然后再由Python Virtual Machine（Python<a target=_blank href="/item/%E8%99%9A%E6%8B%9F%E6%9C%BA">虚拟机</a>）来执行这些编译好的byte code。这种机制的基本思想跟Java，.NET是一致的。然而，Python Virtual Machine与Java或.NET的Virtual Machine不同的是，Python的Virtual Machine是一种更高级的Virtual Machine。这里的高级并不是通常意义上的高级，不是说Python的Virtual Machine比Java或.NET的功能更强大，而是说和Java 或.NET相比，Python的Virtual Machine距离真实机器的距离更远。或者可以这么说，Python的Virtual Machine是一种抽象层次更高的Virtual Machine。</div>
<div class="para" label-module="para">基于C的Python编译出的<a target=_blank href="/item/%E5%AD%97%E8%8A%82%E7%A0%81">字节码</a>文件，通常是.pyc格式。</div>
<div class="para" label-module="para">除此之外，Python还可以以交互模式运行，比如主流操作系统Unix/Linux、Mac、Windows都可以直接在命令模式下直接运行Python交互环境。直接下达操作指令即可实现交互操作。</div><div class="anchor-list">
<a name="5" class="lemma-anchor para-title" ></a>
<a name="sub21087_5" class="lemma-anchor " ></a>
<a name="基本语法" class="lemma-anchor " ></a>
</div><div class="para-title level-2" label-module="para-title">
<h2 class="title-text"><span class="title-prefix">Python</span>基本语法</h2>
<a class="edit-icon j-edit-link" data-edit-dl="5" href="javascript:;"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_edit-lemma"></em>编辑</a>
</div>
<div class="para" label-module="para">Python的设计目标之一是让代码具备高度的可阅读性。它设计时尽量使用其它语言经常使用的标点符号和英文单字，让代码看起来整洁美观。它不像其他的静态语言如C、Pascal那样需要重复书写声明语句，也不像它们的语法那样经常有特殊情况和意外。</div><div class="anchor-list">
<a name="5_1" class="lemma-anchor para-title" ></a>
<a name="sub21087_5_1" class="lemma-anchor " ></a>
<a name="缩进" class="lemma-anchor " ></a>
</div><div class="para-title level-3" label-module="para-title">
<h3 class="title-text"><span class="title-prefix">Python</span>缩进</h3>
</div>
<div class="para" label-module="para">Python开发者有意让违反了缩进规则的程序不能通过编译，以此来强制程序员养成良好的编程习惯。并且Python语言利用缩进表示语句块的开始和退出（Off-side规则），而非使用花括号或者某种关键字。增加缩进表示语句块的开始，而减少缩进则表示语句块的退出。缩进成为了语法的一部分。例如if语句：</div>
<pre class="brush: python">if&nbsp;age&lt;21:
&nbsp;&nbsp;&nbsp;&nbsp;print(&quot;你不能买酒。&quot;)
&nbsp;&nbsp;&nbsp;&nbsp;print(&quot;不过你能买口香糖。&quot;)
print(&quot;这句话处於if语句块的外面。&quot;)
</pre><div class="para" label-module="para">注:上述例子为python 3.0版本的代码</div>
<div class="para" label-module="para">根据PEP的规定，必须使用<b>4个空格</b>来表示每级缩进（不清楚4个空格的规定如何，在实际编写中可以自定义空格数，但是要满足每级缩进间空格数相等）。使用Tab字符和其它数目的空格虽然都可以编译通过，但不符合编码规范。支持Tab字符和其它数目的空格仅仅是为兼容很旧的的Python程序和某些有问题的编辑程序。</div><div class="anchor-list">
<a name="5_2" class="lemma-anchor para-title" ></a>
<a name="sub21087_5_2" class="lemma-anchor " ></a>
<a name="控制语句" class="lemma-anchor " ></a>
</div><div class="para-title level-3" label-module="para-title">
<h3 class="title-text"><span class="title-prefix">Python</span>控制语句</h3>
</div>
<div class="para" label-module="para">if语句，当条件成立时运行语句块。经常与else, elif(相当于else if) 配合使用。</div>
<div class="para" label-module="para">for语句，遍历列表、字符串、字典、集合等<a target=_blank href="/item/%E8%BF%AD%E4%BB%A3%E5%99%A8">迭代器</a>，依次处理迭代器中的每个元素。</div>
<div class="para" label-module="para">while语句，当条件为真时，循环运行语句块。</div>
<div class="para" label-module="para">try语句。与except,finally配合使用处理在程序运行中出现的异常情况。</div>
<div class="para" label-module="para">class语句。用于定义<a target=_blank href="/item/%E7%B1%BB%E5%9E%8B/6737759" data-lemmaid="6737759">类型</a>。</div>
<div class="para" label-module="para">def语句。用于定义函数和类型的方法。</div>
<div class="para" label-module="para">pass语句。表示此行为空，不运行任何操作。</div>
<div class="para" label-module="para">assert语句。用于程序调试阶段时测试运行条件是否满足。</div>
<div class="para" label-module="para">with语句。Python2.6以后定义的语法，在一个场景中运行语句块。比如，运行语句块前加密，然后在语句块运行退出后解密。</div>
<div class="para" label-module="para">yield语句。在迭代器函数内使用，用于返回一个元素。自从Python 2.5版本以后。这个语句变成一个运算符。</div>
<div class="para" label-module="para">raise语句。制造一个错误。</div>
<div class="para" label-module="para">import语句。导入一个模块或包。</div>
<div class="para" label-module="para">from import语句。从包导入模块或从模块导入某个对象。</div>
<div class="para" label-module="para">import as语句。将导入的对象赋值给一个变量。</div>
<div class="para" label-module="para">in语句。判断一个对象是否在一个字符串/列表/元组里。</div><div class="anchor-list">
<a name="5_3" class="lemma-anchor para-title" ></a>
<a name="sub21087_5_3" class="lemma-anchor " ></a>
<a name="表达式" class="lemma-anchor " ></a>
</div><div class="para-title level-3" label-module="para-title">
<h3 class="title-text"><span class="title-prefix">Python</span>表达式</h3>
</div>
<div class="para" label-module="para">Python的表达式写法与C/C++类似。只是在某些写法有所差别。</div>
<div class="para" label-module="para">主要的算术运算符与C/C++类似。+, -, *, /, //, **, ~, %分别表示加法或者取正、减法或者取负、乘法、除法、整除、乘方、取补、取模。&gt;&gt;, &lt;&lt;表示右移和左移。&amp;, |, ^表示二进制的AND, OR, XOR运算。&gt;, &lt;, ==, !=, &lt;=, &gt;=用于比较两个表达式的值，分别表示大于、小于、等于、不等于、小于等于、大于等于。在这些运算符里面，~, |, ^, &amp;, &lt;&lt;, &gt;&gt;必须应用于整数。</div>
<div class="para" label-module="para">Python使用and, or, not表示逻辑运算。</div>
<div class="para" label-module="para">is, is not用于比较两个变量是否是同一个对象。in, not in用于判断一个对象是否属于另外一个对象。</div>
<div class="para" label-module="para">Python支持“列表推导式”（list comprehension），比如计算0-9的平方和:</div>
<div class="para" label-module="para">&gt;&gt;&gt; sum(x * x for x in range(10))</div>
<div class="para" label-module="para">285</div>
<div class="para" label-module="para">Python使用lambda表示匿名函数。匿名函数体只能是表达式。比如：</div>
<div class="para" label-module="para">&gt;&gt;&gt; add=lambda x, y : x + y</div>
<div class="para" label-module="para">&gt;&gt;&gt; add(3,2)</div>
<div class="para" label-module="para">5</div>
<div class="para" label-module="para">Python使用y if cond else x表示条件表达式。意思是当cond为真时，表达式的值为y，否则表达式的值为x。相当于C++和Java里的cond?y:x。</div>
<div class="para" label-module="para">Python区分列表(list)和元组(tuple)两种类型。list的写法是[1,2,3]，而tuple的写法是(1,2,3)。可以改变list中的元素，而不能改变tuple。在某些情况下，tuple的括号可以省略。tuple对于赋值语句有特殊的处理。因此，可以同时赋值给多个变量，比如：</div>
<div class="para" label-module="para">&gt;&gt;&gt; x, y=1,2#同时给x,y赋值，最终结果：x=1, y=2</div>
<div class="para" label-module="para">特别地，可以使用以下这种形式来交换两个变量的值：</div>
<div class="para" label-module="para">&gt;&gt;&gt; x, y=y, x #最终结果：y=1, x=2</div>
<div class="para" label-module="para">Python使用&#39;(单引号)和&quot;(双引号)来表示字符串。与Perl、Unix Shell语言或者Ruby、Groovy等语言不一样，两种符号作用相同。一般地，如果字符串中出现了双引号，就使用单引号来表示字符串;反之则使用双引号。如果都没有出现，就依个人喜好选择。出现在字符串中的\(反斜杠)被解释为特殊字符，比如\n表示换行符。表达式前加r指示Python不解释字符串中出现的\。这种写法通常用于编写正则表达式或者Windows文件路径。</div>
<div class="para" label-module="para">Python支持列表切割(list slices)，可以取得完整列表的一部分。支持切割操作的类型有str, bytes, list, tuple等。它的语法是...[left:right]或者...[left:right:stride]。假定nums变量的值是[1, 3, 5, 7, 8, 13, 20]，那么下面几个语句为真：</div>
<div class="para" label-module="para">nums[2:5] == [5, 7, 8] 从下标为2的元素切割到下标为5的元素，但不包含下标为2的元素。</div>
<div class="para" label-module="para">nums[1:] == [3, 5, 7, 8, 13, 20] 切割到最后一个元素。</div>
<div class="para" label-module="para">nums[:-3] == [1, 3, 5, 7] 从最开始的元素一直切割到倒数第3个元素。</div>
<div class="para" label-module="para">nums[:] == [1, 3, 5, 7, 8, 13, 20] 返回所有元素。改变新的列表不会影响到nums。</div>
<div class="para" label-module="para">nums[1:5:2] == [3, 7] 从下标为1的元素切割到下标为5的元素但不包含下标为5的元素，且步长为2。</div><div class="anchor-list">
<a name="5_4" class="lemma-anchor para-title" ></a>
<a name="sub21087_5_4" class="lemma-anchor " ></a>
<a name="函数" class="lemma-anchor " ></a>
</div><div class="para-title level-3" label-module="para-title">
<h3 class="title-text"><span class="title-prefix">Python</span>函数</h3>
</div>
<div class="para" label-module="para">Python的函数支持递归、默认参数值、可变参数，但不支持函数重载。为了增强代码的可读性，可以在函数后书写“文档字符串”(Documentation Strings，或者简称docstrings)，用于解释函数的作用、参数的类型与意义、返回值类型与取值范围等。可以使用内置函数help()打印出函数的使用帮助。比如：</div>
<div class="para" label-module="para">&gt;&gt;&gt; def randint(a, b):</div>
<div class="para" label-module="para">... &quot;Return random integer in range [a, b], including both end points.&quot;...</div>
<div class="para" label-module="para">&gt;&gt;&gt; help(randint)</div>
<div class="para" label-module="para">Help on function randint in module __main__:</div>
<div class="para" label-module="para">randint(a, b)</div>
<div class="para" label-module="para">Return random integer inrange[a, b], including both end points.</div><div class="anchor-list">
<a name="5_5" class="lemma-anchor para-title" ></a>
<a name="sub21087_5_5" class="lemma-anchor " ></a>
<a name="对象的方法" class="lemma-anchor " ></a>
</div><div class="para-title level-3" label-module="para-title">
<h3 class="title-text"><span class="title-prefix">Python</span>对象的方法</h3>
</div>
<div class="para" label-module="para">对象的方法是指绑定到对象的函数。调用对象方法的语法是instance.method(arguments)。它等价于调用Class.method(instance, arguments)。当定义对象方法时，必须显式地定义第一个参数，一般该参数名都使用self，用于访问对象的内部数据。这里的self相当于C++, Java里面的this变量，但是我们还可以使用任何其它合法的参数名，比如this 和 mine 等，self与C++,Java里面的this不完全一样，它可以被看作是一个习惯性的用法，我们传入任何其它的合法名称都行，比如：</div>
<pre class="brush: python">class&nbsp;Fish:
&nbsp;&nbsp;&nbsp;&nbsp;def&nbsp;eat(self,food):
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if&nbsp;food&nbsp;is&nbsp;not&nbsp;None:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.hungry=False

class&nbsp;User:
&nbsp;&nbsp;&nbsp;&nbsp;def__init__(myself,name):
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;myself.name=name

#构造Fish的实例：
f=Fish()
#以下两种调用形式是等价的：
Fish.eat(f,&quot;earthworm&quot;)
f.eat(&quot;earthworm&quot;)
u=User(&#39;username&#39;)
print(u.name)
</pre><div class="para" label-module="para">Python认识一些以“__”开始并以“__”结束的特殊方法名，它们用于实现运算符重载和实现多种特殊功能。</div><div class="anchor-list">
<a name="5_6" class="lemma-anchor para-title" ></a>
<a name="sub21087_5_6" class="lemma-anchor " ></a>
<a name="类型" class="lemma-anchor " ></a>
</div><div class="para-title level-3" label-module="para-title">
<h3 class="title-text"><span class="title-prefix">Python</span>类型</h3>
</div>
<div class="para" label-module="para">Python采用动态类型系统。在编译的时候，Python不会检查对象是否拥有被调用的方法或者属性，而是直至运行时，才做出检查。所以操作对象时可能会抛出异常。不过，虽然Python采用动态类型系统，它同时也是强类型的。Python禁止没有明确定义的操作，比如数字加字符串。</div>
<div class="para" label-module="para">与其它面向对象语言一样，Python允许程序员定义类型。构造一个对象只需要像函数一样调用类型即可，比如，对于前面定义的Fish类型，使用Fish()。类型本身也是特殊类型type的对象(type类型本身也是type对象)，这种特殊的设计允许对类型进行反射编程。</div>
<div class="para" label-module="para">Python内置丰富的数据类型。与Java、C++相比，这些数据类型有效地减少代码的长度。下面这个列表简要地描述了Python内置数据类型(适用于Python 3.x)：</div>
<table log-set-param="table_view" class="table-view log-set-param"><tr><th><div class="para" label-module="para">类型</div>
</th><th><div class="para" label-module="para">描述</div>
</th><th><div class="para" label-module="para">例子</div>
</th><th>备注</th></tr><tr><td width="153" align="left" valign="center"><div class="para" label-module="para"><a target=_blank href="/item/str">str</a></div>
</td><td width="153" align="left" valign="center"><div class="para" label-module="para">一个由字符组成的不可更改的有串行。</div>
</td><td width="153" align="left" valign="center"><div class="para" label-module="para">&#39;Wikipedia&#39;</div>
<div class="para" label-module="para">&quot;Wikipedia&quot;</div>
<div class="para" label-module="para">&quot;&quot;&quot;Spanning</div>
<div class="para" label-module="para">multiple</div>
<div class="para" label-module="para">lines&quot;&quot;&quot;</div>
</td><td width="153" align="left" valign="center">在Python 3.x里，字符串由Unicode字符组成</td></tr><tr><td width="153" align="left" valign="center"><div class="para" label-module="para">bytes</div>
</td><td width="153" align="left" valign="center"><div class="para" label-module="para">一个由字节组成的不可更改的有串行。</div>
</td><td width="153" align="left" valign="center"><div class="para" label-module="para">b&#39;Some ASCII&#39;</div>
<div class="para" label-module="para">b&quot;Some ASCII&quot;</div>
</td><td width="153" align="left" valign="center">　</td></tr><tr><td width="153" align="left" valign="center"><div class="para" label-module="para">list</div>
</td><td width="153" align="left" valign="center"><div class="para" label-module="para">可以包含多种类型的可改变的有串行</div>
</td><td width="153" align="left" valign="center"><div class="para" label-module="para">[4.0, &#39;string&#39;, True]</div>
</td><td width="153" align="left" valign="center">　</td></tr><tr><td width="153" align="left" valign="center"><div class="para" label-module="para">tuple</div>
</td><td width="153" align="left" valign="center"><div class="para" label-module="para">可以包含多种类型的不可改变的有串行</div>
</td><td width="153" align="left" valign="center"><div class="para" label-module="para">(4.0, &#39;string&#39;, True)</div>
</td><td width="153" align="left" valign="center">　</td></tr><tr><td width="153" align="left" valign="center"><div class="para" label-module="para">set, frozenset</div>
</td><td width="153" align="left" valign="center"><div class="para" label-module="para">与数学中集合的概念类似。无序的、每个元素唯一。</div>
</td><td width="153" align="left" valign="center"><div class="para" label-module="para">{4.0, &#39;string&#39;, True}</div>
<div class="para" label-module="para">frozenset([4.0, &#39;string&#39;, True])</div>
</td><td width="153" align="left" valign="center">　</td></tr><tr><td width="153" align="left" valign="center"><div class="para" label-module="para">dict</div>
</td><td width="153" align="left" valign="center"><div class="para" label-module="para">一个可改变的由键值对组成的无串行。</div>
</td><td width="153" align="left" valign="center"><div class="para" label-module="para">{&#39;key1&#39;: 1.0, 3: False}</div>
</td><td width="153" align="left" valign="center">　</td></tr><tr><td width="153" align="left" valign="center"><div class="para" label-module="para">int</div>
</td><td width="153" align="left" valign="center"><div class="para" label-module="para">精度不限的整数</div>
</td><td width="153" align="left" valign="center"><div class="para" label-module="para">42</div>
</td><td width="153" align="left" valign="center">　</td></tr><tr><td width="153" align="left" valign="center"><div class="para" label-module="para">float</div>
</td><td width="153" align="left" valign="center"><div class="para" label-module="para">浮点数。精度与系统相关。</div>
</td><td width="153" align="left" valign="center"><div class="para" label-module="para">3.1415927</div>
</td><td width="153" align="left" valign="center">　</td></tr><tr><td width="153" align="left" valign="center"><div class="para" label-module="para">complex</div>
</td><td width="153" align="left" valign="center"><div class="para" label-module="para">复数</div>
</td><td width="153" align="left" valign="center"><div class="para" label-module="para">3+2.7j</div>
</td><td width="153" align="left" valign="center">　</td></tr><tr><td width="153" align="left" valign="center"><div class="para" label-module="para">bool</div>
</td><td width="153" align="left" valign="center"><div class="para" label-module="para">逻辑值。只有两个值：真、假</div>
</td><td width="153" align="left" valign="center"><div class="para" label-module="para">True</div>
<div class="para" label-module="para">False</div>
</td><td width="153" align="left" valign="center">　</td></tr></table><div class="para" label-module="para">除了各种数据类型，Python语言还用类型来表示函数、模块、类型本身、对象的方法、编译后的Python代码、运行时信息等等。因此，Python具备很强的动态性。</div><div class="anchor-list">
<a name="5_7" class="lemma-anchor para-title" ></a>
<a name="sub21087_5_7" class="lemma-anchor " ></a>
<a name="数学运算" class="lemma-anchor " ></a>
</div><div class="para-title level-3" label-module="para-title">
<h3 class="title-text"><span class="title-prefix">Python</span>数学运算</h3>
</div>
<div class="para" label-module="para">Python使用与C、Java类似的运算符，支持整数与浮点数的数学运算。同时还支持复数运算与无穷位数（实际受限于计算机的能力）的整数运算。除了求绝对值函数abs()外，大多数数学函数处于math和cmath模块内。前者用于实数运算，而后者用于复数运算。使用时需要先导入它们，比如：</div>
<div class="para" label-module="para">&gt;&gt;&gt; import math</div>
<div class="para" label-module="para">&gt;&gt;&gt; print(math.sin(math.pi/2))</div>
<div class="para" label-module="para">1.0</div>
<div class="para" label-module="para">fractions模块用于支持分数运算；decimal模块用于支持高精度的浮点数运算。</div>
<div class="para" label-module="para">Python定义求余运行a % b的值处于开区间[0, b)内，如果b是负数，开区间变为(b, 0]。这是一个很常见的定义方式。不过其实它依赖于整除的定义。为了让方程式：b * (a // b) + a % b = a恒真，整除运行需要向负无穷小方向取值。比如7 // 3的结果是2，而(-7) // 3的结果却是-3。这个算法与其它很多编程语言不一样，需要注意，它们的整除运算会向0的方向取值。</div>
<div class="para" label-module="para">Python允许像数学的常用写法那样连着写两个比较运行符。比如a &lt; b &lt; c与a &lt; b and b &lt; c等价。C++的结果与Python不一样，首先它会先计算a &lt; b，根据两者的大小获得0或者1两个值之一，然后再与c进行比较。</div><div class="anchor-list">
<a name="6" class="lemma-anchor para-title" ></a>
<a name="sub21087_6" class="lemma-anchor " ></a>
<a name="CGI" class="lemma-anchor " ></a>
</div><div class="para-title level-2" label-module="para-title">
<h2 class="title-text"><span class="title-prefix">Python</span>CGI</h2>
<a class="edit-icon j-edit-link" data-edit-dl="6" href="javascript:;"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_edit-lemma"></em>编辑</a>
</div>
<div class="para" label-module="para">CGI 目前由NCSA维护，NCSA定义CGI如下：<sup>[4]</sup><a class="sup-anchor" name="ref_[4]_21087">&nbsp;</a>
</div>
<div class="para" label-module="para">CGI(Common Gateway Interface)，通用网关接口，它是一段程序，运行在服务器上如：HTTP服务器，提供同客户端HTML页面的接口。</div>
<div class="para" label-module="para">CGI程序可以是Python脚本、Perl脚本、Shell脚本、C或者C++程序等。</div><div class="anchor-list">
<a name="6_1" class="lemma-anchor para-title" ></a>
<a name="sub21087_6_1" class="lemma-anchor " ></a>
<a name="服务器" class="lemma-anchor " ></a>
</div><div class="para-title level-3" label-module="para-title">
<h3 class="title-text"><span class="title-prefix">Python</span>服务器</h3>
</div>
<div class="para" label-module="para">在你进行CGI编程前，确保您的Web服务器支持CGI及已经配置了CGI的处理程序。</div>
<div class="para" label-module="para">所有的HTTP服务器执行CGI程序都保存在一个预先配置的目录。这个目录被称为CGI目录，并按照惯例，它被命名为/var/www/cgi-bin目录。</div>
<div class="para" label-module="para">CGI文件的扩展名为.cgi，python也可以使用.py扩展名。</div>
<div class="para" label-module="para">默认情况下，Linux服务器配置运行的cgi-bin目录中为/var/www。</div>
<div class="para" label-module="para">如果想指定的其他运行CGI脚本的目录，可以修改httpd.conf配置文件，如下所示：</div>
<pre class="brush: xml">&lt;Directory&quot;/var/www/cgi-bin&quot;&gt;
Allow&nbsp;Override&nbsp;None
Options&nbsp;ExecCGI
Order&nbsp;allow,deny
Allow&nbsp;from&nbsp;all
&lt;/Directory&gt;
&lt;Directory&quot;/var/www/cgi-bin&quot;&gt;
Options&nbsp;All
&lt;/Directory&gt;
</pre><div class="anchor-list">
<a name="6_2" class="lemma-anchor para-title" ></a>
<a name="sub21087_6_2" class="lemma-anchor " ></a>
<a name="程序" class="lemma-anchor " ></a>
</div><div class="para-title level-3" label-module="para-title">
<h3 class="title-text"><span class="title-prefix">Python</span>程序</h3>
</div>
<div class="para" label-module="para">使用Python创建第一个CGI程序，文件名为hello.py，文件位于/var/www/cgi-bin目录中，内容如下，修改文件的权限为755：<sup>[4]</sup><a class="sup-anchor" name="ref_[4]_21087">&nbsp;</a>
</div>
<pre class="brush: python">#!/usr/bin/env&nbsp;python
print(&quot;Content-type:text/html\r\n\r\n&quot;)
print(&quot;&lt;html&gt;&quot;)
print(&quot;&lt;head&gt;&quot;)
print(&quot;&quot;)
print(&quot;&lt;/head&gt;&quot;)
print(&quot;&lt;body&gt;&quot;)
print(&quot;&lt;h2&gt;Hello&nbsp;World!&nbsp;This&nbsp;is&nbsp;my&nbsp;first&nbsp;CGI&nbsp;program&lt;/h2&gt;&quot;)
print(&quot;&lt;/body&gt;&quot;)
print(&quot;&lt;/html&gt;&quot;)
</pre><div class="para" label-module="para">以上程序在浏览器访问显示结果如下：</div>
<pre class="brush: python">Hello&nbsp;World!&nbsp;This&nbsp;is&nbsp;my&nbsp;first&nbsp;CGI&nbsp;program
</pre><div class="para" label-module="para">这个的hello.py脚本是一个简单的Python脚本，脚本第一的输出内容&quot;Content-type:text/html\r\n\r\n&quot;发送到浏览器并告知浏览器显示的内容类型为&quot;text/html&quot;。</div><div class="anchor-list">
<a name="6_3" class="lemma-anchor para-title" ></a>
<a name="sub21087_6_3" class="lemma-anchor " ></a>
<a name="环境变量" class="lemma-anchor " ></a>
</div><div class="para-title level-3" label-module="para-title">
<h3 class="title-text"><span class="title-prefix">Python</span>环境变量</h3>
</div>
<div class="para" label-module="para">所有的CGI程序都接收以下的环境变量，这些变量在CGI程序中发挥了重要的作用：<sup>[4]</sup><a class="sup-anchor" name="ref_[4]_21087">&nbsp;</a>
</div>
<table log-set-param="table_view" class="reference"><tr><th><div class="para" label-module="para">变量名</div>
</th><th><div class="para" label-module="para">描述</div>
</th></tr><tr><td><div class="para" label-module="para">CONTENT_TYPE</div>
</td><td><div class="para" label-module="para">这个环境变量的值指示所传递来的信息的MIME类型。目前，环境变量CONTENT_TYPE一般都是：application/x-www-form-urlencoded,他表示数据来自于HTML表单。</div>
</td></tr><tr><td><div class="para" label-module="para">CONTENT_LENGTH</div>
</td><td><div class="para" label-module="para">如果服务器与CGI程序信息的传递方式是POST，这个环境变量即使从标准输入STDIN中可以读到的有效数据的字节数。这个环境变量在读取所输入的数据时必须使用。</div>
</td></tr><tr><td><div class="para" label-module="para">HTTP_COOKIE</div>
</td><td><div class="para" label-module="para">客户机内的 COOKIE 内容。</div>
</td></tr><tr><td><div class="para" label-module="para">HTTP_USER_AGENT</div>
</td><td><div class="para" label-module="para">提供包含了版本数或其他专有数据的客户浏览器信息。</div>
</td></tr><tr><td><div class="para" label-module="para">PATH_INFO</div>
</td><td><div class="para" label-module="para">这个环境变量的值表示紧接在CGI程序名之后的其他路径信息。它常常作为CGI程序的参数出现。</div>
</td></tr><tr><td><div class="para" label-module="para">QUERY_STRING</div>
</td><td><div class="para" label-module="para">如果服务器与CGI程序信息的传递方式是GET，这个环境变量的值即使所传递的信息。这个信息经跟在CGI程序名的后面，两者中间用一个问号&#39;?&#39;分隔。</div>
</td></tr><tr><td><div class="para" label-module="para">REMOTE_ADDR</div>
</td><td><div class="para" label-module="para">这个环境变量的值是发送请求的客户机的IP地址，例如上面的192.168.1.67。这个值总是存在的。而且它是Web客户机需要提供给Web服务器的唯一标识，可以在CGI程序中用它来区分不同的Web客户机。</div>
</td></tr><tr><td><div class="para" label-module="para">REMOTE_HOST</div>
</td><td><div class="para" label-module="para">这个环境变量的值包含发送CGI请求的客户机的主机名。如果不支持你想查询，则无需定义此环境变量。</div>
</td></tr><tr><td><div class="para" label-module="para">REQUEST_METHOD</div>
</td><td><div class="para" label-module="para">提供脚本被调用的方法。对于使用 HTTP/1.0 协议的脚本，仅 GET 和 POST 有意义。</div>
</td></tr><tr><td><div class="para" label-module="para">SCRIPT_FILENAME</div>
</td><td><div class="para" label-module="para">CGI脚本的完整路径</div>
</td></tr><tr><td><div class="para" label-module="para">SCRIPT_NAME</div>
</td><td><div class="para" label-module="para">CGI脚本的的名称</div>
</td></tr><tr><td><div class="para" label-module="para">SERVER_NAME</div>
</td><td><div class="para" label-module="para">这是你的 WEB 服务器的主机名、别名或IP地址。</div>
</td></tr><tr><td><div class="para" label-module="para">SERVER_SOFTWARE</div>
</td><td><div class="para" label-module="para">这个环境变量的值包含了调用CGI程序的HTTP服务器的名称和版本号。例如，上面的值为Apache/2.2.14(Unix)</div>
</td></tr></table><div class="para" label-module="para">以下是一个简单的CGI脚本输出CGI的环境变量：</div>
<pre class="brush: python">#!/usr/bin/python
import&nbsp;os
print&quot;Content-type:text/html\r\n\r\n&quot;
print&quot;Environment&quot;
for&nbsp;param&nbsp;in&nbsp;os.environ.keys():
&nbsp;&nbsp;&nbsp;&nbsp;print&quot;&lt;b&gt;%20s&lt;/b&gt;:%s&lt;\br&gt;&quot;&nbsp;%(param,os.environ[param])</pre><div class="anchor-list">
<a name="7" class="lemma-anchor para-title" ></a>
<a name="sub21087_7" class="lemma-anchor " ></a>
<a name="特点" class="lemma-anchor " ></a>
</div><div class="para-title level-2" label-module="para-title">
<h2 class="title-text"><span class="title-prefix">Python</span>特点</h2>
<a class="edit-icon j-edit-link" data-edit-dl="7" href="javascript:;"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_edit-lemma"></em>编辑</a>
</div>
<div class="anchor-list">
<a name="7_1" class="lemma-anchor para-title" ></a>
<a name="sub21087_7_1" class="lemma-anchor " ></a>
<a name="优点" class="lemma-anchor " ></a>
</div><div class="para-title level-3" label-module="para-title">
<h3 class="title-text"><span class="title-prefix">Python</span>优点</h3>
</div>
<div class="para" label-module="para"><b>简单</b>：Python是一种代表简单主义思想的语言。阅读一个良好的Python程序就感觉像是在读英语一样。它使你能够专注于解决问题而不是去搞明白语言本身。</div>
<div class="para" label-module="para"><b>易学</b>：Python极其容易上手，因为Python有极其简单的说明文档<sup>[6]</sup><a class="sup-anchor" name="ref_[6]_21087">&nbsp;</a>
。</div>
<div class="para" label-module="para"><b>速度快：</b>Python 的底层是用 C 语言写的，很多标准库和第三方库也都是用 C 写的，运行速度非常快。<sup>[4]</sup><a class="sup-anchor" name="ref_[4]_21087">&nbsp;</a>
</div>
<div class="para" label-module="para"><b>免费、开源</b>：Python是<a target=_blank href="/item/FLOSS">FLOSS</a>（自由/<a target=_blank href="/item/%E5%BC%80%E6%94%BE%E6%BA%90%E7%A0%81">开放源码</a>软件）之一。使用者可以自由地发布这个软件的拷贝、阅读它的<a target=_blank href="/item/%E6%BA%90%E4%BB%A3%E7%A0%81">源代码</a>、对它做改动、把它的一部分用于新的自由软件中。FLOSS是基于一个团体分享知识的概念。</div>
<div class="para" label-module="para"><b>高层语言</b>：用Python语言编写程序的时候无需考虑诸如如何管理你的程序使用的内存一类的底层细节。</div>
<div class="para" label-module="para"><b>可移植性</b>：由于它的开源本质，Python已经被移植在许多平台上（经过改动使它能够工作在不同平台上）。这些平台包括Linux、Windows、FreeBSD、Macintosh、Solaris、OS/2、Amiga、AROS、AS/400、BeOS、OS/390、z/OS、Palm OS、QNX、VMS、Psion、Acom RISC OS、VxWorks、PlayStation、Sharp Zaurus、Windows CE、PocketPC、Symbian以及Google基于linux开发的android平台。</div>
<div class="para" label-module="para"><b>解释性</b>：一个用编译性语言比如C或C++写的程序可以从<a target=_blank href="/item/%E6%BA%90%E6%96%87%E4%BB%B6">源文件</a>（即C或C++语言）转换到一个你的计算机使用的语言（<a target=_blank href="/item/%E4%BA%8C%E8%BF%9B%E5%88%B6%E4%BB%A3%E7%A0%81">二进制代码</a>，即0和1）。这个过程通过<a target=_blank href="/item/%E7%BC%96%E8%AF%91%E5%99%A8">编译器</a>和不同的标记、选项完成。</div>
<div class="para" label-module="para">运行程序的时候，连接/转载器软件把你的程序从硬盘复制到内存中并且运行。而Python语言写的程序不需要编译成二进制代码。你可以直接从<a target=_blank href="/item/%E6%BA%90%E4%BB%A3%E7%A0%81">源代码</a>运行 程序。</div>
<div class="para" label-module="para">在计算机内部，Python<a target=_blank href="/item/%E8%A7%A3%E9%87%8A%E5%99%A8">解释器</a>把源代码转换成称为<a target=_blank href="/item/%E5%AD%97%E8%8A%82%E7%A0%81">字节码</a>的中间形式，然后再把它翻译成计算机使用的<a target=_blank href="/item/%E6%9C%BA%E5%99%A8%E8%AF%AD%E8%A8%80">机器语言</a>并运行。这使得使用Python更加简单。也使得Python程序更加易于移植。</div>
<div class="para" label-module="para"><a target=_blank href="/item/%E9%9D%A2%E5%90%91%E5%AF%B9%E8%B1%A1"><b>面向对象</b></a>：Python既支持<a target=_blank href="/item/%E9%9D%A2%E5%90%91%E8%BF%87%E7%A8%8B">面向过程</a>的编程也支持面向对象的编程。在“面向过程”的语言中，程序是由过程或仅仅是可重用代码的函数构建起来的。在“<a target=_blank href="/item/%E9%9D%A2%E5%90%91%E5%AF%B9%E8%B1%A1">面向对象</a>”的语言中，程序是由数据和功能组合而成的对象构建起来的。</div>
<div class="para" label-module="para"><b>可扩展性</b>：如果需要一段关键代码运行得更快或者希望某些算法不公开，可以部分程序用C或C++编写，然后在Python程序中使用它们。</div>
<div class="para" label-module="para"><b>可嵌入性</b>：可以把Python嵌入C/C++程序，从而向程序用户提供脚本功能。</div>
<div class="para" label-module="para"><b>丰富的库</b>：Python标准库确实很庞大。它可以帮助处理各种工作，包括<a target=_blank href="/item/%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F">正则表达式</a>、文档生成、<a target=_blank href="/item/%E5%8D%95%E5%85%83%E6%B5%8B%E8%AF%95">单元测试</a>、<a target=_blank href="/item/%E7%BA%BF%E7%A8%8B">线程</a>、数据库、网页浏览器、CGI、FTP、电子邮件、XML、XML-RPC、HTML、WAV文件、密码系统、GUI（<a target=_blank href="/item/%E5%9B%BE%E5%BD%A2%E7%94%A8%E6%88%B7%E7%95%8C%E9%9D%A2">图形用户界面</a>）、Tk和其他与系统有关的操作。这被称作Python的“功能齐全”理念。除了标准库以外，还有许多其他高质量的库，如wxPython、Twisted和Python图像库等等。</div>
<div class="para" label-module="para">规范的代码：Python采用强制缩进的方式使得代码具有较好可读性。而Python语言写的程序不需要编译成二进制代码。</div><div class="anchor-list">
<a name="7_2" class="lemma-anchor para-title" ></a>
<a name="sub21087_7_2" class="lemma-anchor " ></a>
<a name="缺点" class="lemma-anchor " ></a>
</div><div class="para-title level-3" label-module="para-title">
<h3 class="title-text"><span class="title-prefix">Python</span>缺点</h3>
</div>
<div class="para" label-module="para"><b>单行语句和<a target=_blank href="/item/%E5%91%BD%E4%BB%A4%E8%A1%8C">命令行</a>输出问题</b>：很多时候不能将程序连写成一行，如import sys;for i in sys.path:print i。而perl和awk就无此限制，可以较为方便的在shell下完成简单程序，不需要如Python一样，必须将程序写入一个.py文件。</div>
<div class="para" label-module="para"><b>独特的语法</b></div>
<div class="para" label-module="para">这也许不应该被称为局限，但是它用缩进来区分语句关系的方式还是给很多初学者带来了困惑。即便是很有经验的Python程序员，也可能陷入陷阱当中。最常见的情况是tab和空格的混用会导致错误，而这是用肉眼无法分别的。</div>
<div class="para" label-module="para"><b>运行速度慢</b>：这里是指与C和C++相比。</div><div class="anchor-list">
<a name="8" class="lemma-anchor para-title" ></a>
<a name="sub21087_8" class="lemma-anchor " ></a>
<a name="应用" class="lemma-anchor " ></a>
</div><div class="para-title level-2" label-module="para-title">
<h2 class="title-text"><span class="title-prefix">Python</span>应用</h2>
<a class="edit-icon j-edit-link" data-edit-dl="8" href="javascript:;"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_edit-lemma"></em>编辑</a>
</div>
<div class="para" label-module="para">系统编程：提供<a target=_blank href="/item/API">API</a>（<a target=_blank href="/item/Application%20Programming%20Interface">Application Programming Interface</a>应用程序编程接口），能方便进行系统维护和管理，Linux下标志性语言之一，是很多系统管理员理想的编程工具<sup>[7]</sup><a class="sup-anchor" name="ref_[7]_21087">&nbsp;</a>
。</div>
<div class="para" label-module="para"><b>图形处理：</b>有PIL、<a target=_blank href="/item/Tkinter">Tkinter</a>等图形库支持，能方便进行图形处理。</div>
<div class="para" label-module="para"><b>数学处理：</b>NumPy扩展提供大量与许多标准数学库的接口。</div>
<div class="para" label-module="para"><b>文本处理：</b>python提供的re模块能支持<a target=_blank href="/item/%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F">正则表达式</a>，还提供<a target=_blank href="/item/SGML">SGML</a>，<a target=_blank href="/item/XML">XML</a>分析模块，许多程序员利用python进行XML程序的开发。</div>
<div class="para" label-module="para">数据库编程：程序员可通过遵循Python DB-API（数据库<a target=_blank href="/item/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E7%BC%96%E7%A8%8B%E6%8E%A5%E5%8F%A3">应用程序编程接口</a>）规范的模块与Microsoft SQL Server，Oracle，Sybase，DB2，MySQL、SQLite等数据库通信。python自带有一个Gadfly模块，提供了一个完整的SQL环境。</div>
<div class="para" label-module="para"><a target=_blank href="/item/%E7%BD%91%E7%BB%9C%E7%BC%96%E7%A8%8B">网络编程</a>：提供丰富的模块支持sockets编程，能方便快速地开发<a target=_blank href="/item/%E5%88%86%E5%B8%83%E5%BC%8F%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F">分布式应用程序</a>。很多大规模软件开发计划例如<a target=_blank href="/item/Zope">Zope</a>，Mnet 及<a target=_blank href="/item/BitTorrent">BitTorrent</a>. Google都在广泛地使用它。</div>
<div class="para" label-module="para"><b>Web编程</b>：应用的开发语言，支持最新的XML技术。</div>
<div class="para" label-module="para"><b>多媒体应用：</b>Python的PyOpenGL模块封装了“OpenGL应用程序编程接口”，能进行二维和三维<a target=_blank href="/item/%E5%9B%BE%E5%83%8F%E5%A4%84%E7%90%86">图像处理</a>。PyGame模块可用于编写游戏软件。</div>
<div class="para" label-module="para"><b>pymo引擎：</b>PYMO全称为python memories off，是一款运行于Symbian S60V3,Symbian3,S60V5, Symbian3, Android系统上的AVG游戏引擎。因其基于python2.0平台开发，并且适用于创建<a target=_blank href="/item/%E7%A7%8B%E4%B9%8B%E5%9B%9E%E5%BF%86">秋之回忆</a>（<a target=_blank href="/item/memories%20off">memories off</a>）风格的AVG游戏，故命名为PYMO。</div>
<div class="para" label-module="para"><b>黑客编程：</b>python有一个hack的库,内置了你熟悉的或不熟悉的函数，但是缺少成就感。</div>
<div class="para" label-module="para"><b>用Python写简单爬虫</b></div>
<div class="para" label-module="para">首先，要通过urllib2这个Module获得对应的<a target=_blank href="/item/HTML">HTML</a>源码。</div>
<pre class="brush: python">import&nbsp;urllib2&nbsp;&nbsp;#调用urllib2&nbsp;&nbsp;
url=&#39;http://www.baidu.com/s?wd=cloga&#39;&nbsp;#把等号右边的网址赋值给url
html=urllib2.urlopen(url).read()&nbsp;&nbsp;&nbsp;#html随意取名&nbsp;等号后面的动作是打开源代码页面，并阅读
print&nbsp;html&nbsp;#打印
</pre><div class="para" label-module="para">通过上面这三句就可以将URL的源码存在content变量中，其类型为字符型。</div>
<div class="para" label-module="para">接下来是要从这堆HTML源码中提取我们需要的内容。用Chrome查看一下对应的内容的代码（也可以用Firefox的Firebug）。</div>
<div class="para" label-module="para">可以看到url的信息存储在span标签中，要获取其中的信息可以用正则式。</div><div class="anchor-list">
<a name="9" class="lemma-anchor para-title" ></a>
<a name="sub21087_9" class="lemma-anchor " ></a>
<a name="工具功能" class="lemma-anchor " ></a>
</div><div class="para-title level-2" label-module="para-title">
<h2 class="title-text"><span class="title-prefix">Python</span>工具功能</h2>
<a class="edit-icon j-edit-link" data-edit-dl="9" href="javascript:;"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_edit-lemma"></em>编辑</a>
</div>
<div class="para" label-module="para"><b>Tkinter</b></div>
<div class="para" label-module="para">Python默认的图形界面接口。Tkinter是一个和Tk接口的Python模块，Tkinter库提供了对Tk API的接口，它属于Tcl/Tk的GUI工具组。</div>
<div class="para" label-module="para"><a target=_blank href="/item/PyGTK"><b>PyGTK</b></a></div>
<div class="para" label-module="para">用于python GUI程序开发的GTK+库。GTK就是用来实现GIMP和Gnome的库。</div>
<div class="para" label-module="para"><a target=_blank href="/item/PyQt"><b>PyQt</b></a></div>
<div class="para" label-module="para">用于python的Qt开发库。QT就是实现了KDE环境的那个库，由一系列的模块组成，有qt, qtcanvas, qtgl, qtnetwork, qtsql, qttable, qtui and qtxml，包含有300个类和超过5750个的函数和方法。PyQt还支持一个叫qtext的模块，它包含一个QScintilla库。该库是Scintillar编辑器类的Qt接口。</div>
<div class="para" label-module="para"><a target=_blank href="/item/wxPython"><b>wxPython</b></a></div>
<div class="para" label-module="para">GUI编程框架，熟悉MFC的人会非常喜欢，简直是同一架构（对于初学者或者对设计要求不高的用户来说，使用Boa Constructor可以方便迅速的进行wxPython的开发）</div>
<div class="para" label-module="para"><a target=_blank href="/item/PIL"><b>PIL</b></a></div>
<div class="para" label-module="para">python提供强大的图形处理的能力，并提供广泛的图形文件格式支持，该库能进行图形格式的转换、打印和显示。还能进行一些图形效果的处理，如图形的放大、缩小和旋转等。是Python用户进行图象处理的强有力工具。</div>
<div class="para" label-module="para"><b>Psyco</b></div>
<div class="para" label-module="para">一个Python代码加速度器，可使Python代码的执行速度提高到与编译语言一样的水平。</div>
<div class="para" label-module="para"><b>xmpppy</b></div>
<div class="para" label-module="para">Jabber服务器采用开发的XMPP协议，Google Talk也是采用XMPP协议的IM系统。在Python中有一个xmpppy模块支持该协议。也就是说，我们可以通过该模块与Jabber服务器通信，是不是很Cool。</div>
<div class="para" label-module="para"><b>PyMedia</b></div>
<div class="para" label-module="para">用于多媒体操作的python模块。它提供了丰富而简单的接口用于多媒体处理(wav, mp3, ogg, avi, divx, dvd, cdda etc)。可在Windows和Linux平台下使用。</div>
<div class="para" label-module="para"><b>Pmw</b></div>
<div class="para" label-module="para">Python megawidgets，Python超级GUI组件集，一个在python中利用Tkinter模块构建的高级GUI组件，每个Pmw都合并了一个或多个Tkinter组件，以实现更有用和更复杂的功能。</div>
<div class="para" label-module="para"><b>PyXML</b></div>
<div class="para" label-module="para">用Python解析和处理XML文档的工具包，包中的4DOM是完全相容于W3C DOM规范的。它包含以下内容：</div>
<div class="para" label-module="para">xmlproc: 一个符合规范的XML解析器。Expat: 一个快速的，非验证的XML解析器。还有其他和他同级别的还有 PyHtml PySGML。</div>
<div class="para" label-module="para"><a target=_blank href="/item/PyGame"><b>PyGame</b></a></div>
<div class="para" label-module="para">用于多媒体开发和游戏软件开发的模块。</div>
<div class="para" label-module="para"><b>PyOpenGL</b></div>
<div class="para" label-module="para">模块封装了“OpenGL应用程序编程接口”，通过该模块python程序员可在程序中集成2D和3D的图形。</div>
<div class="para" label-module="para"><b>NumPy、NumArray、</b><a target=_blank href="/item/SAGE">SAGE</a></div>
<div class="para" label-module="para">NumArray是Python的一个扩展库，主要用于处理任意维数的固定类型数组，简单说就是一个矩阵库。它的底层代码使用C来编写，所以速度的优势很明显。SAGE是基于NumPy和其他几个工具所整合成的数学软件包，目标是取代Magma, Maple, Mathematica和Matlab 这类工具。</div>
<div class="para" label-module="para"><a target=_blank href="/item/MySQLdb"><b>MySQLdb</b></a></div>
<div class="para" label-module="para">用于连接MySQL数据库。还有用于zope的ZMySQLDA模块，通过它就可在zope中连接mysql数据库。</div>
<div class="para" label-module="para"><b>S</b><b>qlite3</b></div>
<div class="para" label-module="para">用于连接sqlite数据库。<b><br/>　　</b></div>
<div class="para" label-module="para"><b>Python-ldap</b></div>
<div class="para" label-module="para">提供一组面向对象的API，可方便地在python中访问ldap目录服务，它基于OpenLDAP2.x。</div>
<div class="para" label-module="para"><b>smtplib</b></div>
<div class="para" label-module="para">发送电子邮件。</div>
<div class="para" label-module="para"><b>ftplib</b></div>
<div class="para" label-module="para">定义了FTP类和一些方法，用以进行客户端的ftp编程。如果想了解ftp协议的详细内容，请参考RFC959。</div>
<div class="para" label-module="para"><b>PyOpenCL</b></div>
<div class="para" label-module="para">OpenCL的Python接口，通过该模块可以使用GPU实现并行计算。</div><div class="anchor-list">
<a name="10" class="lemma-anchor para-title" ></a>
<a name="sub21087_10" class="lemma-anchor " ></a>
<a name="标准库" class="lemma-anchor " ></a>
</div><div class="para-title level-2" label-module="para-title">
<h2 class="title-text"><span class="title-prefix">Python</span>标准库</h2>
<a class="edit-icon j-edit-link" data-edit-dl="10" href="javascript:;"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_edit-lemma"></em>编辑</a>
</div>
<div class="para" label-module="para">Python拥有一个强大的标准库。Python语言的核心只包含数字、字符串、列表、字典、文件等常见类型和函数，而由Python标准库提供了系统管理、网络通信、文本处理、数据库接口、图形系统、XML处理等额外的功能。Python标准库命名接口清晰、文档良好，很容易学习和使用。</div>
<div class="para" label-module="para">Python社区提供了大量的第三方模块，使用方式与标准库类似。它们的功能无所不包，覆盖科学计算、Web开发、数据库接口、图形系统多个领域，并且大多成熟而稳定。第三方模块可以使用Python或者<a target=_blank href="/item/C%E8%AF%AD%E8%A8%80">C语言</a>编写。<a target=_blank href="/item/SWIG">SWIG</a>,SIP常用于将C语言编写的程序库转化为Python模块。Boost C++ Libraries包含了一组库，Boost.Python，使得以 Python 或 C++ 编写的程序能互相调用。借助于拥有基于标准库的大量工具、能够使用低级语言如C和可以作为其他库接口的C++，Python已成为一种强大的应用于其他语言与工具之间的<a target=_blank href="/item/%E8%83%B6%E6%B0%B4%E8%AF%AD%E8%A8%80">胶水语言</a>。</div>
<div class="para" label-module="para">Python标准库的主要功能有：</div>
<div class="para" label-module="para">文本处理，包含文本格式化、正则表达式匹配、文本差异计算与合并、Unicode支持，二进制数据处理等功能</div>
<div class="para" label-module="para">文件处理，包含文件操作、创建临时文件、文件压缩与归档、操作配置文件等功能</div>
<div class="para" label-module="para">操作系统功能，包含线程与进程支持、IO复用、日期与时间处理、调用系统函数、写日记(logging)等功能</div>
<div class="para" label-module="para">网络通信，包含网络套接字，SSL加密通信、异步网络通信等功能</div>
<div class="para" label-module="para">网络协议，支持HTTP，FTP，SMTP，POP，IMAP，NNTP，XMLRPC等多种网络协议，并提供了编写网络服务器的框架</div>
<div class="para" label-module="para">W3C格式支持，包含HTML，SGML，XML的处理。</div>
<div class="para" label-module="para">其它功能，包括国际化支持、数学运算、HASH、Tkinter等</div><div class="anchor-list">
<a name="11" class="lemma-anchor para-title" ></a>
<a name="sub21087_11" class="lemma-anchor " ></a>
<a name="开发环境" class="lemma-anchor " ></a>
</div><div class="para-title level-2" label-module="para-title">
<h2 class="title-text"><span class="title-prefix">Python</span>开发环境</h2>
<a class="edit-icon j-edit-link" data-edit-dl="11" href="javascript:;"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_edit-lemma"></em>编辑</a>
</div>
<div class="para" label-module="para">●IDLE：Python内置IDE (随python安装包提供)</div>
<div class="para" label-module="para">●PyCharm<sup>[8]</sup><a class="sup-anchor" name="ref_[8]_21087">&nbsp;</a>
：详见百度百科<a target=_blank href="/item/PyCharm">PyCharm</a>，由著名的JetBrains公司开发，带有一整套可以帮助用户在使用Python语言开发时提高其效率的工 具，比如调试、语法高亮、Project管理、代码跳转、智能提示、自动完成、单元测试、版本控制。此外，该IDE提供了一些高级功能，以用于支持Django框架下的专业Web开发。</div>
<div class="para" label-module="para">●Komodo和Komodo Edit：后者是前者的免费精简版</div>
<div class="para" label-module="para">●Spyder：安装Anaconda自带的高级IDE</div>
<div class="para" label-module="para">●PythonWin：<a target=_blank href="/item/ActivePython">ActivePython</a>或pywin32均提供该IDE，仅适用于Windows</div>
<div class="para" label-module="para">●SPE（Stani&#39;s Python Editor）：功能较多的自由软件，基于wxPython</div>
<div class="para" label-module="para">●Ulipad：功能较全的自由软件，基于wxPython；作者是中国Python高手limodou</div>
<div class="para" label-module="para">●WingIDE：可能是功能最全的<a target=_blank href="/item/IDE">IDE</a>，但不是自由软件(教育用户和开源用户可以申请免费key)</div>
<div class="para" label-module="para">●Eric：基于<a target=_blank href="/item/PyQt">PyQt</a>的自由软件，功能强大。全名是：The Eric Python IDE</div>
<div class="para" label-module="para">●DrPython</div>
<div class="para" label-module="para">●<a target=_blank href="/item/PyScripter">PyScripter</a>：使用Delphi开发的轻量级的开源Python IDE， 支持Python2.6和3.0。</div>
<div class="para" label-module="para">●<a target=_blank href="/item/PyPE">PyPE</a>：一个开源的跨平台的PythonIDE。</div>
<div class="para" label-module="para">●<a target=_blank href="/item/bpython">bpython</a>： 类Unix操作系统下使用curses库开发的轻量级的Python<a target=_blank href="/item/%E8%A7%A3%E9%87%8A%E5%99%A8">解释器</a>。语法提示功能。</div>
<div class="para" label-module="para">●eclipse + pydev<a target=_blank href="/item/%E6%8F%92%E4%BB%B6">插件</a>：方便调试程序</div>
<div class="para" label-module="para">●emacs：自带python支持，自动补全、refactor等功能需要插件支持</div>
<div class="para" label-module="para">●<a target=_blank href="/item/Vim">Vim</a>: 最新7.3版编译时可以加入python支持，提供python代码自动提示支持</div>
<div class="para" label-module="para">●Visual Studio 2003 + VisualPython：仅适用Windows，已停止维护，功能较差</div>
<div class="para" label-module="para">●<a target=_blank href="/item/SlickEdit">SlickEdit</a></div>
<div class="para" label-module="para">●Visual Studio 2010 + Python Tools for Visual Studio</div>
<div class="para" label-module="para">●<a target=_blank href="/item/TextMate">TextMate</a></div>
<div class="para" label-module="para">●Netbeans IDE</div>
<div class="para" label-module="para">●<a target=_blank href="/item/Sublime">Sublime</a></div>
<div class="para" label-module="para">●ipython</div>
<div class="para" label-module="para">另外，诸如<a target=_blank href="/item/Notepad%2B%2B">Notepad++</a>、<a target=_blank href="/item/EditPlus">EditPlus</a>、<a target=_blank href="/item/UltraEdit">UltraEdit</a>等通用的程序员<a target=_blank href="/item/%E6%96%87%E6%9C%AC%E7%BC%96%E8%BE%91%E5%99%A8">文本编辑器</a>软件也能对Python代码编辑提供一定的支持，比如代码自动着色、注释快捷键等，但是否够得上<a target=_blank href="/item/%E9%9B%86%E6%88%90%E5%BC%80%E5%8F%91%E7%8E%AF%E5%A2%83">集成开发环境</a>的水平，尚有待评估。</div><div class="anchor-list">
<a name="12" class="lemma-anchor para-title" ></a>
<a name="sub21087_12" class="lemma-anchor " ></a>
<a name="解释器" class="lemma-anchor " ></a>
</div><div class="para-title level-2" label-module="para-title">
<h2 class="title-text"><span class="title-prefix">Python</span>解释器</h2>
<a class="edit-icon j-edit-link" data-edit-dl="12" href="javascript:;"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_edit-lemma"></em>编辑</a>
</div>
<div class="para" label-module="para">Python是一门跨平台的脚本语言，Python规定了一个Python语法规则，实现了Python语法的解释程序就成为了Python的<a target=_blank href="/item/%E8%A7%A3%E9%87%8A%E5%99%A8">解释器</a>。</div>
<div class="para" label-module="para">CPython（<b>C</b>lassic<b>Python</b>，也就是原始的<b>Python</b>实现，需要区别于其他实现的时候才以CPython称呼；或解作<b>C</b>语言实现的<b>Python</b>）。这是最常用的Python版本。</div>
<div class="para" label-module="para"><a target=_blank href="/item/Jython">Jython</a>（原名<b>JPython</b>；<b>J</b>ava语言实现的P<b>ython</b>，现已正式发布）。Jython可以直接调用Java的各种函数库。</div>
<div class="para" label-module="para"><a target=_blank href="/item/PyPy">PyPy</a>（使用<b>Py</b>thon语言写的<b>Py</b>thon）</div>
<div class="para" label-module="para"><a target=_blank href="/item/IronPython">IronPython</a>（面向<a target=_blank href="/item/.NET">.NET</a>和ECMA CLI的Python实现）。IronPython能够直接调用.net平台的各种函数库。可以将Python程序编译成.net程序。</div>
<div class="para" label-module="para">ZhPy（周蟒）（支持使用繁/简中文语句编写程序的<b>Py</b>thon语言）</div><div class="anchor-list">
<a name="13" class="lemma-anchor para-title" ></a>
<a name="sub21087_13" class="lemma-anchor " ></a>
<a name="著名应用" class="lemma-anchor " ></a>
</div><div class="para-title level-2" label-module="para-title">
<h2 class="title-text"><span class="title-prefix">Python</span>著名应用</h2>
<a class="edit-icon j-edit-link" data-edit-dl="13" href="javascript:;"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_edit-lemma"></em>编辑</a>
</div>
<div class="para" label-module="para"><a target=_blank href="/item/Pylons">Pylons</a>-<a target=_blank href="/item/Web%E5%BA%94%E7%94%A8%E6%A1%86%E6%9E%B6">Web应用框架</a></div>
<div class="para" label-module="para"><a target=_blank href="/item/Zope">Zope</a>- 应用服务器</div>
<div class="para" label-module="para"><a target=_blank href="/item/Plone">Plone</a>- 内容管理系统</div>
<div class="para" label-module="para">Django- 鼓励快速开发的Web应用框架</div>
<div class="para" label-module="para"><a target=_blank href="/item/Uliweb">Uliweb</a>- 国人开发的轻量级Web框架</div>
<div class="para" label-module="para">TurboGears- 另一个Web应用快速开发框架</div>
<div class="para" label-module="para">Twisted--Python的网络应用程序框架</div>
<div class="para" label-module="para">Python Wikipedia Robot Framework- MediaWiki的机器人程序</div>
<div class="para" label-module="para">MoinMoinWiki- Python写成的<a target=_blank href="/item/Wiki">Wiki</a>程序</div>
<div class="para" label-module="para"><a target=_blank href="/item/flask">flask</a>- Python 微Web框架</div>
<div class="para" label-module="para">tornado- 非阻塞式服务器</div>
<div class="para" label-module="para">Webpy- Python 微Web框架</div>
<div class="para" label-module="para">Bottle- Python 微Web框架</div>
<div class="para" label-module="para"><a target=_blank href="/item/EVE">EVE</a>- 网络游戏EVE大量使用Python进行开发</div>
<div class="para" label-module="para">Reddit - 社交分享网站</div>
<div class="para" label-module="para">Dropbox - 文件分享服务</div>
<div class="para" label-module="para">Pylons - Web应用框架</div>
<div class="para" label-module="para">TurboGears - 另一个Web应用快速开发框架</div>
<div class="para" label-module="para">Fabric - 用于管理成百上千台Linux主机的程序库</div>
<div class="para" label-module="para">Trac - 使用Python编写的BUG管理系统</div>
<div class="para" label-module="para">Mailman - 使用Python编写的邮件列表软件</div>
<div class="para" label-module="para">Mezzanine - 基于Django编写的内容管理系统</div>
<div class="para" label-module="para">Blender - 以C与Python开发的开源3D绘图软件</div><div class="anchor-list">
<a name="14" class="lemma-anchor para-title" ></a>
<a name="sub21087_14" class="lemma-anchor " ></a>
<a name="学习网站" class="lemma-anchor " ></a>
</div><div class="para-title level-2" label-module="para-title">
<h2 class="title-text"><span class="title-prefix">Python</span>学习网站</h2>
<a class="edit-icon j-edit-link" data-edit-dl="14" href="javascript:;"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_edit-lemma"></em>编辑</a>
</div>
<div class="para" label-module="para">Python官方文档<sup>[9]</sup><a class="sup-anchor" name="ref_[9]_21087">&nbsp;</a>
</div>
<div class="para" label-module="para">PythonTab中文网</div>
<div class="para" label-module="para">Python爱好者论坛<sup>[10]</sup><a class="sup-anchor" name="ref_[10]_21087">&nbsp;</a>
</div>
<div class="para" label-module="para">Pythoner在线互动交流平台</div>
<div class="para" label-module="para">python菜鸟教程<sup>[3]</sup><a class="sup-anchor" name="ref_[3]_21087">&nbsp;</a>
</div>
<div class="para" label-module="para">python基础教程<sup>[11-12]</sup><a class="sup-anchor" name="ref_[11-12]_21087">&nbsp;</a>
</div>
<div class="para" label-module="para">Python教程 - 廖雪峰<sup>[12]</sup><a class="sup-anchor" name="ref_[12]_21087">&nbsp;</a>
</div>
<div class="para" label-module="para">python 网络教育-百度传课<sup>[13]</sup><a class="sup-anchor" name="ref_[13]_21087">&nbsp;</a>
</div>
<dl class="lemma-reference collapse nslog-area log-set-param" data-nslog-type="2" log-set-param="ext_reference">
<dt class="reference-title">参考资料<em class="toggle"></em></dt>
<dd class="reference-list-wrap">
<ul class="reference-list">
<li class="reference-item " id="reference-[1]-21087-wrap">
<span class="index">1.</span>
<a class="gotop anchor"  name="refIndex_1_21087" id="refIndex_1_21087" title="向上跳转" href="#ref_[1]_21087">&nbsp;&nbsp;</a>
<a rel="nofollow" href="http://baike.baidu.com/redirect/5409z6JL1DeGwDr1-Aekk0cSj2gm2Dvgtrk-wJYmcw_vIzpa4xKvHk2doEPoJbG3ULc" target="_blank" class="text">Welcome to Python.org<span class="linkout">&nbsp;</span></a>
<span class="site">．官网</span><span>&#91;引用日期2016-12-11&#93;</span></li><li class="reference-item " id="reference-[2]-21087-wrap">
<span class="index">2.</span>
<a class="gotop anchor"  name="refIndex_2_21087" id="refIndex_2_21087" title="向上跳转" href="#ref_[2]_21087">&nbsp;&nbsp;</a>
<a rel="nofollow" href="http://baike.baidu.com/redirect/9backJQNcayc-O4xBnRmCZQZzqqgMIBL8i47AkA4VreOqiebZqePdWrggitIQUhmCPwmbWqXbicTknglPGVBqzvT5QzS5RYSb791uiryfN_ma9EEyCA" target="_blank" class="text">Python 基础教程<span class="linkout">&nbsp;</span></a>
<span class="site">．自强学堂</span><span>&#91;引用日期2012-07-20&#93;</span></li><li class="reference-item " id="reference-[3]-21087-wrap">
<span class="index">3.</span>
<a class="gotop anchor"  name="refIndex_3_21087" id="refIndex_3_21087" title="向上跳转" href="#ref_[3]_21087">&nbsp;&nbsp;</a>
<a rel="nofollow" href="http://baike.baidu.com/redirect/ae853OvBFK53lPI9JUpnOZ27eDrxmpFE-iXwedEKVdEUnu6gZg7503SquBlyh-IJbCrz9Q" target="_blank" class="text">Python学习视频互动问答<span class="linkout">&nbsp;</span></a>
<span class="site">．Pythoner</span><span>&#91;引用日期2013-04-22&#93;</span></li><li class="reference-item " id="reference-[4]-21087-wrap">
<span class="index">4.</span>
<a class="gotop anchor"  name="refIndex_4_21087" id="refIndex_4_21087" title="向上跳转" href="#ref_[4]_21087">&nbsp;&nbsp;</a>
<a rel="nofollow" href="http://baike.baidu.com/redirect/58a4-A1Ic0FPMRq4MGs_e-i_wNKUve0HSAS8PW_aIdnW-QNKLuXvvKJZHUAhIvi1Aa8U1cDuPRttPdd0FY_fb9oAMJII30LVXIZrhrtj3HF1" target="_blank" class="text">Python CGI 编程<span class="linkout">&nbsp;</span></a>
<span class="site">．自强学堂</span><span>&#91;引用日期2014-01-22&#93;</span></li><li class="reference-item " id="reference-[5]-21087-wrap">
<span class="index">5.</span>
<a class="gotop anchor"  name="refIndex_5_21087" id="refIndex_5_21087" title="向上跳转" href="#ref_[5]_21087">&nbsp;&nbsp;</a>
<a rel="nofollow" href="http://baike.baidu.com/redirect/7549L8cjXG0c1PI9q2veAlbdP5SvkEBS4T0EvD_fuF7dKNNsXPUAYjEWLDTof65Y2P9j9bO2Wa1Hu_kRGg82ldCi" target="_blank" class="text">python流行指数<span class="linkout">&nbsp;</span></a>
<span class="site">．python吧</span><span>&#91;引用日期2013-02-20&#93;</span></li><li class="reference-item " id="reference-[6]-21087-wrap">
<span class="index">6.</span>
<a class="gotop anchor"  name="refIndex_6_21087" id="refIndex_6_21087" title="向上跳转" href="#ref_[6]_21087">&nbsp;&nbsp;</a>
<a rel="nofollow" href="http://baike.baidu.com/redirect/cd6dqzCZeNGrV-7wbdT_VvWqYpDcAeS4H0bmQNqfVlzn7M_-GjvDD9tCnIJlIWTEsfXR0ao" target="_blank" class="text">python tutorial中文<span class="linkout">&nbsp;</span></a>
<span class="site">．python中文文档</span><span>&#91;引用日期2013-02-20&#93;</span></li><li class="reference-item " id="reference-[7]-21087-wrap">
<span class="index">7.</span>
<a class="gotop anchor"  name="refIndex_7_21087" id="refIndex_7_21087" title="向上跳转" href="#ref_[7]_21087">&nbsp;&nbsp;</a>
<a rel="nofollow" href="http://baike.baidu.com/redirect/2640p_TqEKK7YvGQ80q2ZIbfSh1f2XfTP_YeHBbIFxS_YxCFIyrXiiDsGUmpM-2coqfIMw3k" target="_blank" class="text">Python教程在线学习<span class="linkout">&nbsp;</span></a>
<span class="site">．.</span><span>&#91;引用日期2012-11-28&#93;</span></li><li class="reference-item " id="reference-[8]-21087-wrap">
<span class="index">8.</span>
<a class="gotop anchor"  name="refIndex_8_21087" id="refIndex_8_21087" title="向上跳转" href="#ref_[8]_21087">&nbsp;&nbsp;</a>
<a rel="nofollow" href="http://baike.baidu.com/redirect/742d_b8fvEVn72H48SXWKaTPDQH-a3BWjZrVgzmX6WyOAvDQiTcLLF0Cg-JU5cogJGYX5UxwGP9REjC-4Ts" target="_blank" class="text">PyCharm产品官网<span class="linkout">&nbsp;</span></a>
<span class="site">．JetBrains的PyCharm产品官网</span><span>&#91;引用日期2013-09-10&#93;</span></li><li class="reference-item " id="reference-[9]-21087-wrap">
<span class="index">9.</span>
<a class="gotop anchor"  name="refIndex_9_21087" id="refIndex_9_21087" title="向上跳转" href="#ref_[9]_21087">&nbsp;&nbsp;</a>
<a rel="nofollow" href="http://baike.baidu.com/redirect/5a5eZQ_4dYLUCG7sqtIsoJzrn8KZCPazkgwcml_0TFbPRzZsm4zDb0nyhnaB-QvqhJnibyJDSA" target="_blank" class="text">Python3 官方文档（英文）<span class="linkout">&nbsp;</span></a>
<span class="site">．Python3 官方文档</span><span>&#91;引用日期2015-01-14&#93;</span></li><li class="reference-item " id="reference-[10]-21087-wrap">
<span class="index">10.</span>
<a class="gotop anchor"  name="refIndex_10_21087" id="refIndex_10_21087" title="向上跳转" href="#ref_[10]_21087">&nbsp;&nbsp;</a>
<a rel="nofollow" href="http://baike.baidu.com/redirect/2989zydOFtbmWbkjHxQLmtXuaYQjrfG79Fk3cErmlg8eL5nyIDleb2ahD9jfnXaXG_1Up14" target="_blank" class="text">Python爱好者<span class="linkout">&nbsp;</span></a>
<span class="site">．Python爱好者论坛</span><span>&#91;引用日期2013-01-22&#93;</span></li><li class="reference-item more" id="reference-[11]-21087-wrap">
<span class="index">11.</span>
<a class="gotop anchor"  name="refIndex_11_21087" id="refIndex_11_21087" title="向上跳转" href="#ref_[11]_21087">&nbsp;&nbsp;</a>
<a rel="nofollow" href="http://baike.baidu.com/redirect/9c234KPr8EHNRyi5Q7zCUNCxsLf1QnzXf6qoWclWHhs2Oh8-diaeB1ZR1Bh7zfHPL3a5vmr2IPx_SF_8XqdoFli1Rw" target="_blank" class="text">python教程<span class="linkout">&nbsp;</span></a>
<span class="site">．麦子学院</span><span>．2014-12-29</span><span>&#91;引用日期2016-04-29&#93;</span></li><li class="reference-item more" id="reference-[12]-21087-wrap">
<span class="index">12.</span>
<a class="gotop anchor"  name="refIndex_12_21087" id="refIndex_12_21087" title="向上跳转" href="#ref_[12]_21087">&nbsp;&nbsp;</a>
<a rel="nofollow" href="http://baike.baidu.com/redirect/abc1OxC8TX5w5Yo_whfN1yjuUVI0SBp_rGUfiHeFUOlTOjmmPQHUJicgZxVBBzqlVGzH_XMuKYX69JrNDHDNDBbjLpMrg2fHv_HajmJ9g_aDiS-5dt8m9XEp75C4FOJ6SOjtdk21uIWCbTBHQ4G0" target="_blank" class="text">Python教程 - 廖雪峰的官方网站<span class="linkout">&nbsp;</span></a>
<span class="site">．廖雪峰的官方网站</span><span>&#91;引用日期2016-09-24&#93;</span></li><li class="reference-item more" id="reference-[13]-21087-wrap">
<span class="index">13.</span>
<a class="gotop anchor"  name="refIndex_13_21087" id="refIndex_13_21087" title="向上跳转" href="#ref_[13]_21087">&nbsp;&nbsp;</a>
<a rel="nofollow" href="http://baike.baidu.com/redirect/c0e4mQ1El92-qalU-U3FShazRX10nhdJYZmqSpD6PKetKoFMYatW93XzkU8Lk59ruRW4ADfuDvr2tqhpC27bP1OVO56XKZKic-gm4Q" target="_blank" class="text">网络课程 python 网络教育-百度传课<span class="linkout">&nbsp;</span></a>
<span class="site">．百度传课</span><span>&#91;引用日期2016-09-24&#93;</span></li></ul>
</dd>
</dl>
</div>
<div class="side-content">
<div class="summary-pic" >
<a href="/pic/Python/407313/0/0eb30f2442a7d9331abfc6f3ad4bd11373f0011e?fr=lemma&amp;ct=single" target="_blank" nslog-type="10002401">
<img src="http://c.hiphotos.baidu.com/baike/w%3D268%3Bg%3D0/sign=3b7a229ac65c1038247ec9c48a2af42e/0eb30f2442a7d9331abfc6f3ad4bd11373f0011e.jpg" />
<button class="picAlbumBtn"><em></em><span>图集</span></button>
<div>Python图册</div>
</a>
</div>
<div id="promotion_xunke"></div>
<div class="lemmaWgt-promotion-vbaike">
<div class="promotion_title">V百科<a href="/vbaike#gallary" target="_blank">往期回顾</a></div>
<div class="promotion_viewport">
<dl>
</dl>
<div class="promotion_viewport_pager"></div>
</div>
</div><div class="lemmaWgt-promotion-rightPreciseAd" data-lemmaId="407313" data-lemmaTitle="Python"></div><div class="lemmaWgt-sideRecommend">
<a name="zhixinWrap" class="qnAnchor"></a>
<div class="zhixin-box" id="zhixinWrap" data-source="" data-newLemmaId="407313">
</div>
<form id="zhixinErrorForm" class="hidden" action="http://f3.baidu.com/index.php/feedback/zx/baikeJC" target="zhixinSubErr" method="post">
<input class="js-url" name="fb_html_url" type="hidden" />
<input class="js-query" name="fb_query" type="hidden" />
<input class="js-title" name="fb_card_title" type="hidden" />
<input class="js-content" name="fb_content" type="hidden" />
<input class="js-souceId" name="fb_source_id" type="hidden" />
</form>
<iframe id="zhixinSubErr" name="zhixinSubErr" style="display:none" frameborder="0"></iframe>
</div><div class="lemmaWgt-promotion-slide">
<div class="promotion_viewport">
<dl>
</dl>
<div class="promotion_viewport_pager"></div>
</div>
</div><div class="lemmaWgt-promotion-rightBigAd">
</div><dl class="side-box lemma-statistics">
<dt class="title">词条统计</dt>
<dd class="description">
<ul>
<li>浏览次数：<span id="j-lemmaStatistics-pv"></span>次</li>
<li>编辑次数：301次<a href="/historylist/Python/407313" class="nslog:1021" target="_blank">历史版本</a></li>
<li>最近更新：<span class="j-modified-time" style="display:none">2017-03-17</span></li>
<li>创建者：<a class="show-userCard" data-uid="4903591" title="查看此用户资料" target="_blank" href="http://www.baidu.com/p/%E9%A6%A5%E7%BA%A2" nslog-type="1022">馥红</a></li>
</ul>
</dd>
</dl>
<div class="side-catalog" style="visibility:hidden">
<div class="side-bar">
<em class="circle start"></em>
<em class="circle end"></em>
</div>
<div class="catalog-scroller">
<dl class="catalog-list">
<dt class="catalog-title level1">
<em class="pointer"></em>
<a href="#1" class="title-link">
<span class="text">
<span class="title-index">1</span>
<span class="title-link" nslog-type="10002802">发展历程</span>
</span>
</a>
</dt>
<dt class="catalog-title level1">
<em class="pointer"></em>
<a href="#2" class="title-link">
<span class="text">
<span class="title-index">2</span>
<span class="title-link" nslog-type="10002802">风格</span>
</span>
</a>
</dt>
<dt class="catalog-title level1">
<em class="pointer"></em>
<a href="#3" class="title-link">
<span class="text">
<span class="title-index">3</span>
<span class="title-link" nslog-type="10002802">设计定位</span>
</span>
</a>
</dt>
<dt class="catalog-title level1">
<em class="pointer"></em>
<a href="#4" class="title-link">
<span class="text">
<span class="title-index">4</span>
<span class="title-link" nslog-type="10002802">执行</span>
</span>
</a>
</dt>
<dt class="catalog-title level1">
<em class="pointer"></em>
<a href="#5" class="title-link">
<span class="text">
<span class="title-index">5</span>
<span class="title-link" nslog-type="10002802">基本语法</span>
</span>
</a>
</dt>
<dd class="catalog-title level2">
<a href="#5_1" class="title-link">
<span class="text">
<span class="title-index">5.1</span>
<span class="title-link" nslog-type="10002802">缩进</span>
</span>
</a>
</dd>
<dd class="catalog-title level2">
<a href="#5_2" class="title-link">
<span class="text">
<span class="title-index">5.2</span>
<span class="title-link" nslog-type="10002802">控制语句</span>
</span>
</a>
</dd>
<dd class="catalog-title level2">
<a href="#5_3" class="title-link">
<span class="text">
<span class="title-index">5.3</span>
<span class="title-link" nslog-type="10002802">表达式</span>
</span>
</a>
</dd>
<dd class="catalog-title level2">
<a href="#5_4" class="title-link">
<span class="text">
<span class="title-index">5.4</span>
<span class="title-link" nslog-type="10002802">函数</span>
</span>
</a>
</dd>
<dd class="catalog-title level2">
<a href="#5_5" class="title-link">
<span class="text">
<span class="title-index">5.5</span>
<span class="title-link" nslog-type="10002802">对象的方法</span>
</span>
</a>
</dd>
<dd class="catalog-title level2">
<a href="#5_6" class="title-link">
<span class="text">
<span class="title-index">5.6</span>
<span class="title-link" nslog-type="10002802">类型</span>
</span>
</a>
</dd>
<dd class="catalog-title level2">
<a href="#5_7" class="title-link">
<span class="text">
<span class="title-index">5.7</span>
<span class="title-link" nslog-type="10002802">数学运算</span>
</span>
</a>
</dd>
<dt class="catalog-title level1">
<em class="pointer"></em>
<a href="#6" class="title-link">
<span class="text">
<span class="title-index">6</span>
<span class="title-link" nslog-type="10002802">CGI</span>
</span>
</a>
</dt>
<dd class="catalog-title level2">
<a href="#6_1" class="title-link">
<span class="text">
<span class="title-index">6.1</span>
<span class="title-link" nslog-type="10002802">服务器</span>
</span>
</a>
</dd>
<dd class="catalog-title level2">
<a href="#6_2" class="title-link">
<span class="text">
<span class="title-index">6.2</span>
<span class="title-link" nslog-type="10002802">程序</span>
</span>
</a>
</dd>
<dd class="catalog-title level2">
<a href="#6_3" class="title-link">
<span class="text">
<span class="title-index">6.3</span>
<span class="title-link" nslog-type="10002802">环境变量</span>
</span>
</a>
</dd>
<dt class="catalog-title level1">
<em class="pointer"></em>
<a href="#7" class="title-link">
<span class="text">
<span class="title-index">7</span>
<span class="title-link" nslog-type="10002802">特点</span>
</span>
</a>
</dt>
<dd class="catalog-title level2">
<a href="#7_1" class="title-link">
<span class="text">
<span class="title-index">7.1</span>
<span class="title-link" nslog-type="10002802">优点</span>
</span>
</a>
</dd>
<dd class="catalog-title level2">
<a href="#7_2" class="title-link">
<span class="text">
<span class="title-index">7.2</span>
<span class="title-link" nslog-type="10002802">缺点</span>
</span>
</a>
</dd>
<dt class="catalog-title level1">
<em class="pointer"></em>
<a href="#8" class="title-link">
<span class="text">
<span class="title-index">8</span>
<span class="title-link" nslog-type="10002802">应用</span>
</span>
</a>
</dt>
<dt class="catalog-title level1">
<em class="pointer"></em>
<a href="#9" class="title-link">
<span class="text">
<span class="title-index">9</span>
<span class="title-link" nslog-type="10002802">工具功能</span>
</span>
</a>
</dt>
<dt class="catalog-title level1">
<em class="pointer"></em>
<a href="#10" class="title-link">
<span class="text">
<span class="title-index">10</span>
<span class="title-link" nslog-type="10002802">标准库</span>
</span>
</a>
</dt>
<dt class="catalog-title level1">
<em class="pointer"></em>
<a href="#11" class="title-link">
<span class="text">
<span class="title-index">11</span>
<span class="title-link" nslog-type="10002802">开发环境</span>
</span>
</a>
</dt>
<dt class="catalog-title level1">
<em class="pointer"></em>
<a href="#12" class="title-link">
<span class="text">
<span class="title-index">12</span>
<span class="title-link" nslog-type="10002802">解释器</span>
</span>
</a>
</dt>
<dt class="catalog-title level1">
<em class="pointer"></em>
<a href="#13" class="title-link">
<span class="text">
<span class="title-index">13</span>
<span class="title-link" nslog-type="10002802">著名应用</span>
</span>
</a>
</dt>
<dt class="catalog-title level1">
<em class="pointer"></em>
<a href="#14" class="title-link">
<span class="text">
<span class="title-index">14</span>
<span class="title-link" nslog-type="10002802">学习网站</span>
</span>
</a>
</dt>
<a class="arrow" href="javascript:void(0);"></a>
</dl>
</div>
<div class="right-wrap">
<a class="go-up disable" href="javascript:void(0);"></a>
<a class="go-down" href="javascript:void(0);"></a>
</div>
<div class="bottom-wrap">
<a class="toggle-button" href="javascript:void(0);"></a>
<a class="gotop-button" href="javascript:void(0);"></a>
</div>
</div>
<div class="unionAd_fromPs side-box" id="unionAd_fromPs">
<script type="BAIDU_HH">
    {
        type : 'pageembed',
        di   : 'u2140330',
        rsi0 : 270,
        rsi1 : 175
    }
    </script>
</div>
<div id="side_box_fengchao" class="fengchao side-box" nslog="area" nslog-type="10000902">
</div>
<div id="side_box_unionAd" class="unionAd side-box">
<div class="union-content"></div>
</div>
</div>
</div>
</div>
<div class="after-content">
<div class="fc-guess-like new" id="fc_guess_like_new">
<span class="logo-du">
<em class="cmn-icon cmn-icons cmn-icons_logo-du"></em>
</span>
<h6>猜你喜欢</h6>
<ul class="cmn-clearfix">
</ul>
</div>
<div class="bottom-promotion" id="bottom-promotion">
<div id="BOTTOM_PRO_AD"></div>
</div></div>
</div>

<div class="wgt-footer-main">
<div class="content">
<dl class="fresh">
<dt><em class="cmn-icon cmn-icons cmn-icons_footer-fresh"></em>新手上路</dt>
<dd>
<div><a target="_blank" href="/usercenter/tasks#guide">成长任务</a></div>
<div><a target="_blank" href="/help#main01">编辑入门</a></div>
<div><a target="_blank" href="/help#main06">编辑规则</a></div>
<div><a target="_blank" href="/help#main05">百科术语</a></div>
</dd>
</dl>
<dl class="question">
<dt><em class="cmn-icon cmn-icons cmn-icons_footer-question"></em>我有疑问</dt>
<dd>
<div><a target="_blank" href="/wikiui/doubt?lemmaId=407313&fr=lemma"
            nslog-type="10070001">我要质疑</a></div>
<div><a target="_blank" href="http://ikefu.baidu.com/baidubaike/chat.html" nslog-type="10000003">我要提问</a></div>
<div><a target="_blank" href="http://tieba.baidu.com/f?ie=utf-8&fr=bks0000&kw=%E7%99%BE%E5%BA%A6%E7%99%BE%E7%A7%91">参加讨论</a></div>
<div><a target="_blank" href="/feedback">意见反馈</a></div>
</dd>
</dl>
<dl class="suggestion">
<dt><em class="cmn-icon cmn-icons cmn-icons_footer-suggestion"></em>投诉建议</dt>
<dd>
<div><a target="_blank" href="http://tousu.baidu.com/baike#1">举报不良信息</a></div>
<div><a target="_blank" href="http://tousu.baidu.com/baike#2">未通过词条申诉</a></div>
<div><a target="_blank" href="http://tousu.baidu.com/baike#4">投诉侵权信息</a></div>
<div><a target="_blank" href="http://tousu.baidu.com/baike#3">封禁查询与解封</a></div>
</dd>
</dl>
</div>
<div class="copyright">©2017&nbsp;Baidu&nbsp;<a href="http://www.baidu.com/duty/" target="_blank">使用百度前必读</a>&nbsp;|&nbsp;<a href="http://help.baidu.com/question?prod_en=baike&class=159&id=1047" target="_blank">百科协议</a>&nbsp;|&nbsp;<a href="/operation/cooperation" target="_blank">百度百科合作平台</a></div>
</div>

<div class="lemmaWgt-searchHeader">
<div class="layout">
<div class="logo-container">
<a class="logo cmn-inline-block" title="到百科首页" href="/">
<span class="cmn-baike-logo">
<em class="cmn-icon cmn-icons cmn-icons_logo-bai"></em>
<em class="cmn-icon cmn-icons cmn-icons_logo-du"></em>
<em class="cmn-icon cmn-icons cmn-icons_logo-baike"></em>
</span>
</a>
</div>
<div class="search">
<div class="form">
<form id="searchForm" action="/search/word" method="GET" target="_self">
<input id="query" name="word" type="text" autocomplete="off" autocorrect="off" value="Python" /><a id="search" href="javascript:;"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_search" nslog-type="10010004"></em></a>
</form>
<form id="searchEnterForm" action="/search/word" method="GET" target="_self">
<input id="searchEnterWord" name="word" type="hidden" />
<input name="sefr" type="hidden" value="cr" />
</form>
<form id="searchQueryForm" action="/search/word" method="GET" target="_self">
<input id="searchQueryWord" name="word" type="hidden" />
<input name="sefr" type="hidden" value="enterbtn" />
</form>
<ul id="suggestion" class="suggestion">
<div></div>
<li class="extra">
<span id="close">关闭</span>
</li>
</ul>
</div>
</div>
<div class="tool-buttons">
<a class="toolButtons-edit button j-edit-link" href="javascript:;" nslog-type="10010001"></a>
<a class="toolButtons-collect button" href="javascript:;" nslog-type="10010002"></a>
<a class="toolButtons-vote button top-vote" href="javascript:;" nslog-type="10010003"></a>
</div>
<div class="user-info">
<a class="user-link unlogin" href="javascript:;" nslog-type="10010005" target="_blank">登录</a>
</div>
</div></div>
<div class="new-bdsharebuttonbox new-side-share" id="side-share">
<span class="title">分享</span>
<div class="side-border">
<div class="triangle"></div>
<a class="share-link bds_qzone"  href="javascript:void(0);" nslog-type="10060101">
<em class="cmn-icon cmn-icons cmn-icons_logo-qzone"></em>
</a>
<a class="share-link bds_tsina" href="javascript:void(0);" nslog-type="10060301">
<em class="cmn-icon cmn-icons cmn-icons_logo-sina-weibo"></em>
</a>
<a class="bds_wechat"  href="javascript:void(0);" nslog-type="10060001">
<em class="cmn-icon cmn-icons cmn-icons_logo-wechat"></em>
</a>
<a class="share-link bds_tqq"  href="javascript:void(0);" nslog-type="10060201">
<em class="cmn-icon cmn-icons cmn-icons_logo-qq"></em>
</a>
</div>
</div>
<div class="qrcode-wrapper" id="layer" style="display: none">
<div class="bd_weixin_popup_header">
<em class="cmn-icon cmn-icons cmn-icons_close"></em>
<span>分享到微信朋友圈</span>
</div>
<div id="wechat-qrcode-img"></div>
<div class="bd_weixin_popup_footer">打开微信“扫一扫”即可将网页分享至朋友圈</div>
</div>
<div></div><div></div>
</body><script type="text/javascript" src="http://baike.bdimg.com/static/wiki-common/pkg/wiki-common_sync_js_0_6be349d.js"></script>
<script type="text/javascript">require.resourceMap({"res":{"wiki-lemma:widget/lemma_content/mainContent/lemmaRelation/lemmaInsert.js":{"url":"http://baike.bdimg.com/static/wiki-lemma/widget/lemma_content/mainContent/lemmaRelation/lemmaInsert_17d225d.js","pkg":"wiki-lemma:p5","deps":["wiki-common:widget/component/nslog/nslog.js"]},"wiki-lemma:widget/lemma_content/mainContent/lemmaRelation/tangram.js":{"url":"http://baike.bdimg.com/static/wiki-lemma/widget/lemma_content/mainContent/lemmaRelation/tangram_1e4b3aa.js","pkg":"wiki-lemma:p5"},"wiki-lemma:widget/lemma_content/mainContent/lemmaReference/lemmaReferenceTip/lemmaReferenceTip.js":{"url":"http://baike.bdimg.com/static/wiki-lemma/widget/lemma_content/mainContent/lemmaReference/lemmaReferenceTip/lemmaReferenceTip_d50e02d.js","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/util/string.js"]}},"pkg":{"wiki-lemma:p5":{"url":"http://baike.bdimg.com/static/wiki-lemma/pkg/wiki-lemma-module-lemmaRelation_782158b.js"}}});</script><script type="text/javascript" src="http://baike.bdimg.com/static/wiki-common/widget/lib/jsmart/PHPJS_3347e0a.js"></script>
<script type="text/javascript" src="http://baike.bdimg.com/static/wiki-common/pkg/wiki-common_sync_js_1_f0a981d.js"></script>
<script type="text/javascript" src="http://baike.bdimg.com/static/wiki-common/pkg/wiki-common_sync_js_2_7a24e62.js"></script>
<script type="text/javascript" src="http://baike.bdimg.com/static/wiki-common/pkg/wiki-common_sync_js_5_62d9343.js"></script>
<script type="text/javascript" src="http://baike.bdimg.com/static/wiki-lemma/pkg/wiki-lemma_5c6109a.js"></script>
<script type="text/javascript" src="http://baike.bdimg.com/static/wiki-lemma/lemmaCode/script/XRegExp_3e3f85b.js"></script>
<script type="text/javascript" src="http://baike.bdimg.com/static/wiki-lemma/lemmaCode/script/shCore_e2d4316.js"></script>
<script type="text/javascript" src="http://baike.bdimg.com/static/wiki-lemma/lemmaCode/script/shBrushPython_40891a8.js"></script>
<script type="text/javascript" src="http://baike.bdimg.com/static/wiki-lemma/lemmaCode/script/shBrushXml_ce712fe.js"></script>
<script type="text/javascript" src="http://baike.bdimg.com/static/wiki-lemma/widget/lemma_content/configModule/zhixin/zhixin_587af69.js"></script>
<script type="text/javascript">!function(){  var $ = require('wiki-common:widget/lib/jquery/jquery.js'),
    userbar = require('wiki-common:widget/component/userbar/userbar.js');

  $(function() {
    userbar.buildUserbar($('.wgt-userbar'), null);
  });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery.js'),
      initSearchbar = require('wiki-common:widget/component/searchbar/searchbar.js');
    initSearchbar($('.wgt-searchbar-main'));
  }();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery.js');
    var cookie = require('wiki-common:widget/util/cookie.js');
    if (!cookie.get('baikedeclare')) {
        $('#J-declare-wrap').css('display', 'block');
    }
    $('#J-declare-close').on('click', function () {
        // 用户关闭后，不再显示，这里暂设过期时间为1年
        cookie.set('baikedeclare', 'showed', {
            expires: 365 * 60 * 60 * 24 * 1000
        });
        $('#J-declare-wrap').css('display', 'none');
    });
}();
!function(){  var $ = require('wiki-common:widget/lib/jquery/jquery.js');

  var timer = '';

  $('.wgt-navbar').on('mouseenter', 'dl', function() {
  clearTimeout(timer);
  timer = setTimeout(function() {
  $('.wgt-navbar').addClass('wgt-navbar-hover');
}, 300);
}).on('mouseleave', function() {
clearTimeout(timer);
$('.wgt-navbar').removeClass('wgt-navbar-hover');
}).on('click', 'a', function() {
clearTimeout(timer);
$('.wgt-navbar').removeClass('wgt-navbar-hover');
});
}();
!function(){                var $ = require('wiki-common:widget/lib/jquery/jquery.js');
                var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck.js');

                // 展现策略
                rightCheck.editView('407313', function(res) {
                    if (!res.errno) {
                        if (res.data.edit) {
                            $('.lemmaWgt-lemmaTitle .add-subLemma').css('display', 'inline-block');
                            $('.top-tool .add-sub-icon').css('display', 'inline-block');
                        }
                    } else {
                        if ('1') {
                            $('.lemmaWgt-lemmaTitle .add-subLemma').css('display', 'inline-block');
                            $('.top-tool .add-sub-icon').css('display', 'inline-block');
                        }
                    }
                });
                require('wiki-lemma:widget/basicElement/addSub/addSub.js')({                    lemmaId: '407313',                    lemmaTitle: 'Python',                    lemmaDesc: '',                    versionId: '117285608',                    subLemmaId: '21087'                });
            }();
!function(){        var $ = require('wiki-common:widget/lib/jquery/jquery.js');
        var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck.js');

        // 展现策略
        rightCheck.editView('407313', function(res) {
            if (!res.errno) {
                if (res.data.divide) {
                    $('.top-tool .split-icon').css('display', 'block');
                }
            }
        });
    }();
!function(){    var nslog = require('wiki-common:widget/component/nslog/nslog.js');
	require.async("wiki-lemma:widget/basicElement/collect/collect.js",function(collect){
		collect({
            newLemmaId:"407313",
			lemmaId:"21087",
			subLemmaId:"21087"
		});
	});
}();
!function(){    require.async("wiki-lemma:widget/basicElement/topShare/topShare.js",function(topShare){
        topShare({
            newLemmaId: '407313'
        });
    });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery.js');
    var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck.js');

    // 展现策略
    rightCheck.editView('407313', function(res) {
        if (!res.errno) {
            if (res.data.edit) {
                $('.lemmaWgt-lemmaTitle .edit-lemma').css('display', 'inline-block');
            } else {
                $('.lemmaWgt-lemmaTitle .lock-lemma').show();
            }
        } else {
            if ('1') {
                $('.lemmaWgt-lemmaTitle .edit-lemma').css('display', 'inline-block');
            } else {
                $('.lemmaWgt-lemmaTitle .lock-lemma').show();
            }
        }
    });
}();
!function(){	require('wiki-lemma:widget/lemma_content/mainContent/basicInfo/basicInfo.js')();
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery.js');
    var nslog = require('wiki-common:widget/component/nslog/nslog.js');
    nslog(10002701);
    $('.lemmaWgt-lemmaCatalog a').on('click', function () {
           nslog(10002702);
    });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery.js');
    var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck.js');

    // 展现策略
    rightCheck.editView('407313', function(res) {
        if (!res.errno) {
            if (res.data.edit) {
                $('.para-title .edit-icon').css('display', 'block');
            }
        } else {
            if ('1') {
                $('.para-title .edit-icon').css('display', 'block');
            }
        }
    });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery.js');
    var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck.js');

    // 展现策略
    rightCheck.editView('407313', function(res) {
        if (!res.errno) {
            if (res.data.edit) {
                $('.para-title .edit-icon').css('display', 'block');
            }
        } else {
            if ('1') {
                $('.para-title .edit-icon').css('display', 'block');
            }
        }
    });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery.js');
    var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck.js');

    // 展现策略
    rightCheck.editView('407313', function(res) {
        if (!res.errno) {
            if (res.data.edit) {
                $('.para-title .edit-icon').css('display', 'block');
            }
        } else {
            if ('1') {
                $('.para-title .edit-icon').css('display', 'block');
            }
        }
    });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery.js');
    var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck.js');

    // 展现策略
    rightCheck.editView('407313', function(res) {
        if (!res.errno) {
            if (res.data.edit) {
                $('.para-title .edit-icon').css('display', 'block');
            }
        } else {
            if ('1') {
                $('.para-title .edit-icon').css('display', 'block');
            }
        }
    });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery.js');
    var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck.js');

    // 展现策略
    rightCheck.editView('407313', function(res) {
        if (!res.errno) {
            if (res.data.edit) {
                $('.para-title .edit-icon').css('display', 'block');
            }
        } else {
            if ('1') {
                $('.para-title .edit-icon').css('display', 'block');
            }
        }
    });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery.js');
    var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck.js');

    // 展现策略
    rightCheck.editView('407313', function(res) {
        if (!res.errno) {
            if (res.data.edit) {
                $('.para-title .edit-icon').css('display', 'block');
            }
        } else {
            if ('1') {
                $('.para-title .edit-icon').css('display', 'block');
            }
        }
    });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery.js');
    var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck.js');

    // 展现策略
    rightCheck.editView('407313', function(res) {
        if (!res.errno) {
            if (res.data.edit) {
                $('.para-title .edit-icon').css('display', 'block');
            }
        } else {
            if ('1') {
                $('.para-title .edit-icon').css('display', 'block');
            }
        }
    });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery.js');
    var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck.js');

    // 展现策略
    rightCheck.editView('407313', function(res) {
        if (!res.errno) {
            if (res.data.edit) {
                $('.para-title .edit-icon').css('display', 'block');
            }
        } else {
            if ('1') {
                $('.para-title .edit-icon').css('display', 'block');
            }
        }
    });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery.js');
    var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck.js');

    // 展现策略
    rightCheck.editView('407313', function(res) {
        if (!res.errno) {
            if (res.data.edit) {
                $('.para-title .edit-icon').css('display', 'block');
            }
        } else {
            if ('1') {
                $('.para-title .edit-icon').css('display', 'block');
            }
        }
    });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery.js');
    var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck.js');

    // 展现策略
    rightCheck.editView('407313', function(res) {
        if (!res.errno) {
            if (res.data.edit) {
                $('.para-title .edit-icon').css('display', 'block');
            }
        } else {
            if ('1') {
                $('.para-title .edit-icon').css('display', 'block');
            }
        }
    });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery.js');
    var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck.js');

    // 展现策略
    rightCheck.editView('407313', function(res) {
        if (!res.errno) {
            if (res.data.edit) {
                $('.para-title .edit-icon').css('display', 'block');
            }
        } else {
            if ('1') {
                $('.para-title .edit-icon').css('display', 'block');
            }
        }
    });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery.js');
    var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck.js');

    // 展现策略
    rightCheck.editView('407313', function(res) {
        if (!res.errno) {
            if (res.data.edit) {
                $('.para-title .edit-icon').css('display', 'block');
            }
        } else {
            if ('1') {
                $('.para-title .edit-icon').css('display', 'block');
            }
        }
    });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery.js');
    var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck.js');

    // 展现策略
    rightCheck.editView('407313', function(res) {
        if (!res.errno) {
            if (res.data.edit) {
                $('.para-title .edit-icon').css('display', 'block');
            }
        } else {
            if ('1') {
                $('.para-title .edit-icon').css('display', 'block');
            }
        }
    });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery.js');
    var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck.js');

    // 展现策略
    rightCheck.editView('407313', function(res) {
        if (!res.errno) {
            if (res.data.edit) {
                $('.para-title .edit-icon').css('display', 'block');
            }
        } else {
            if ('1') {
                $('.para-title .edit-icon').css('display', 'block');
            }
        }
    });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery.js');
    var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck.js');

    // 展现策略
    rightCheck.editView('407313', function(res) {
        if (!res.errno) {
            if (res.data.edit) {
                $('.para-title .edit-icon').css('display', 'block');
            }
        } else {
            if ('1') {
                $('.para-title .edit-icon').css('display', 'block');
            }
        }
    });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery.js');
    var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck.js');

    // 展现策略
    rightCheck.editView('407313', function(res) {
        if (!res.errno) {
            if (res.data.edit) {
                $('.para-title .edit-icon').css('display', 'block');
            }
        } else {
            if ('1') {
                $('.para-title .edit-icon').css('display', 'block');
            }
        }
    });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery.js');
    var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck.js');

    // 展现策略
    rightCheck.editView('407313', function(res) {
        if (!res.errno) {
            if (res.data.edit) {
                $('.para-title .edit-icon').css('display', 'block');
            }
        } else {
            if ('1') {
                $('.para-title .edit-icon').css('display', 'block');
            }
        }
    });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery.js');
    var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck.js');

    // 展现策略
    rightCheck.editView('407313', function(res) {
        if (!res.errno) {
            if (res.data.edit) {
                $('.para-title .edit-icon').css('display', 'block');
            }
        } else {
            if ('1') {
                $('.para-title .edit-icon').css('display', 'block');
            }
        }
    });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery.js');
    var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck.js');

    // 展现策略
    rightCheck.editView('407313', function(res) {
        if (!res.errno) {
            if (res.data.edit) {
                $('.para-title .edit-icon').css('display', 'block');
            }
        } else {
            if ('1') {
                $('.para-title .edit-icon').css('display', 'block');
            }
        }
    });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery.js');
    var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck.js');

    // 展现策略
    rightCheck.editView('407313', function(res) {
        if (!res.errno) {
            if (res.data.edit) {
                $('.para-title .edit-icon').css('display', 'block');
            }
        } else {
            if ('1') {
                $('.para-title .edit-icon').css('display', 'block');
            }
        }
    });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery.js');
    var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck.js');

    // 展现策略
    rightCheck.editView('407313', function(res) {
        if (!res.errno) {
            if (res.data.edit) {
                $('.para-title .edit-icon').css('display', 'block');
            }
        } else {
            if ('1') {
                $('.para-title .edit-icon').css('display', 'block');
            }
        }
    });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery.js');
    var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck.js');

    // 展现策略
    rightCheck.editView('407313', function(res) {
        if (!res.errno) {
            if (res.data.edit) {
                $('.para-title .edit-icon').css('display', 'block');
            }
        } else {
            if ('1') {
                $('.para-title .edit-icon').css('display', 'block');
            }
        }
    });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery.js');
    var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck.js');

    // 展现策略
    rightCheck.editView('407313', function(res) {
        if (!res.errno) {
            if (res.data.edit) {
                $('.para-title .edit-icon').css('display', 'block');
            }
        } else {
            if ('1') {
                $('.para-title .edit-icon').css('display', 'block');
            }
        }
    });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery.js');
    var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck.js');

    // 展现策略
    rightCheck.editView('407313', function(res) {
        if (!res.errno) {
            if (res.data.edit) {
                $('.para-title .edit-icon').css('display', 'block');
            }
        } else {
            if ('1') {
                $('.para-title .edit-icon').css('display', 'block');
            }
        }
    });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery.js');
    var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck.js');

    // 展现策略
    rightCheck.editView('407313', function(res) {
        if (!res.errno) {
            if (res.data.edit) {
                $('.para-title .edit-icon').css('display', 'block');
            }
        } else {
            if ('1') {
                $('.para-title .edit-icon').css('display', 'block');
            }
        }
    });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery.js');
    var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck.js');

    // 展现策略
    rightCheck.editView('407313', function(res) {
        if (!res.errno) {
            if (res.data.edit) {
                $('.para-title .edit-icon').css('display', 'block');
            }
        } else {
            if ('1') {
                $('.para-title .edit-icon').css('display', 'block');
            }
        }
    });
}();
!function(){        SyntaxHighlighter.all();
    }();
!function(){		require.async(["wiki-lemma:widget/lemma_content/mainContent/lemmaReference/lemmaReference.js", "wiki-lemma:widget/lemma_content/mainContent/lemmaReference/lemmaReferenceTip/lemmaReferenceTip.js"],function(Reference,ReferenceTip){
			new Reference({
				subLemmaId:"21087"
			});
			new ReferenceTip({
				subLemmaId:"21087"
			});
		});
	}();
!function(){    require.async('wiki-lemma:widget/promotion/xunke/xunke.js', function (app) {
        app.init({
            lemmaTitle: 'Python',
            adManager: {"wapRelatedBusiness":1}
        });
    });
}();
!function(){        require('wiki-lemma:widget/lemma_content/configModule/zhixin/zhixin.js')(
            407313,
            'Python'
        );
    }();
!function(){    require.async("wiki-lemma:widget/lemma_content/mainContent/lemmaStatistics/lemmaStatistics.js",function(init){
        init({
            newLemmaIdEnc:"242a1308b00febde401c451c"
        });
    });
}();
!function(){	require.async("wiki-lemma:widget/lemma_content/mainContent/sideCatalog/sideCatalog.js",function(SideCatalog){
		new SideCatalog();
	});
}();
!function(){        require.async(['wiki-lemma:widget/promotion/unionAdFromPs/unionAdFromPs.js'], function (init) {
            init({
                adManager: {"wapRelatedBusiness":1}
            });
        });
    }();
!function(){    require.async(["wiki-lemma:widget/promotion/fengchao/fengchao.js", "wiki-lemma:widget/promotion/unionAd/unionAd.js"], function (init, unionAd) {
        init({
            newLemmaId: "407313",
            lemmaTitle: "Python",
            encodeLemmaTitle: "Python",
            adManager: {"wapRelatedBusiness":1}
        }, {
            errFn: unionAd,
            dom: $('#side_box_unionAd')
        });
    });
}();
!function(){    require.async('wiki-lemma:widget/promotion/guessLike/guessLike.js', function (app) {
        app.init({
            lemmaTitle: 'Python',
            adManager: {"wapRelatedBusiness":1}
        });
    });
}();
!function(){        require.async('wiki-lemma:widget/promotion/bottomAd/bottomAd.js', function (init) {
            init({
                sId: 'BOTTOM_PRO_AD',
                adManager: {"wapRelatedBusiness":1}
            });
        });
    }();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery.js');
    var Dialog = require("wiki-common:widget/ui/dialog/dialog.js");
    var userLogin = require('wiki-common:widget/component/userLogin/userLogin.js');
    var unameFiller = require('wiki-common:widget/component/unameFiller/unameFiller.js');
    var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck.js');

            var isEnterprise = false;
        var enterpriseOwnerUserId = 0;

    var userId = 0;
    var editUrl = '/edit/' + encodeURIComponent('Python') + '/' + '407313';
    var pgcUrl = '/enterprise/editpgc?lemmaId=407313';

    userLogin.regist({
        onLogin: function(user) {
            userId = user ? user.uid : 0;
        }
    });

    function gotoEdit(url, isMidNight) {
        if (isMidNight) {
            Dialog.alert({
                title: '编辑提示',
                subMsg: '晚23:00至次日8:00，因审核系统例行维护，您提交的版本可能需要较长时间才能通过，望您谅解。',
                onConfirm: function() {
                    window.location.href = url;
                }
            });
        } else {
            window.location.href = url;
        }
    }

    function showChoseEditDialog(pgcCallback, ugcCallback) {
        new Dialog({
            title: '编辑提示',
            subMsg: '<p>您已开通企业百科服务，推荐您直接编辑“官方资料”，官方资料仅限企业百科绑定的百科账号修改，其他用户账号不可修改。</p><p>如果您想修改其他网友编辑的普通词条内容，请注意遵守百科百科编辑规则。<p>',
            btns: [{
            key: 'pgc',
            text: '编辑官方资料'
            }, {
            style: 'white',
            text: '修改普通词条',
            key: 'ugc'
            }],
            onBtnClick: function(btnKey){
                if (btnKey === 'pgc') {
                    pgcCallback && pgcCallback();
                } else if (btnKey === 'ugc') {
                    ugcCallback && ugcCallback();
                }
            }
        }).show();
    }

    function checkUserLegal(res) {
        var legal = false;
        switch (res.errno) {
            case 100001:
                userLogin.showLoginPop();
                break;
            case 100006:
                unameFiller.show();
                break;
            default:
                legal = true;
        }
        return true;
    }

    function checkUgc(res, url) {
        if (res.errno) {
            switch (res.errno) {
                case 100005:
                    alert('对不起，您目前被封禁');
                    break;
                case 110001:
                    alert('对不起，该词条被锁定');
                    break;
                case 110007:
                    alert('对不起，消歧页无法编辑');
                    break;
                case 110005:
                    Dialog.alert({
                    title: '编辑提示',
                    mainMsg: '对不起，您暂时没有权限编辑该词条。',
                    subMsg: '<p>您好，该词条内容已较丰富，现仅对百科等级达到<b>四级</b>且通过率达到<b>85%</b>的科友开放编辑。</p><p>当您通过努力达到以上要求，就可以参与编辑该词条了。</p><p><img src="http://img.baidu.com/img/baike/usercenter/growuptask/star.gif" class="star" />参加<a target="_blank" href="/usercenter#guide">成长任务</a>，更快掌握百科编辑技巧，加速升级！</p>'
                    });
                    break;
                case 110008:
                    Dialog.alert({
                    title: '编辑提示',
                    mainMsg: '对不起，您暂时没有权限编辑该词条。',
                    subMsg: '<p>您好，该词条内容已较丰富，现仅对百科等级达到<b>六级</b>且通过率达到<b>85%</b>的科友开放编辑。</p><p>当您通过努力达到以上要求，就可以参与编辑该词条了。</p><p><img src="http://img.baidu.com/img/baike/usercenter/growuptask/star.gif" class="star" />参加<a target="_blank" href="/usercenter#guide">成长任务</a>，更快掌握百科编辑技巧，加速升级！</p>'
                    });
                    break;
                case 470001:
                    alert('系统错误，请刷新重试');
                    break;
            }
        } else {
            if (!res.data.right.noAudit) {
                Dialog.alert({
                    title: '编辑提示',
                    subMsg: '很抱歉，该词条有其他用户编辑的版本正在提交，您暂时无法编辑。<br/>百科建议您晚些时候再编辑该词条，或者尝试编辑其他的词条。'
                });
                return;
            }
            gotoEdit(url, res.data.notice.isMidNight);
        }
    }

    $(document.body).on('click', '.j-edit-link', function() {
        var dl = $(this).attr('data-edit-dl');
        if (dl) {
            var url = editUrl + '?dl=' + dl;
        } else {
            var url = editUrl;
        }

        rightCheck.preeditCheck('407313', 'Python', 'Python', '117285608', function(res) {
            if (!checkUserLegal(res)) {
                return;
            }
            if (isEnterprise && enterpriseOwnerUserId === userId) {
                showChoseEditDialog(function() {
                    location.href = pgcUrl;
                }, function() {
                    checkUgc(res, url);
                });
            } else {
                checkUgc(res, url);
            }
        });
    });
}();
!function(){    require.async("wiki-lemma:widget/tools/searchHeader/toolButtons/toolButtons.js",function(init){
        init({
            lemmaId:"21087",
            subLemmaId:"21087",
            newLemmaId:"407313"
        });
    });
}();
!function(){    require('wiki-lemma:widget/tools/searchHeader/toolButtons/userInfo.js')();
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery.js'),
      animation = require('wiki-common:widget/util/animation.js'),
      nslog = require('wiki-common:widget/component/nslog/nslog.js'),
      initSearchbar = require('wiki-common:widget/component/searchbar/searchbar.js');

    var isFadeIn = false,
        isFadeOut = false;

    var fadeInAni, fadeOutAni;

    $(window).on('scroll', function(e) {
        var scrollTop = $(this).scrollTop();

        if (scrollTop > 200 && !isFadeIn && $('.lemmaWgt-searchHeader').css('display') == 'none') {
            fadeOutAni && fadeOutAni.stop();
            fadeInAni = animation({
                duration: 200,
                easing: 'linear',
                onStart: function() {
                    isFadeOut = false;
                    isFadeIn = true;
                    $('.lemmaWgt-searchHeader').css('display', 'block');
                },
                onStep: function(progress) {
                    $('.lemmaWgt-searchHeader').css('opacity', progress)
                },
                onComplete: function(progress) {
                    isFadeIn = false;
                    nslog(10010006);
                }
            });
        } else if (scrollTop <= 200 && !isFadeOut && $('.lemmaWgt-searchHeader').css('display') == 'block') {
            fadeInAni && fadeInAni.stop();
            fadeOutAni = animation({
                duration: 300,
                easing: 'linear',
                onStart: function() {
                    $('.lemmaWgt-searchHeader #suggestion').hide();
                    isFadeIn = false;
                    isFadeOut = true;
                },
                onStep: function(progress) {
                    $('.lemmaWgt-searchHeader').css('opacity', 1 - progress);
                },
                onComplete: function(progress) {
                    isFadeOut = false;
                    $('.lemmaWgt-searchHeader').css('display', 'none');
                }
            });
        }
    });

    initSearchbar($('.lemmaWgt-searchHeader'));
}();
!function(){    require('wiki-lemma:widget/tools/newSideShare/qzopensl.js');
    require.async("wiki-lemma:widget/tools/newSideShare/taskSideShare.js",function(taskShare){
        taskShare.init({
            title: 'Python',
            desc: "Python\uff08\u82f1\u56fd\u53d1\u97f3\uff1a\\\/\u02c8pa\u026a\u03b8\u0259n\\\/ \u7f8e\u56fd\u53d1\u97f3\uff1a\\\/\u02c8pa\u026a\u03b8\u0251\u02d0n\\\/\uff09, \u662f\u4e00\u79cd\u9762\u5411\u5bf9\u8c61\u7684\u89e3\u91ca\u578b\u8ba1\u7b97\u673a\u7a0b\u5e8f\u8bbe\u8ba1\u8bed\u8a00\uff0c\u7531\u8377\u5170\u4ebaGuido van Rossum\u4e8e1989\u5e74\u53d1\u660e\uff0c\u7b2c\u4e00\u4e2a\u516c\u5f00\u53d1\u884c\u7248\u53d1\u884c\u4e8e1991\u5e74\u3002Python\u662f\u7eaf\u7cb9\u7684\u81ea\u7531\u8f6f\u4ef6\uff0c \u6e90\u4ee3\u7801\u548c\u89e3\u91ca\u5668CPython\u9075\u5faa GPL(GNU General Public License)\u534f\u8bae\u3002Python\u8bed\u6cd5\u7b80\u6d01\u6e05\u6670\uff0c\u7279\u8272\u4e4b\u4e00\u662f\u5f3a\u5236\u7528\u7a7a\u767d\u7b26(whit",
            pic: 'http:\/\/c.hiphotos.baidu.com\/baike\/w%3D268\/sign=032aad11cd11728b302d8b24f0fdc3b3\/0eb30f2442a7d9331abfc6f3ad4bd11373f0011e.jpg',
            url: '',
            qqPic: 'http:\/\/c.hiphotos.baidu.com\/baike\/whfpf%3D286%2C286%2C0\/sign=72c61f4a513d26972e865b1d33c680c3\/0eb30f2442a7d9331abfc6f3ad4bd11373f0011e.jpg'
        });
    });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery.js');
    var nslog = require("wiki-common:widget/component/nslog/nslog.js");
    var testElem = require('wiki-common:widget/component/testElem/testElem.js');
    var cmsModuleLoader = require('wiki-common:widget/component/cmsModuleLoader/cmsModuleLoader.js');

    function requireAsync() {
        require.async('wiki-lemma:widget/tools/announcement/announcement.js');
    }

    cmsModuleLoader('/cms/global/lemma_config.json', [{
        name: 'announcement',
        script: 'wiki-lemma:widget/tools/announcement/announcement.js'
    }]);

    require.async("wiki-lemma:widget/tools/lazyLoad/lazyLoad.js", function(LazyLoad) {
        new LazyLoad();
    });

    require.async(['wiki-common:widget/component/nslog/nslog.js', 'wiki-common:widget/lib/jquery/jquery.js'], function(nslog, $) {
        nslog().setGlobal({
            lemmaId: "21087",
            newLemmaId: "407313",
            subLemmaId: "21087",
            lemmaTitle: "Python"
        });

        // 词条页 pv
        nslog(9322);

        // 新版头部pv（小流量）
        if ($('.pc-header-new').length > 0) {
            nslog(9069);
        }

        // 链接点击 pv
        var lemmaPageRegExp = new RegExp(/\/subview\/\d+|\/view\/\d+|\/item\//i);
        $('body').on('mousedown', 'a', function() {
            var href = $(this).attr('href');
            if (href && href.indexOf('/') >= 0 && href.indexOf('#') !== 0) {
                // 链接点击 pv
                nslog(10000001);
                if (lemmaPageRegExp.test(href)) {
                    // 词条页链接点击 pv
                    nslog(10000002, window.location.href, {
                        targetTitle: $(this).text()
                    });
                }
            }
        });

        /****** 词条页站内流转需求统计 start ******/
        (function () {
            // 各种统计配置
            var circulationLinkCfg = {
                innerLink: [ // 内链
                    '.para',
                    '.lemmaWgt-baseInfo-simple-largeMovie',
                    '.lemmaWgt-baseInfo-simple-largeStar',
                    '.basic-info .basicInfo-block',
                    '.lemma-summary',
                    '.lemmaWgt-lemmaSummary',
                    '.view-tip-panel',
                    '.horizontal-module',
                    '.lemmaWgt-roleIntroduction',
                    '.dramaSeries .dramaSerialList',
                    '.module-music',
                    '.table-view',
                    '[log-set-param="table_view"]',
                    '.list-module',
                    '.cell-module',
                    '.baseBox .dl-baseinfo', // 配置后台字段
                    '.pvBtn-box .leadPVBtnWrapper',
                    '.drama-actor',
                    '#staffList',
                    '.starMovieAndTvplay',
                    '.main_tab:not(.main_tab-defaultTab)' // 除去词条tab外的tab
                ],
                relationTable: '.rs-container-foot', // 关系表
                peopleRelation: '.star-info-block.relations, .lemmaWgt-focusAndRelation', // 人物关系（明星+普通）
                moduleActors: '.featureBaseInfo .actors, .lemmaWgt-majorActors', // 主要演员、嘉宾、主持人
                moduleWorks: '.featureBaseInfo .works, .large-feature .works', // 代表作品
                moduleQuarterly: '.featureBaseInfo .po_quarterly, .mian_quarterly', // 分季介绍
                rankStar: '.rank-list.stars-rank', // 明星榜
                rankDrama: '.drama-rank-list', // 电视剧榜
                specialTopic: '.special-topic', // 专题模块
                modDetailTable: '#modDetailTable', // 关系表出图
                chuizhitu: '.chuizhitu', // 垂直化模块
                polysemantList: '.polysemantList-wrapper' // 义项切换
            };
            /****** 连接统计 ******/
            function clickNslogFn() {
                for (var k in circulationLinkCfg) {
                    if (k === 'innerLink') {
                        // 词条内链到词条页
                        var tempArr = circulationLinkCfg[k];
                        for (var i = 0, l = tempArr.length; i < l; i++) {
                            tempArr[i] += ' a';
                        }
                        var sSelector = tempArr.join(', ');

                        $('body').on('mousedown', sSelector, {key: k},function(e) {
                            var key = e.data.key;
                            var href = $(this).attr('href');
                            var tar = $(this).attr('target') || '';
                            if (href && href.indexOf('/') >= 0 && href.indexOf('#') !== 0
                            && tar === '_blank' && lemmaPageRegExp.test(href)) {
                                // 词条页普通内链点击 pv
                                nslog(10000004, null ,{division: key});
                            }
                        });
                    } else {
                        // 模块到词条页链接
                        $(circulationLinkCfg[k]).on('mousedown', 'a', {key: k}, function (e) {
                            var key = e.data.key;
                            var href = $(this).attr('href');
                            if (href && href.indexOf('#') !== 0 && lemmaPageRegExp.test(href)) {
                                // 词条页配置模块链接点击 pv
                                nslog(10000004, null, {division: key});
                            }
                        });
                    }
                }
            }
            // 发起统计请求
            clickNslogFn();

            /****** 各模块展现量pv ******/
            function checkModuleIsShow() {
                var result = [];
                for (var k in circulationLinkCfg) {
                    if (k !== 'innerLink' && k !== 'relationTable') {
                        !!$(circulationLinkCfg[k]).html() && result.push(k);
                    }
                }
                if (result.length > 0) {
                    nslog(10000005, null, {showModules: result.join(',')});
                }
            }
            checkModuleIsShow();

        })();
        /****** 词条页站内流转需求统计 end ******/

    });

    // 广告接入 wikiad 统一加载
    // log 词条页广告被拦截情况（此处 log 请求行为）
    nslog(70000101, window.location.href, {
        api: 'lemma-ad',
        action: 'request'
    });
    $.ajax({
        type: 'GET',
        url: '/api/wikiad/getsquirrels',
        data: {
            lemmaId: 407313
        },
        cache: false,
        dataType: 'JSON',
        success: function (res) {
            // log 词条页广告被拦截情况（此处 log 请求成功）
            nslog(70000101, window.location.href, {
                api: 'lemma-ad',
                action: 'success'
            });

            if (!res.errno) {
                if (res.data[5]) {
                    require.async(['wiki-lemma:widget/promotion/rightPreciseAd/rightPreciseAd.js'], function(rightPreciseAd) {
                        rightPreciseAd(res.data[5]);
                        nslog(10002201, location.href, {
                            adId: res.data[5][0].adId,
                            adTitle: res.data[5][0].name,
                            adPos: 5
                        });
                    });
                } else if (res.data[1]) {
                    require.async(['wiki-lemma:widget/promotion/vbaike/vbaike.js'], function(vbaike) {
                        vbaike(res.data[1]);
                        for(var i in res.data[1]) {
                            nslog(10002201, location.href, {
                                adId: res.data[1][i].adId,
                                adTitle: res.data[1][i].name,
                                adPos: 1
                            });
                        }
                    });
                }
                if (res.data[9]) {
                    require.async(['wiki-lemma:widget/promotion/rightBigAd/rightBigAd.js'], function(rightBigAd) {
                        rightBigAd(res.data[9]);
                            nslog(10002201, location.href, {
                                adId: res.data[9][0].adId,
                                adTitle: res.data[9][0].name,
                                adPos: 9
                            });
                    });
                } else if(res.data[2]) {
                    require.async(['wiki-lemma:widget/promotion/slide/slide.js'], function(slide) {
                        slide(res.data[2]);
                        for(var i in res.data[2]) {
                            nslog(10002201, location.href, {
                                adId: res.data[2][i].adId,
                                adTitle: res.data[2][i].name,
                                adPos: 2
                            });
                        }
                    });
                }
                if (res.data[3]) {
                    require.async(['wiki-lemma:widget/promotion/topAd/topAd.js'], function(topAd) {
                        topAd(res.data[3]);
                        nslog(10002201, location.href, {
                            adId: res.data[3][0].adId,
                            adTitle: res.data[3][0].name,
                            adPos: 3
                        });
                    });
                }
                if (res.data[4]) {
                    require.async(['wiki-lemma:widget/promotion/rightAd/rightAd.js'], function(rightAd) {
                        rightAd(res.data[4]);
                        nslog(10002201, location.href, {
                            adId: res.data[4][0].adId,
                            adTitle: res.data[4][0].name,
                            adPos: 4
                        });
                    });
                }
                if (res.data[15]) {
                    require.async(['wiki-lemma:widget/promotion/banner/banner.js'], function(banner) {
                        banner(res.data[15]);
                        nslog(10002201, location.href, {
                            adId: res.data[15][0].adId,
                            adTitle: res.data[15][0].name,
                            adPos: 15
                        });
                    });
                }
                if (res.data[16]) {
                    require.async(['wiki-lemma:widget/promotion/declaration/declaration.js'], function(declaration) {
                        declaration(res.data[16]);
                        nslog(10002201, location.href, {
                            adId: res.data[16][0].adId,
                            adTitle: res.data[16][0].name,
                            adPos: 16
                        });
                    })
                }
            } else {
                return;
            }

            setTimeout(function () {
                var elemArr = {};
                res.data[1] && res.data[1].length > 0 && (elemArr['lemma-vbaike-ad'] = $('.lemmaWgt-promotion-vbaike .promotion_viewport a:eq(0) img').get(0));
                res.data[2] && res.data[2].length > 0 && (elemArr['lemma-slide-ad'] = $('.lemmaWgt-promotion-slide .promotion_viewport a:eq(0) img').get(0));
                res.data[3] && res.data[3].length > 0 && (elemArr['lemma-navbar-ad'] = {
                    node: $('.header [nslog-type="10002202"]').get(0),
                    validations: {
                        'noBackgroundImage': function() {
                            return $('.header [nslog-type="10002202"]').css('background-image').indexOf(res.data[3][0].picUrl) < 0
                        }
                    }
                });
                res.data[4] && res.data[4].length > 0 && (elemArr['lemma-side-ad'] = {
                    node: $('.right-ad img').get(0),
                    validations: {
                        'noBackgroundImage': function() {
                            return $('.right-ad img').attr('src').indexOf(res.data[4][0].picUrl) < 0
                        }
                    }
                });
                res.data[15] && res.data[15].length > 0 && (elemArr['lemma-configModule-banner'] = $('.configModuleBanner').get(0));
                res.data[16] && res.data[16].length > 0 && (elemArr['lemma-configModule-declaration'] = $('.lemmaWgt-declaration').get(0));

                testElem.log(elemArr, 70000102);
            }, 1000);
        },
        error: function () {
            // log 词条页广告被拦截情况（此处 log 请求失败）
            nslog(70000101, window.location.href, {
                api: 'lemma-ad',
                action: 'error'
            });
        }
    });

    // 设置分享内容
    window.BKShare.setCommon({
        bdText: "\u3010Python_\u767e\u5ea6\u767e\u79d1\u3011Python\uff08\u82f1\u56fd\u53d1\u97f3\uff1a\/\u02c8pa\u026a\u03b8\u0259n\/ \u7f8e\u56fd\u53d1\u97f3\uff1a\/\u02c8pa\u026a\u03b8\u0251\u02d0n\/\uff09, \u662f\u4e00\u79cd\u9762\u5411\u5bf9\u8c61\u7684\u89e3\u91ca\u578b\u8ba1\u7b97\u673a\u7a0b\u5e8f\u8bbe\u8ba1\u8bed\u8a00\uff0c\u7531\u8377\u5170\u4ebaGuido van Rossum\u4e8e1989\u5e74\u53d1\u660e\uff0c\u7b2c\u4e00\u4e2a\u516c\u5f00\u53d1\u884c\u7248\u53d1\u884c\u4e8e1991\u5e74\u3002Python\u662f\u7eaf\u7cb9\u7684\u81ea\u7531\u8f6f\u4ef6\uff0c \u6e90\u4ee3\u7801\u548c\u89e3\u91ca\u5668CPython\u9075\u5faa GPL(GNU General Public License)\u534f\u8bae\u3002Python\u8bed\u6cd5\u7b80\u6d01\u6e05\u6670\uff0c\u7279\u8272\u4e4b\u4e00\u662f\u5f3a\u5236\u7528\u7a7a\u767d\u7b26(whit.....\uff08\u5206\u4eab\u81ea@\u767e\u5ea6\u767e\u79d1\uff09",
        bdDesc: '',
        bdUrl: 'http:\/\/baike.baidu.com\/subview\/21087\/21087.htm',
        bdPic: '',
        onBeforeClick: function (){
            $('.bdshare_dialog_box').hide();
        }
    });

    // 底部投诉带入当前页面 url
    var map = [1, 2, 4, 3];
    $('.wgt-footer-main .suggestion').find('a').each(function(i) {
        $(this).attr('href', 'http://tousu.baidu.com/baike/add?word=Python' + '&&submit_link=' + encodeURIComponent(window.location.href) + '#' + map[i]);
    });

    // 为超出预设内容的表格添加table-responsive控制
    $('.main-content').find('table').each(function(index) {
        var $that = $(this);
        if ($that.width() > 790) {
            $that.wrap('<div class="table-responsive"></div>');
        }
    });
}();
!function(){      require('wiki-common:widget/component/psLink/psLink.js');
    }();</script><script type="text/javascript">(new Image()).src="https://gsp0.baidu.com/5aAHeD3nKhI2p27j8IqW0jdnxx1xbK/tb/pms/img/st.gif?pid=242&v=2&fs=d17c11e,6cf69d7,245a071,0c8a499,6989571,8489f15,3b87af4,55b8460,5d75544,610f001,04b6dcb,6caef55,ea15059,1e698a5,4e6f885,a8d1422,f3869a1,e8122d1,08c0ca0,7c09ce8,16addac,bf8f8ff,1ec069b,429109e,4751f41,599060d,9a244fa,6d3f55c,ff792b0,2f3cb53,d968012,63854a5,e3da08e,8f25bc7,9d4c3fb,5ec9780,b6a75d6,fbad8c8,c3f013b,6c7071e,8ad3c5a,ff01574,7046c2e,82ccc49,f781616,f770c7c,79f1b80,060d084,d2b396c,fcae7b0,bc8d043,93e2dbc,9ef720d,1e296fe,c2d6b6c,df2f43f,5e5bbf2,de21595,3863f12,a2c6e33,7d13e8e,9c3a8fa,f1f5abb,3e9410c,ba4de73,117d9c9,49d5515,03483af,4ebc297,52f3fd6,00cd86b,c02b5b1,e741536,aa8964e,1d27d9a,fa38f44,97ab102,912dba1,5a73c4a,0469f06,630e49a,b44b6c1,35aca65&otherStr=&page=wiki-lemma/page/normal/normal.tpl&sid=1489721579&hash=04b29d82c3&fid=baike";</script>
<script type="text/javascript">
  var Hunter = window.Hunter || {};
  Hunter.userConfig = Hunter.userConfig || [];
  </script>
<script type="text/javascript" src="https://gss0.baidu.com/70cFsjip0QIZ8tyhnq/hunter/baike.js?st=17242" defer></script><script type="text/javascript">
  // DOM Ready时，统计用户可操作时间。
  alog('speed.set', 'drt', +new Date);

  void function(a,b,c,d,e,f){function g(b){a.attachEvent?a.attachEvent("onload",b,!1):a.addEventListener&&a.addEventListener("load",b)}function h(a,c,d){d=d||15;var e=new Date;e.setTime((new Date).getTime()+1e3*d),b.cookie=a+"="+escape(c)+";path=/;expires="+e.toGMTString()}function i(a){var c=b.cookie.match(new RegExp("(^| )"+a+"=([^;]*)(;|$)"));return null!=c?unescape(c[2]):null}function j(){var a=i("PMS_JT");if(a){h("PMS_JT","",-1);try{a=a.match(/{["']s["']:(\d+),["']r["']:["']([\s\S]+)["']}/),a=a&&a[1]&&a[2]?{s:parseInt(a[1]),r:a[2]}:{}}catch(c){a={}}a.r&&b.referrer.replace(/#.*/,"")!=a.r||alog("speed.set","wt",a.s)}}if(a.alogObjectConfig){var k=a.alogObjectConfig.sample,l=a.alogObjectConfig.rand;d="https:"===a.location.protocol?"https://fex.bdstatic.com"+d:"http://fex.bdstatic.com"+d,k&&l&&l>k||(g(function(){alog("speed.set","lt",+new Date),e=b.createElement(c),e.async=!0,e.src=d+"?v="+~(new Date/864e5)+~(new Date/864e5),f=b.getElementsByTagName(c)[0],f.parentNode.insertBefore(e,f)}),j())}}(window,document,"script","/hunter/alog/dp.min.js");
</script>
</html>

<class 'NoneType'>
None

Process finished with exit code 0

'''