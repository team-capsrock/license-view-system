var t;

function setCookie(c_name) {
    var date = new Date();
    date.setTime(date.getTime()+(900*1000));
    document.cookie = c_name+"=8sdj3nc7cg2bwlv0byhbthpjq233bt;expires="+date.toGMTString()+";path=/;domain="+location.host;
    //$.cookie(c_name, '8sdj3nc7cg2bwlv0byhbthpjq233bt', { path: '/', domain: location.host});
    //document.cookie = c_name+"=8sdj3nc7cg2bwlv0byhbthpjq233bt";
	//alert(document.cookie);
}

function c_rand(minV,maxV) {
    maxV++;
    var range = maxV - minV;
    var n = Math.floor(Math.random()*range) + minV;
    return n;
}

function generateSessionId() {
    session_id = "";
    session_id = session_id + String.fromCharCode(c_rand(97, 122));
    for(var i = 1; i < 30; i++) {
        if(c_rand(0, 1)) {
            session_id = session_id + String.fromCharCode(c_rand(97, 122));
        } else {
            session_id = session_id + String.fromCharCode(c_rand(48, 57));
        }
    }
    return session_id;
}

function setVal() {
    var sessId = generateSessionId();
    if(sessId) {
        setCookie(sessId);
		$(".krv_val")[0].id = sessId;
    }
    t = setTimeout("hideVal()",5000);
}

function hideVal() {
    $(".trv_val")[0].id = "lwe3gxcv82gkl7cdsnrtjklskwe4x";
    clearTimeout(t);
}

var oper_systems = [
	"Windows 8",
	"Windows 7",
	"Windows Vista",
	"Windows XP",
	"Windows 2000",
	"Windows Server 2012",
	"Windows Server 2008",
	"Windows Server 2003"
	];

var tni_licenses = [
	"25 nodes",
	"50 nodes",
	"100 nodes",
	"150 nodes",
	"250 nodes",
	"350 nodes",
	"500 nodes",
	"750 nodes",
	"1000 nodes",
	"1500 nodes",
	"2000 nodes",
	"Unlimited",
	"MSP 100 nodes",
	"MSP 500 nodes",
	"MSP Unlimited"
	];
	
var upgrade_not_applicable = "N/A";

function update_upgrade() {
	var current_index = $("#tni_upgrade_form").find("input#selectCurrentLicense").val(),
		needed_index = $("#tni_upgrade_form").find("input#selectNeededLicense").val(),
		current_version = $("#tni_upgrade_form").find("input#selectCurrentLicenseVersion").val(),
		needed_version = $("#tni_upgrade_form").find("input#selectNeededLicenseVersion").val(),
		index = current_index,
		$scroll_license = $("#cusel-scroll-selectNeededLicense"),
		$scroll_version = $("#cusel-scroll-selectNeededLicenseVersion"),
		text = "";

};

function reset_select(selectid, values, stop, start){
	var $select = $("#" + selectid);
		$scroll = $("#cusel-scroll-" + selectid),
		text = "";
		
	start = start || 0;
	stop = stop || values.length;
		
	for(var i = start; i < stop; i++){
		text = text + "\n\t\t\t\t\t\t\t\t<span " + (i == start ? "class='cuselActive' selected='selected'" : "") + " value='" + i + "'>" + values[i] + "</span>";
	};
	$scroll.html(text);
	$("#cuselFrame-" + selectid).find("div.cuselText").html(values[start]);
	$("#cuselFrame-" + selectid).find("input#" + selectid).val(start);
	var cuSelParams = {
		refreshEl: "#" + selectid,
		visRows: 8
	};
	cuSelRefresh(cuSelParams);
};

function check_form(form){
	//return true; //DEBUG

	var
		res,
		result = true,
		elements = $(form).find(".mandatory"),
		el;
	
	for (i=0; i<elements.length; i++){
		el = elements[i];
		if (el.type == "email"){
			res = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/.test(el.value);
		} else {
			res = (el.value != "");
		};
		if (result && !res){
			el.focus();
			el.select();
		};
		if (!res)
			el.style.backgroundColor="#eaeaea"
		else
			el.style.backgroundColor="#ffffff";
		result = result && res;
	};
	
	if(($(form).attr("id") == "tni_upgrade_form") && ($("#labelUpdradePrice").html() == upgrade_not_applicable)){
		result = false;
	}
	
	$(form).find("div#form_result").html("Please fill in the required fields.")
	return result;
};

$(document).ready(function() {
	$("form").submit(function(){
		if(check_form(this)){
			// Show animation and hide button.
			$(".loading").show();
			$(".btnSetD").hide();

			var $form = $(this);
			
			// Clear result.
			$form.find("div#form_result").html("");

			// Send email.
			$.post("/scripts/zmail.php", $form.serialize() + "&krv_val=" + $(".krv_val")[0].id + "&trv_val=" + $(".trv_val")[0].id, function(data){
				// Hide animation and show button.
				$(".loading").hide();
				$(".btnSetD").show();

				// Clear current form fields.
				$form.find(":input:not(:hidden)").val("");
				$form.find("textarea").val("");
				$(".watermark").watermark();
				
				// Clear select of current form.
				var $select = $form.find("div.resettable_select");
				if($select[0]){
					selectidstring = $select[0].id;
					var selectidarr = selectidstring.split("|");
					for (i = 0; i < selectidarr.length; i++) {
						var selectid = selectidarr[i].split(";");
						if(selectid[2] && (selectid[2].indexOf("-") > -1)) {
							var limits = selectid[2].split("-");
							reset_select(selectid[0], eval(selectid[1]), limits[1], limits[0])
						} else
							reset_select(selectid[0], eval(selectid[1]), selectid[2]);
						if(selectid[3])
							eval(selectid[3]);
					};
				};
				
				// Output the result.
				if (data == "0")
					{$form.find("div#form_result").html("Thanks, your message has been sent.");}
				else if (data == "1")
					{$form.find("div#form_result").html("Error sending your message.");}
				else if (data == "2")
					{$form.find("div#form_result").html("Some error happened.");} //Antispam.
				else if (data.indexOf("http")==0)
					{window.location = data;}
				else
					$form.find("div#form_result").html(data);

			}); //$.post()
		}; //if(check_form)
		event.preventDefault();
		return false;
	});
});

// Cookie and value for antispam.
setVal();
