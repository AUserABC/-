var ec_right1 = echarts.init(document.getElementById('r1'),"dark");
var ec_right1_Option = {
	backgroundColor: 'black',
	//标题样式
	title : {
	    text : "城市确诊TOP5",
	    textStyle : {
	        color : 'white',
	    },
	    left : 'left'
	},
	  color: ['#3398DB'],
	    tooltip: {
	        trigger: 'axis',
	        axisPointer: {            // 坐标轴指示器，坐标轴触发有效
	            type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
	        }
	    },
	//图形位置
	grid: {
		left: '3%',
		right: '6%',
		bottom: '4%',
		top: 50,
		containLabel: true
	},
    xAxis: {
        type: 'category',
        data: []
    },
    yAxis: {
        type: 'value'
    },
    series: [{
        data: [],
        type: 'bar',
		barMaxWidth:"50%"
    }]
};
ec_right1.setOption(ec_right1_Option);