import urllib.parse

import streamlit as st

from src.constants import default_description, skills, tech_stacks


def add_personal_info(tab, **kwargs):
    """
    Add personal info to tab.

    :param tab: Streamlit tab
    """
    with tab:
        col1, col2 = st.columns(2)
        kwargs['name'] = col1.text_input('Name', 'Ali Hejazizo')
        kwargs['email'] = col2.text_input('Email', 'hejazizo@ualberta.ca')

    return kwargs


def add_social_accounts(tab, **kwargs):
    """
    Add social accounts to tab.

    :param tab: Streamlit tab
    """
    with tab:
        col1, col2 = st.columns(2)
        kwargs['homepage'] = col1.text_input('Homepage', 'https://pytopia.ai')
        kwargs['linkedin'] = col2.text_input('Linkedin', 'hejazizo')
        kwargs['twitter'] = col1.text_input('Twitter', 'hejazizo')
        kwargs['instagram'] = col2.text_input('Instagram', 'ali.hejazzii')

    return kwargs

def add_description(tab, **kwargs):
    """
    Add description to tab.

    :param tab: Streamlit tab
    """
    with tab:
        st.write('''Write a short description about yourself.''')
        kwargs['description'] = st.text_area('Description', default_description, height=300)

    return kwargs

def add_extensions(tab, **kwargs):
    """
    Add extensions to tab.

    :param tab: Streamlit tab
    """
    with tab:
        st.write('''Add more to your profile. You can add Github stats, Github profile views, and more.''')
        kwargs['github'] = st.text_input('Github', 'hejazizo')
        if not kwargs['github']:
            st.warning('For extensions, you must enter your Github username.')
            kwargs['profile_views'] = None
            kwargs['github_stats'] = None
            return kwargs

        kwargs['github_stats'] = None
        if st.checkbox('Show Github Stats', value=True):
            kwargs['github_stats'] = kwargs['github']

        kwargs['profile_views'] = None
        if st.checkbox('Show Github Profile Views', value=True):
            kwargs['profile_views'] = kwargs['github']

    return kwargs


def add_tech_stack(tab, **kwargs):
    """
    Add tech stacks to tab.

    :param tab: Streamlit tab
    """
    BADGE_TEMPLATE = '![Bootstrap](https://img.shields.io/badge/-{badge}-05122A?style={style}&logo={logo}&color={color})'
    with tab:
        st.write('''Add your tech stacks. You can add any tech stack and skills you want.
        **Just make sure to separate them with a new line.**
        ''')
        # Badge style and color
        col1, col2 = st.columns(2)
        style = col1.selectbox('Style', ['flat-square', 'flat', 'plastic', 'for-the-badge', 'social'], key='stack_style')
        color = col2.color_picker('Color', '#353535', key='stack_color')
        color = color.lstrip('#')

        # Tech stacks
        col1, col2 = st.columns(2)
        kwargs['tech_stacks'] = col1.text_area('Tech Stacks:', tech_stacks, height=300, key='tech_stacks')
        kwargs['tech_stacks'] = kwargs['tech_stacks'].split('\n')
        kwargs['tech_stacks'] = list(filter(lambda x: x, kwargs['tech_stacks']))

        # Logos and badges
        logos = ['-'.join(tech_stack.split()) for tech_stack in kwargs['tech_stacks']]
        badges = [urllib.parse.quote(tech_stack) for tech_stack in kwargs['tech_stacks']]

        # Format the final url
        kwargs['tech_stacks'] = zip(badges, logos)
        kwargs['tech_stacks'] = [BADGE_TEMPLATE.format(
            badge=badge, logo=logo, style=style, color=color
        ) for badge, logo in kwargs['tech_stacks']]
        kwargs['tech_stacks'] = ' '.join(kwargs['tech_stacks'])

    return kwargs


def add_skills(tab, **kwargs):
    with tab:
        st.write('''Add your skills. You can add any skills you want.
        **Just make sure to separate them with a new line.**
        ''')
        col1, col2 = st.columns(2)
        kwargs['skills'] = col1.text_area('Skills:', skills, height=300, key='skills')
        kwargs['skills'] = kwargs['skills'].split('\n')
        kwargs['skills'] = filter(lambda x: x, kwargs['skills'])
        kwargs['skills'] = [f'- {skill}' for skill in kwargs['skills']]
        kwargs['skills'] = '\n'.join(kwargs['skills'])

    return kwargs
