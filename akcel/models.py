from django.db import models
from django.contrib.auth.models import User  # Default User model
from django.utils.text import slugify
from datetime import timedelta
from django.utils import timezone



class Category(models.Model):
    """Model representing a campaign category (e.g., Health, Education)."""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    icon_class = models.CharField(max_length=100, default="flaticon-default")  # Add a field for the icon CSS class

    def __str__(self):
        return self.name


class Campaign(models.Model):
    """Model representing a fundraising campaign."""
    title = models.CharField(max_length=255)
    description = models.TextField()
    goal_amount = models.DecimalField(max_digits=10, decimal_places=2)
    current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='campaigns')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='category', null=True, blank=True)
    image = models.ImageField(upload_to='campaign_images/', null=True, blank=True)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    days_left = models.IntegerField(blank=True,null=True)
    progress = models.DecimalField(blank=True,null=True,max_digits=10,decimal_places=2)

    # Extra fields for fundraiser details
    address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    bank_account_number = models.CharField(max_length=50, null=True, blank=True)
    qr_code = models.ImageField(upload_to='QR_CODES/', null=True, blank=True)
    citizenship_photo = models.ImageField(upload_to='citizenship_photos/', null=True, blank=True)
    additional_info = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        today = timezone.now()
        self.days_left = (self.end_date - today).days
        self.progress = (self.current_amount/self.goal_amount)*100
        super(Campaign, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Donation(models.Model):
    """Model representing a donation to a campaign."""
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='donations')
    donor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='donations')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    donated_at = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.donor.username if self.donor else 'Anonymous'} donated {self.amount}"


class Comment(models.Model):
    """Model representing comments on a campaign."""
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username}"


class CampaignUpdate(models.Model):
    """Model representing updates provided by the campaign creator."""
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='updates')
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Update: {self.title}"


class WithdrawalRequest(models.Model):
    """Model representing a campaign owner's request to withdraw funds."""
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='withdrawal_requests')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    requested_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('approved', 'Approved'),
            ('rejected', 'Rejected'),
        ],
        default='pending'
    )
    processed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Withdrawal Request: {self.amount} for {self.campaign.title}"


class Report(models.Model):
    """Model for reporting campaigns."""
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='reports')
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)
    reason = models.TextField()
    reported_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report for {self.campaign.title} by {self.reported_by.username}"


class AboutUs(models.Model):
    """Model for dynamically managing the 'About Us' page."""
    title = models.CharField(max_length=255)
    content = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class FAQ(models.Model):
    """Model for dynamically managing FAQs."""
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question


class ContactUs(models.Model):
    """Model for storing contact us form submissions."""
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.full_name}"


class TermsAndConditions(models.Model):
    """Model for dynamically managing the 'Terms and Conditions' page."""
    content = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Terms and Conditions"
