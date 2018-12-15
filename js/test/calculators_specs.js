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
      assert.equal(calculators.howMuchWillIHave(100, 0.10, 0), 121);
    });
  });

});

