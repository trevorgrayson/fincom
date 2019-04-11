module.exports = {

  compoundInterest: function (principal, rate, years, per_year=1.0) {
    var base = (1 + rate); // /per_year);
    var exponent = per_year * years;

    return Math.round(
      principal * Math.pow(base, exponent) 
    ) 
  },

  todaysDollars: function(amount, years, inflateRate=0.029) {
    return 0;
  }

}

