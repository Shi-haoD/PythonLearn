from pyecharts import Pie

atter = ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
V1=[11,12,14,10,20,10]
V2=[19,22,34,22,42,16]
pie=Pie('饼图-玫瑰图',title_pos='center',width=1000)
pie.add("商品A",atter,V1,center=[25,50],is_random=True,radius=[30,75],rosetype='radius',is_more_utils=True)
pie.add("商品B",atter,V2,center=[75,50],is_random=True,radius=[30,75],rosetype='area',is_more_utils=True,is_legend_show=False,is_label_show=True)
pie.show_config()
pie.render('ss.html')
