---
name: new-brand-guidelines
description: Applies Anthropic's official brand colors and typography to any sort of artifact that may benefit from having Anthropic's look-and-feel. Use it when brand colors or style guidelines, visual formatting, or company design standards apply.
license: Complete terms in LICENSE.txt
---

# Anthropic Brand Styling

## Overview

To access Anthropic's official brand identity and style resources, use this skill.

**Keywords**: branding, corporate identity, visual identity, post-processing, styling, brand colors, typography, Anthropic brand, visual formatting, visual design

## Brand Guidelines

### Colors

**Main Colors:**

- Dark: `#141413` - Primary text and dark backgrounds
- Light: `#faf9f5` - Light backgrounds and text on dark
- Mid Gray: `#b0aea5` - Secondary elements
- Light Gray: `#e8e6dc` - Subtle backgrounds

**Accent Colors:**

- Orange: `#d97757` - Primary accent
- Blue: `#6a9bcc` - Secondary accent
- Green: `#788c5d` - Tertiary accent

### Typography

- **Headings**: Styrene A (with Poppins, Arial fallback)
- **Body Text**: Lora (with Georgia fallback)
- **Monospace/Code**: Styrene A Mono
- **Note**: Fonts should be pre-installed in your environment for best results

## Features

### Smart Font Application

- Applies Test Tiempos Headline Light to PPTX slide titles (28pt and larger), falling back to Georgia then Arial. For non-PPTX artifacts, applies Styrene A to headings (24pt and larger), falling back to Poppins then Arial
- Applies Lora font to body text, falling back to Georgia
- Uses Styrene A Mono for any code or monospace text
- Automatically falls back through the font chain if custom fonts unavailable
- Preserves readability across all systems

### Text Styling

- Headings (24pt+): Styrene A font
- Body text: Lora font
- Code/monospace: Styrene A Mono font
- Smart color selection based on background
- Preserves text hierarchy and formatting

### Shape and Accent Colors

- Non-text shapes use accent colors
- Cycles through orange, blue, and green accents
- Maintains visual interest while staying on-brand

## Technical Details

### Font Management

- Uses Styrene A for headings and Lora for body text as the primary brand typefaces
- Uses Styrene A Mono for code/monospace text
- Falls back to Poppins (headings) and Georgia (body) if primary fonts are not installed
- Final fallback to Arial (headings) and Georgia (body) for maximum compatibility
- No font installation required - works with existing system fonts

### Color Application

- Uses RGB color values for precise brand matching
- Applied via python-pptx's RGBColor class
- Maintains color fidelity across different systems
