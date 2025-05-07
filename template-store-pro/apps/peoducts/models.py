# Django Imports
from django.db import models
from django.utils.text import slugify
# from django.conf import settings # Uncomment if settings.AUTH_USER_MODEL is used for ProductReview
# from django.core.validators import MinValueValidator, MaxValueValidator # Uncomment for ProductReview

# Local Application Imports
from apps.core.models import TimestampedEcho # Inheriting the echo of time

# --- Supporting Glyphs: The Facets of Categorization & Compatibility ---

class Software(TimestampedEcho):
    """
    Software with which templates are compatible (e.g., MS Excel, Notion, Figma).
    A facet for filtering and discovery, enhancing the template's narrative of utility.
    """
    name = models.CharField(
        max_length=100,
        unique=True,
        help_text="e.g., Microsoft Excel, Notion, Figma, Adobe Photoshop. The digital chisel or scroll."
    )
    slug = models.SlugField(
        max_length=120,
        unique=True,
        editable=False,
        help_text="URL-friendly sigil, auto-inscribed from the name."
    )
    # icon = models.ImageField(
    #     upload_to='software_icons/',
    #     blank=True,
    #     null=True,
    #     help_text="Optional visual glyph for the software. (Future optimization: imagekit for performance)"
    # )

    class Meta:
        verbose_name = "Software Compatibility Sigil"
        verbose_name_plural = "Software Compatibility Sigils"
        ordering = ['name']
        indexes = [
            models.Index(fields=['slug']),
        ]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Industry(TimestampedEcho):
    """
    Target industries for templates (e.g., Healthcare, Nonprofit, SaaS).
    Allows for niche-specific offerings, tailoring the narrative to specific professional realms.
    """
    name = models.CharField(
        max_length=100,
        unique=True,
        help_text="e.g., Healthcare, Nonprofit, Financial Services, Creative Arts. The domain of application."
    )
    slug = models.SlugField(
        max_length=120,
        unique=True,
        editable=False,
        help_text="URL-friendly sigil, auto-inscribed from the name."
    )
    description = models.TextField(
        blank=True,
        help_text="Optional brief narrative describing the industry focus and its unique challenges or needs."
    )

    class Meta:
        verbose_name = "Industry Focus Rune"
        verbose_name_plural = "Industry Focus Runes"
        ordering = ['name']
        indexes = [
            models.Index(fields=['slug']),
        ]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class ProfessionalRole(TimestampedEcho):
    """
    Target professional roles for templates (e.g., Data Analyst, HR Manager, Founder).
    Ensures templates resonate with the specific quests and responsibilities of the user.
    """
    name = models.CharField(
        max_length=100,
        unique=True,
        help_text="e.g., Data Analyst, Marketing Manager, Startup Founder, Project Weaver. The persona of the seeker."
    )
    slug = models.SlugField(
        max_length=120,
        unique=True,
        editable=False,
        help_text="URL-friendly sigil, auto-inscribed from the name."
    )
    description = models.TextField(
        blank=True,
        help_text="Optional brief narrative describing the role's common objectives and how VoidBloom empowers them."
    )

    class Meta:
        verbose_name = "Professional Role Archetype"
        verbose_name_plural = "Professional Role Archetypes"
        ordering = ['name']
        indexes = [
            models.Index(fields=['slug']),
        ]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Tag(TimestampedEcho):
    """
    Descriptive tags for nuanced filtering (e.g., minimalist, data-driven, annual report).
    Keywords of Power for discovery, adding layers to the product's narrative.
    """
    name = models.CharField(
        max_length=50,
        unique=True,
        help_text="e.g., minimalist, data-driven, corporate, startup, agile, strategic. A resonant keyword."
    )
    slug = models.SlugField(
        max_length=60,
        unique=True,
        editable=False,
        help_text="URL-friendly sigil, auto-inscribed from the name."
    )

    class Meta:
        verbose_name = "Product Keyword of Power"
        verbose_name_plural = "Product Keywords of Power"
        ordering = ['name']
        indexes = [
            models.Index(fields=['slug']),
        ]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


# --- The Central Artifact: The Product Itself ---

class Product(TimestampedEcho):
    """
    The core offering: a template or a bundle of templates from the VoidBloom Sanctum.
    Each product is an artifact from the Artisan's Forge, imbued with purpose, poetic logic, and transformative potential.
    """
    WCAG_COMPLIANCE_CHOICES = [
        ('NONE', 'Not Assessed / Not Applicable'),
        ('A', 'WCAG Level A'),
        ('AA', 'WCAG Level AA'),
        ('AAA', 'WCAG Level AAA'),
    ]

    name = models.CharField(
        max_length=255,
        help_text="The clear, evocative title of the template or bundle. e.g., 'Executive Pitch Deck Pro'."
    )
    slug = models.SlugField(
        max_length=280, # Accommodates longer names if necessary
        unique=True,
        editable=False, # Auto-generated and managed
        help_text="URL-friendly identifier, auto-inscribed. The product's unique resonance in the digital ether."
    )
    tagline = models.CharField(
        max_length=150,
        blank=True,
        help_text="A brief, compelling subtitle. The opening verse of its narrative. e.g., 'Secure Funding & Impress Stakeholders'."
    )
    description = models.TextField(
        help_text="Detailed narrative: features, benefits, use cases, included items, and the transformative journey it offers."
    )
    
    sku = models.CharField(
        max_length=50,
        unique=True,
        blank=True,
        null=True,
        help_text="Stock Keeping Unit or VoidBloom Product Sigil (VPS). For internal chronicles and integrations."
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Base price of the product. The offering to the seeker."
    )
    discounted_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        help_text="Optional promotional price. If set, this is the active selling price, a temporary flux in the offering."
    )
    
    is_active = models.BooleanField(
        default=True,
        help_text="Is this product currently manifest and purchasable in the Sanctum?"
    )
    is_featured = models.BooleanField(
        default=False,
        help_text="Should this product be illuminated in a place of honor (e.g., homepage spotlight)?"
    )
    is_subscription_exclusive = models.BooleanField(
        default=False,
        help_text="Is this artifact only accessible to those initiated into a subscription pact?"
    )

    digital_product_file = models.FileField(
        upload_to='product_files/%Y/%m/', # Organized by creation date
        blank=True, # Might be a bundle of other products, or a service
        null=True,
        help_text="The downloadable template file (e.g., .zip). Ensure storage is secured by VoidBloom's wards (server config)."
    )
    
    version = models.CharField(
        max_length=20,
        default="1.0",
        blank=True, # Some products might not have versions
        help_text="Version sigil (e.g., 1.0, 2.1 Omega, Nova Edition). Tracks its evolution."
    )
    release_notes = models.TextField(
        blank=True,
        help_text="Chronicle of changes, enhancements, and bug fixes in new versions of this template."
    )
    documentation_url = models.URLField(
        blank=True,
        help_text="Link to detailed scrolls, video grimoires, or external knowledge bases for this artifact."
    )

    # Relational Glyphs - Connecting to Facets of its Being
    software_compatibility = models.ManyToManyField(
        Software,
        blank=True, # A product might be software-agnostic (e.g., a methodology document)
        related_name="products",
        help_text="The digital chisels or scrolls this template is attuned to."
    )
    industry_focus = models.ManyToManyField(
        Industry,
        blank=True,
        related_name="products",
        help_text="The specific professional realms this template serves."
    )
    role_focus = models.ManyToManyField(
        ProfessionalRole,
        blank=True,
        related_name="products",
        help_text="The seeker archetypes this template empowers."
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name="products",
        help_text="Resonant Keywords of Power for discovery and nuanced understanding."
    )

    # Accessibility & Design Sigils - Reflecting Inclusive Craftsmanship
    wcag_compliance_level = models.CharField(
        max_length=4,
        choices=WCAG_COMPLIANCE_CHOICES,
        default='NONE',
        help_text="Web Content Accessibility Guidelines (WCAG) compliance level. A testament to inclusive design."
    )
    is_dark_mode_compatible = models.BooleanField(
        default=False,
        help_text="Does this template embrace the shadow aesthetic or function harmoniously within it?"
    )
    is_mobile_responsive_design = models.BooleanField(
        default=False, # Default to False; explicitly set True for web templates, presentations etc.
        help_text="Does this template adapt its form gracefully to various viewing conduits (e.g., web, mobile screens)?"
    )

    class Meta:
        verbose_name = "Product Artifact"
        verbose_name_plural = "Product Artifacts"
        ordering = ['-is_featured', '-created_at', 'name'] # Spotlighted artifacts first, then newest chronicles
        indexes = [
            models.Index(fields=['slug']),
            models.Index(fields=['is_active', 'is_featured', '-created_at']),
            models.Index(fields=['price']),
        ]

    def __str__(self):
        return f"{self.name}{f' (v{self.version})' if self.version else ''}"

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            # Simple collision avoidance: if a product with this name might exist,
            # this ensures versioning or other differentiators in name are key.
            # For more robust collision handling if names aren't unique, a loop with a counter/random suffix would be needed.
            self.slug = base_slug
        super().save(*args, **kwargs) # Save first to get an ID if it's a new object

    @property
    def is_on_sale(self) -> bool:
        """Checks if the product has a discounted price currently active."""
        return self.discounted_price is not None and self.discounted_price < self.price

    @property
    def get_display_price(self) -> models.DecimalField:
        """Returns the effective selling price (discounted if available, else base price)."""
        return self.discounted_price if self.is_on_sale else self.price

    # @property
    # def get_primary_image_url(self) -> str | None:
    #     """Retrieves the URL of the primary display image, if one exists."""
    #     primary_image = self.images.filter(is_primary_display=True).first()
    #     if primary_image and primary_image.image:
    #         try:
    #             return primary_image.image.url
    #         except ValueError: # Handle case where file might be missing from storage
    #             return None
    #     return None


class ProductImage(TimestampedEcho):
    """
    Visual incantations (images) showcasing a Product's essence and form.
    Each image is a window into the artifact's potential.
    """
    product = models.ForeignKey(
        Product,
        related_name='images', # Allows product.images.all()
        on_delete=models.CASCADE, # If product is removed, its images fade with it
        help_text="The Product Artifact this visual incantation belongs to."
    )
    image = models.ImageField(
        upload_to='product_images/%Y/%m/', # Organized by upload date
        help_text="High-quality image showcasing the template. The visual echo of the artifact."
    )
    alt_text = models.CharField(
        max_length=255, # Standard length for alt text
        help_text="Descriptive narrative for accessibility (e.g., screen readers) and SEO. What story does this image tell?"
    )
    caption = models.CharField(
        max_length=255,
        blank=True,
        help_text="Optional brief verse accompanying the image."
    )
    is_primary_display = models.BooleanField(
        default=False,
        help_text="Is this the foremost visual echo, the main image shown in listings and product detail?"
    )
    order = models.PositiveIntegerField(
        default=0,
        db_index=True, # Often sorted by this
        help_text="Order in which images are displayed in a gallery. The sequence of the visual narrative."
    )

    class Meta:
        verbose_name = "Product Visual Incantation"
        verbose_name_plural = "Product Visual Incantations"
        ordering = ['product', 'order', '-is_primary_display'] # Group by product, then by defined order

    def __str__(self):
        return f"Image for {self.product.name} - {self.alt_text[:50] if self.alt_text else 'Untitled Visual'}"

    def save(self, *args, **kwargs):
        # Ensure only one primary display image per product
        if self.is_primary_display:
            ProductImage.objects.filter(product=self.product, is_primary_display=True).exclude(pk=self.pk).update(is_primary_display=False)
        super().save(*args, **kwargs)

# --- Future Glyphs (Seedlings for Recursive Expansion of the Artisan's Forge) ---

# class Bundle(TimestampedEcho):
#     """
#     A curated collection of Product Artifacts, offered as a single, synergistic purchasable unit.
#     A constellation of solutions.
#     """
#     name = models.CharField(max_length=255, help_text="Evocative name of the bundle.")
#     slug = models.SlugField(max_length=280, unique=True, editable=False)
#     tagline = models.CharField(max_length=150, blank=True, help_text="Compelling subtitle for the bundle.")
#     description = models.TextField(help_text="Narrative detailing the collective power and synergy of the bundled artifacts.")
#     products = models.ManyToManyField(Product, related_name="bundles", help_text="The individual Product Artifacts composing this bundle.")
#     bundle_price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price for the entire bundle, often reflecting a collective value.")
#     is_active = models.BooleanField(default=True)
#     is_featured = models.BooleanField(default=False)
#     # Consider inheriting from a common 'Offerable' abstract model if Product and Bundle share many fields.
#
#     class Meta:
#         verbose_name = "Product Bundle Constellation"
#         verbose_name_plural = "Product Bundle Constellations"
#
#     def __str__(self):
#         return self.name
#
#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.name)
#         super().save(*args, **kwargs)


# class ProductReview(TimestampedEcho):
#     """
#     Echoes from seekers: feedback and testimonials for Product Artifacts.
#     The community's voice shaping the myth.
#     """
#     product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, help_text="The seeker who left the echo. Null if anonymous or user deleted.")
#     reviewer_name = models.CharField(max_length=100, blank=True, help_text="Display name if user is not registered or prefers anonymity.")
#     rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], help_text="Resonance score from 1 (dissonant) to 5 (harmonious).")
#     title = models.CharField(max_length=150, blank=True, help_text="A concise title for the review's narrative.")
#     comment = models.TextField(help_text="The seeker's detailed narrative about their experience with the artifact.")
#     is_approved = models.BooleanField(default=False, help_text="Has this echo been approved by the Sanctum Scribes for public view?")
#     is_verified_purchase = models.BooleanField(default=False, help_text="Does this echo come from a seeker who verifiably acquired the artifact?")
#
#     class Meta:
#         verbose_name = "Seeker's Echo (Product Review)"
#         verbose_name_plural = "Seekers' Echoes (Product Reviews)"
#         ordering = ['-created_at']
#
#     def __str__(self):
#         return f"Review for {self.product.name} by {self.user.get_username() if self.user else self.reviewer_name or 'Anonymous'}"
