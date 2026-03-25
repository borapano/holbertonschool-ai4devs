# AI Configuration – Copilot & AI Tools

This document outlines the configuration settings for GitHub Copilot and other AI-assisted workflows used in the project. It ensures consistent AI behavior, language-specific rules, and specialized workflows like code review assistance and automated documentation generation.

## 1. Copilot Settings

- **Enabled Languages:** JavaScript, TypeScript, Python
- **Autocompletion:** Suggests full lines and entire functions
- **Inline Suggestions:** Enabled with inline previews
- **Commit Context Awareness:** Uses Git context for better suggestions
- **Security/Privacy:** Local-only telemetry; no private code sent externally

### Language-Specific Rules
- **JavaScript/TypeScript**
  - Prefer `const` over `let` where applicable
  - Enforce camelCase naming for variables and functions
  - Include JSDoc comments for all exported functions
- **Python**
  - Use type hints for all function parameters and return values
  - Follow PEP8 formatting
  - Include docstrings for all public functions

## 2. Specialized AI Workflows

- **Automated Code Review**
  - Copilot reviews pull requests for syntax errors, code smells, and missing type annotations
  - Highlights potential performance issues in JavaScript/TypeScript
- **Documentation Generator**
  - AI generates README sections, function docstrings, and API reference templates
  - Supports Markdown output for easy inclusion in the repo