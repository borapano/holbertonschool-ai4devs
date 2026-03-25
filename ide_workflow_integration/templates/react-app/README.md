# React Template with AI Support

## Features
- Pre-configured Copilot settings
- ESLint + Prettier
- AI code review workflow
- AI documentation generation workflow

## AI Configuration
```yaml
languages:
  javascript:
    enable: true
    rules:
      - prefer_const: true
      - camelCase: true
      - jsdoc_required: true
workflows:
  code_review:
    enabled: true
    checks:
      - syntax
      - performance
      - missing_types
  doc_generator:
    enabled: true
    output_format: markdown