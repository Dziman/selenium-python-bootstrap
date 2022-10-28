from seleniumbase import BaseCase

class GoogleSearchTest(BaseCase):

    def test_redirect_to_https(self):
        self.open("http://www.google.com")
        assert self.get_current_url().startswith("https://")

    def test_nothing_found(self):
        self.open("https://www.google.com")
        self.type("[name=q]", "chromeziioo\n")
        self.assert_text("0 results", "#result-stats")

    def test_sign_in_with_invalid_credentials(self):
        self.open("https://www.google.com")
        self.click_link("Sign in")
        self.type("[name=identifier]", "tom.cruz\n")
        self.type("[name=Passwd]", "tom.cruz.c00l!\n") # Failing here because Google blocks process
        self.assert_text("Wrong password")

    def test_amazon_sign_in_with_invalid_credentials(self):
        self.open("https://www.amazon.com")
        self.click_link("Sign in")
        self.type("#ap_email", "tom.cruz@gmail.com\n")
        self.type("#ap_password", "tom.cruz.c00l!\n")
        self.assert_text("Your password is incorrect")
