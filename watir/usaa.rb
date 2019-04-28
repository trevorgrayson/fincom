require 'watir'

# Watir.default_timeout = 60

# require 'headless'
# headless = Headless.new
# headless.start
# headless.destroy

def download_account(b)
  b.link(text: /Asset Management/).when_present.click
  b.button(text: 'Export').when_present.click
end

download_directory = "#{Dir.pwd}/downloads"

prefs = {
  download: {
    prompt_for_download: false,
    default_directory: download_directory
  }
}

browser = Watir::Browser.new :chrome, options: {prefs: prefs}

browser.goto 'https://www.usaa.com/inet/ent_logon/Logon'
browser.link(text: 'Log On').click

browser.text_field(id: 'j_usaaNum').when_present.set ENV['WATIR_USER']
browser.text_field(id: 'j_usaaPass').set ENV['WATIR_PASS']
browser.send_keys :enter

browser.button(id: 'idc').when_present.click

browser.wait_until { |b| browser.text_field(type: 'password').value.length > 5 }

browser.button(text: "Next").when_present.click

# download_account(browser)
# sleep(10)
# browser.tr(id: 'row_1').link.when_present.click

browser.goto('https://www.usaa.com/inet/imco_brokerage/Trading?action=INIT')
browser.button(name: 'positionsExcelLink').when_present.click

# pin = gets
# browser.text_field(id: 'j_usaaPin').set pin

puts browser.title
browser.close
