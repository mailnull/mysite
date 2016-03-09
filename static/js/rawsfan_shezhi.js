function shezhi(room){
	$("#topNav li").removeClass("hover");
	$("dt,dd").removeClass("hover");//清除样式
	$("li#"+room).addClass("hover"); //添加样式
	$("#ktKG b").text($("small#"+room).text());//设置关闭"房间"空调字样
	$("b#stmd").text($("b."+room).text());//设置空调状态"状态"字样
	$("b#KT_room").text($("small#"+room).text()+":");//设置空调状态"房间"字样
	 if($("small."+room).text()){   //检查空调状态”温度“  不为空
	  temp=+$("small."+room).text();
	  $("b#sttm").text(temp);
	  $("#c").text(temp+"℃");
	  $("#fuhao").text("℃");
	  $("span#time").text("开机时间："+$("em."+room).text());
	  		//if((($("small#"+room).text())=="制暖/"){
			if(($("b."+room).text())=="制暖/"){
				$("#heat").addClass("hover");
	  		}else{
				$("#cold").addClass("hover");
			};
		  
	   }else{   //为空  空调关机  设置缺省温度   清"℃"符号
	   temp=25; 
	   $("#c").text(temp+"℃");
	   $("dt#Mode").addClass("hover");
 #      $("#ktKG").css("display","none");
	   $("b#sttm").text("");
	   $("#fuhao").text("");
	   $("span#time").text("");
	   }};
	   //<div style="">
//{% for kt in kt_status %}
//<p><small id="{{ kt.rm_en }}">{{ kt.room }}</small><b id="{{ kt.rm_en }}">{{ kt.rm_en }}</b><b class="{{ kt.rm_en }}">{{ kt.rawmode }}</b>
//<small class="{{ kt.rm_en }}">{{ kt.rawtemp }}</small>at<em class="{{ kt.rm_en }}">{% if kt.rawtemp %}{{ kt.timestamp|date:"m月d日H:i" }}{% endif %}</em></p>
//{% endfor %}
//</div>
function addorsub_on(){
	mode=""
	if(($("b."+room).text())=="制暖/")mode="AC_on_heat";
	if(($("b."+room).text())=="制冷/")mode="AC_on_cold";
	if($("small."+room).text()){
		
		$.post("/kongtiao/"+room+"/",{mode:temp,room:room},function(jsons){
			//$("#sttm").text(jsons.kt_temp);
			//$("#fuhao").text("℃");
			//$("span#time").text(jsons.up_time);
			//$("em."+room).text(jsons.up_time);
			$("small."+room).text(jsons.kt_temp)
			});
	}};
