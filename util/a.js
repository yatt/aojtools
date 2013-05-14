        var rec = function(j, stk, notindent){
            // TODO
            var d = rsp[j].depth
            var once = rsp[j].freq === '1'
            var head = new Array(notindent ? d + 1: d + 2).join('    ')

            if (rsp[j].type === '') {
                if (!once) console.log(head + 'for i' + d + ' in len(' + makerepr(j) + '):')
                for (var k = j + 1; k < rsp.length && d !== rsp[k].depth; k++)
                    if (d + 1 == rsp[k].depth)
                        rec(k, once ? stk: stk.concat([j]), rsp[j].type === '')
            }else{
                console.log(head + makerepr(j,stk) + ' = ' + fn[rsp[j].type] + '(' + repr + ')')
            }
        }
