import streamlit as st
from src.constants import default_description


def add_personal_info(tab, **kwargs):
    """
    Add personal info to tab.

    :param tab: Streamlit tab
    """
    with tab:
        col1, col2 = st.columns(2)
        kwargs['name'] = col1.text_input('Name', 'Ali Hejazizo')
        kwargs['email'] = col2.text_input('Email', 'hejazizo@ualberta.ca')
        kwargs['phone'] = col1.text_input('Phone', '+1 780 680 3295')
        kwargs['homepage'] = col2.text_input('Homepage', 'https://pytopia.ai')
        kwargs['location'] = col1.text_input('Location', 'Toronto, Canada')

    return kwargs


def add_social_accounts(tab, **kwargs):
    """
    Add social accounts to tab.

    :param tab: Streamlit tab
    """
    with tab:
        col1, col2 = st.columns(2)
        kwargs['github'] = col1.text_input('Github', 'hejazizo')
        kwargs['linkedin'] = col2.text_input('Linkedin', 'hejazizo')
        kwargs['twitter'] = col1.text_input('Twitter', 'hejazizo')
        kwargs['facebook'] = col2.text_input('Facebook', 'hejazizo')
        kwargs['instagram'] = col1.text_input('Instagram', 'ali.hejazzii')
        kwargs['youtube'] = col2.text_input('Youtube')
        kwargs['medium'] = col1.text_input('Medium')

    return kwargs

def add_description(tab, **kwargs):
    """
    Add description to tab.

    :param tab: Streamlit tab
    """
    with tab:
        kwargs['description'] = st.text_area('Description', default_description, height=300)

    return kwargs

def add_extensions(tab, **kwargs):
    """
    Add extensions to tab.

    :param tab: Streamlit tab
    """
    with tab:
        if not kwargs['github']:
            st.error('For extensions, please enter your Github username in Social Accounts section.')
            return

        kwargs['github_stats'] = None
        if st.checkbox('Show Github Stats', value=True):
            kwargs['github_stats'] = kwargs['github']

        kwargs['profile_views'] = None
        if st.checkbox('Show Github Profile Views', value=True):
            kwargs['profile_views'] = kwargs['github']

    return kwargs
