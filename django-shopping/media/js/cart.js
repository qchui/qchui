$(function (){
	//1.全选和取消全选
	$(".checkAll").click(function (){
		//如果当前元素为选中状态
		if($(this).attr("checked")){
			//修改为取消选中
			$(this).removeAttr("checked")
				.attr("src","/media/images/cart/product_normal.png");
			$(".checkItem").removeAttr("checked")
				.attr("src","/media/images/cart/product_normal.png")

		}else{
			$(this).attr("checked","true")
				.attr("src","/media/images/cart/product_true.png");
			$(".checkItem").attr("checked","true")
				.attr("src","/media/images/cart/product_true.png")
		}
		/*
			1.为全选按钮添加点击事件，事件函数中，判断当前按钮是否是选中状态（查看是否存在checked属性值）
			2.如果当前元素存在checked属性值，说明本身为选中状态，需要修改为取消选中。（移除checked属性，修改状态标识；更改 图片路径）
			3.根据全选按钮的状态获取商品按钮，统一调整状态标识和图片路径

		*/
		sum();
	})


	//2.反选
	$(".checkItem").click(function (){
		if($(this).attr("checked")){
			$(this).removeAttr("checked")
				.attr("src","/media/images/cart/product_normal.png");
		}else{
			$(this).attr("checked","true")
				.attr("src","/media/images/cart/product_true.png")
		}
		//被选中的商品数量等于商品元素的个数，视为全选
		//console.log($(".checkItem[checked]"));
		if($(".checkItem[checked]").length == $(".checkItem").length){
			//视为全选
			$(".checkAll").attr("checked","true")
				.attr("src","/media/images/cart/product_true.png")
		}else{
			//取消全选
			$(".checkAll").removeAttr("checked")
				.attr("src","/media/images/cart/product_normal.png");
		}
		sum()
	})


	//3.数量增减
	$(".add").click(function (){
		//获取前一个兄弟元素（输入框）的值
		var value = $(this).prev().val();
		value++;
		$(this).prev().val(value);
		countPrice($(this),value);
		sum();

	})
	$(".minus").click(function (){
		var value = $(this).next().val();
		if(value > 1){
			value--;
		}
		$(this).next().val(value);
		countPrice($(this),value)
		sum()

	})

	//价格联动
	function countPrice(that,value){
		//价格联动 单价*数量，修改总金额
		var str = that.parents(".item").find(".gprice p").html();//"￥ 299.00"
		var price = str.substring(2);//"299.00"
		var sum = price * value;
		sum = sum.toFixed(2);
		that.parent().next().html("￥ "+sum);

	}

	//移除操作
	$(".item .action").click(function (){
		//移除整个商品记录
		$(this).parents(".item").remove();
		sum()
	})

	//总价格和总数量的联动
	function sum(){
		//获取被选中的商品，累加商品数量和总结
		var num = 0;//保存总数量
		var price = 0;//保存总价格
		//数据遍历，each(function (){})
		$(".checkItem[checked]").each(function (){
			//每取到一个元素就调用当前函数,this指代函数的调用者
			var n = $(this).parents(".item").find(".gcount input").val();
			var p = $(this).parents(".item").find(".gsum").html();
			//转number
			n = Number(n);
			p = Number(p.substring(2));
			num += n;
			price += p;
		});

		$(".total-num").html(num);
		$(".total-price").html(price);
	}

})
