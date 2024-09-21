import time

class report_html:
    def __init__(self):
        pass

    def create_html(self, total_result):
        times = time.strftime("%Y%m%d-%H%M%S")
        html_name = times + '测试报告.html'

        total_result_all = [['product', '总数', '成功', '失败']]
        for name in total_result:
            result = []
            result.append(name)
            for num in total_result[name].split(','):
                result.append(num)

            total_result_all.append(result)

        # 打开文件，准备写入
        file = open(html_name, 'w', encoding='utf-8')
        # 写入HTML界面中
        message = """ 
        <!DOCTYPE html>
        <html lang="zh-CN" style="height: 100%%">
        <head>
          <meta charset="utf-8">
        </head>
        <body style="height: 100%%; margin: 0">
          <div id="container" style="height: 100%%"></div>
        
        
          <script type="text/javascript" src="https://fastly.jsdelivr.net/npm/echarts@5.4.1/dist/echarts.min.js"></script>
          <!-- Uncomment this line if you want to dataTool extension
          <script type="text/javascript" src="https://fastly.jsdelivr.net/npm/echarts@5.4.1/dist/extension/dataTool.min.js"></script>
          -->
          <!-- Uncomment this line if you want to use gl extension
          <script type="text/javascript" src="https://fastly.jsdelivr.net/npm/echarts-gl@2/dist/echarts-gl.min.js"></script>
          -->
          <!-- Uncomment this line if you want to echarts-stat extension
          <script type="text/javascript" src="https://fastly.jsdelivr.net/npm/echarts-stat@latest/dist/ecStat.min.js"></script>
          -->
          <!-- Uncomment this line if you want to use map
          <script type="text/javascript" src="https://fastly.jsdelivr.net/npm/echarts@4.9.0/map/js/china.js"></script>
          <script type="text/javascript" src="https://fastly.jsdelivr.net/npm/echarts@4.9.0/map/js/world.js"></script>
          -->
          <!-- Uncomment these two lines if you want to use bmap extension
          <script type="text/javascript" src="https://api.map.baidu.com/api?v=3.0&ak=YOUR_API_KEY"></script>
          <script type="text/javascript" src="https://fastly.jsdelivr.net/npm/echarts@5.4.1/dist/extension/bmap.min.js"></script>
          -->
        
          <script type="text/javascript">
            var dom = document.getElementById('container');
            var myChart = echarts.init(dom, null, {
              renderer: 'canvas',
              useDirtyRect: false
            });
            var app = {};
        
            var option;
        
            option = {
          color: ['#2b40e0','#2be067','#e02b2b'],
          legend: {},
          tooltip: {},
          dataset: {
            source: %s
            
          },
          xAxis: { type: 'category' },
          yAxis: {},
          // Declare several bar series, each will be mapped
          // to a column of dataset.source by default.
          series: [{ type: 'bar' }, { type: 'bar' }, { type: 'bar' }]
        };
        
            if (option && typeof option === 'object') {
              myChart.setOption(option);
            }
        
            window.addEventListener('resize', myChart.resize);
          </script>
        </body>
        </html>
        """%(total_result_all)

        file.write(message)
        file.close()

        return html_name