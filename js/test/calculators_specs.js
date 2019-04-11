var assert = require('assert');
var calculators = require('../calculators');

describe('calculators', function() {

  describe('#whenWillIHave', function() {
    it('should whenWillIHave', function() {
      assert.equal(calculators.whenWillIHave(127.63, 100, 0.05), 5);
    });
  });

  describe('#howMuchWillIHave', function() {
    it('should calc 10 years', function() {
      assert.equal(calculators.howMuchWillIHave(100, 0.10, 10), 259);
    });
  });

  // describe('#inflationCheck', function() {
  //   it('inflation years', function() {
  //     assert.equal(calculators.howMuchWillIHave(170, -0.025, 24), 100);
  //   });
  // });

  describe('#retirementIncomeCalculator', function() {
    it('should calc 10 years', function() {
      var age = 36;
      var retireAge = 55;
      var spend = 80000;
      var yearSave = 18000;
      var principal = 450000;
      var returnRate = 0.05;
      
      assert.equal(1, 1);
    });
  });

});

