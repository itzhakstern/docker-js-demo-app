import pytest
import page_object

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@pytest.fixture(scope='function')
def context():
    return {}

@scenario('edit_profile.feature', 'Edit my profile')
def test_edit_my_profile(context):
    pass


@given('I have profile with name "Anna Smith" ,email "anna.smith@example.com", interests "coding"')
def i_am_in_js_app(context):
    context['page_home'] = page_object.PageObject()


@when('I want edit the profile with name "Itzhak Stern" ,email "sss@example.com", interests "AI"')
def i_want_to_edit_my_profile(context):
    context['page_home'].edit_button()
    context['page_home'].edit_name()
    context['page_home'].edit_email()
    context['page_home'].edit_interests()
    context['page_home'].update_button()
    """I want to edit my profile."""


@then('The data will be update in the data base')
def the_data_in_mongo_db_is_equal_to_the_data_in_mongo_express(context):
    context['page_home'].open_mongo_express()
    assert context['page_home'].mongo_express_name() == "Itzhak Stern"
    assert context['page_home'].mongo_express_email() == "sss@example.com"
    assert context['page_home'].mongo_express_interests() == "AI"