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

browser = Watir::Browser.new

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

browser.goto('https://www.usaa.com/inet/imco_brokerage/Trading?action=INIT&Type=1&RegId=encrypted6726c2772eecb950e79cda258da0fc9d&MFWrap=N')
browser.button(name: 'positionsExcelLink').when_present.click

browser.goto('https://www.usaa.com/inet/imco_brokerage/Trading/BrokerageTradingMainPage?MFWrap=N&Type=1&RegId=encrypted5d6bcf27042f1cc3daf561f651a4ef87&action=INIT&w:pageMapName=w-6')
browser.button(name: 'positionsExcelLink').when_present.click

browser.goto('https://www.usaa.com/inet/imco_brokerage/Trading/BrokerageTradingMainPage?MFWrap=N&Type=1&RegId=encrypted9e2056d975d708c300cbf912857d3c73&action=INIT&w:pageMapName=w-7')
browser.button(name: 'positionsExcelLink').when_present.click

browser.goto('https://www.usaa.com/inet/imco_brokerage/Trading/BrokerageTradingMainPage?MFWrap=N&Type=1&RegId=encrypted5a3d7a36512669df4707fc477a489585&action=INIT&w:pageMapName=w-8')
browser.button(name: 'positionsExcelLink').when_present.click

# pin = gets
# browser.text_field(id: 'j_usaaPin').set pin

puts browser.title
# browser.close
