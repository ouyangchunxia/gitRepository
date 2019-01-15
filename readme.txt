postman功能测试用例集：entrytask.postman_collection.json

使用newman跑自动化脚本的命令：newman run entrytask.postman_collection.json --reporters json --reporter-json-export entryTaskReport.json 

postman功能测试报告：entryTaskReport.json 和 entryTaskReport.txt

postman接口自动化设计流程图：postman接口自动化测试流程.pages

性能测试脚本：entryTask_loadTest.jmx

性能测试命令：jmeter -n -t entryTask_loadTest.jmx -l entryTask_loadTest_result1-60s.log

性能测试报告：entryTask_loadTest_result1-60s.log（并发量为1，跑60s的结果。测试中并发量超过7时，会出现err）
