require 'watir'

# Watir.default_timeout = 60

# require 'headless'
# headless = Headless.new
# headless.start
# headless.destroy

login_url = 'https://global.americanexpress.com/login?inav=iNavLnkLog'

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

browser.goto login_url

sleep 3
browser.text_field(id: 'eliloUserID').when_present.set ENV['WATIR_USER']
browser.text_field(id: 'eliloPassword').when_present.set ENV['WATIR_PASS']
browser.button(text: "Log In").click

# wait
sleep 3
# browser.link(text: "Statements & Activity").when_present.click

browser.goto('https://online.americanexpress.com/myca/ofxdl/us/domesticOptions.do?request_type=authreg_ofxdownload&appVerID=CSV|0100&cardSelected=Y')

browser.checkbox(id: 'bpindex00').when_present.set
browser.checkbox(id: 'bpindex01').when_present.set
browser.button(name: 'Download').when_present.click

puts browser.title
browser.close
