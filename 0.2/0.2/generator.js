// -----------------------------------------------------------------------------
// title  : aojapi.js
// author : brainfs/yatt
// date   : 2012/05/23 
// license: MIT
// desc   :  
//    aoj (aizu online judge)のAPIリファレンスから、APIクライアントコード
//    生成に使う情報を抽出、フォーマット関数を呼び出します。
// usage  :
//    chrome等で
//      http://judge.u-aizu.ac.jp/onlinejudge/api.jsp
//    を開いてコンソールで以下を実行してください。
// -----------------------------------------------------------------------------

(function(formatter){

var main = function(){
    // apiのテーブルを一覧取得
    var api = $(".infoBack")
        .filter(function(i, item){ return item.children.length > 0 })
        .map(function(i,n){ n=$(n); return {
            parameter: prmfn($(n.find('table')[0])),
            response: bdyfn($(n.find('table')[1])),
            name: n.find('h3')[0].innerText.replace(/ /g, ''),
            desc: n.find('p')[0].innerText,
            url: n.find('p')[1].innerText
                    // .xml only
                    .split('\n')[0]
                    // replace parameter string to format string
                    .replace(/<messageId>/g, '$')
                    .replace(/<problemId>/g, '$')
                    .replace(/<messageId>/g, '$')
                    .replace(/<threadId>/g, '$')
                    .replace(/<number>/g, '$')
            }})
    formatter(api)
}

var fn = function(t,i){ return t.children[i] && t.children[i].innerText || ''}

// ----------------------------------
// リスエスト側
// ----------------------------------
var prmfn = function(req){
    return req
        .find("tr")
        .filter(function(i){ return i > 0 })
        .map(function(i,item){ return {
            name: fn(item,0),
            desc: fn(item,1),
            type: fn(item,2),
            required: fn(item,3) == 'yes',
            sample: fn(item,4)
            }})
        .filter(function(i,n){ return n.name !== '' })
}

// ----------------------------------
// レスポンス側
// ----------------------------------
var bdyfn = function(bdy){
    // パラメータの取得
    
    // Thread Search API移行はfrequencyが無い
    var speccase = bdy.find('tr')[0].innerText.indexOf('Freq') == -1

    bdy = bdy
        .find("tr")
        .filter(function(i){ return i > 0 })
        .map(function(i,item){ var fn0=fn(item,0); return {
            name: fn0.indexOf('-') == -1
                        ? fn0
                        : fn0.substring(fn0.indexOf('-') + 2, fn0.length),
            desc: fn(item,1),
            type: fn(item,2),
            freq: speccase ? '1': fn(item,3),
            sample: fn(item, speccase ? 3: 4),
            depth: fn0.indexOf('-') == -1 ? 0: fn0.indexOf('-') / 2,
            path: '',
            }})
        .filter(function(i,n){ return n.name !== '' })
    
    // attribute_id以下にパラメータではない4つの説明がある。その部分を削除
    var loop = bdy.length;
    for (var i = 0; i < loop; i++) {
        if (bdy[i].name == 'attribute_id') {
            bdy = bdy.slice(0, i).add( bdy.slice(i + 5) )
            break
        }
    }
    var recursion = function (idx, stk){
/*
console.log(idx);
console.log(bdy[idx].name);
console.log(stk);
*/
        var path = (stk.length>0?'/':'') + stk.join('/') + '/' + idx
        bdy[idx].path = path

        if (idx + 1 === bdy.length)
            return

        var n = bdy[idx + 1].depth - bdy[idx].depth
        if (n === 0)
            recursion(idx + 1, stk)
        else
        if (n > 0)
            recursion(idx + 1, stk.concat([idx]))
        else
            recursion(idx + 1, stk.slice(0, -n))
    }
    if (bdy.length)
        recursion(0, [])
//console.log(bdy);

    return bdy
}

main()

})(function(api){
// -------------------------------------------------------------
// replace content of this function
// -------------------------------------------------------------

    console.log('#! /usr/bin/python2.6')
    console.log('# coding: utf-8')
    console.log('')
    console.log('import parse')
    console.log('')
    console.log('def time2date(s):')
    console.log('    return time.gmtime(int(s) / 1000.)')
    console.log('def date2str(d):')
    console.log('    return  time.strftime(\'%Y/%m/%d %H:%M:%S\', d)')
    console.log('')
    console.log('')
    console.log('')
    for (var i = 0; i < api.length; i++){

        var prm = api[i].parameter
        // param
        var required = $.makeArray(
            $(api[i].parameter)
            .filter(function(i, n){ return n.required })
            .map(function(i,n){ return n.name })
            )
        console.log('def ' + api[i].name + '(' + required.join(', ') + (required.length > 0 ? ', ' : '') + '**kwargs):')

        // format check
        console.log('    # type check')
        for (var j = 0; j < prm.length; j++){
            var repr = {
                true: prm[j].name,
                false: 'kwargs[\'' + prm[j].name + '\']',
            }[prm[j].required]

            var selection = {
                'string': '[str, unicode]',
                'integer': '[int, long]',
                'long integer': '[int, long]',
            }[prm[j].type]

            var mustbe = {
                'string': 'string',
                'integer': 'integer',
                'long integer': 'integer',
            }[prm[j].type]

            var r = (prm[j].required ? '': '\'' + prm[j].name + '\' in kwargs and ')

            console.log('    if ' + r + 'type(' + repr + ') not in ' + selection + ':')
            console.log('        raise Exception(\'parameter \\\'' + prm[j].name + '\\\' must be ' + mustbe + '\')')
        }
        
        console.log('    # initialize url, fill if necessary')
        // set parameter
        var url = api[i].url
        var prm2 = prm
        console.log('    url = \'' + api[i].url + '\'')
        while (url.indexOf('$') > -1){
            var repr = {
                true: prm2[0].name,
                false: 'kwargs[\'' + prm2[0].name + '\']',
            }[prm2[0].required]
            console.log('    url = url.replace(\'$\', ' + repr + ', 1)')

            prm2 = prm2.slice(1)
            url = url.replace('$', '')
        }

        console.log('    # set parameter')
        console.log('    prm = kwargs.copy()')
        for (var j = 0; j < prm2.length; j++){
            if (prm[j].required)
                console.log('    prm[\'' + prm2[j].name + '\'] = ' + prm2[j].name)
        }
        
        console.log('    # call api')
        console.log('    rsp = parse.fromweb(url, prm)')
        
        // normalize response xml
        console.log('    # format')
        var rsp = api[i].response
        var fn = {
            'string': 'str',
            'integer': 'int',
            'long integer': i<14 ? 'time2date': 'int',
            'long': i<14 ? 'time2date': 'int',
            'float': 'float',
            'Date': 'date2str',
        }

        var makerepr = function(idx, stk){
            stk = stk || []
            var lst = rsp[idx].path.slice(1).split('/')
            //lst = $.makeArray($(lst).map(function(i,n){ return rsp[n].name }))
            lst = $.makeArray($(lst).map(function(i,n){
                var idx = stk.indexOf(parseInt(n))
                
                return idx === -1 ? rsp[n].name: rsp[n].name + '[i' + idx + ']'
            }))
            return repr = 'rsp.' + lst.join('.')
        }
        var rec = function(j, stk){
            var d = rsp[j].depth
            var head = new Array(d + 2).join('    ')
            if (rsp[j].type === ''){
                console.log(head + 'for i' + d + ' in len(' + makerepr(j) + '):')
                for (var k = j + 1; k < rsp.length && d !== rsp[k].depth; k++)
                    if (d + 1 == rsp[k].depth)
                        rec(k, stk.concat([j]))
            }else
            if (stk.legnth === 0){
                console.log(head + makerepr(j) + ' = ' + fn[rsp[j].type] + '(' + repr + ')')
            }else{
                console.log(head + makerepr(j,stk) + ' = ' + fn[rsp[j].type] + '(' + repr + ')')
            }
        }
        for (var j = 0; j < rsp.length; j++)
            if (rsp[j].depth == 0)
                rec(j, [])
    
        
        console.log('    return rsp')
        //
        console.log('')
    }
/*
    for (var i = 0; i < api.length; i++){
        console.log('=======================================')
        console.log(i)
        console.log(api[i].name)
        console.log(api[i].url[0])
        console.log('=======================================')

        console.log('parameter:')
        var prm = api[i].parameter
        for (var j = 0; j < prm.length; j++)
            console.log('    ' + prm[j].name)

        console.log('response:')
        var rsp = api[i].response
        for (var j = 0; j < rsp.length; j++){
            var head = new Array(rsp[j].depth + 2).join('    ')
            console.log(head + (rsp[j].freq == '1' ? '': '+ ') + rsp[j].name)
        }
    }
*/
})
