/*
* Name: jquery.currency
* Version: 0.1
*/
(function($) {
    $.rateOfCurrency = {
        defaults: {
			valueClass: ".price-value",
			captionClass: ".price-currency",
			fldsContainer: ".tabs-content", // General ancestor element for the elements group,for which currency rate is changed
			currencyRatioArr: { USD: 1, EUR: 1.2, GBP: 1.4, CHF: 1.109, CAD: 0.9, JPY: 0.0120 }, // Sequence is insignificant
			currencyCaptionArr: { USD: " $", EUR: " €", GBP: " £", CAD: " $", CHF: " ₣", JPY: " ¥" } // Sequence is insignificant
        },
		rateOfCurrencyInit: function(opts) {
			return this.each(function() {
                this.opts = {};
                $.extend(this.opts, $.rateOfCurrency.defaults);
                $.extend(this.opts, opts);
				
				/* html-elements */
				var currencySelectObj = this,
				fldsContainerObj = this.opts.fldsContainer,
				currencyValueObj = $(this).parentsUntil(fldsContainerObj).find(this.opts.valueClass),
				currencyCaptionObj = $(this).parentsUntil(fldsContainerObj).find(this.opts.captionClass);

				var currencyRatio = this.opts.currencyRatioArr,
				currencyCaption = this.opts.currencyCaptionArr;
				
				/* values by default */
				var defaultCurrencyName = $(this).attr("value"),
				defaultCurrencyRatio = currencyRatio[defaultCurrencyName],
				defaultCurrencyCaption = currencyCaption[defaultCurrencyName];

				/* we find all initial price values and put them into array */
				var defaultPriceValues = [];
				var spaceRe = / +/g;
				function removeSpaces(s) {
					return s.replace(spaceRe, "");
				}
				currencyValueObj.each(function(i){
					var tempPrice = $(this).text();
					tempPrice = parseFloat(removeSpaces(tempPrice));
					defaultPriceValues.push(tempPrice);
				});
				currencyCaptionObj.each(function(){
					$(this).text(defaultCurrencyCaption);
				});

				var curPriceIncr,				
				curPriceValue,
				curPriceTemp;
				var selectedCurrencyNum,
				selectedCurrencyName,
				selectedCurrencyRatio;
				
				$(this).change(function(){
					selectedCurrencyName = $(this).attr("value");
					selectedCurrencyRatio = currencyRatio[selectedCurrencyName];
					selectedCurrencyCaption = currencyCaption[selectedCurrencyName];
					curPriceIncr = defaultCurrencyRatio/selectedCurrencyRatio;
					currencyValueObj.each(function(i){
						curPriceTemp = (defaultPriceValues[i]*curPriceIncr).toFixed(0);
						if(selectedCurrencyName == "USD"){
							curPriceValue = Math.round(curPriceTemp/5)*5;
						} else {
							curPriceValue = Math.round(curPriceTemp/2)*2;
						}
						$(this).text(curPriceValue);
					});
					currencyCaptionObj.each(function(){
						$(this).text(selectedCurrencyCaption);
					});
				});
				
			});
		}
	};
    $.fn.rateOfCurrency = $.rateOfCurrency.rateOfCurrencyInit;
})(jQuery);

$(function() {
	$("#selectExchangeRate1, #selectExchangeRate2").rateOfCurrency();
});