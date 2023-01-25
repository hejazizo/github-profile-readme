from pathlib import Path


class GenerateProfile:

    def __init__(self, theme, **kwargs):
        self.theme = theme
        self.kwargs = kwargs
        self.profile_theme = self.read_profile_theme()

    def read_profile_theme(self):
        """Generate profile readme from theme and kwargs"""
        # Read theme profile
        with open(f"src/themes/{self.theme}/profile.txt") as f:
            profile = f.read()
        return profile


    def __call__(self):
        # Replace placeholders with items
        for item, value in self.kwargs.items():
            # Skip empty values
            if not value:
                self.profile_theme = self.profile_theme.replace(f"{{ {item} }}", '')
                continue

            # Skip items that don't exist in theme
            item_path = Path(f"src/themes/{self.theme}/{item}.txt")
            if not item_path.exists():
                continue

            # Replace placeholder with item
            with open(item_path) as f:
                profile_item = f.read().strip()
            profile_item = profile_item.replace("{ value }", value)
            self.profile_theme = self.profile_theme.replace(f"{{ {item} }}", profile_item)

        return self.profile_theme
        