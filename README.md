<!DOCTYPE html>
<html lang="zh-cn">
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="referrer" content="origin" />
    <meta property="og:description" content="Django 开发个人博客全过程（未完） 一、建立项目 建立虚拟环境：python -m venv&#x2B;虚拟环境名 激活虚拟环境：虚拟环境名\Scripts\activate 安装Django:解决安装超" />
    <meta http-equiv="Cache-Control" content="no-transform" />
    <meta http-equiv="Cache-Control" content="no-siteapp" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <title>Django的使用 - AI大白学AI - 博客园</title>
    <link id="favicon" rel="shortcut icon" href="//common.cnblogs.com/favicon.ico?v=20200522" type="image/x-icon" />

    <link rel="stylesheet" href="/css/blog-common.min.css?v=KCO3_f2W_TC__-jZ7phSnmoFkQuWMJH2yAgA16eE3eY" />
    <link id="MainCss" rel="stylesheet" href="/skins/classic/bundle-classic.min.css?v=LNjaeqzfaVENCz5baMYjJ-wfGY4ICdlMQpBppQoyWBg" />

    <link id="mobile-style" media="only screen and (max-width: 767px)" type="text/css" rel="stylesheet" href="/skins/classic/bundle-classic-mobile.min.css?v=ADiCwO2hOTdd5yYidcx7eob7ix2VJI4o_TXjEycTHjs" />

    <link type="application/rss+xml" rel="alternate" href="https://www.cnblogs.com/qsj-python/rss" />
    <link type="application/rsd+xml" rel="EditURI" href="https://www.cnblogs.com/qsj-python/rsd.xml" />
    <link type="application/wlwmanifest+xml" rel="wlwmanifest" href="https://www.cnblogs.com/qsj-python/wlwmanifest.xml" />
    <script src="https://common.cnblogs.com/scripts/jquery-2.2.0.min.js"></script>
    <script src="/js/blog-common.min.js?v=6bwfCY2e02dLOXNW99G2BHZkYFmw9QyYTWeJ-W-sudo"></script>
    <script>
        var currentBlogId = 604984;
        var currentBlogApp = 'qsj-python';
        var cb_enable_mathjax = false;
        var isLogined = true;
        var skinName = 'classic';
    </script>

</head>
<body>
    <a name="top"></a>

    <table align="center" width="98%" cellspacing="0" cellpadding="0" border="0" style="margin-top:10px">
<tr>
	<td valign=top width="70%" style="padding:0">
		<table align="center" width="100%" height="90" cellspacing="0" cellpadding="5" border="0" bgcolor="white">
		<tr>
			<td class="banner">

<div id="header">
	<span>
		[AI大白学AI](https://www.cnblogs.com/qsj-python/)

		<div class="sub">

</div>
	</span>
</div>

			</td>
		</tr>
		</table>
		<table align="center" width="100%" height="90" cellspacing="0" cellpadding="5" border="0" bgcolor="white" class="index">
		<tr>
			<td class="main">
			<div id="post_detail">
<div class="block">

# 
[Django的使用](https://www.cnblogs.com/qsj-python/p/12920673.html)

	<div class="post">
		<div class="postcontent">

<div id="cnblogs_post_body" class="blogpost-body ">

# <span style="font-family: 楷体; font-size: 18pt;">**Django 开发个人博客全过程（未完）**</span>

## 一、<span style="font-family: 宋体;">建立项目</span>

1.  <span style="font-family: 宋体;">建立虚拟环境：</span>python -m &nbsp;venv+<span style="font-family: 宋体;">虚拟环境名</span>
2.  <span style="font-family: 宋体;">激活虚拟环境：虚拟环境名</span>\Scripts\activate
3.  <span style="font-family: 宋体;">安装</span>Django:<span style="font-family: 宋体;">解决安装超时的方法</span>

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;　　1<span style="font-family: 宋体;">）直接复制网站下载 </span>

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 2<span style="font-family: 宋体;">）</span><span style="font-family: Arial;">pip&nbsp; --default-timeout=</span><span style="font-family: 宋体;">延长的时间 </span><span style="font-family: Arial;">install ...</span>

　　4.<span style="font-family: 宋体;">利用</span><span style="font-family: Arial;">django</span><span style="font-family: 宋体;">创建项目：</span><span style="font-family: Arial;">django-admin startobject+</span><span style="font-family: 宋体;">项目名</span>

　　5.<span style="font-family: 宋体;">创建</span><span style="font-family: Arial;">SQLite</span><span style="font-family: 宋体;">数据库：</span><span style="font-family: Arial;">python manage.py migrate</span>

　　6.<span style="font-family: 宋体;">运行查看项目：</span><span style="font-family: Arial;">python manage.py &nbsp;runserver</span>

&nbsp;

## <span style="font-family: 宋体;">二、创建应用程序APP：</span>

　　1.<span style="font-family: 宋体;">定义模型 &nbsp;</span><span style="font-family: Arial;">def __str__(self): &nbsp;#</span><span style="font-family: 宋体;">该方法的调用用于显示模型</span>

　　2.<span style="font-family: 宋体;">激活模型：设置</span><span style="font-family: Arial;">settings.py </span><span style="font-family: 宋体;">向</span><span style="font-family: Arial;">INSTALL_APP</span><span style="font-family: 宋体;">加入相应的应用程序</span>

　　3.<span style="font-family: 宋体;">让</span><span style="font-family: Arial;">Django</span><span style="font-family: 宋体;">迁移修改数据库：</span><span style="font-family: Arial;">python manage.py makemigrations+</span><span style="font-family: 宋体;">项目名</span>

　　4.Django<span style="font-family: 宋体;">管理网站</span>

　　　　1<span style="font-family: 宋体;">）创建超级用户：</span><span style="font-family: Arial;">python manage.py createsuperuser</span>

　　　　2<span style="font-family: 宋体;">）向管理网站注册模型分为两步：Ⅰ、</span>&nbsp;from <span style="font-family: 宋体;">应用名</span><span style="font-family: Arial;">.models import </span><span style="font-family: 宋体;">类</span>&nbsp;

　　　　　　　　　　　　　　　　　　　&nbsp; Ⅱ、admin.site.register(<span style="font-family: 宋体;">类名</span><span style="font-family: Arial;">)</span>

　　5.models.Model : &nbsp;&nbsp;django<span style="font-family: 宋体;">中一个定义了模型基本功能的类</span>

　　6.Django shell

　　　　1)<span style="font-family: 宋体;">启动</span><span style="font-family: Arial;">python</span><span style="font-family: 宋体;">解释器：</span><span style="font-family: Arial;">python manage.py shell</span>

　　　　2<span style="font-family: 宋体;">）获取模型中的实例：</span><span style="font-family: Arial;">from </span><span style="font-family: 宋体;">某模块 </span><span style="font-family: Arial;">import </span><span style="font-family: 宋体;">类，&nbsp;</span>&nbsp;<span style="font-family: 宋体;">类</span>.objects.all()

&nbsp;

　　　　3）<span style="font-family: 宋体;">获取实例中的元素：</span>msgs = <span style="font-family: 宋体;">类</span><span style="font-family: Arial;">.objects.all()</span>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For msg in msgs:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print(msg.id, msg)

　　　　4<span style="font-family: 宋体;">）</span><span style="font-family: 宋体;">外键</span>Foreignkey<span style="font-family: 宋体;">相关联的实例</span><span style="font-family: 宋体;">可以直接用相关模型的</span><span style="font-family: 宋体;">小写名称</span>+<span style="font-family: 宋体;">下划线</span>+set<span style="font-family: 宋体;">来获取数据</span>

&nbsp;

### <span style="font-family: 宋体;">三、创建网页</span>

　　1.<span style="font-family: 宋体;">映射</span><span style="font-family: Arial;">URL</span>

　　　　1) path<span style="font-family: 宋体;">不是不能用正则而是要调用</span><span style="font-family: Arial;">django.urls.re_path()</span><span style="font-family: 宋体;">函数，来使用正则。</span>

　　2.<span style="font-family: 宋体;">编写视图</span>

　　3.<span style="font-family: 宋体;">编写模板</span>

　　4.<span style="font-family: 宋体;">模板继承</span>

&nbsp;

&nbsp;

## 四、<span style="font-family: 宋体;">用户账户</span>:user

1.  HttpResponseRedirect() <span style="font-family: 宋体;">和 </span><span style="font-family: Arial;">reverse()</span>
2.  <span style="font-family: 宋体;">在</span>Django2.0<span style="font-family: 宋体;">中内置登陆视图不再是函数，而是类，位置在</span><span style="font-family: Arial;">django.contrib.auth.views</span>&nbsp;import LoginView

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; from django.contrib.auth.views import LoginView

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; urlpatterns = [

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;#<span style="font-family: 宋体;">登录界面 &nbsp;</span><span style="font-family: Arial;">LoginView.as_view</span><span style="font-family: 宋体;">后面要加上</span><span style="font-family: Arial;">()</span>

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;url(r'^login/$',LoginView.as_view(template_name='users/login.html'),name='login')]

&nbsp;　　3.<span style="font-family: 宋体;">登陆功能的实现</span>

<span style="font-family: 宋体;">　　</span><span style="font-family: 宋体;">4.注销功能的实现</span>

<span style="font-family: 宋体;">　　</span><span style="font-family: 宋体;">5.注册功能的实现</span>

<span style="font-family: 宋体;">　　</span><span style="font-family: 宋体;">6.</span>{% if is_usercreationform&nbsp;%} <span style="font-family: 宋体;">身份验证</span>

　　7.authenticate,login,logout

　　8.{% csrf_token %}&nbsp;:<span style="font-family: 宋体;">跨站请求伪造</span>

　　9.{{ form.as_p }}&nbsp;:<span style="font-family: 宋体;">让</span><span style="font-family: Arial;">Django</span><span style="font-family: 宋体;">自动创建显示表单所需的全部字段</span>

<span style="font-family: 宋体;">　　</span><span style="font-family: 宋体;">10.让用户拥有自己的数据</span>

<span style="font-family: 宋体;">　　</span><span style="font-family: 宋体;">11.将数据关联到特定的用户：Ⅰ、设置外键</span>owner = models.Foreignkey(User)

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Ⅱ、<span style="font-family: 宋体;">用过滤器</span>objects.filter(owner=request.user)

　　12.django.contrib.auth.decorators import login_required(<span style="font-family: 宋体;">装饰器</span><span style="font-family: Arial;">)</span>

　　13.@login_required<span style="font-family: 宋体;">装饰器：一种放在函数定义前面的指令，只允许已登录的用户访问。</span>

<span style="font-family: 宋体;">　　</span><span style="font-family: 宋体;">14.了解</span>django.contrib.auth<span style="font-family: 宋体;">模块里有什么</span>:

<span style="font-family: 宋体;">　　15.报错</span>__init__() missing 1 required positional argument: 'on_delete'<span style="font-family: 宋体;">的原因：</span> <span style="font-family: 宋体;">在</span>django2.0<span style="font-family: 宋体;">后，定义外键和一对一关系的时候需要加</span><span style="font-family: Arial;">on_delete=models.CASCADE</span><span style="font-family: 宋体;">（级联删除，避免关联错误）选项，此参</span> <span style="font-family: 宋体;">数为了避免两个表里的数据不一致问题，不然会报错</span>

<span style="font-family: 宋体;">　　</span><span style="font-family: 宋体;">16.重新定向或是固定定向到某页面：在</span>settings.py<span style="font-family: 宋体;">文件设置：</span><span style="font-family: Arial;">LOGIN_URL=</span>&rsquo;/users/login/&rsquo;<span style="font-family: 宋体;">一般为登录页面</span>

&nbsp;

&nbsp;

## 第五、<span style="font-family: 宋体;">设置样式</span>

1.  <span style="font-family: 宋体;">熟悉应用程序</span>django-bootstrap:
2.  Settings<span style="font-family: 宋体;">设置 &nbsp;</span>BOOTSTRAP3 = {'include_jquery':True,}: <span style="font-family: 宋体;">这样能让能够使用</span><span style="font-family: Arial;">Bootstrap</span><span style="font-family: 宋体;">模板的一些交互式元素，无需手工下载</span><span style="font-family: Arial;">jQuery</span><span style="font-family: 宋体;">并将其放到正确的地方。</span>
3.  <span style="font-family: 宋体;">使用</span>jumbotron<span style="font-family: 宋体;">（超大屏样式）设置样式：</span>
</div>
<div id="MySignature"></div>
<div class="clear"></div>
<div id="blog_post_info_block">
    <div id="blog_post_info"></div>
    <div class="clear"></div>
    <div id="post_next_prev"></div>
</div>
		</div>
		<div class="itemdesc">
			发表于 
<span id="post-date">2020-05-20 00:45</span>&nbsp;
[AI大白学AI](https://www.cnblogs.com/qsj-python/)&nbsp;
阅读(<span id="post_view_count">...</span>)&nbsp;
评论(<span id="post_comment_count">...</span>)&nbsp;
[编辑](https://i.cnblogs.com/EditPosts.aspx?postid=12920673)&nbsp;
[收藏](javascript:void(0))
		</div>
	</div>
	<div class="seperator">&nbsp;</div>

<script src="https://common.cnblogs.com/highlight/9.12.0/highlight.min.js"></script>
<script>markdown_highlight();</script>
<script>
    var allowComments = true, cb_blogId = 604984, cb_blogApp = 'qsj-python', cb_blogUserGuid = 'bc10f5bd-5f6f-408b-2369-08d7fbd22d6e';
    var cb_entryId = 12920673, cb_entryCreatedDate = '2020-05-20 00:45', cb_postType = 1; 
    loadViewCount(cb_entryId);
    loadSideColumnAd();
</script><a name="!comments"></a>
<div id="blog-comments-placeholder"></div>
<script>
    var commentManager = new blogCommentManager();
    commentManager.renderComments(0);
</script>

<div id="comment_form" class="commentform">
    <a name="commentform"></a>
    <div id="divCommentShow"></div>
    <div id="comment_nav"><span id="span_refresh_tips"></span>[刷新评论](javascript:void(0);)[刷新页面](#)[返回顶部](#top)</div>
    <div id="comment_form_container"></div>
    <div class="ad_text_commentbox" id="ad_text_under_commentbox"></div>
    <div id="ad_t2"></div>
    <div id="opt_under_post"></div>
    <script async="async" src="https://www.googletagservices.com/tag/js/gpt.js"></script>
    <script>
        var googletag = googletag || {};
        googletag.cmd = googletag.cmd || [];
    </script>
    <script>
        googletag.cmd.push(function () {
            googletag.defineSlot("/1090369/C1", [300, 250], "div-gpt-ad-1546353474406-0").addService(googletag.pubads());
            googletag.defineSlot("/1090369/C2", [468, 60], "div-gpt-ad-1539008685004-0").addService(googletag.pubads());
            googletag.pubads().enableSingleRequest();
            googletag.enableServices();
        });
    </script>
    <div id="cnblogs_c1" class="c_ad_block">
        <div id="div-gpt-ad-1546353474406-0" style="height:250px; width:300px;"></div>
    </div>
    <div id="under_post_news"></div>
    <div id="cnblogs_c2" class="c_ad_block">
        <div id="div-gpt-ad-1539008685004-0" style="height:60px; width:468px;"></div>
    </div>
    <div id="under_post_kb"></div>
    <div id="HistoryToday" class="c_ad_block"></div>
    <script type="text/javascript">
        fixPostBody();
        deliverBigBanner();
        deliverAdT2();
        deliverAdC1();
        deliverAdC2();
        loadNewsAndKb();
        loadBlogSignature();
LoadPostCategoriesTags(cb_blogId, cb_entryId);        LoadPostInfoBlock(cb_blogId, cb_entryId, cb_blogApp, cb_blogUserGuid);
        GetPrevNextPost(cb_entryId, cb_blogId, cb_entryCreatedDate, cb_postType);
        loadOptUnderPost();
        GetHistoryToday(cb_blogId, cb_blogApp, cb_entryCreatedDate);
    </script>
</div></div>
</div>

			</td>
		</tr>
		</table>
	</td>
	<td width=10>&nbsp;</td>
	<td valign=top>
		<table align="center" width="100%" height="90" cellspacing="0" cellpadding="5" border="0" bgcolor="white">
		<tr>
			<td class=banner>

			<table width="100%" height="200">
			<tr>
				<td><div id="blog-calendar" style="display:none"></div><script>loadBlogDefaultCalendar();</script></td>
			</tr>
			</table>

<div id="sidebar_news" class="newsItem">
            <script>loadBlogNews();</script>
</div>

<div id="sidebar_ad"></div>	

# &nbsp;导航

*   [
博客园](https://www.cnblogs.com/)

*   [
首页](https://www.cnblogs.com/qsj-python/)

*   [
新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)

*   [新文章](https://i.cnblogs.com/EditArticles.aspx?opt=1)

*   [
联系](https://msg.cnblogs.com/send/AI%E5%A4%A7%E7%99%BD%E5%AD%A6AI)
*   [
订阅](javascript:void(0))
[
    ![订阅](/skins/classic/images/xml.gif)
](https://www.cnblogs.com/qsj-python/rss/)
*   [
管理](https://i.cnblogs.com/)

# &nbsp;统计

*   随笔：1
*   文章：0
*   评论：0
*   引用：0

				<div id="blog-sidecolumn"></div>
                    <script>loadBlogSideColumn();</script>

			<div class="footer">
	Powered by: [博客园](http://www.cnblogs.com)

	Copyright &copy; 2020 AI大白学AI

<span id="poweredby">Powered by .NET Core on Kubernetes</span>

</div>

			</td>
		</tr>
		</table>
	</td>
</tr>
</table>

</body>
</html>
