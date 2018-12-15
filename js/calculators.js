// Common Calculators
var compound = require('./compound');

module.exports = {

  whenWillIHave: function (amount, principal, rate) {
    // less inflation? In todays dollars or not?
    var log = Math.log;

    var num = log(amount/principal);
    var denom = log(1+rate)

    return Math.round(num / denom);
  },

  // whenCanIRetire

  howMuchWillIHave: function(principal, rate, years) {
    return Math.round(
      compound.compoundInterest(principal, rate, years)
    );
  }

}
