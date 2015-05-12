/*
* Name: jquery.
* Version: 0.1
*/
(function($) {
    $.linkGenerator = {
        defaults: {
			languageObj: "",
			currencyObj: "",
			licenseObj: "",
			paymentObj: "",
			samObj: ""
        },
        
		linkGeneratorInit: function(opts) {
			return this.each(function() {
                this.opts = {};
                $.extend(this.opts, $.linkGenerator.defaults);
                $.extend(this.opts, opts);
				
				var linkGenerator = this,
				languageObj = linkGenerator.opts.languageObj,
				currencyObj = linkGenerator.opts.currencyObj; 
				
				var link;
				
				var paymentSystem;
				var paymentWay;
				var paymentWayByLanguage;
				var licenseType;
				var licenseSam;
				var selectedLanguage;
				var selectedCurrency;
				var template;
				var currencyForLink;
				
				var idxOfPS;
				var idxOfPW;
				var idxOfPT;
				var idxOfLT;
				var idxOfSL;
				
				var arrKeysPaymentSystems = [
					"psPlimus",
					"psShareit"
				];
				var arrValuesPaymentSystems = [
					"https://secure.plimus.com/jsp/buynow.jsp?contractId=",
					"https://secure.element5.com/shareit/checkout.html?productid="
				];
				
				var arrProductTypes = [
					"ptTNI"
				];
				

				var arrKeysPaymentWays = [
					"psCC",
					"psPP",
					"psWire"
				];
				var arrValuesPaymentWays = [
					[
						'&paymentMethod=step2',
						'&paymentMethod=paypal',
						'&paymentMethod=wire'
					],
					[
						'&PAYMENTTYPE_ID=CCA',
						'&PAYMENTTYPE_ID=PAL',
						'&PAYMENTTYPE_ID=WTR'
					]
				];
				var arrValuesPaymentWaysByLanguage = [
					//"language-eng"
					[
						'psShareit',
						'psShareit',
						'psPlimus'
					],
					//"language-ger"
					[
						'psShareit',
						'psShareit',
						'psShareit'
					],
					//"language-fra"
					[
						'psShareit',
						'psShareit',
						'psShareit'
					],
					//"language-spa"
					[
						'psShareit',
						'psShareit',
						'psPlimus'
					],
					//"language-ita"
					[
						'psShareit',
						'psShareit',
						'psShareit'
					],
					//"language-por"
					[
						'psShareit',
						'psShareit',
						'psPlimus'
					],
					//"language-nld"
					[
						'psShareit',
						'psShareit',
						'psShareit'
					],
					//"language-swe"
					[
						'psShareit',
						'psShareit',
						'psShareit'
					],
					//"language-fin"
					[
						'psShareit',
						'psShareit',
						'psShareit'
					],
					//"language-ces"
					[
						'psShareit',
						'psShareit',
						'psPlimus'
					],
					//"language-tur"
					[
						'psShareit',
						'psShareit',
						'psPlimus'
					],
					//"language-pol"
					[
						'psShareit',
						'psShareit',
						'psPlimus'
					]
				];

				var arrLicenseTypes = [
					"tni25",
					"tni50",
					"tni100",
					"tni150",
					"tni250",
					"tni350",
					"tni500",
					"tni750",
					"tni1000",
					"tni1500",
					"tni2000",
					"tniUnlimited",
					"tniMSP100",
					"tniMSP500",
					"tniMSPUnlimited"
					//"tniMSP"
			    ];
				
				var arrSelectedLanguage = [
					"language-eng",
					"language-ger",
					"language-fra",
					"language-spa",
					"language-ita",
					"language-por",
					"language-nld",
					"language-swe",
					"language-fin",
					"language-ces",
					"language-tur",
					"language-pol"
				];
				
				/* ---------- */
				
				var languages = [
					[
						'&language=ENGLISH',
						'&language=GERMAN',
						'&language=FRENCH',
						'&language=SPANISH',
						'&language=ITALIAN',
						'&language=PORTUGUESE',
						'&language=DUTCH',
						'&language=SWEDISH',
						'&language=FINNISH',
						'&language=CZECH',
						'&language=TURKISH',
						'&language=POLISH'
					],
					[
						'&languageid=1',
						'&languageid=2',
						'&languageid=6',
						'&languageid=4',
						'&languageid=5',
						'&languageid=3',
						'&languageid=8',
						'&languageid=9',
						'&languageid=10',
						'&languageid=18',
						'&languageid=20',
						'&languageid=16'
					]
				];
				
				var currencies = [
						'&currency=%',
						'&currencies=%,all'
				];
				
				var productIDs = [
					[
						[
							[ 
								'1678588',
								'1678589',
								'1678590',
								'1685837',
								'1678591',
								'1685838',
								'1678592',
								'3120396',
								'3120398',
								'3120402',
								'3120404',
								'1678593',
								'3154246',
								'3154238',
								'1694196' // Product ID
							], // Product type // Base
							[ 
								'3225952',
								'3225956',
								'3225958',
								'3225960',
								'3225962',
								'3225964',
								'3225966',
								'3225968',
								'3225970',
								'3225972',
								'3225974',
								'3225976',
								'3225978',
								'3225980',
								'3225982' 
							] // SAM
						]
					], // Payment system
					[
						[
							[
								'300133613',
								'300133663',
								'300133667',
								'300140232',
								'300133670',
								'300140236',
								'300133675',
								'300506327',
								'300506328',
								'300506330',
								'300506331',
								'300133680',
								'300552143',
								'300552136',
								'300160443'
							], // Base
							[
								'300619007',
								'300619008',
								'300619009',
								'300619010',
								'300619011',
								'300619012',
								'300619013',
								'300619014',
								'300619015',
								'300619016',
								'300619017',
								'300619018',
								'300619019',
								'300619020',
								'300619021'
							] // SAM
						]
					]
				];
				
				var templates = [
					[
					'&templateId=271262',
					'&templateId=271262',
					'&templateId=271262',
					'&templateId=271262',
					'&templateId=271262',
					'&templateId=271262',
					'&templateId=271262',
					'&templateId=271262',
					'&templateId=271262',
					'&templateId=271262',
					'&templateId=271262',
					'&templateId=271262'
					]
				];
				
				$(linkGenerator).bind("click", function() {
					
					// Google tracking.
					ga('send', '_trackEvent', 'Form', 'Purchase', '/purchase/total-network-inventory/');
					
					selectedLanguage = $(linkGenerator.opts.languageObj).attr("class");
					selectedCurrency = $(linkGenerator).parentsUntil(".tabs-content").find(linkGenerator.opts.currencyObj).attr("value");
					licenseType = $(linkGenerator).parentsUntil(".tabs-content").find(linkGenerator.opts.licenseObj).attr("value");
					//paymentSystem = $(linkGenerator).parentsUntil(".tabs-content").find(linkGenerator.opts.paymentObj).attr("value");
					paymentWay = $(linkGenerator).parentsUntil(".tabs-content").find(linkGenerator.opts.paymentObj).attr("value");
					licenseSam = ($(linkGenerator).parentsUntil(".tabs-content").find(linkGenerator.opts.samObj).attr("value") == "full" ? 1 : 0);

					for (i = 0; i < arrSelectedLanguage.length; i++) {
						if (arrSelectedLanguage[i] == selectedLanguage) {
							idxOfSL = i;
						}
					}
					for (i = 0; i < arrKeysPaymentWays.length; i++) {
						if (arrKeysPaymentWays[i] == paymentWay) {
							idxOfPW = i;
						}
					}

					paymentSystem = arrValuesPaymentWaysByLanguage[idxOfSL][idxOfPW];
					
					for (i = 0; i < arrKeysPaymentSystems.length; i++) {
						if (arrKeysPaymentSystems[i] == paymentSystem) {
							idxOfPS = i;
						}
					}
					idxOfPT = 0;
					for (i = 0; i < arrLicenseTypes.length; i++) {
						if (arrLicenseTypes[i] == licenseType) {
							idxOfLT = i;
						}
					}
					currencyForLink = currencies[idxOfPS].replace("%", selectedCurrency);
					
					if (paymentSystem == "psPlimus") {
						template = templates[idxOfPT][idxOfSL];
					}
					else {
						template = "";
					}
					
					
					link = arrValuesPaymentSystems[idxOfPS] + productIDs[idxOfPS][idxOfPT][licenseSam][idxOfLT] + arrValuesPaymentWays[idxOfPS][idxOfPW] + languages[idxOfPS][idxOfSL] + currencyForLink + template;
				/*
					// SYSDAY2013
					if (paymentSystem == "psPlimus") {
						link = link + '&couponCode=SYSDAY2013';
					}
					else {
						link = link + '&COUPON1=SYSDAY2013';
					}
				*/
				/*
					// TNI3RELEASE
					if (paymentSystem == "psPlimus") {
						link = link + '&couponCode=TNI3RELEASE';
					}
					else {
						link = link + '&COUPON1=TNI3RELEASE';
					}
				*/
					// Hide coupon field.
					if (paymentSystem == "psPlimus") {
						link = link + '&showCouponBox=N';
					}
					else {
						link = link + '&hidecoupon=1';
					}

					window.location.href = link;
					
					return false;
				});
			});
		
		}

	};
    $.fn.linkGenerator = $.linkGenerator.linkGeneratorInit;
/*	
	$("#linkPayment1").linkGenerator({
		languageObj: "#selectedLanguage",
		currencyObj: "#selectExchangeRate1",
		licenseObj: "input[name='radio-a']:checked",
		paymentObj: "input[name='radio-b']:checked",
		samObj: "input#license_sam"
	});
	$("#linkPayment2").linkGenerator({
		languageObj: "#selectedLanguage",
		currencyObj: "#selectExchangeRate2",
		licenseObj: "input[name='radio-c']:checked",
		paymentObj: "input[name='radio-d']:checked"		
	});
*/	
})(jQuery);