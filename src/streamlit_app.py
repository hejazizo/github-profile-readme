import sys
from pathlib import Path

import streamlit as st

project_root = str(Path(__file__).parent.parent.absolute())
if project_root not in sys.path:
    sys.path.append(project_root)

from src.github_profile import generate_profile
from src.sections import (add_description, add_extensions, add_personal_info,
                          add_social_accounts)

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
st.sidebar.image('src/assets/logo.jpeg', width=300)
st.sidebar.markdown('''
:bulb: Built by [Pytopia](pytopia.ai) team.
''')

'''
This app generates a Github profile readme file. To learn how to add a readme file to your Github profile, check out
[this](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/managing-your-profile-readme).
You can customize it and use it in your Github profile.
- First, fill out the forms below.
- Then, go to **Code** tab to copy the code and paste it in your `README.md` file.

You can also change the theme of the readme file by selecting a theme from the dropdown below.
Themes are added by the community. If you want to add a theme, check out the [Github repo](https://github.com/hejazizo/github-profile-readme).
'''

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

st.header('README.md Preview')
'''
- Select a theme from the dropdown below.
- Go to **Code** tab to copy the code and paste it in your `README.md` file.
- **Github extensions will not work in the preview.** You can only see them in the code and in your Github profile.
'''

# Select Theme
themes = Path('src/themes').iterdir()
themes = [theme.name for theme in themes]
theme = st.selectbox('Theme:', themes)

# Generate Profile
profile = generate_profile(theme, **kwargs)
tab1, tab2 = st.tabs(['Preview', 'Code'])
tab1.markdown(profile)

with tab2:
    'Copy the code below and paste it in your README.md file'
    st.code(profile)
