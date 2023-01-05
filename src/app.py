import streamlit as st
from pathlib import Path
from src.github_profile import generate_profile
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

st.set_page_config(
    page_title='Github Profile Readme Generator',
    page_icon='🧊',
    layout='wide',
    initial_sidebar_state='expanded',
    menu_items={
        'Report a bug': 'https://github.com/hejazizo/github-profile-readme/issues',
        'About': 'Built by [Pytopia](pytopia.ai) team.'
    }
)

st.title(':zap: Github Profile Readme Generator')
st.header('Personalize your Readme')
tab1, tab2, tab3, tab4 = st.tabs([
    ':bust_in_silhouette: Profile Info',
    ':globe_with_meridians: Social Accounts',
    ':memo: Description',
    ':heavy_plus_sign: Extensions'
])
kwargs = {}
kwargs = add_personal_info(tab1, **kwargs)
kwargs = add_social_accounts(tab2, **kwargs)
kwargs = add_description(tab3, **kwargs)
kwargs = add_extensions(tab4, **kwargs)

st.header('Preview')
# Select Theme
themes = Path('src/themes').iterdir()
themes = [theme.name for theme in themes]
theme = st.selectbox('Theme:', themes)

# Generate Readme
profile = generate_profile(theme, **kwargs)
tab1, tab2 = st.tabs(['Preview', 'Code'])
tab1.markdown(profile)

with tab2:
    st.text('Copy the code below and paste it in your README.md file')
    st.code(profile)
