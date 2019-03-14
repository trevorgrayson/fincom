require 'watir'

# Watir.default_timeout = 60

# require 'headless'
# headless = Headless.new
# headless.start
# headless.destroy

browser = Watir::Browser.new

browser.goto 'http://trevorgrayson.com'

browser.link(text: /esum/).when_present.click
sleep(10)
puts browser.title
# browser.close
