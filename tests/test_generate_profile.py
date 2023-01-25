from unittest import TestCase

from src.github_profile import GenerateProfile


class GenerateProfileTestCase(TestCase):
    def setUp(self):
        with open('tests/data/profile_readme.txt') as f:
            self.profile = f.read()
            
    def test_profile(self):
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
        
        self.assertEqual(generated_profile, self.profile)
