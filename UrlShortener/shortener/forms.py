from django import forms 

class URLForm(forms.Form):
    original_url = forms.URLField(
        label="Enter URL to shorten",
        widget=forms.URLInput(attrs={"placeholder": "https://example.com"}),
    )
    custom_slug = forms.CharField(
        label="Custom slug (optional)",
        max_length=20,
        required=False,
        help_text="Only letters, numbers, hyphens, and underscores allowed",
    )