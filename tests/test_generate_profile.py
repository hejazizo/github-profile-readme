import pytest
from src.github_profile import GenerateProfile


def test_generate_profile():
    with open('tests/data/profile_readme.txt') as f:
        profile = f.read()

    # Personal Info
    name = "John Doe"
    email = "johndoe@gmail.com"
    phone = "+1 123 456 7890"
    homepage = "https://johndoe.com"
    location = "New York, USA"

    # Social Media
    github = "johndoe"
    linkedin = "johndoe"
    twitter = "johndoe"
    facebook = "johndoe"
    instagram = "johndoe"
    youtube = "johndoe"
    medium = "johndoe"

    # Select Theme
    theme = "default"

    # Generate Readme
    profile_obj = GenerateProfile(
        theme,
        name=name,
        email=email,
        phone=phone,
        homepage=homepage,
        location=location,
        github=github,
        linkedin=linkedin,
        twitter=twitter,
        facebook=facebook,
        instagram=instagram,
        youtube=youtube,
        medium=medium,
    )
    generated_profile = profile_obj()
    
    assert generated_profile == profile
