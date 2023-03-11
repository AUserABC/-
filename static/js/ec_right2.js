var ec_right2 = echarts.init(document.getElementById('r2'), "dark");

var ddd = [{'name': '肺炎', 'value': '12734670'}, {'name': '实时', 'value': '12734670'},
{'name': '新型', 'value': '12734670'}];
var ec_right2_Option = {
                        backgroundColor: 'black',
						title : {
						    text : "今日疫情热搜",
						    textStyle : {
						        color : 'white',
						    },
						    left : 'left'
						},
                        tooltip: {
                            show: true,
                            padding: 12,
                            extraCssText: "box-shadow: 0px 2px 8px 0px #cacaca;border-radius: 4px;opacity: 0.9;",
                            formatter: function(p) {
                                return `热度：${p.data.value}<br/> 药物：${
                                p.data.script}`;
                            }
                        },
                         grid: {
                            containLabel: true,
                            left: '0%',
                            right: '6%',
                            bottom: '3%',
                            top: 30,
                            containLabel: true
                        },
                        series: [{

                                type: 'wordCloud',
								//drawOutOfBound:true,
                                gridSize: 1,
                                sizeRange: [12, 85],
                                rotationRange: [-45, 0, 45, 90],
                                // maskImage: maskImage,
                                textStyle: {
                                    normal: {
                                        color: function () {
                                            return 'rgb(' +
                                                    Math.round(Math.random() * 255) +
                                                    ', ' + Math.round(Math.random() * 255) +
                                                    ', ' + Math.round(Math.random() * 255) + ')'
                                        }
                                    }
                                },

                                left: 'center',
                                top: 'center',
                                width: '96%',
                                height: '100%',
                                //shape: 'pentagon',

                                right: null,
                                bottom: null,
                                // width: 300,
                                // height: 200,
                                // top: 20,
                                data:  []
                            }]
                    };

ec_right2.setOption(ec_right2_Option);
