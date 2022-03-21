var ec_right2 = echarts.init(document.getElementById('r2'));
var ec_right2_option = {
     title: {
    text: '车型占比统计',
    textStyle:{
      color:"white",
      fontSize:"30",
      fontWeight:"bold",
      fontFamily:"幼圆",

    },
    left: 'center'
  },
  tooltip: {
    trigger: 'item',
    formatter: '{a} <br/>{b} : {c} ({d}%)'
  },
  legend: {
    type: 'scroll',
    orient: 'vertical',
    right: 10,
    top: 20,
    bottom: 20,
    data: []
  },
  series: [
    {
      name: 'CX',
      type: 'pie',
      radius: '55%',
      center: ['40%', '50%'],
      data: [],
      emphasis: {
        itemStyle: {
          shadowBlur: 10,
          shadowOffsetX: 0,
          shadowColor: 'rgba(0, 0, 0, 0.5)'
        }
      }
    }
  ]
};
ec_right2.setOption(ec_right2_option);
