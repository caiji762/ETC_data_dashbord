var ec_right1 = echarts.init(document.getElementById('r1'));
var ec_right1_option = {
     title: {
    text: '车牌地区Top5',
    textStyle:{
      color:"white",
      fontFamily:"幼圆",
      fontSize:30

    },
  },
  tooltip: {
    trigger: 'axis',
    axisPointer: {
      type: 'shadow'
    }
  },
  legend: {
  icon: 'rect',
        itemWidth: 14,
        itemHeight: 5,
        itemGap: 13,
        data: ['客车', '货车'],
        right: '10px',
        top: '0px',
        textStyle: {
            fontSize: 15,
            color: '#fff'
        }},
  grid: {
    left: '3%',
    right: '4%',
    bottom: '3%',
    containLabel: true
  },
  xAxis: {
    type: 'value',
    boundaryGap: [0, 0.01]
  },
  yAxis: {
    type: 'category',
    data: ['Brazil', 'Indonesia', 'USA', 'India', 'China', 'World']
  },
  series: [
    {
      name: '客车',
      type: 'bar',
      data: [18203, 23489, 29034, 104970, 131744, 630230]
    },
    {
      name: '货车',
      type: 'bar',
      data: [19325, 23438, 31000, 121594, 134141, 681807]
    }
  ]
};
ec_right1.setOption(ec_right1_option)