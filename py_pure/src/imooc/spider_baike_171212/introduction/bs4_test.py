import re
from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="net://example.com/elsie" class="sister" id="link1">Elsie中文</a>,
<a href="net://example.com/lacie" class="sister" id="link2">Lacie</a> and
<div class="test"><a href="net://example.com/tillie" class="sister" id="link3">Tillie</a></div>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

liaoxuefeng = """<!DOCTYPE html>
<html xmlns:itranswarp="net://www.itranswarp.com/" xmlns:wb="net://open.weibo.com/wb">
<!--

-->
<head>
    <meta charset="utf-8" />
    <title>Python教程 - 廖雪峰的官方网站</title>
    <meta name="viewport" content="width=device-width" />
    <meta name="keywords" content="javascript,node,jquery,git,python,java,sql,linux,ios,android,教程,软件,编程,开发,运维,云计算,网络,互联网" />
    <meta name="description" content="研究互联网产品和技术，提供原创中文精品教程" />
    <meta property="x-nav" content=" /wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000 " />
    <link rel="alternate" href="/feed" title="廖雪峰的官方网站" type="application/rss+xml" />
    
    <meta property="og:type" content="article" />
    <meta property="og:url" content="net://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000" />
    <meta property="og:title" content="Python教程" />
    <meta property="og:description" content="小白的Python新手教程，基于最新的Python 3.6！" />
    <meta property="og:image" content="https://cdn.liaoxuefeng.com/cdn/files/attachments/001431608955727f25be118770e460fad1296261e01213d000/l" />
    <meta property="og:tag" content="python" />

    
    <link rel="stylesheet" href="https://cdn.liaoxuefeng.com/cdn/static/themes/default/css/all.css?v=4edf87a" />
    
    <!--[if lt IE 9]>
    <link rel="stylesheet" href="/static/themes/default/css/ie.css?v=4edf87a" />
    <![endif]-->
    
    <script src="https://cdn.liaoxuefeng.com/cdn/static/themes/default/js/all.js?v=4edf87a"></script>
    
    <script id="tplComment" type="text/plain">
        <div class="uk-comment">
            <div class="uk-comment-header" style="margin-bottom:0">
                <a target="_blank" href="/user/{ user.id }"><img class="uk-comment-avatar uk-border-circle x-avatar" src="{ user.image_url }" width="50" height="50" alt=""></a>
                <h4 class="uk-comment-title"><a target="_blank" href="/discuss/{ board_id }/{ id }">{ name }</a></h4>
                <div class="uk-comment-meta"><a target="_blank" href="/user/{ user.id }">{ user.name }</a> created at { created_at.toSmartDate() }, Last updated at { updated_at.toSmartDate() }</div>
            </div>
            <div class="uk-comment-body x-auto-content">
                { content|safe }
            </div>
        </div>
    </script>

    <script id="tplCommentReply" type="text/plain">
        <div class="uk-comment">
            <div class="uk-comment-header" style="margin-bottom:0">
                <a target="_blank" href="/user/{ user.id }"><img class="uk-comment-avatar uk-border-circle x-avatar" src="{ user.image_url }" width="50" height="50" alt=""></a>
                <div class="uk-comment-meta"><a target="_blank" href="/user/{ user.id }">{ user.name }</a></div>
                <div class="uk-comment-meta">Created at { created_at.toSmartDate() }, Last updated at { updated_at.toSmartDate() }</div>
            </div>
            <div class="uk-comment-body x-auto-content">
                { content|safe }
            </div>
        </div>
    </script>

    <script id="tplCommentInfo" type="text/plain">
        <li>
            <div class="x-comment-info">
                <hr>
                <a target="_blank" class="uk-button uk-button-small" href="/discuss/{ board_id }/{ id }"><i class="uk-icon-list-ul"></i> 全部讨论</a>
                &nbsp;
                <a target="_blank" class="uk-button uk-button-small" href="/discuss/{ board_id }/{ id }#reply"><i class="uk-icon-reply"></i> 回复</a>
            </div>
        </li>
    </script>

    <script id="tplCommentArea" type="text/plain">
        <div class="x-display-if-signin">
            <p><button id="comment-make-button" type="button" class="uk-button uk-button-primary"><i class="uk-icon-comment"></i> 发表评论</button></p>
            <form id="comment-form" class="uk-form" style="display:none;">
                <fieldset>
                    <div class="uk-alert uk-alert-danger" style="display:none"></div>
                    <div class="uk-form-row">
                        <label>标题:</label>
                    </div>
                    <div class="uk-form-row">
                        <input type="text" name="name" maxlength="100" style="width:100%">
                    </div>
                    <div class="uk-form-row">
                        <label>内容:</label>
                    </div>
                    <div class="uk-form-row x-textarea">
                    </div>
                    <div class="uk-form-row">
                        <button type="submit" class="uk-button uk-button-primary"><i class="uk-icon-check"></i> 发布</button>
                        &nbsp;&nbsp;
                        <button type="button" class="uk-button x-cancel"><i class="uk-icon-close"></i> 取消</button>
                    </div>
                </fieldset>
            </form>
        </div>
    </script>

    <style id="x-doc-style">
        .x-display-none { display: none; }

        .x-display-if-signin { display: none; }

    </style>
    <script>
        // global variables:
        var g_time = parseFloat('1513481386946');
        var g_signins = JSON.parse('[{"id":"weibo","icon":"weibo","name":"使用新浪微博登录"}]');
//
        var g_user = null;
//
        var g_ads = JSON.parse(decodeURIComponent('%7B%22a%22%3A%7B%22name%22%3A%22A%22%2C%22width%22%3A336%2C%22height%22%3A280%2C%22auto_fill%22%3A%22%3Cins%20class%3D%5C%22adsbygoogle%5C%22%20style%3D%5C%22display%3Ainline-block%3Bwidth%3A336px%3Bheight%3A280px%5C%22%20data-ad-client%3D%5C%22ca-pub-6727358730461554%5C%22%20data-ad-slot%3D%5C%228492060710%5C%22%3E%3C%2Fins%3E%5Cn%3Cscript%3E%5Cn(adsbygoogle%20%3D%20window.adsbygoogle%20%7C%7C%20%5B%5D).push(%7B%7D)%3B%5Cn%3C%2Fscript%3E%22%2C%22num_auto_fill%22%3A2%2C%22adperiods%22%3A%5B%7B%22user%22%3A%22%E7%94%A8%E6%88%B78316456992%22%2C%22admaterials%22%3A%5B%7B%22image%22%3A%22%2Ffiles%2Fattachments%2F00151074766666011d09de79f2f450a884274d263816b19000%2F0%22%2C%22weight%22%3A100%2C%22keywords%22%3A%22%E5%89%8D%E7%AB%AF%2Cjs%2Cvue%2Creact%2Cangular%22%2C%22url%22%3A%22https%3A%2F%2Fwww.zhufengpeixun.cn%2Fmain%2Fcourse%2Findex.html%3Fref%3Dliaoxuefeng.com%22%7D%5D%7D%2C%7B%22user%22%3A%22%E9%BA%A6%E5%AD%90%E5%AD%A6%E9%99%A2%22%2C%22admaterials%22%3A%5B%7B%22image%22%3A%22%2Ffiles%2Fattachments%2F001513132151055db554981f3844257b3cac60819cc9373000%2F0%22%2C%22weight%22%3A100%2C%22keywords%22%3A%22%22%2C%22url%22%3A%22http%3A%2F%2Fm.maiziedu.com%2Fland%2Fpages%2Fpython%2Flxf01%22%7D%5D%7D%2C%7B%22user%22%3A%22%E7%A8%80%E5%9C%9F%E6%8E%98%E9%87%91%22%2C%22admaterials%22%3A%5B%7B%22image%22%3A%22%2Ffiles%2Fattachments%2F00150839838075647d7b0cd1ca54b32b46eee76a70deb63000%2F0%22%2C%22weight%22%3A100%2C%22keywords%22%3A%22%22%2C%22url%22%3A%22https%3A%2F%2Fjuejin.im%3Futm_source%3Dliaoxuefeng%26utm_medium%3Dbanner1%26utm_campaign%3Dpersonal%22%7D%2C%7B%22image%22%3A%22%2Ffiles%2Fattachments%2F001508398629669f436b375fe9749449b2106e7a0146a94000%2F0%22%2C%22weight%22%3A100%2C%22keywords%22%3A%22%22%2C%22url%22%3A%22https%3A%2F%2Fjuejin.im%3Futm_source%3Dliaoxuefeng%26utm_medium%3Dbanner2%26utm_campaign%3Dpersonal%22%7D%5D%7D%2C%7B%22user%22%3A%22%E9%A9%AC%E5%93%A5Linux%E5%9F%B9%E8%AE%AD%22%2C%22admaterials%22%3A%5B%7B%22image%22%3A%22%2Ffiles%2Fattachments%2F00151194943983916dbf52218ed403d8a51a4541b215756000%2F0%22%2C%22weight%22%3A4%2C%22keywords%22%3A%22%E9%A9%AC%E5%93%A5Python%22%2C%22url%22%3A%22http%3A%2F%2Fwww.magedu.com%2Fkczx%2Fpythonkf.html%3Fwztf_liaoxuefeng_2017.11.29%22%7D%5D%7D%5D%7D%2C%22b%22%3A%7B%22name%22%3A%22B%22%2C%22width%22%3A300%2C%22height%22%3A600%2C%22auto_fill%22%3A%22%3Cins%20class%3D%5C%22adsbygoogle%5C%22%20style%3D%5C%22display%3Ainline-block%3Bwidth%3A300px%3Bheight%3A600px%5C%22%20data-ad-client%3D%5C%22ca-pub-6727358730461554%5C%22%20data-ad-slot%3D%5C%224769867116%5C%22%3E%3C%2Fins%3E%5Cn%3Cscript%3E%5Cn(adsbygoogle%20%3D%20window.adsbygoogle%20%7C%7C%20%5B%5D).push(%7B%7D)%3B%5Cn%3C%2Fscript%3E%22%2C%22num_auto_fill%22%3A1%2C%22adperiods%22%3A%5B%7B%22user%22%3A%22%E4%B8%83%E6%9C%88%E5%9C%A8%E7%BA%BFAI%E5%AE%9E%E9%AA%8C%E5%AE%A4%22%2C%22admaterials%22%3A%5B%7B%22image%22%3A%22%2Ffiles%2Fattachments%2F00151175312421960f1051bbe4e4a78bf934e50aa78b381000%2F0%22%2C%22weight%22%3A100%2C%22keywords%22%3A%22%22%2C%22url%22%3A%22http%3A%2F%2Fwww.julyedu.com%2Fweekend%2Ftrain3%3Ffrom%3Dlxf%22%7D%5D%7D%2C%7B%22user%22%3A%22%E9%BA%A6%E5%AD%90%E5%AD%A6%E9%99%A2%22%2C%22admaterials%22%3A%5B%7B%22image%22%3A%22%2Ffiles%2Fattachments%2F00151209534813570342a5292a94805a82b55c4c49b4181000%2F0%22%2C%22weight%22%3A100%2C%22keywords%22%3A%22%22%2C%22url%22%3A%22http%3A%2F%2Fwww.maiziedu.com%2Fland%2Fai%2F%22%7D%5D%7D%2C%7B%22user%22%3A%22%E5%87%B3%E5%AD%90%E5%AD%A6%E9%99%A2%22%2C%22admaterials%22%3A%5B%7B%22image%22%3A%22%2Ffiles%2Fattachments%2F001511418632447e0f43467fa344e7f878d1518c949deb5000%2F0%22%2C%22weight%22%3A100%2C%22keywords%22%3A%22python%2Cpython%E5%85%A8%E6%A0%88%E5%BC%80%E5%8F%91%EF%BC%8C%E5%87%B3%E5%AD%90%E5%AD%A6%E9%99%A2%22%2C%22url%22%3A%22http%3A%2F%2Fwww.dengzixy.com%2F%22%7D%5D%7D%5D%7D%7D'));
        var meta_keywords = $('meta[property="og:tag"]').attr('content');
        if (meta_keywords) {
            meta_keywords = meta_keywords.toLowerCase().split(',');
            _.mapObject(g_ads, function (adslot, adkey) {
                _.map(adslot.adperiods, function (adp) {
                    var matched_adms = _.filter(adp.admaterials, function (adm) {
                        var ks = adm.keywords.toLowerCase().split(',');
                        // ad keywords = [a, b, c, d]
                        // meta keywords = [b, c]
                        var ms = _.filter(meta_keywords, function (mkey) {
                            return ks.indexOf(mkey) >= 0;
                        });
                        return ms.length > 0;
                    });
                    if (matched_adms.length > 0) {
                        adp.admaterials = matched_adms;
                    }
                });
            });
        }
        $(function () {
            var fnRandom = function (adms) {
                if (adms.length === 1) {
                    return adms[0];
                }
                var
                    weights = _.map(adms, function (m) {
                        return m.weight;
                    }),
                    total_weights = _.reduce(weights, function (ax, w) {
                        return ax + w;
                    }, 0),
                    rnd = Math.random(),
                    ws = 0,
                    i,
                    hit;
                for (i=0; i<weights.length; i++) {
                    ws = ws + weights[i];
                    if (rnd < ws / total_weights) {
                        return adms[i];
                    }
                }
                return adms[0];
            };
            _.mapObject(g_ads, function (ad, k) {
                _.map(ad.adperiods, function (adp) {
                    if (adp.admaterials.length === 0) {
                        add_sponsor('#x-sponsor-' + k, ad.width, ad.height, adp.user, 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIAAAAAkCAMAAAB2bcIBAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyNpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuNS1jMDE0IDc5LjE1MTQ4MSwgMjAxMy8wMy8xMy0xMjowOToxNSAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENDIChNYWNpbnRvc2gpIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOjE0NDhCRDA3QTM3MjExRTc4QjI0RjRCQjQzOTgwRDc3IiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOjE0NDhCRDA4QTM3MjExRTc4QjI0RjRCQjQzOTgwRDc3Ij4gPHhtcE1NOkRlcml2ZWRGcm9tIHN0UmVmOmluc3RhbmNlSUQ9InhtcC5paWQ6MTQ0OEJEMDVBMzcyMTFFNzhCMjRGNEJCNDM5ODBENzciIHN0UmVmOmRvY3VtZW50SUQ9InhtcC5kaWQ6MTQ0OEJEMDZBMzcyMTFFNzhCMjRGNEJCNDM5ODBENzciLz4gPC9yZGY6RGVzY3JpcHRpb24+IDwvcmRmOlJERj4gPC94OnhtcG1ldGE+IDw/eHBhY2tldCBlbmQ9InIiPz5Adyw0AAAADFBMVEXm5uazs7NdXV3///8WehxTAAAABHRSTlP///8AQCqp9AAAAaVJREFUeNrslsuWwyAMQyXy//88LX7JhEw7q9mQRQ8QEBcjO8X1zw8OwAE4AAdA2xzvh7Nj7eq/RuYQ+STl71PR1ayPlBt4AkCbUgBGgBwwySLjsoCLGheAwT0A7Hz0GZwdOxVCoPpXncUA2F+L2pTD6HobAAor8lwxzlgHV2yXhYoI6zXiIjiXse/zCFA7CgCK25sVzABw2dew8FrzbwAgNQJzqa6ydnOLATkw2XeZbwoATwDoFu8RUEE4AJluCQ+gbarAX0QgjEo2ALtDiiBmTN8/Qy+LS45cewA+mjAzOc+VTxe8IgJuh4DLRFVHRMS+SEOFYANQR8gVjLoe9FqGbQT2lUhMSGqIow6Q68UxI2DJNwHMueqZmweyDjxEoKCpgVUoNZgNTF2fri4XYPQswMdC5Dt0gF55x5W3TA8qxq1u1IZrIcJzGkbRvc/z/ICU4iCrNHQTsLISVco/Afxiu2vzcWofHbSvDe9q3xQiWYM7qOzAbplI7MxCbtQ6QHPXkoMMN2dD/y/IYCZNzUQmzU1tvlvnn79kB+AAHIADMJ8fAQYAbSgvpXjD4xEAAAAASUVORK5CYII=', '/');
                        return;
                    }
                    var hit = fnRandom(adp.admaterials);
                    add_sponsor('#x-sponsor-' + k, ad.width, ad.height, adp.user, 'https://cdn.liaoxuefeng.com/cdn'+ hit.image, hit.url);
                });
                var i;
                for (i=0; i<ad.num_auto_fill; i++) {
                    add_sponsor('#x-sponsor-' + k, ad.width, ad.height, ad.auto_fill);
                }
            });
        });
    </script>
    <script>
        (function () {
            eval(decodeURIComponent('%69f%28%21get%43%6F%6F%6B%69%65(%27%61tsp%27))%73%65%74C%6F%6F%6B%69%65(%27%61tsp%27%2C%20%271513481386946%5F%27%2Bnew%20Date%28%29.getTime%28%29%2C%20580%29%3B'));
        })();
    </script>


    
    
<style>
.x-wiki-visible {
    display: block;
}
</style>

<script>
loadComments('0014316089557264a6b348958f449949df42a6d3a2e542c000');

var
    comment_type = 'wiki',
    comment_ref_id = '0014316089557264a6b348958f449949df42a6d3a2e542c000',
    comment_tag = 'python';

function onAuthSuccess() {
    initCommentArea(comment_type, comment_ref_id, comment_tag);
}

$(function () {
    if (g_user !== null) {
        initCommentArea(comment_type, comment_ref_id, comment_tag);
    }
});

$(function () {
    $('#0014316089557264a6b348958f449949df42a6d3a2e542c000').addClass('uk-active');
    $('#off-0014316089557264a6b348958f449949df42a6d3a2e542c000').addClass('uk-active');
    // expand current:
    expandActiveNode();
    // add prev, next:
    $('div.x-wiki-prev-next').css('padding-left', '15px').css('padding-right', '15px');
    var prev = getPrevNode();
    var next = getNextNode();
    if (prev) {
        $('div.x-wiki-prev-next').append("<a href=\"" + prev.find("a").attr("href") + "\"><i class=\"uk-icon-chevron-left\"></i> 上一页</a>");
    }
    if (next) {
        $('div.x-wiki-prev-next').append("<a href=\"" + next.find("a").attr("href") + "\" class=\"uk-float-right\">下一页 <i class=\"uk-icon-chevron-right\"></i></a>");
    }
    $('div.x-wiki-prev-next').after('<hr>');
});

function getPrevNode() {
    var activeNode = $('#0014316089557264a6b348958f449949df42a6d3a2e542c000');
    var prev = activeNode.prev('div');
    var lastChild;
    if (prev.get(0)) {
        lastChild = prev.find('div:last');
        if (lastChild.get(0)) {
            return lastChild;
        }
        return prev;
    }
    prev = activeNode.parent('div');
    if (prev.get(0)) {
        return prev;
    }
    return null;
}

function getNextNode() {
    var activeNode = $('#0014316089557264a6b348958f449949df42a6d3a2e542c000');
    var next = activeNode.find('div:first');
    var node;
    if (next.get(0)) {
        return next;
    }
    next = activeNode.next('div');
    if (next.get(0)) {
        return next;
    }
    node = activeNode;
    for (;;) {
        node = node.parent('div');
        if (node.get(0)) {
            next = node.next('div');
            if (next.get(0)) {
                return next;
            }
        } else {
            break;
        }
    }
    return null;
}

function expandActiveNode() {
    var activeNode = $('#0014316089557264a6b348958f449949df42a6d3a2e542c000');
    for (;;) {
        i = activeNode.find('i').get(0);
        if (i) {
            expandWikiNode(i);
        }
        activeNode = activeNode.parent();
        if (! activeNode.is('div')) {
            break;
        }
    }
}

function toggleWikiNode(icon) {
    var
        $i = $(icon),
        $div = $i.parent(),
        expand = $div.attr('expand');
    if (expand === 'true') {
        collapseWikiNode(icon);
    } else {
        expandWikiNode(icon);
    }
}

function collapseWikiNode(icon, rec) {
    var
        $i = $(icon),
        $div = $i.parent();
    $div.attr('expand', 'false');
    $i.removeClass('uk-icon-minus-square-o');
    $i.addClass('uk-icon-plus-square-o');
    $div.find('>div').hide();
    if (rec) {
        $div.find('>div>i').each(function () {
            collapseWikiNode(this, rec);
        });
    }
}

function expandWikiNode(icon, rec) {
    var
        $i = $(icon),
        $div = $i.parent();
    $div.attr('expand', 'true');
    $i.removeClass('uk-icon-plus-square-o');
    $i.addClass('uk-icon-minus-square-o');
    $div.find('>div').show();
    if (rec) {
        $div.find('>div>i').each(function () {
            expandWikiNode(this, rec);
        });
    }
}

</script>


<style>
.x-center {
    margin: 0;
}


.x-center {
    margin-left: 316px;
    padding-left: 15px;
}




</style>

<!-- BEGIN custom_header -->
<script src="https://tjs.sjs.sinajs.cn/open/api/js/wb.js" type="text/javascript" charset="utf-8"></script>
<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>

<script>
var CDN = 'https://cdn.webxueyuan.com/cdn';

// add table class:
$(function () {
    $('table').addClass('uk-table');
});

function shareToWeibo() {
    var url = 'net://service.weibo.com/share/share.php?type=button&ralateUid=1658384301&language=zh_cn&appkey=1391944217&searchPic=false&style=full';
    url = url + '&title=' + encodeURIComponent(document.title);
    url = url + '&url=' + encodeURIComponent(location.href);
    url = url + '&pic=' + encodeURIComponent($('meta[property="og:image"]').attr('content'));
    window.open(url, 'share_liaoxuefeng_com', 'top=200,left=400,width=600,height=380,directories=no,menubar=no,toolbar=no,resizable=no');
}

var SHARE_TO_WEIBO = '<p><a href="#0" onclick="shareToWeibo()" class="uk-button uk-button-danger"><i class="uk-icon-weibo"></i> 分享到微博</button></p>';
</script>

<script>
// sql: import alasql
  if (location.pathname.indexOf('/wiki/001508284671805d39d23243d884b8b99f440bfae87b0f4000') === 0) {
    $.ajax({
      url: '//cdn.liaoxuefeng.com/static/js/alasql.js',
      dataType: 'script',
      cache: true,
      success: function () {
        console.log('alasql loaded.');
        alasql.options.joinstar = 'underscore';
        var
          i,
          classes_data = [['一班'], ['二班'], ['三班'], ['四班']],
          students_data = [[1, '小明', 'M', 90], [1, '小红', 'F', 95], [1, '小军', 'M', 88], [1, '小米', 'F', 73], [2, '小白', 'F', 81], [2, '小兵', 'M', 55], [2, '小林', 'M', 85], [3, '小新', 'F', 91], [3, '小王', 'M', 89], [3, '小丽', 'F', 88]];
        alasql('CREATE TABLE classes (id BIGINT NOT NULL AUTO_INCREMENT, name VARCHAR(10) NOT NULL, PRIMARY KEY (id))');
        alasql('CREATE TABLE students (id BIGINT NOT NULL AUTO_INCREMENT, class_id BIGINT NOT NULL, name VARCHAR(10) NOT NULL, gender CHAR(1) NOT NULL, score BIGINT NOT NULL, PRIMARY KEY (id))');
        for (i=0; i<classes_data.length; i++) {
          alasql('INSERT INTO classes (name) VALUES (?)', classes_data[i]);
        }
        for (i=0; i<students_data.length; i++) {
          alasql('INSERT INTO students (class_id, name, gender, score) VALUES (?, ?, ?, ?)', students_data[i]);
        }
      }
    });
  }
</script>

<script>
// git: add app link:
$(function () {
  if (location.pathname.indexOf('/wiki/0013739516305929606dd18361248578c67b8067c8c017b000')===0) {
    $('.x-wiki-info').parent().css('position', 'relative').append('<a href="/webpage/gitapp" target="_blank" style="display:block;width:135px;height:40px;position:absolute;right:10px;top:10px;"><img src="' + CDN + '/static/img/download-on-the-app-store.png" /></a>');
  }
});
</script>

<script>
// add new:
$(function () {
  var img_new = '<img style="position:absolute;right:-10px;top:3px;z-index:999" src="' + CDN + '/files/attachments/001477919415261ebc91072244149e0ab69f60ae2abe39f000/l">';
  $('#ul-navbar a[href="https://www.feiyangedu.com/category/CryptoCurrency"]').parent().append(img_new);
  $('#ul-navbar a[href="https://www.feiyangedu.com/category/JavaSE"]').parent().append(img_new);
});
</script>

<script>
// python 3: add 2.7 link:
$(function () {
  if (location.pathname.indexOf('/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000')===0) {
    $('.x-wiki-info').parent().css('position', 'relative').append('<a href="/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000" target="_blank" style="display:block;position:absolute;right:10px;top:10px;">2.7旧版教程</a>');
  }
});
</script>

<script>
// python 2.7: add py3 link:
$(function () {
  if (location.pathname.indexOf('/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000')===0) {
    $('#main .x-container').prepend('<div class="uk-alert uk-alert-danger">您目前正在学习的2.7版本的Python教程已过期，请立刻前往最新的Python 3 教程：<a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000" class="uk-button uk-button-success">我要学 Python 3</a></div>');
  }
});
</script>

<script>
// add share:
$(function () {
  if (location.pathname.indexOf('/wiki/')===0) {
    $('.x-wiki-content').find('a[href^=net]').attr('target', '_blank');
    if (!window.hurry) {
      $('.x-wiki-content').after('<h3>感觉本站内容不错，读后有收获？</h3><p><a target="_blank" href="/webpage/donate" class="uk-button uk-button-primary"><i class="uk-icon-cny"></i> 我要小额赞助，鼓励作者写出更好的教程</a></p><h3>还可以分享给朋友</h3>' + SHARE_TO_WEIBO);
    } else {
      $('.x-wiki-content').after('<h3>等待时间太久？</h3><p><a target="_blank" href="/webpage/donate" class="uk-button uk-button-primary"><i class="uk-icon-cny"></i> 我要催促作者更新教程</a></p><h3>还可以分享给朋友</h3>' + SHARE_TO_WEIBO);
    }
  }
});
</script>

<script>
// article: add share:
$(function () {
  if (location.pathname.indexOf('/article/')===0) {
    $('.x-article-content').find('a[href^=net]').attr('target', '_blank');
    $('.x-article-content').after('<h3>感觉本站内容不错，读后有收获？</h3><p><a target="_blank" href="/webpage/donate" class="uk-button uk-button-primary"><i class="uk-icon-cny"></i> 我要小额赞助，鼓励作者写出更好的文章</a></p><h3>还可以分享给朋友</h3>' + SHARE_TO_WEIBO);
  }
});
</script>

<script>
// footer:
$(function() {
  $('.x-footer-copyright').find('p').append('<br>由<a target="_blank" href="https://promotion.aliyun.com/ntms/act/ambassador/sharetouser.html?userCode=cz36baxa&productCode=vm&utm_source=cz36baxa">阿里云</a>托管<br><a href="#0" onclick="location.assign(decodeURIComponent(\'moc.36104%fxlksaA3%otliam\'.split(\'\').reverse().join(\'\')))">广告合作</a>');
  $('.x-footer').append('<hr><div style="text-align:center"><p>友情链接: <a href="net://www.shi-ci.com" target="_blank">中华诗词</a> - <a href="https://promotion.aliyun.com/ntms/act/ambassador/sharetouser.html?userCode=cz36baxa&amp;utm_source=cz36baxa" target="_blank">阿里云</a> - <a href="https://bbs.ksyun.com" target="_blank">金山云</a> - <a href="net://mitpress.mit.edu/sicp/full-text/book/book.html" target="_blank">SICP</a> - <a href="net://www.4clojure.com/" target="_blank">4clojure</a></p></div>');
});
</script>

<script>
// tongji:
var _hmt = _hmt || [];
(function () {
  var hm = document.createElement("script");
  hm.src = "//hm.baidu.com/hm.js?2efddd14a5f2b304677462d06fb4f964";
  hm.async = "async";
  var s = document.getElementsByTagName("script")[0]; 
  s.parentNode.insertBefore(hm, s);
})();
</script>

<!-- END custom_header -->
</head>

<body>
    <div class="x-goto-top">
        <div class="x-arrow"></div>
        <div class="x-stick"></div>
    </div>

    <div id="header" class="uk-navbar uk-navbar-attached">
        <div class="uk-container x-container">
            <div class="uk-navbar uk-navbar-attached">
                
                <ul class="uk-navbar-nav uk-visible-small">
                    <li><a href="#0" onclick="UIkit.offcanvas.show('#x-offcanvas-left')">目录</a></li>
                </ul>
                
                <a href="/" class="uk-navbar-brand uk-visible-large">廖雪峰的官方网站</a>
                <a href="/" class="uk-navbar-brand uk-hidden-large"><i class="uk-icon-home"></i></a>
                <ul id="ul-navbar" class="uk-navbar-nav uk-hidden-small">
                    
                    <li><a href="/category/0013738748415562fee26e070fa4664ad926c8e30146c67000">编程</a></li>
                    
                    <li><a href="/category/0013738748248885ddf38d8cd1b4803aa74bcda32f853fd000">读书</a></li>
                    
                    <li><a href="https://www.feiyangedu.com/category/JavaSE">Java教程</a></li>
                    
                    <li><a href="https://www.feiyangedu.com/category/CryptoCurrency">数字货币</a></li>
                    
                    <li><a href="/wiki/001434446689867b27157e896e74d51a89c25cc8b43bdb3000">JavaScript教程</a></li>
                    
                    <li><a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000">Python教程</a></li>
                    
                    <li><a href="/wiki/0013739516305929606dd18361248578c67b8067c8c017b000">Git教程</a></li>
                    
                    <li><a href="/discuss">问答</a></li>
                    
                    <li><a href="/webpage/donate">赞助</a></li>
                    
                    <li class="x-display-none"><a href="/blog/1513481386946">Blog</a></li>
                </ul>
                
                <ul class="uk-navbar-nav uk-visible-small">
                    <li class="uk-parent" data-uk-dropdown>
                        <a href="#0"><i class="uk-icon-navicon"></i></a>
                        <div class="uk-dropdown uk-dropdown-navbar">
                            <ul class="uk-nav uk-nav-navbar">
                                
                                <li><a href="/category/0013738748415562fee26e070fa4664ad926c8e30146c67000">编程</a></li>
                                
                                <li><a href="/category/0013738748248885ddf38d8cd1b4803aa74bcda32f853fd000">读书</a></li>
                                
                                <li><a href="https://www.feiyangedu.com/category/JavaSE">Java教程</a></li>
                                
                                <li><a href="https://www.feiyangedu.com/category/CryptoCurrency">数字货币</a></li>
                                
                                <li><a href="/wiki/001434446689867b27157e896e74d51a89c25cc8b43bdb3000">JavaScript教程</a></li>
                                
                                <li><a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000">Python教程</a></li>
                                
                                <li><a href="/wiki/0013739516305929606dd18361248578c67b8067c8c017b000">Git教程</a></li>
                                
                                <li><a href="/discuss">问答</a></li>
                                
                                <li><a href="/webpage/donate">赞助</a></li>
                                
                            </ul>
                        </div>
                    </li>
                </ul>
                

<!--
                <div class="uk-navbar-content x-hidden-tiny">
                    <form id="form-search" class="uk-form uk-margin-remove uk-display-inline-block">
                        <div class="uk-form-icon">
                            <i class="uk-icon-search"></i>
                            <input type="text" placeholder="Search">
                        </div>
                    </form>
                </div>
-->

                <div class="uk-navbar-flip">
                    <ul class="uk-navbar-nav">
                        <li class="uk-parent x-display-if-signin" data-uk-dropdown>
                            <a href="#0"><i class="uk-icon-user"></i><span class="x-hidden-tiny">&nbsp;</span><span class="x-user-name x-hidden-tiny"></span></a>
                            <div class="uk-dropdown uk-dropdown-navbar">
                                <ul class="uk-nav uk-nav-navbar">
                                    <li><a target="_blank" href="/me/profile"><i class="uk-icon-cog"></i> 个人资料</a></li>
                                    <li class="uk-nav-divider"></li>
                                
                                
                                    <li><a href="/auth/signout"><i class="uk-icon-power-off"></i> 登出</a></li>
                                </ul>
                            </div>
                        </li>
                        <li class="x-display-if-not-signin uk-hidden-small"><a href="javascript:showSignin()"><i class="uk-icon-sign-in"></i> 登录</a></li>
                        <li class="x-display-if-not-signin uk-visible-small"><a href="javascript:showSignin()"><i class="uk-icon-sign-in"></i></a></li>
                    </ul>
                </div>
            </div>
        </div>
    </div><!-- // header -->

    <div id="main">
        <div class="x-placeholder-50"><!-- placeholder --></div>
        <div class="x-placeholder"><!-- placeholder --></div>
        <div class="uk-container x-container">
            <div class="uk-grid">
                <div class="x-body-top uk-width-1-1">
                    <!-- body_top -->
                </div>
                <div class="uk-width-1-1">
                
                    <div class="x-sidebar-left">
                        <div class="x-sidebar-left-top">
                            <!-- sidebar_left_top -->
                        </div>
                        <div class="x-sidebar-left-content">
                            
    <div class="uk-float-right" style="padding-top:5px">
        <a href="#0" onclick="collapseWikiNode($('#x-wiki-index>div>i').get(0), true);expandActiveNode()" style="margin-left:5px"><i class="uk-icon-check-square"></i></a>
        <a href="#0" onclick="expandWikiNode($('#x-wiki-index>div>i').get(0), true)" style="margin-left:5px"><i class="uk-icon-minus-square"></i></a>
        <a href="#0" onclick="collapseWikiNode($('#x-wiki-index>div>i').get(0), true)" style="margin-left:5px"><i class="uk-icon-plus-square"></i></a>
    </div>
    <ul class="uk-nav uk-nav-side">
        <li class="uk-nav-header">目录</li>
    </ul>
    <ul id="x-wiki-index" class="uk-nav uk-nav-side" style="margin-right:-15px;">
        <div id="0014316089557264a6b348958f449949df42a6d3a2e542c000" depth="0" style="position:relative;margin-left:15px;">
            <i onclick="toggleWikiNode(this)" class="uk-icon-plus-square-o" style="position:absolute;margin-left:-1em;padding-top:8px;"></i>
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000" class="x-wiki-index-item">Python教程</a>
            
    
        <div id="001431608990315a01b575e2ab041168ff0df194698afac000" depth="1" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431608990315a01b575e2ab041168ff0df194698afac000" class="x-wiki-index-item">Python简介</a>
            
        </div>
    
        <div id="0014316090478912dab2a3a9e8f4ed49d28854b292f85bb000" depth="1" style="display:none;position:relative;margin-left:15px;">
            
            <i onclick="toggleWikiNode(this)" class="uk-icon-plus-square-o" style="position:absolute;margin-left:-1em;padding-top:8px;"></i>
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014316090478912dab2a3a9e8f4ed49d28854b292f85bb000" class="x-wiki-index-item">安装Python</a>
            
    
        <div id="00143161198846783e33de56d4041058c3dfc7e44ee1203000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143161198846783e33de56d4041058c3dfc7e44ee1203000" class="x-wiki-index-item">Python解释器</a>
            
        </div>
    

            
        </div>
    
        <div id="001431611988455689d4c116b2c4ed6aec000776c00ed52000" depth="1" style="display:none;position:relative;margin-left:15px;">
            
            <i onclick="toggleWikiNode(this)" class="uk-icon-plus-square-o" style="position:absolute;margin-left:-1em;padding-top:8px;"></i>
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431611988455689d4c116b2c4ed6aec000776c00ed52000" class="x-wiki-index-item">第一个Python程序</a>
            
    
        <div id="0014316399410395f704750ee9440228135925a6ca1dad8000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014316399410395f704750ee9440228135925a6ca1dad8000" class="x-wiki-index-item">使用文本编辑器</a>
            
        </div>
    
        <div id="001432523496782e0946b0f454549c0888d05959b99860f000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432523496782e0946b0f454549c0888d05959b99860f000" class="x-wiki-index-item">Python代码运行助手</a>
            
        </div>
    
        <div id="001431643484137e38b44e5925440ec8b1e4c70f800b4e2000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431643484137e38b44e5925440ec8b1e4c70f800b4e2000" class="x-wiki-index-item">输入和输出</a>
            
        </div>
    

            
        </div>
    
        <div id="001431658427513eef3d9dd9f7c48599116735806328e81000" depth="1" style="display:none;position:relative;margin-left:15px;">
            
            <i onclick="toggleWikiNode(this)" class="uk-icon-plus-square-o" style="position:absolute;margin-left:-1em;padding-top:8px;"></i>
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431658427513eef3d9dd9f7c48599116735806328e81000" class="x-wiki-index-item">Python基础</a>
            
    
        <div id="001431658624177ea4f8fcb06bc4d0e8aab2fd7aa65dd95000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431658624177ea4f8fcb06bc4d0e8aab2fd7aa65dd95000" class="x-wiki-index-item">数据类型和变量</a>
            
        </div>
    
        <div id="001431664106267f12e9bef7ee14cf6a8776a479bdec9b9000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431664106267f12e9bef7ee14cf6a8776a479bdec9b9000" class="x-wiki-index-item">字符串和编码</a>
            
        </div>
    
        <div id="0014316724772904521142196b74a3f8abf93d8e97c6ee6000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014316724772904521142196b74a3f8abf93d8e97c6ee6000" class="x-wiki-index-item">使用list和tuple</a>
            
        </div>
    
        <div id="001431675624710bb20e9734ef343bbb4bd64bcd37d4b52000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431675624710bb20e9734ef343bbb4bd64bcd37d4b52000" class="x-wiki-index-item">条件判断</a>
            
        </div>
    
        <div id="001431676242561226b32a9ec624505bb8f723d0027b3e7000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431676242561226b32a9ec624505bb8f723d0027b3e7000" class="x-wiki-index-item">循环</a>
            
        </div>
    
        <div id="00143167793538255adf33371774853a0ef943280573f4d000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143167793538255adf33371774853a0ef943280573f4d000" class="x-wiki-index-item">使用dict和set</a>
            
        </div>
    

            
        </div>
    
        <div id="00143167832686474803d3d2b7d4d6499cfd093dc47efcd000" depth="1" style="display:none;position:relative;margin-left:15px;">
            
            <i onclick="toggleWikiNode(this)" class="uk-icon-plus-square-o" style="position:absolute;margin-left:-1em;padding-top:8px;"></i>
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143167832686474803d3d2b7d4d6499cfd093dc47efcd000" class="x-wiki-index-item">函数</a>
            
    
        <div id="0014316784721058975e02b46cc45cb836bb0827607738d000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014316784721058975e02b46cc45cb836bb0827607738d000" class="x-wiki-index-item">调用函数</a>
            
        </div>
    
        <div id="001431679203477b5b364aeba8c4e05a9bd4ec1b32911e2000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431679203477b5b364aeba8c4e05a9bd4ec1b32911e2000" class="x-wiki-index-item">定义函数</a>
            
        </div>
    
        <div id="001431752945034eb82ac80a3e64b9bb4929b16eeed1eb9000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431752945034eb82ac80a3e64b9bb4929b16eeed1eb9000" class="x-wiki-index-item">函数的参数</a>
            
        </div>
    
        <div id="001431756044276a15558a759ec43de8e30eb0ed169fb11000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431756044276a15558a759ec43de8e30eb0ed169fb11000" class="x-wiki-index-item">递归函数</a>
            
        </div>
    

            
        </div>
    
        <div id="0014317568446245b3e1c8837414168bcd2d485e553779e000" depth="1" style="display:none;position:relative;margin-left:15px;">
            
            <i onclick="toggleWikiNode(this)" class="uk-icon-plus-square-o" style="position:absolute;margin-left:-1em;padding-top:8px;"></i>
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014317568446245b3e1c8837414168bcd2d485e553779e000" class="x-wiki-index-item">高级特性</a>
            
    
        <div id="001431756919644a792ee4ead724ef7afab3f7f771b04f5000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431756919644a792ee4ead724ef7afab3f7f771b04f5000" class="x-wiki-index-item">切片</a>
            
        </div>
    
        <div id="0014317793224211f408912d9c04f2eac4d2af0d5d3d7b2000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014317793224211f408912d9c04f2eac4d2af0d5d3d7b2000" class="x-wiki-index-item">迭代</a>
            
        </div>
    
        <div id="001431779637539089fd627094a43a8a7c77e6102e3a811000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431779637539089fd627094a43a8a7c77e6102e3a811000" class="x-wiki-index-item">列表生成式</a>
            
        </div>
    
        <div id="0014317799226173f45ce40636141b6abc8424e12b5fb27000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014317799226173f45ce40636141b6abc8424e12b5fb27000" class="x-wiki-index-item">生成器</a>
            
        </div>
    
        <div id="00143178254193589df9c612d2449618ea460e7a672a366000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143178254193589df9c612d2449618ea460e7a672a366000" class="x-wiki-index-item">迭代器</a>
            
        </div>
    

            
        </div>
    
        <div id="0014317848428125ae6aa24068b4c50a7e71501ab275d52000" depth="1" style="display:none;position:relative;margin-left:15px;">
            
            <i onclick="toggleWikiNode(this)" class="uk-icon-plus-square-o" style="position:absolute;margin-left:-1em;padding-top:8px;"></i>
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014317848428125ae6aa24068b4c50a7e71501ab275d52000" class="x-wiki-index-item">函数式编程</a>
            
    
        <div id="0014317849054170d563b13f0fa4ce6ba1cd86e18103f28000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <i onclick="toggleWikiNode(this)" class="uk-icon-plus-square-o" style="position:absolute;margin-left:-1em;padding-top:8px;"></i>
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014317849054170d563b13f0fa4ce6ba1cd86e18103f28000" class="x-wiki-index-item">高阶函数</a>
            
    
        <div id="0014317852443934a86aa5bb5ea47fbbd5f35282b331335000" depth="3" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014317852443934a86aa5bb5ea47fbbd5f35282b331335000" class="x-wiki-index-item">map/reduce</a>
            
        </div>
    
        <div id="001431821084171d2e0f22e7cc24305ae03aa0214d0ef29000" depth="3" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431821084171d2e0f22e7cc24305ae03aa0214d0ef29000" class="x-wiki-index-item">filter</a>
            
        </div>
    
        <div id="0014318230588782cac105d0d8a40c6b450a232748dc854000" depth="3" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318230588782cac105d0d8a40c6b450a232748dc854000" class="x-wiki-index-item">sorted</a>
            
        </div>
    

            
        </div>
    
        <div id="001431835236741e42daf5af6514f1a8917b8aaadff31bf000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431835236741e42daf5af6514f1a8917b8aaadff31bf000" class="x-wiki-index-item">返回函数</a>
            
        </div>
    
        <div id="001431843456408652233b88b424613aa8ec2fe032fd85a000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431843456408652233b88b424613aa8ec2fe032fd85a000" class="x-wiki-index-item">匿名函数</a>
            
        </div>
    
        <div id="0014318435599930270c0381a3b44db991cd6d858064ac0000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318435599930270c0381a3b44db991cd6d858064ac0000" class="x-wiki-index-item">装饰器</a>
            
        </div>
    
        <div id="00143184474383175eeea92a8b0439fab7b392a8a32f8fa000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143184474383175eeea92a8b0439fab7b392a8a32f8fa000" class="x-wiki-index-item">偏函数</a>
            
        </div>
    

            
        </div>
    
        <div id="0014318447437605e90206e261744c08630a836851f5183000" depth="1" style="display:none;position:relative;margin-left:15px;">
            
            <i onclick="toggleWikiNode(this)" class="uk-icon-plus-square-o" style="position:absolute;margin-left:-1em;padding-top:8px;"></i>
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318447437605e90206e261744c08630a836851f5183000" class="x-wiki-index-item">模块</a>
            
    
        <div id="001431845183474e20ee7e7828b47f7b7607f2dc1e90dbb000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431845183474e20ee7e7828b47f7b7607f2dc1e90dbb000" class="x-wiki-index-item">使用模块</a>
            
        </div>
    
        <div id="00143186362353505516c5d4e38456fb225c18cc5b54ffb000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143186362353505516c5d4e38456fb225c18cc5b54ffb000" class="x-wiki-index-item">安装第三方模块</a>
            
        </div>
    

            
        </div>
    
        <div id="0014318645694388f1f10473d7f416e9291616be8367ab5000" depth="1" style="display:none;position:relative;margin-left:15px;">
            
            <i onclick="toggleWikiNode(this)" class="uk-icon-plus-square-o" style="position:absolute;margin-left:-1em;padding-top:8px;"></i>
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318645694388f1f10473d7f416e9291616be8367ab5000" class="x-wiki-index-item">面向对象编程</a>
            
    
        <div id="001431864715651c99511036d884cf1b399e65ae0d27f7e000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431864715651c99511036d884cf1b399e65ae0d27f7e000" class="x-wiki-index-item">类和实例</a>
            
        </div>
    
        <div id="0014318650247930b1b21d7d3c64fe38c4b5a80d4469ad7000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318650247930b1b21d7d3c64fe38c4b5a80d4469ad7000" class="x-wiki-index-item">访问限制</a>
            
        </div>
    
        <div id="001431865288798deef438d865e4c2985acff7e9fad15e3000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431865288798deef438d865e4c2985acff7e9fad15e3000" class="x-wiki-index-item">继承和多态</a>
            
        </div>
    
        <div id="001431866385235335917b66049448ab14a499afd5b24db000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431866385235335917b66049448ab14a499afd5b24db000" class="x-wiki-index-item">获取对象信息</a>
            
        </div>
    
        <div id="0014319117128404c7dd0cf0e3c4d88acc8fe4d2c163625000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319117128404c7dd0cf0e3c4d88acc8fe4d2c163625000" class="x-wiki-index-item">实例属性和类属性</a>
            
        </div>
    

            
        </div>
    
        <div id="00143186738532805c392f2cc09446caf3236c34e3f980f000" depth="1" style="display:none;position:relative;margin-left:15px;">
            
            <i onclick="toggleWikiNode(this)" class="uk-icon-plus-square-o" style="position:absolute;margin-left:-1em;padding-top:8px;"></i>
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143186738532805c392f2cc09446caf3236c34e3f980f000" class="x-wiki-index-item">面向对象高级编程</a>
            
    
        <div id="00143186739713011a09b63dcbd42cc87f907a778b3ac73000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143186739713011a09b63dcbd42cc87f907a778b3ac73000" class="x-wiki-index-item">使用__slots__</a>
            
        </div>
    
        <div id="00143186781871161bc8d6497004764b398401a401d4cce000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143186781871161bc8d6497004764b398401a401d4cce000" class="x-wiki-index-item">使用@property</a>
            
        </div>
    
        <div id="0014318680104044a55f4a9dbf8452caf71e8dc68b75a18000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318680104044a55f4a9dbf8452caf71e8dc68b75a18000" class="x-wiki-index-item">多重继承</a>
            
        </div>
    
        <div id="0014319098638265527beb24f7840aa97de564ccc7f20f6000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319098638265527beb24f7840aa97de564ccc7f20f6000" class="x-wiki-index-item">定制类</a>
            
        </div>
    
        <div id="00143191235886950998592cd3e426e91687cdae696e64b000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143191235886950998592cd3e426e91687cdae696e64b000" class="x-wiki-index-item">使用枚举类</a>
            
        </div>
    
        <div id="0014319106919344c4ef8b1e04c48778bb45796e0335839000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319106919344c4ef8b1e04c48778bb45796e0335839000" class="x-wiki-index-item">使用元类</a>
            
        </div>
    

            
        </div>
    
        <div id="001431913726557e5e43e1ee8d54ee486bddc3f607afb75000" depth="1" style="display:none;position:relative;margin-left:15px;">
            
            <i onclick="toggleWikiNode(this)" class="uk-icon-plus-square-o" style="position:absolute;margin-left:-1em;padding-top:8px;"></i>
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431913726557e5e43e1ee8d54ee486bddc3f607afb75000" class="x-wiki-index-item">错误、调试和测试</a>
            
    
        <div id="00143191375461417a222c54b7e4d65b258f491c093a515000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143191375461417a222c54b7e4d65b258f491c093a515000" class="x-wiki-index-item">错误处理</a>
            
        </div>
    
        <div id="001431915578556ad30ab3933ae4e82a03ee2e9a4f70871000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431915578556ad30ab3933ae4e82a03ee2e9a4f70871000" class="x-wiki-index-item">调试</a>
            
        </div>
    
        <div id="00143191629979802b566644aa84656b50cd484ec4a7838000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143191629979802b566644aa84656b50cd484ec4a7838000" class="x-wiki-index-item">单元测试</a>
            
        </div>
    
        <div id="0014319170285543a4d04751f8846908770660de849f285000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319170285543a4d04751f8846908770660de849f285000" class="x-wiki-index-item">文档测试</a>
            
        </div>
    

            
        </div>
    
        <div id="001431917590955542f9ac5f5c1479faf787ff2b028ab47000" depth="1" style="display:none;position:relative;margin-left:15px;">
            
            <i onclick="toggleWikiNode(this)" class="uk-icon-plus-square-o" style="position:absolute;margin-left:-1em;padding-top:8px;"></i>
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431917590955542f9ac5f5c1479faf787ff2b028ab47000" class="x-wiki-index-item">IO编程</a>
            
    
        <div id="001431917715991ef1ebc19d15a4afdace1169a464eecc2000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431917715991ef1ebc19d15a4afdace1169a464eecc2000" class="x-wiki-index-item">文件读写</a>
            
        </div>
    
        <div id="001431918785710e86a1a120ce04925bae155012c7fc71e000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431918785710e86a1a120ce04925bae155012c7fc71e000" class="x-wiki-index-item">StringIO和BytesIO</a>
            
        </div>
    
        <div id="001431925324119bac1bc7979664b4fa9843c0e5fcdcf1e000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431925324119bac1bc7979664b4fa9843c0e5fcdcf1e000" class="x-wiki-index-item">操作文件和目录</a>
            
        </div>
    
        <div id="00143192607210600a668b5112e4a979dd20e4661cc9c97000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143192607210600a668b5112e4a979dd20e4661cc9c97000" class="x-wiki-index-item">序列化</a>
            
        </div>
    

            
        </div>
    
        <div id="0014319272686365ec7ceaeca33428c914edf8f70cca383000" depth="1" style="display:none;position:relative;margin-left:15px;">
            
            <i onclick="toggleWikiNode(this)" class="uk-icon-plus-square-o" style="position:absolute;margin-left:-1em;padding-top:8px;"></i>
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319272686365ec7ceaeca33428c914edf8f70cca383000" class="x-wiki-index-item">进程和线程</a>
            
    
        <div id="001431927781401bb47ccf187b24c3b955157bb12c5882d000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431927781401bb47ccf187b24c3b955157bb12c5882d000" class="x-wiki-index-item">多进程</a>
            
        </div>
    
        <div id="00143192823818768cd506abbc94eb5916192364506fa5d000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143192823818768cd506abbc94eb5916192364506fa5d000" class="x-wiki-index-item">多线程</a>
            
        </div>
    
        <div id="001431928972981094a382e5584413fa040b46d46cce48e000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431928972981094a382e5584413fa040b46d46cce48e000" class="x-wiki-index-item">ThreadLocal</a>
            
        </div>
    
        <div id="0014319292979766bd3285c9d6b4942a8ea9b4e9cfb48d8000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319292979766bd3285c9d6b4942a8ea9b4e9cfb48d8000" class="x-wiki-index-item">进程 vs. 线程</a>
            
        </div>
    
        <div id="001431929340191970154d52b9d484b88a7b343708fcc60000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431929340191970154d52b9d484b88a7b343708fcc60000" class="x-wiki-index-item">分布式进程</a>
            
        </div>
    

            
        </div>
    
        <div id="00143193331387014ccd1040c814dee8b2164bb4f064cff000" depth="1" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143193331387014ccd1040c814dee8b2164bb4f064cff000" class="x-wiki-index-item">正则表达式</a>
            
        </div>
    
        <div id="0014319347182373b696e637cc04430b8ee2d548ca1b36d000" depth="1" style="display:none;position:relative;margin-left:15px;">
            
            <i onclick="toggleWikiNode(this)" class="uk-icon-plus-square-o" style="position:absolute;margin-left:-1em;padding-top:8px;"></i>
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319347182373b696e637cc04430b8ee2d548ca1b36d000" class="x-wiki-index-item">常用内建模块</a>
            
    
        <div id="001431937554888869fb52b812243dda6103214cd61d0c2000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431937554888869fb52b812243dda6103214cd61d0c2000" class="x-wiki-index-item">datetime</a>
            
        </div>
    
        <div id="001431953239820157155d21c494e5786fce303f3018c86000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431953239820157155d21c494e5786fce303f3018c86000" class="x-wiki-index-item">collections</a>
            
        </div>
    
        <div id="001431954588961d6b6f51000ca4279a3415ce14ed9d709000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431954588961d6b6f51000ca4279a3415ce14ed9d709000" class="x-wiki-index-item">base64</a>
            
        </div>
    
        <div id="001431955007656a66f831e208e4c189b8a9e9f3f25ba53000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431955007656a66f831e208e4c189b8a9e9f3f25ba53000" class="x-wiki-index-item">struct</a>
            
        </div>
    
        <div id="0014319556588648dd1fb0047a34d0c945ee33e8f4c90cc000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319556588648dd1fb0047a34d0c945ee33e8f4c90cc000" class="x-wiki-index-item">hashlib</a>
            
        </div>
    
        <div id="0015108777177966ef0f4f8510a41b3b8c48cdcf7047b2d000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0015108777177966ef0f4f8510a41b3b8c48cdcf7047b2d000" class="x-wiki-index-item">hmac</a>
            
        </div>
    
        <div id="00143200162233153835cfdd1a541a18ddc15059e3ddeec000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143200162233153835cfdd1a541a18ddc15059e3ddeec000" class="x-wiki-index-item">itertools</a>
            
        </div>
    
        <div id="001478651770626de401ff1c0d94f379774cabd842222ff000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001478651770626de401ff1c0d94f379774cabd842222ff000" class="x-wiki-index-item">contextlib</a>
            
        </div>
    
        <div id="001432688314740a0aed473a39f47b09c8c7274c9ab6aee000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432688314740a0aed473a39f47b09c8c7274c9ab6aee000" class="x-wiki-index-item">urllib</a>
            
        </div>
    
        <div id="001432002075057b594f70ecb58445da6ef6071aca880af000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432002075057b594f70ecb58445da6ef6071aca880af000" class="x-wiki-index-item">XML</a>
            
        </div>
    
        <div id="0014320023122880232500da9dc4a4486ad00426f081c15000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014320023122880232500da9dc4a4486ad00426f081c15000" class="x-wiki-index-item">HTMLParser</a>
            
        </div>
    

            
        </div>
    
        <div id="001432002680493d1babda364904ca0a6e28374498d59a7000" depth="1" style="display:none;position:relative;margin-left:15px;">
            
            <i onclick="toggleWikiNode(this)" class="uk-icon-plus-square-o" style="position:absolute;margin-left:-1em;padding-top:8px;"></i>
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432002680493d1babda364904ca0a6e28374498d59a7000" class="x-wiki-index-item">常用第三方模块</a>
            
    
        <div id="0014320027235877860c87af5544f25a8deeb55141d60c5000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014320027235877860c87af5544f25a8deeb55141d60c5000" class="x-wiki-index-item">Pillow</a>
            
        </div>
    
        <div id="0015109021115795adfc5c8629f4f98985063b5a7e3ff87000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0015109021115795adfc5c8629f4f98985063b5a7e3ff87000" class="x-wiki-index-item">requests</a>
            
        </div>
    
        <div id="001510905171877ca6fdf08614e446e835ea5d9bce75cf5000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001510905171877ca6fdf08614e446e835ea5d9bce75cf5000" class="x-wiki-index-item">chardet</a>
            
        </div>
    
        <div id="001511052957192bb91a56a2339485c8a8c79812b400d49000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001511052957192bb91a56a2339485c8a8c79812b400d49000" class="x-wiki-index-item">psutil</a>
            
        </div>
    

            
        </div>
    
        <div id="001432712108300322c61f256c74803b43bfd65c6f8d0d0000" depth="1" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432712108300322c61f256c74803b43bfd65c6f8d0d0000" class="x-wiki-index-item">virtualenv</a>
            
        </div>
    
        <div id="00143200341926302f99cf6f6414dca9dfaaf6e5a25a5b1000" depth="1" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143200341926302f99cf6f6414dca9dfaaf6e5a25a5b1000" class="x-wiki-index-item">图形界面</a>
            
        </div>
    
        <div id="0014320037274136d31bd9979d648cd822375394e29a871000" depth="1" style="display:none;position:relative;margin-left:15px;">
            
            <i onclick="toggleWikiNode(this)" class="uk-icon-plus-square-o" style="position:absolute;margin-left:-1em;padding-top:8px;"></i>
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014320037274136d31bd9979d648cd822375394e29a871000" class="x-wiki-index-item">网络编程</a>
            
    
        <div id="0014320037768360d53e4e935ca4a1f96eed1c896ad1217000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014320037768360d53e4e935ca4a1f96eed1c896ad1217000" class="x-wiki-index-item">TCP/IP简介</a>
            
        </div>
    
        <div id="001432004374523e495f640612f4b08975398796939ec3c000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432004374523e495f640612f4b08975398796939ec3c000" class="x-wiki-index-item">TCP编程</a>
            
        </div>
    
        <div id="001432004977916a212e2168e21449981ad65cd16e71201000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432004977916a212e2168e21449981ad65cd16e71201000" class="x-wiki-index-item">UDP编程</a>
            
        </div>
    

            
        </div>
    
        <div id="001432005156604f38836be1707453eb025ce8c3079978d000" depth="1" style="display:none;position:relative;margin-left:15px;">
            
            <i onclick="toggleWikiNode(this)" class="uk-icon-plus-square-o" style="position:absolute;margin-left:-1em;padding-top:8px;"></i>
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432005156604f38836be1707453eb025ce8c3079978d000" class="x-wiki-index-item">电子邮件</a>
            
    
        <div id="001432005226355aadb8d4b2f3f42f6b1d6f2c5bd8d5263000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432005226355aadb8d4b2f3f42f6b1d6f2c5bd8d5263000" class="x-wiki-index-item">SMTP发送邮件</a>
            
        </div>
    
        <div id="0014320098721191b70a2cf7b5441deb01595edd8147196000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014320098721191b70a2cf7b5441deb01595edd8147196000" class="x-wiki-index-item">POP3收取邮件</a>
            
        </div>
    

            
        </div>
    
        <div id="001432010325987131e75bf6b3543429a2975f88ce8ffa9000" depth="1" style="display:none;position:relative;margin-left:15px;">
            
            <i onclick="toggleWikiNode(this)" class="uk-icon-plus-square-o" style="position:absolute;margin-left:-1em;padding-top:8px;"></i>
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432010325987131e75bf6b3543429a2975f88ce8ffa9000" class="x-wiki-index-item">访问数据库</a>
            
    
        <div id="001432010494717e1db78cd172e4d52b853e7fd38d6985c000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432010494717e1db78cd172e4d52b853e7fd38d6985c000" class="x-wiki-index-item">使用SQLite</a>
            
        </div>
    
        <div id="0014320107391860b39da6901ed41a296e574ed37104752000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014320107391860b39da6901ed41a296e574ed37104752000" class="x-wiki-index-item">使用MySQL</a>
            
        </div>
    
        <div id="0014320114981139589ac5f02944601ae22834e9c521415000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014320114981139589ac5f02944601ae22834e9c521415000" class="x-wiki-index-item">使用SQLAlchemy</a>
            
        </div>
    

            
        </div>
    
        <div id="0014320118765877e93ecea4e6449acb157e9efae8b40b6000" depth="1" style="display:none;position:relative;margin-left:15px;">
            
            <i onclick="toggleWikiNode(this)" class="uk-icon-plus-square-o" style="position:absolute;margin-left:-1em;padding-top:8px;"></i>
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014320118765877e93ecea4e6449acb157e9efae8b40b6000" class="x-wiki-index-item">Web开发</a>
            
    
        <div id="001432011939547478fd5482deb47b08716557cc99764e0000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432011939547478fd5482deb47b08716557cc99764e0000" class="x-wiki-index-item">HTTP协议简介</a>
            
        </div>
    
        <div id="0014320122322996f770fbf5da84ead84a1731e1dde129f000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014320122322996f770fbf5da84ead84a1731e1dde129f000" class="x-wiki-index-item">HTML简介</a>
            
        </div>
    
        <div id="001432012393132788f71e0edad4676a3f76ac7776f3a16000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432012393132788f71e0edad4676a3f76ac7776f3a16000" class="x-wiki-index-item">WSGI接口</a>
            
        </div>
    
        <div id="001432012745805707cb9f00a484d968c72dbb7cfc90b91000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432012745805707cb9f00a484d968c72dbb7cfc90b91000" class="x-wiki-index-item">使用Web框架</a>
            
        </div>
    
        <div id="0014320129740415df73bf8f81e478982bf4d5c8aa3817a000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014320129740415df73bf8f81e478982bf4d5c8aa3817a000" class="x-wiki-index-item">使用模板</a>
            
        </div>
    

            
        </div>
    
        <div id="00143208573480558080fa77514407cb23834c78c6c7309000" depth="1" style="display:none;position:relative;margin-left:15px;">
            
            <i onclick="toggleWikiNode(this)" class="uk-icon-plus-square-o" style="position:absolute;margin-left:-1em;padding-top:8px;"></i>
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143208573480558080fa77514407cb23834c78c6c7309000" class="x-wiki-index-item">异步IO</a>
            
    
        <div id="001432090171191d05dae6e129940518d1d6cf6eeaaa969000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432090171191d05dae6e129940518d1d6cf6eeaaa969000" class="x-wiki-index-item">协程</a>
            
        </div>
    
        <div id="001432090954004980bd351f2cd4cc18c9e6c06d855c498000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432090954004980bd351f2cd4cc18c9e6c06d855c498000" class="x-wiki-index-item">asyncio</a>
            
        </div>
    
        <div id="00144661533005329786387b5684be385062a121e834ac7000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00144661533005329786387b5684be385062a121e834ac7000" class="x-wiki-index-item">async/await</a>
            
        </div>
    
        <div id="0014320981492785ba33cc96c524223b2ea4e444077708d000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014320981492785ba33cc96c524223b2ea4e444077708d000" class="x-wiki-index-item">aiohttp</a>
            
        </div>
    

            
        </div>
    
        <div id="001432170876125c96f6cc10717484baea0c6da9bee2be4000" depth="1" style="display:none;position:relative;margin-left:15px;">
            
            <i onclick="toggleWikiNode(this)" class="uk-icon-plus-square-o" style="position:absolute;margin-left:-1em;padding-top:8px;"></i>
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432170876125c96f6cc10717484baea0c6da9bee2be4000" class="x-wiki-index-item">实战</a>
            
    
        <div id="001432170937506ecfb2f6adf8e4757939732f3e32b781c000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432170937506ecfb2f6adf8e4757939732f3e32b781c000" class="x-wiki-index-item">Day 1 - 搭建开发环境</a>
            
        </div>
    
        <div id="00143217133614028a244ea855b40a586b551c616d3b2c9000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143217133614028a244ea855b40a586b551c616d3b2c9000" class="x-wiki-index-item">Day 2 - 编写Web App骨架</a>
            
        </div>
    
        <div id="0014323389656575142d0bcfeec434e9639a80d3684a7da000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014323389656575142d0bcfeec434e9639a80d3684a7da000" class="x-wiki-index-item">Day 3 - 编写ORM</a>
            
        </div>
    
        <div id="001432338991719a4c5c42ef08e4f44ad0f293ad728a27b000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432338991719a4c5c42ef08e4f44ad0f293ad728a27b000" class="x-wiki-index-item">Day 4 - 编写Model</a>
            
        </div>
    
        <div id="001432339008728d0ddbe19ee594980be3f0644a9371894000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432339008728d0ddbe19ee594980be3f0644a9371894000" class="x-wiki-index-item">Day 5 - 编写Web框架</a>
            
        </div>
    
        <div id="001432339034336cbf72acd43354d72831461e3871d9f2e000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432339034336cbf72acd43354d72831461e3871d9f2e000" class="x-wiki-index-item">Day 6 - 编写配置文件</a>
            
        </div>
    
        <div id="001432339095180ce91c53cdab841bfa9c342a297b886fe000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432339095180ce91c53cdab841bfa9c342a297b886fe000" class="x-wiki-index-item">Day 7 - 编写MVC</a>
            
        </div>
    
        <div id="001432339124159f00f6ab876c44349a3fd8eb26d0c291e000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432339124159f00f6ab876c44349a3fd8eb26d0c291e000" class="x-wiki-index-item">Day 8 - 构建前端</a>
            
        </div>
    
        <div id="0014323391480651a75b5fda4cb4c789208191682fc2c70000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014323391480651a75b5fda4cb4c789208191682fc2c70000" class="x-wiki-index-item">Day 9 - 编写API</a>
            
        </div>
    
        <div id="001432339169382f45b9bd7b45d47ceb3e2b42846e0e991000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432339169382f45b9bd7b45d47ceb3e2b42846e0e991000" class="x-wiki-index-item">Day 10 - 用户注册和登录</a>
            
        </div>
    
        <div id="00143233918656129f4ad3ac29e4f728dc72b5d2368215a000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143233918656129f4ad3ac29e4f728dc72b5d2368215a000" class="x-wiki-index-item">Day 11 - 编写日志创建页</a>
            
        </div>
    
        <div id="001432339210950e063b4795d574036bc5dcf0c2449bc52000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432339210950e063b4795d574036bc5dcf0c2449bc52000" class="x-wiki-index-item">Day 12 - 编写日志列表页</a>
            
        </div>
    
        <div id="001432339228196a8eb6fb8832b48b5aa0d740346536ead000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432339228196a8eb6fb8832b48b5aa0d740346536ead000" class="x-wiki-index-item">Day 13 - 提升开发效率</a>
            
        </div>
    
        <div id="001432339247097eea476bf61f8496092cc1b663eae1848000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432339247097eea476bf61f8496092cc1b663eae1848000" class="x-wiki-index-item">Day 14 - 完成Web App</a>
            
        </div>
    
        <div id="0014323392805925d5b69ddad514511bf0391fe2a0df2b0000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014323392805925d5b69ddad514511bf0391fe2a0df2b0000" class="x-wiki-index-item">Day 15 - 部署Web App</a>
            
        </div>
    
        <div id="001432339330096121ae7e38be44570b7fbd0d8faae26f6000" depth="2" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432339330096121ae7e38be44570b7fbd0d8faae26f6000" class="x-wiki-index-item">Day 16 - 编写移动App</a>
            
        </div>
    

            
        </div>
    
        <div id="00143278155868605a65e244e6642dfa533753e6338ab5b000" depth="1" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143278155868605a65e244e6642dfa533753e6338ab5b000" class="x-wiki-index-item">FAQ</a>
            
        </div>
    
        <div id="0014323396477522f8ff26917934f53b49559ab4dc5eab2000" depth="1" style="display:none;position:relative;margin-left:15px;">
            
            <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014323396477522f8ff26917934f53b49559ab4dc5eab2000" class="x-wiki-index-item">期末总结</a>
            
        </div>
    

        </div>
    </ul>
    <div class="x-placeholder"></div>

                        </div>
                        <div class="x-sidebar-left-bottom">
                            <h3>关于作者</h3>
<iframe width="100%" height="90" class="share_self"  frameborder="0" scrolling="no" src="net://widget.weibo.com/weiboshow/index.php?language=&width=0&height=550&fansRow=2&ptype=1&speed=0&skin=5&isTitle=0&noborder=0&isWeibo=0&isFans=0&uid=1658384301&verifier=078cedea&colors=0593d3,ffffff,666666,0593d3,0477ab&dpc=1"></iframe>

                        </div>
                        <div id="x-sponsor-b" class="uk-clearfix"><!-- sponsor B --></div>
                    </div>
                
                

                    <div class="x-center">
                        <div class="x-content-top">
                            <!-- content_top -->
                        </div>
                        <div class="x-content" style="width:100%">
                            
    <h4>Python教程</h4>
    <div class="x-wiki-info"><span>阅读: 6062932</span></div>

    <hr>

    <div class="x-wiki-content x-main-content"><p>这是小白的Python新手教程，具有如下特点：</p>
<h1><a name="#-E4-B8-AD-E6-96-87-EF-BC-8C-E5-85-8D-E8-B4-B9-EF-BC-8C-E9-9B-B6-E8-B5-B7-E7-82-B9-EF-BC-8C-E5-AE-8C-E6-95-B4-E7-A4-BA-E4-BE-8B-EF-BC-8C-E5-9F-BA-E4-BA-8E-E6-9C-80-E6-96-B0-E7-9A-84Python-3-E7-89-88-E6-9C-AC-E3-80-82"></a>中文，免费，零起点，完整示例，基于最新的Python 3版本。</h1>
<p>Python是一种计算机程序设计语言。你可能已经听说过很多种流行的编程语言，比如非常难学的C语言，非常流行的Java语言，适合初学者的Basic语言，适合网页编程的JavaScript语言等等。</p>
<p>那Python是一种什么语言？</p>
<p>首先，我们普及一下编程语言的基础知识。用任何编程语言来开发程序，都是为了让计算机干活，比如下载一个MP3，编写一个文档等等，而计算机干活的CPU只认识机器指令，所以，尽管不同的编程语言差异极大，最后都得“翻译”成CPU可以执行的机器指令。而不同的编程语言，干同一个活，编写的代码量，差距也很大。</p>
<p>比如，完成同一个任务，C语言要写1000行代码，Java只需要写100行，而Python可能只要20行。</p>
<p>所以Python是一种相当高级的语言。</p>
<p>你也许会问，代码少还不好？代码少的代价是运行速度慢，C程序运行1秒钟，Java程序可能需要2秒，而Python程序可能就需要10秒。</p>
<p>那是不是越低级的程序越难学，越高级的程序越简单？表面上来说，是的，但是，在非常高的抽象计算中，高级的Python程序设计也是非常难学的，所以，高级程序语言不等于简单。</p>
<p>但是，对于初学者和完成普通任务，Python语言是非常简单易用的。连Google都在大规模使用Python，你就不用担心学了会没用。</p>
<p>用Python可以做什么？可以做日常任务，比如自动备份你的MP3；可以做网站，很多著名的网站包括YouTube就是Python写的；可以做网络游戏的后台，很多在线游戏的后台都是Python开发的。总之就是能干很多很多事啦。</p>
<p>Python当然也有不能干的事情，比如写操作系统，这个只能用C语言写；写手机应用，只能用Swift/Objective-C（针对iPhone）和Java（针对Android）；写3D游戏，最好用C或C++。</p>
<p>如果你是小白用户，满足以下条件：</p>
<ul>
<li>会使用电脑，但从来没写过程序；</li>
<li>还记得初中数学学的方程式和一点点代数知识；</li>
<li>想从编程小白变成专业的软件架构师；</li>
<li>每天能抽出半个小时学习。</li>
</ul>
<p>不要再犹豫了，这个教程就是为你准备的！</p>
<p>准备好了吗？</p>
<p><img src="https://cdn.liaoxuefeng.com/cdn/static/themes/default/img/loading.gif" data-src="https://cdn.liaoxuefeng.com/cdn/files/attachments/00138676512923004999ceca5614eb2afc5c0efdd2e4640000/0" alt="challenge-accepted"></p>
<h3><a name="#-E5-85-B3-E4-BA-8E-E4-BD-9C-E8-80-85"></a>关于作者</h3>
<p><a href="net://weibo.com/liaoxuefeng">廖雪峰</a>，十年软件开发经验，业余产品经理，精通Java/Python/Ruby/Scheme/Objective C等，对开源框架有深入研究，著有《spring 2.0核心技术与最佳实践》一书，多个业余开源项目托管在<a target="_blank" href="https://github.com/michaelliao">GitHub</a>，欢迎微博交流：</p>
<iframe width="100%" height="90" class="share_self"  frameborder="0" scrolling="no" src="net://widget.weibo.com/weiboshow/index.php?language=&width=0&height=550&fansRow=2&ptype=1&speed=0&skin=5&isTitle=0&noborder=0&isWeibo=0&isFans=0&uid=1658384301&verifier=078cedea&colors=0593d3,ffffff,666666,0593d3,0477ab&dpc=1"></iframe>
</div>

    <hr>

    <div class="x-wiki-prev-next uk-clearfix"></div>

    <div id="x-sponsor-a" class="uk-clearfix"><!-- sponsor A --></div>

    <div class="x-anchor x-comment-anchor"><a name="comments"></a></div>

    <h3>评论</h3>

    <ul id="x-comment-list" class="uk-comment-list">
    </ul>

    <h3>发表评论</h3>

    <div class="x-display-if-not-signin">
        <p><button type="button" class="uk-button" onclick="showSignin()"><i class="uk-icon-signin"></i> 登录后发表评论</button></p>
    </div>

    <div id="x-comment-area"></div>


                        </div>
                        <div class="x-content-bottom">
                            <!-- content_bottom -->
                        </div>
                    </div>
                </div>

                <div class="x-body-bottom uk-width-1-1">
                    <!-- body_bottom -->
                </div>
            </div>
        </div>
    </div>


    <div id="x-offcanvas-left" class="uk-offcanvas">
        <div class="uk-offcanvas-bar">
            <div class="uk-panel">
                
    <ul class="uk-nav uk-nav-side">
        <li class="uk-nav-header">目录</li>
    </ul>
    <ul class="uk-nav uk-nav-side">
        <li id="off-0014316089557264a6b348958f449949df42a6d3a2e542c000"><a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000">Python教程</a></li>
        
    
    <li id="off-001431608990315a01b575e2ab041168ff0df194698afac000" style="margin-left:1em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431608990315a01b575e2ab041168ff0df194698afac000">Python简介</a>
    </li>
    
    
    <li id="off-0014316090478912dab2a3a9e8f4ed49d28854b292f85bb000" style="margin-left:1em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014316090478912dab2a3a9e8f4ed49d28854b292f85bb000">安装Python</a>
    </li>
    
        
    
    <li id="off-00143161198846783e33de56d4041058c3dfc7e44ee1203000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143161198846783e33de56d4041058c3dfc7e44ee1203000">Python解释器</a>
    </li>
    
    

    
    
    <li id="off-001431611988455689d4c116b2c4ed6aec000776c00ed52000" style="margin-left:1em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431611988455689d4c116b2c4ed6aec000776c00ed52000">第一个Python程序</a>
    </li>
    
        
    
    <li id="off-0014316399410395f704750ee9440228135925a6ca1dad8000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014316399410395f704750ee9440228135925a6ca1dad8000">使用文本编辑器</a>
    </li>
    
    
    <li id="off-001432523496782e0946b0f454549c0888d05959b99860f000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432523496782e0946b0f454549c0888d05959b99860f000">Python代码运行助手</a>
    </li>
    
    
    <li id="off-001431643484137e38b44e5925440ec8b1e4c70f800b4e2000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431643484137e38b44e5925440ec8b1e4c70f800b4e2000">输入和输出</a>
    </li>
    
    

    
    
    <li id="off-001431658427513eef3d9dd9f7c48599116735806328e81000" style="margin-left:1em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431658427513eef3d9dd9f7c48599116735806328e81000">Python基础</a>
    </li>
    
        
    
    <li id="off-001431658624177ea4f8fcb06bc4d0e8aab2fd7aa65dd95000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431658624177ea4f8fcb06bc4d0e8aab2fd7aa65dd95000">数据类型和变量</a>
    </li>
    
    
    <li id="off-001431664106267f12e9bef7ee14cf6a8776a479bdec9b9000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431664106267f12e9bef7ee14cf6a8776a479bdec9b9000">字符串和编码</a>
    </li>
    
    
    <li id="off-0014316724772904521142196b74a3f8abf93d8e97c6ee6000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014316724772904521142196b74a3f8abf93d8e97c6ee6000">使用list和tuple</a>
    </li>
    
    
    <li id="off-001431675624710bb20e9734ef343bbb4bd64bcd37d4b52000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431675624710bb20e9734ef343bbb4bd64bcd37d4b52000">条件判断</a>
    </li>
    
    
    <li id="off-001431676242561226b32a9ec624505bb8f723d0027b3e7000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431676242561226b32a9ec624505bb8f723d0027b3e7000">循环</a>
    </li>
    
    
    <li id="off-00143167793538255adf33371774853a0ef943280573f4d000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143167793538255adf33371774853a0ef943280573f4d000">使用dict和set</a>
    </li>
    
    

    
    
    <li id="off-00143167832686474803d3d2b7d4d6499cfd093dc47efcd000" style="margin-left:1em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143167832686474803d3d2b7d4d6499cfd093dc47efcd000">函数</a>
    </li>
    
        
    
    <li id="off-0014316784721058975e02b46cc45cb836bb0827607738d000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014316784721058975e02b46cc45cb836bb0827607738d000">调用函数</a>
    </li>
    
    
    <li id="off-001431679203477b5b364aeba8c4e05a9bd4ec1b32911e2000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431679203477b5b364aeba8c4e05a9bd4ec1b32911e2000">定义函数</a>
    </li>
    
    
    <li id="off-001431752945034eb82ac80a3e64b9bb4929b16eeed1eb9000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431752945034eb82ac80a3e64b9bb4929b16eeed1eb9000">函数的参数</a>
    </li>
    
    
    <li id="off-001431756044276a15558a759ec43de8e30eb0ed169fb11000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431756044276a15558a759ec43de8e30eb0ed169fb11000">递归函数</a>
    </li>
    
    

    
    
    <li id="off-0014317568446245b3e1c8837414168bcd2d485e553779e000" style="margin-left:1em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014317568446245b3e1c8837414168bcd2d485e553779e000">高级特性</a>
    </li>
    
        
    
    <li id="off-001431756919644a792ee4ead724ef7afab3f7f771b04f5000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431756919644a792ee4ead724ef7afab3f7f771b04f5000">切片</a>
    </li>
    
    
    <li id="off-0014317793224211f408912d9c04f2eac4d2af0d5d3d7b2000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014317793224211f408912d9c04f2eac4d2af0d5d3d7b2000">迭代</a>
    </li>
    
    
    <li id="off-001431779637539089fd627094a43a8a7c77e6102e3a811000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431779637539089fd627094a43a8a7c77e6102e3a811000">列表生成式</a>
    </li>
    
    
    <li id="off-0014317799226173f45ce40636141b6abc8424e12b5fb27000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014317799226173f45ce40636141b6abc8424e12b5fb27000">生成器</a>
    </li>
    
    
    <li id="off-00143178254193589df9c612d2449618ea460e7a672a366000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143178254193589df9c612d2449618ea460e7a672a366000">迭代器</a>
    </li>
    
    

    
    
    <li id="off-0014317848428125ae6aa24068b4c50a7e71501ab275d52000" style="margin-left:1em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014317848428125ae6aa24068b4c50a7e71501ab275d52000">函数式编程</a>
    </li>
    
        
    
    <li id="off-0014317849054170d563b13f0fa4ce6ba1cd86e18103f28000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014317849054170d563b13f0fa4ce6ba1cd86e18103f28000">高阶函数</a>
    </li>
    
        
    
    <li id="off-0014317852443934a86aa5bb5ea47fbbd5f35282b331335000" style="margin-left:3em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014317852443934a86aa5bb5ea47fbbd5f35282b331335000">map/reduce</a>
    </li>
    
    
    <li id="off-001431821084171d2e0f22e7cc24305ae03aa0214d0ef29000" style="margin-left:3em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431821084171d2e0f22e7cc24305ae03aa0214d0ef29000">filter</a>
    </li>
    
    
    <li id="off-0014318230588782cac105d0d8a40c6b450a232748dc854000" style="margin-left:3em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318230588782cac105d0d8a40c6b450a232748dc854000">sorted</a>
    </li>
    
    

    
    
    <li id="off-001431835236741e42daf5af6514f1a8917b8aaadff31bf000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431835236741e42daf5af6514f1a8917b8aaadff31bf000">返回函数</a>
    </li>
    
    
    <li id="off-001431843456408652233b88b424613aa8ec2fe032fd85a000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431843456408652233b88b424613aa8ec2fe032fd85a000">匿名函数</a>
    </li>
    
    
    <li id="off-0014318435599930270c0381a3b44db991cd6d858064ac0000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318435599930270c0381a3b44db991cd6d858064ac0000">装饰器</a>
    </li>
    
    
    <li id="off-00143184474383175eeea92a8b0439fab7b392a8a32f8fa000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143184474383175eeea92a8b0439fab7b392a8a32f8fa000">偏函数</a>
    </li>
    
    

    
    
    <li id="off-0014318447437605e90206e261744c08630a836851f5183000" style="margin-left:1em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318447437605e90206e261744c08630a836851f5183000">模块</a>
    </li>
    
        
    
    <li id="off-001431845183474e20ee7e7828b47f7b7607f2dc1e90dbb000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431845183474e20ee7e7828b47f7b7607f2dc1e90dbb000">使用模块</a>
    </li>
    
    
    <li id="off-00143186362353505516c5d4e38456fb225c18cc5b54ffb000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143186362353505516c5d4e38456fb225c18cc5b54ffb000">安装第三方模块</a>
    </li>
    
    

    
    
    <li id="off-0014318645694388f1f10473d7f416e9291616be8367ab5000" style="margin-left:1em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318645694388f1f10473d7f416e9291616be8367ab5000">面向对象编程</a>
    </li>
    
        
    
    <li id="off-001431864715651c99511036d884cf1b399e65ae0d27f7e000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431864715651c99511036d884cf1b399e65ae0d27f7e000">类和实例</a>
    </li>
    
    
    <li id="off-0014318650247930b1b21d7d3c64fe38c4b5a80d4469ad7000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318650247930b1b21d7d3c64fe38c4b5a80d4469ad7000">访问限制</a>
    </li>
    
    
    <li id="off-001431865288798deef438d865e4c2985acff7e9fad15e3000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431865288798deef438d865e4c2985acff7e9fad15e3000">继承和多态</a>
    </li>
    
    
    <li id="off-001431866385235335917b66049448ab14a499afd5b24db000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431866385235335917b66049448ab14a499afd5b24db000">获取对象信息</a>
    </li>
    
    
    <li id="off-0014319117128404c7dd0cf0e3c4d88acc8fe4d2c163625000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319117128404c7dd0cf0e3c4d88acc8fe4d2c163625000">实例属性和类属性</a>
    </li>
    
    

    
    
    <li id="off-00143186738532805c392f2cc09446caf3236c34e3f980f000" style="margin-left:1em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143186738532805c392f2cc09446caf3236c34e3f980f000">面向对象高级编程</a>
    </li>
    
        
    
    <li id="off-00143186739713011a09b63dcbd42cc87f907a778b3ac73000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143186739713011a09b63dcbd42cc87f907a778b3ac73000">使用__slots__</a>
    </li>
    
    
    <li id="off-00143186781871161bc8d6497004764b398401a401d4cce000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143186781871161bc8d6497004764b398401a401d4cce000">使用@property</a>
    </li>
    
    
    <li id="off-0014318680104044a55f4a9dbf8452caf71e8dc68b75a18000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318680104044a55f4a9dbf8452caf71e8dc68b75a18000">多重继承</a>
    </li>
    
    
    <li id="off-0014319098638265527beb24f7840aa97de564ccc7f20f6000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319098638265527beb24f7840aa97de564ccc7f20f6000">定制类</a>
    </li>
    
    
    <li id="off-00143191235886950998592cd3e426e91687cdae696e64b000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143191235886950998592cd3e426e91687cdae696e64b000">使用枚举类</a>
    </li>
    
    
    <li id="off-0014319106919344c4ef8b1e04c48778bb45796e0335839000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319106919344c4ef8b1e04c48778bb45796e0335839000">使用元类</a>
    </li>
    
    

    
    
    <li id="off-001431913726557e5e43e1ee8d54ee486bddc3f607afb75000" style="margin-left:1em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431913726557e5e43e1ee8d54ee486bddc3f607afb75000">错误、调试和测试</a>
    </li>
    
        
    
    <li id="off-00143191375461417a222c54b7e4d65b258f491c093a515000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143191375461417a222c54b7e4d65b258f491c093a515000">错误处理</a>
    </li>
    
    
    <li id="off-001431915578556ad30ab3933ae4e82a03ee2e9a4f70871000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431915578556ad30ab3933ae4e82a03ee2e9a4f70871000">调试</a>
    </li>
    
    
    <li id="off-00143191629979802b566644aa84656b50cd484ec4a7838000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143191629979802b566644aa84656b50cd484ec4a7838000">单元测试</a>
    </li>
    
    
    <li id="off-0014319170285543a4d04751f8846908770660de849f285000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319170285543a4d04751f8846908770660de849f285000">文档测试</a>
    </li>
    
    

    
    
    <li id="off-001431917590955542f9ac5f5c1479faf787ff2b028ab47000" style="margin-left:1em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431917590955542f9ac5f5c1479faf787ff2b028ab47000">IO编程</a>
    </li>
    
        
    
    <li id="off-001431917715991ef1ebc19d15a4afdace1169a464eecc2000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431917715991ef1ebc19d15a4afdace1169a464eecc2000">文件读写</a>
    </li>
    
    
    <li id="off-001431918785710e86a1a120ce04925bae155012c7fc71e000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431918785710e86a1a120ce04925bae155012c7fc71e000">StringIO和BytesIO</a>
    </li>
    
    
    <li id="off-001431925324119bac1bc7979664b4fa9843c0e5fcdcf1e000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431925324119bac1bc7979664b4fa9843c0e5fcdcf1e000">操作文件和目录</a>
    </li>
    
    
    <li id="off-00143192607210600a668b5112e4a979dd20e4661cc9c97000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143192607210600a668b5112e4a979dd20e4661cc9c97000">序列化</a>
    </li>
    
    

    
    
    <li id="off-0014319272686365ec7ceaeca33428c914edf8f70cca383000" style="margin-left:1em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319272686365ec7ceaeca33428c914edf8f70cca383000">进程和线程</a>
    </li>
    
        
    
    <li id="off-001431927781401bb47ccf187b24c3b955157bb12c5882d000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431927781401bb47ccf187b24c3b955157bb12c5882d000">多进程</a>
    </li>
    
    
    <li id="off-00143192823818768cd506abbc94eb5916192364506fa5d000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143192823818768cd506abbc94eb5916192364506fa5d000">多线程</a>
    </li>
    
    
    <li id="off-001431928972981094a382e5584413fa040b46d46cce48e000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431928972981094a382e5584413fa040b46d46cce48e000">ThreadLocal</a>
    </li>
    
    
    <li id="off-0014319292979766bd3285c9d6b4942a8ea9b4e9cfb48d8000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319292979766bd3285c9d6b4942a8ea9b4e9cfb48d8000">进程 vs. 线程</a>
    </li>
    
    
    <li id="off-001431929340191970154d52b9d484b88a7b343708fcc60000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431929340191970154d52b9d484b88a7b343708fcc60000">分布式进程</a>
    </li>
    
    

    
    
    <li id="off-00143193331387014ccd1040c814dee8b2164bb4f064cff000" style="margin-left:1em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143193331387014ccd1040c814dee8b2164bb4f064cff000">正则表达式</a>
    </li>
    
    
    <li id="off-0014319347182373b696e637cc04430b8ee2d548ca1b36d000" style="margin-left:1em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319347182373b696e637cc04430b8ee2d548ca1b36d000">常用内建模块</a>
    </li>
    
        
    
    <li id="off-001431937554888869fb52b812243dda6103214cd61d0c2000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431937554888869fb52b812243dda6103214cd61d0c2000">datetime</a>
    </li>
    
    
    <li id="off-001431953239820157155d21c494e5786fce303f3018c86000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431953239820157155d21c494e5786fce303f3018c86000">collections</a>
    </li>
    
    
    <li id="off-001431954588961d6b6f51000ca4279a3415ce14ed9d709000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431954588961d6b6f51000ca4279a3415ce14ed9d709000">base64</a>
    </li>
    
    
    <li id="off-001431955007656a66f831e208e4c189b8a9e9f3f25ba53000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431955007656a66f831e208e4c189b8a9e9f3f25ba53000">struct</a>
    </li>
    
    
    <li id="off-0014319556588648dd1fb0047a34d0c945ee33e8f4c90cc000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319556588648dd1fb0047a34d0c945ee33e8f4c90cc000">hashlib</a>
    </li>
    
    
    <li id="off-0015108777177966ef0f4f8510a41b3b8c48cdcf7047b2d000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0015108777177966ef0f4f8510a41b3b8c48cdcf7047b2d000">hmac</a>
    </li>
    
    
    <li id="off-00143200162233153835cfdd1a541a18ddc15059e3ddeec000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143200162233153835cfdd1a541a18ddc15059e3ddeec000">itertools</a>
    </li>
    
    
    <li id="off-001478651770626de401ff1c0d94f379774cabd842222ff000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001478651770626de401ff1c0d94f379774cabd842222ff000">contextlib</a>
    </li>
    
    
    <li id="off-001432688314740a0aed473a39f47b09c8c7274c9ab6aee000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432688314740a0aed473a39f47b09c8c7274c9ab6aee000">urllib</a>
    </li>
    
    
    <li id="off-001432002075057b594f70ecb58445da6ef6071aca880af000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432002075057b594f70ecb58445da6ef6071aca880af000">XML</a>
    </li>
    
    
    <li id="off-0014320023122880232500da9dc4a4486ad00426f081c15000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014320023122880232500da9dc4a4486ad00426f081c15000">HTMLParser</a>
    </li>
    
    

    
    
    <li id="off-001432002680493d1babda364904ca0a6e28374498d59a7000" style="margin-left:1em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432002680493d1babda364904ca0a6e28374498d59a7000">常用第三方模块</a>
    </li>
    
        
    
    <li id="off-0014320027235877860c87af5544f25a8deeb55141d60c5000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014320027235877860c87af5544f25a8deeb55141d60c5000">Pillow</a>
    </li>
    
    
    <li id="off-0015109021115795adfc5c8629f4f98985063b5a7e3ff87000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0015109021115795adfc5c8629f4f98985063b5a7e3ff87000">requests</a>
    </li>
    
    
    <li id="off-001510905171877ca6fdf08614e446e835ea5d9bce75cf5000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001510905171877ca6fdf08614e446e835ea5d9bce75cf5000">chardet</a>
    </li>
    
    
    <li id="off-001511052957192bb91a56a2339485c8a8c79812b400d49000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001511052957192bb91a56a2339485c8a8c79812b400d49000">psutil</a>
    </li>
    
    

    
    
    <li id="off-001432712108300322c61f256c74803b43bfd65c6f8d0d0000" style="margin-left:1em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432712108300322c61f256c74803b43bfd65c6f8d0d0000">virtualenv</a>
    </li>
    
    
    <li id="off-00143200341926302f99cf6f6414dca9dfaaf6e5a25a5b1000" style="margin-left:1em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143200341926302f99cf6f6414dca9dfaaf6e5a25a5b1000">图形界面</a>
    </li>
    
    
    <li id="off-0014320037274136d31bd9979d648cd822375394e29a871000" style="margin-left:1em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014320037274136d31bd9979d648cd822375394e29a871000">网络编程</a>
    </li>
    
        
    
    <li id="off-0014320037768360d53e4e935ca4a1f96eed1c896ad1217000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014320037768360d53e4e935ca4a1f96eed1c896ad1217000">TCP/IP简介</a>
    </li>
    
    
    <li id="off-001432004374523e495f640612f4b08975398796939ec3c000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432004374523e495f640612f4b08975398796939ec3c000">TCP编程</a>
    </li>
    
    
    <li id="off-001432004977916a212e2168e21449981ad65cd16e71201000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432004977916a212e2168e21449981ad65cd16e71201000">UDP编程</a>
    </li>
    
    

    
    
    <li id="off-001432005156604f38836be1707453eb025ce8c3079978d000" style="margin-left:1em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432005156604f38836be1707453eb025ce8c3079978d000">电子邮件</a>
    </li>
    
        
    
    <li id="off-001432005226355aadb8d4b2f3f42f6b1d6f2c5bd8d5263000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432005226355aadb8d4b2f3f42f6b1d6f2c5bd8d5263000">SMTP发送邮件</a>
    </li>
    
    
    <li id="off-0014320098721191b70a2cf7b5441deb01595edd8147196000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014320098721191b70a2cf7b5441deb01595edd8147196000">POP3收取邮件</a>
    </li>
    
    

    
    
    <li id="off-001432010325987131e75bf6b3543429a2975f88ce8ffa9000" style="margin-left:1em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432010325987131e75bf6b3543429a2975f88ce8ffa9000">访问数据库</a>
    </li>
    
        
    
    <li id="off-001432010494717e1db78cd172e4d52b853e7fd38d6985c000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432010494717e1db78cd172e4d52b853e7fd38d6985c000">使用SQLite</a>
    </li>
    
    
    <li id="off-0014320107391860b39da6901ed41a296e574ed37104752000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014320107391860b39da6901ed41a296e574ed37104752000">使用MySQL</a>
    </li>
    
    
    <li id="off-0014320114981139589ac5f02944601ae22834e9c521415000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014320114981139589ac5f02944601ae22834e9c521415000">使用SQLAlchemy</a>
    </li>
    
    

    
    
    <li id="off-0014320118765877e93ecea4e6449acb157e9efae8b40b6000" style="margin-left:1em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014320118765877e93ecea4e6449acb157e9efae8b40b6000">Web开发</a>
    </li>
    
        
    
    <li id="off-001432011939547478fd5482deb47b08716557cc99764e0000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432011939547478fd5482deb47b08716557cc99764e0000">HTTP协议简介</a>
    </li>
    
    
    <li id="off-0014320122322996f770fbf5da84ead84a1731e1dde129f000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014320122322996f770fbf5da84ead84a1731e1dde129f000">HTML简介</a>
    </li>
    
    
    <li id="off-001432012393132788f71e0edad4676a3f76ac7776f3a16000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432012393132788f71e0edad4676a3f76ac7776f3a16000">WSGI接口</a>
    </li>
    
    
    <li id="off-001432012745805707cb9f00a484d968c72dbb7cfc90b91000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432012745805707cb9f00a484d968c72dbb7cfc90b91000">使用Web框架</a>
    </li>
    
    
    <li id="off-0014320129740415df73bf8f81e478982bf4d5c8aa3817a000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014320129740415df73bf8f81e478982bf4d5c8aa3817a000">使用模板</a>
    </li>
    
    

    
    
    <li id="off-00143208573480558080fa77514407cb23834c78c6c7309000" style="margin-left:1em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143208573480558080fa77514407cb23834c78c6c7309000">异步IO</a>
    </li>
    
        
    
    <li id="off-001432090171191d05dae6e129940518d1d6cf6eeaaa969000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432090171191d05dae6e129940518d1d6cf6eeaaa969000">协程</a>
    </li>
    
    
    <li id="off-001432090954004980bd351f2cd4cc18c9e6c06d855c498000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432090954004980bd351f2cd4cc18c9e6c06d855c498000">asyncio</a>
    </li>
    
    
    <li id="off-00144661533005329786387b5684be385062a121e834ac7000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00144661533005329786387b5684be385062a121e834ac7000">async/await</a>
    </li>
    
    
    <li id="off-0014320981492785ba33cc96c524223b2ea4e444077708d000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014320981492785ba33cc96c524223b2ea4e444077708d000">aiohttp</a>
    </li>
    
    

    
    
    <li id="off-001432170876125c96f6cc10717484baea0c6da9bee2be4000" style="margin-left:1em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432170876125c96f6cc10717484baea0c6da9bee2be4000">实战</a>
    </li>
    
        
    
    <li id="off-001432170937506ecfb2f6adf8e4757939732f3e32b781c000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432170937506ecfb2f6adf8e4757939732f3e32b781c000">Day 1 - 搭建开发环境</a>
    </li>
    
    
    <li id="off-00143217133614028a244ea855b40a586b551c616d3b2c9000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143217133614028a244ea855b40a586b551c616d3b2c9000">Day 2 - 编写Web App骨架</a>
    </li>
    
    
    <li id="off-0014323389656575142d0bcfeec434e9639a80d3684a7da000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014323389656575142d0bcfeec434e9639a80d3684a7da000">Day 3 - 编写ORM</a>
    </li>
    
    
    <li id="off-001432338991719a4c5c42ef08e4f44ad0f293ad728a27b000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432338991719a4c5c42ef08e4f44ad0f293ad728a27b000">Day 4 - 编写Model</a>
    </li>
    
    
    <li id="off-001432339008728d0ddbe19ee594980be3f0644a9371894000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432339008728d0ddbe19ee594980be3f0644a9371894000">Day 5 - 编写Web框架</a>
    </li>
    
    
    <li id="off-001432339034336cbf72acd43354d72831461e3871d9f2e000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432339034336cbf72acd43354d72831461e3871d9f2e000">Day 6 - 编写配置文件</a>
    </li>
    
    
    <li id="off-001432339095180ce91c53cdab841bfa9c342a297b886fe000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432339095180ce91c53cdab841bfa9c342a297b886fe000">Day 7 - 编写MVC</a>
    </li>
    
    
    <li id="off-001432339124159f00f6ab876c44349a3fd8eb26d0c291e000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432339124159f00f6ab876c44349a3fd8eb26d0c291e000">Day 8 - 构建前端</a>
    </li>
    
    
    <li id="off-0014323391480651a75b5fda4cb4c789208191682fc2c70000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014323391480651a75b5fda4cb4c789208191682fc2c70000">Day 9 - 编写API</a>
    </li>
    
    
    <li id="off-001432339169382f45b9bd7b45d47ceb3e2b42846e0e991000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432339169382f45b9bd7b45d47ceb3e2b42846e0e991000">Day 10 - 用户注册和登录</a>
    </li>
    
    
    <li id="off-00143233918656129f4ad3ac29e4f728dc72b5d2368215a000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143233918656129f4ad3ac29e4f728dc72b5d2368215a000">Day 11 - 编写日志创建页</a>
    </li>
    
    
    <li id="off-001432339210950e063b4795d574036bc5dcf0c2449bc52000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432339210950e063b4795d574036bc5dcf0c2449bc52000">Day 12 - 编写日志列表页</a>
    </li>
    
    
    <li id="off-001432339228196a8eb6fb8832b48b5aa0d740346536ead000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432339228196a8eb6fb8832b48b5aa0d740346536ead000">Day 13 - 提升开发效率</a>
    </li>
    
    
    <li id="off-001432339247097eea476bf61f8496092cc1b663eae1848000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432339247097eea476bf61f8496092cc1b663eae1848000">Day 14 - 完成Web App</a>
    </li>
    
    
    <li id="off-0014323392805925d5b69ddad514511bf0391fe2a0df2b0000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014323392805925d5b69ddad514511bf0391fe2a0df2b0000">Day 15 - 部署Web App</a>
    </li>
    
    
    <li id="off-001432339330096121ae7e38be44570b7fbd0d8faae26f6000" style="margin-left:2em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432339330096121ae7e38be44570b7fbd0d8faae26f6000">Day 16 - 编写移动App</a>
    </li>
    
    

    
    
    <li id="off-00143278155868605a65e244e6642dfa533753e6338ab5b000" style="margin-left:1em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143278155868605a65e244e6642dfa533753e6338ab5b000">FAQ</a>
    </li>
    
    
    <li id="off-0014323396477522f8ff26917934f53b49559ab4dc5eab2000" style="margin-left:1em;">
        <a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014323396477522f8ff26917934f53b49559ab4dc5eab2000">期末总结</a>
    </li>
    
    

    </ul>
    <div class="x-placeholder"></div>

            </div>
        </div>
    </div>


    <div id="footer">
        <div class="x-footer uk-container x-container">
            <hr>
            <div class="uk-grid">
                <div class="x-footer-copyright uk-width-small-1-2 uk-width-medium-1-3">
                    <p>
                        <a href="/">廖雪峰的官方网站</a>&copy;2017 v4edf87a
                        <br>
                        Powered by <a href="https://github.com/michaelliao/itranswarp.js" target="_blank">iTranswarp.js</a>
                    </p>
                </div>
                <div class="uk-width-small-1-2 uk-width-medium-1-3 x-hidden-tiny">
                    <a href="/feed" target="_blank" class="uk-icon-button uk-icon-rss" data-uk-tooltip title="Subscribe the RSS"></a>
                    <a href="https://github.com/michaelliao/itranswarp.js" target="_blank" class="uk-icon-button uk-icon-github" data-uk-tooltip title="View source code on GitHub"></a>
                    <a href="https://twitter.com/liaoxuefeng" target="_blank" class="uk-icon-button uk-icon-twitter" data-uk-tooltip title="Follow author on Twitter"></a>
                    <a href="https://www.weibo.com/liaoxuefeng" target="_blank" class="uk-icon-button uk-icon-weibo uk-visible-large uk-hidden-medium" data-uk-tooltip title="Follow author on Weibo"></a>
                </div>
                <div class="uk-width-medium-1-3 uk-hidden-small">
                    <p>
                        <a href="https://github.com/michaelliao/itranswarp.js/issues" target="_blank">意见反馈</a>
                        <br>
                        <a href="https://github.com/michaelliao/itranswarp.js/blob/master/LICENSE" target="_blank">使用许可</a>
                    </p>
                </div>
            </div>
        </div>
    </div>

    <div id="modal-signin" class="uk-modal">
        <div class="uk-modal-dialog">
            <a class="uk-modal-close uk-close"></a>
            <div class="uk-modal-header">
                <h2>Please Sign In</h2>
            </div>
            <p>You can sign in directly without register:</p>
            
            <h3><a href="/auth/from/weibo"><i class="uk-icon-weibo"></i> 使用新浪微博登录</a></h3>
            
            <p>You need authorize to allow connect to your social passport for the first time.</p>
        </div>
    </div>

    <div id="oldBrowser">
        <div class="uk-alert uk-alert-danger" data-uk-alert>
            <a href="#0" class="uk-alert-close uk-close"></a>
            <p>
                WARNING: You are using an old browser that does not support HTML5.
                Please choose a modern browser (<a href="https://www.google.com/chrome" target="_blank">Chrome</a> / <a href="https://www.microsoft.com/windows/microsoft-edge" target="_blank">Microsoft Edge</a> / <a href="https://www.mozilla.org/firefox/" target="_blank">Firefox</a> / <a href="https://www.apple.com/safari/" target="_blank">Sarafi</a>) to get a good experience.
            </p>
        </div>
    </div>
</body>
</html>
"""

# 网页解析器[解析页面数据]
# soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')
soup = BeautifulSoup(html_doc, 'html.parser')  # 结构化分析[BeautifulSoup --> DOM]
print("所有链接-->find_all:")

links = soup.find_all('a')
for link in links:
    print(link.name, link['href'], link.get_text())

print('获取指定链接-->find:')
link = soup.find('a', href='net://example.com/tillie')
print(link.name, link['href'], link.get_text())

print("正则匹配:")
link = soup.find('a', href=re.compile(r"ac"))
print(link.name, link['href'], link.get_text())

print("爬取p段落:")
link = soup.find('p', class_='title')
print(link.name, link.get_text())

# 廖雪峰python博客测试
soup = BeautifulSoup(liaoxuefeng, 'html.parser')  # 结构化分析[BeautifulSoup --> DOM]
print("所有链接-->find_all:")

# links = soup.find_all('a', href=re.compile(r"wiki"))
# for link in links:
#     print(link.name, link['href'], link.get_text())

from urllib import request, parse


def download(url):
    if url is None:
        return None

    req = request.Request(url)
    # req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    req.add_header('User-Agent', 'Mozilla/6.0')
    with request.urlopen(req, {}) as f:
        if f.status != 200:
            return None
        return f.read()


soup = BeautifulSoup(download(
    'https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431752945034eb82ac80a3e64b9bb4929b16eeed1eb9000'),
                     'html.parser')

# links = soup.find_all('a', href=re.compile(r"/wiki/00(.*)"))
links = soup.find_all('a', class_="x-wiki-index-item")
for link in links:
    print(link.name, link['href'], link.get_text())

h4s = soup.find_all('h4')
for h4 in h4s:
    print('h4 is:', h4.get_text())
