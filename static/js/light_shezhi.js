// JavaScript Document
function shezhi(room){
	$("#sideNav li").removeClass("hover");
	$("li#"+room).addClass("hover");
	$(".main").attr("id",$("b."+room).text());
	if($("small."+room).text() == "开"){
		$("#dengMain").text("关");
		$("#status b").text("打开");
		}else{
		$("#dengMain").text("开");
		$("#status b").text("关闭");
			};
	};
	
function Posts(room){
	$.post("/light/"+room+"/",
    { dcontrol:room },function(ret){
	//alert(ret);
    if(ret=="1"){
		$("b."+room).text("dengKai");
		$("small."+room).text("开");
		$("#status b").text("打开");
		$("#dengMain").text("关");
    	$(".main").attr("id","dengKai");
		
		
    }
    else if(ret=="0"){
		$("b."+room).text("dengGuan");
		$("small."+room).text("关");
    	$(".main").attr("id","dengGuan");
		$("#dengMain").text("开");
    	$("#status b").text("关闭");
		
	

    }
     }
     );
	
	};