import os

from selene import browser, be, by, have


def test_fill_out_practice_form():
    browser.open("/")
    browser.element("#firstName").should(be.blank).type("Victoria")
    browser.element("#lastName").should(be.blank).type("Testlastname")
    browser.element("#userEmail").should(be.blank).type("madvika89@gmail.com")
    browser.element("#gender-radio-2").double_click()
    browser.element("#userNumber").should(be.blank).type("9876543210")
    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__year-select").click().element(
        by.text("1993")
    ).click()
    browser.element(".react-datepicker__month-select").click().element(
        by.text("November")
    ).click()
    browser.element(".react-datepicker__week .react-datepicker__day--026").click()
    browser.element("#subjectsInput").type("Accounting").press_enter()
    browser.element("[for=hobbies-checkbox-2]").click()
    browser.element("#uploadPicture").type(os.path.abspath("image/image_1.jpeg"))
    browser.element("#react-select-3-input").should(be.blank).type("NCR").press_enter()
    browser.element("#currentAddress").type("USA")
    browser.element("#react-select-4-input").should(be.blank).type(
        "Delhi"
    ).press_enter()
    browser.element("#submit").press_enter()
    browser.element("#example-modal-sizes-title-lg").should(
        have.text("Thanks for submitting the form")
    )

    # # Verify that submitted values are as expected
    browser.element(".table").should(have.text("Victoria Testlastname"))
    browser.element(".table").should(have.text("madvika89@gmail.com"))
    browser.element(".table").should(have.text("Female"))
    browser.element(".table").should(have.text("9876543210"))
    browser.element(".table").should(have.text("26 November,1993"))
    browser.element(".table").should(have.text("Accounting"))
    browser.element(".table").should(have.text("Reading"))
    browser.element(".table").should(have.text("USA"))
    browser.element(".table").should(have.text("NCR Delhi"))
    browser.element(".table").should(have.text("image_1.jpeg"))
