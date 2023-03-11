var ec_left21 = echarts.init(document.getElementById('l21'), "dark");
var ec_left21_Option = {
backgroundColor: 'black',
//标题样式
	title: {
		text: "今日药品热搜",
		textStyle: {
			// color: 'white',
		},
		left: 'left',
	},
  dataset: {

    source: [
      ['score', 'amount', 'product','script'],
      [89.3, 58212, 'Matcha Latte'],
      [57.1, 78254, 'Milk Tea'],
      [74.4, 41032, 'Cheese Cocoa'],
      [50.1, 12755, 'Cheese Brownie'],
      [89.7, 20145, 'Matcha Cocoa'],
      [68.1, 79146, 'Tea'],
      [19.6, 91852, 'Orange Juice'],
      [10.6, 101852, 'Lemon Juice'],
      [32.7, 20112, 'Walnut Brownie']
    ]
  },

  xAxis: { name: 'amount',show: false},
  yAxis: { type: 'category'},
  visualMap: {
    orient: 'horizontal',
    left: 'center',
    min: 0,
    max: 100,
    text: ['High Score', 'Low Score'],
    // Map the score column to color
    dimension: 0,
    inRange: {
      color: ['#00FFFF', '#FFCE34', '#FF0000']
    }
  },

  grid: {
        containLabel: true,
		left: '0%',
		right: '6%',
		bottom: '5%',
		top: 30,
		containLabel: true
	},
   tooltip: {

          trigger: 'item',
          position: 'right',
        show: true,
        padding: 12,
        extraCssText: "box-shadow: 0px 2px 8px 0px #cacaca;border-radius: 4px;opacity: 0.9;",
        formatter: function(p) {
          console.log(p)
          return `药品：${p.value[2]}<br\>功效：${p.value[3]}<br\>热度：${p.value[1]}`;

        }
    },
  series: [
    {
      type: 'bar',
      encode: {
        // Map the "amount" column to X axis.
        x: 'amount',
        // Map the "product" column to Y axis
        y: 'product'
      },
      script:[]
    }
  ]

};
    ec_left21.setOption(ec_left21_Option);